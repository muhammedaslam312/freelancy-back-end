
from rest_framework.views import APIView

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from teacher_app.models import Course,Chapter
from teacher_app.serializers import ChapterSerializer

from .serializers import AccountSerializer,VerifyOtpSerializer,SingleCourseSerializer,CourseRatingSerializer,RecomentedCourseSerializer,EntrolledCourseSerializer,FavoriteCourseSerializer,AssignmentSerializer,CourseSerializer


from .models import Account,FavoriteCourse,StudentAssignment
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from .verify import send,check
from rest_framework import generics,permissions
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from payment.models import StudentEntrollment
from teacher_app.authentication import JWTTeacherAuthentication

from django.db.models import Q
# Create your views here.



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        print("******")
        print(user)
        if user:
            token = super().get_token(user)

            # Add custom claims
            
            token['username'] = user.username
            token['email'] = user.email
        
            token['is_superuser'] = user.is_superuser
            token['mobile'] = user.mobile
            # ...
            print('/////////')
            print(token)
            return token
        else:
            response = Response()

            response.data={
                'message': 'Invalid credential'
            }
            return response


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterAccount(APIView):

    serializer_class =AccountSerializer

    

    def post(self,request,format=None):
        print('*****')
        print(request.data)
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            phone_number=request.data['mobile']
            send(phone_number)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST)  

class VerifyUserOtp(APIView):
    def post(self,request):
        try:
            data=request.data
            phone_number=data['mobile']
            code=data['code']
            print(code)
            print(phone_number)
            if check(phone_number,code):
                
                user = Account.objects.get(mobile=phone_number)   
                print(user)       
                user.is_active= True
                print('****')
                user.save()
                serializer = VerifyOtpSerializer(user,data=data, many=False)
                print('***')
                message = {
                    'detail':'verification Success',
                    'data':data
                    }
                return Response(message)
            else:
                message = {'detail':'otp is not valid'}
                
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
        except:
            message = {'detail':'somthin whent worng'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)     


class GetAllCourses(APIView):
   
    def get(self,request):
        print("//////")
        # teacher = Teacher.objects.filter(id=id)

        # print(teacher)
        courses = Course.objects.all().order_by('-id')[:8]
        serializer = SingleCourseSerializer(courses,many=True)
        
        return Response (serializer.data)

class RecomentedCourses(APIView):
    def get(self,request,id):
        print("//////")
        # teacher = Teacher.objects.filter(id=id)

        # print(teacher)
        student=Account.objects.get(pk=id)
        queries=[Q(used_techs__iendswith=value) for value in student.interests]
        query=queries.pop()
        for item in queries:
            query != item
        courses = Course.objects.filter(query)
        serializer = RecomentedCourseSerializer(courses,many=True)
        
        return Response (serializer.data)


class CourseDetails(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request,id):
        print("//////")
        # teacher = Teacher.objects.filter(id=id)

        # print(teacher)
        course = Course.objects.filter(pk=id)
        
        serializer = SingleCourseSerializer(course,many=True)
        
        return Response (serializer.data)

class GetAllChapters(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request,student_id,course_id):
        student =Account.objects.filter(id=student_id).first()
        course =Course.objects.filter(id=course_id).first()
        entrollStatus=StudentEntrollment.objects.filter(course=course,student=student).count()
        if entrollStatus:
            chapters =Chapter.objects.filter(course=course_id)
            serializer = ChapterSerializer(chapters,many=True)
            return Response(serializer.data)
        

class GetUserEntrolledCourses(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request,id):
        # course=Course.objects.filter(teacher=id)
        # serializer_list=[]
        # for i in course:
        #     entrollment =StudentEntrollment.objects.filter(course__teacher=i.id)
        #     if entrollment:
        #         serializer = EntrollmentSerializer(entrollment,many=True)
        #         serializer_list.append(serializer.data)
        entrollment =StudentEntrollment.objects.filter(student=id)
        serializer = EntrolledCourseSerializer(entrollment,many=True)
        return Response(serializer.data)

class PostRating(APIView):
    permission_classes=[IsAuthenticated]
    
    serializer_classes = CourseRatingSerializer
    def post(self,request):
        data = request.data
        serializer = self.serializer_classes(data=data)
        if serializer.is_valid():
            serializer.save()
            
            print(serializer.data)
            
            response={
                "data" : serializer.data
            }
            return Response(response)
        else:
            print(serializer.errors)
            return Response(serializer.errors)

class StudentFavoriteCourse(APIView):
    permission_classes=[IsAuthenticated]

    def post(self, request, format=None):
        print(request.data)
        serializer = FavoriteCourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,id):
        favoriteCourse=FavoriteCourse.objects.filter(student=id)
        serializer = FavoriteCourseSerializer(favoriteCourse,many=True)
        return Response(serializer.data)



class remove_favorite_course(APIView):
    def delete(self,request,student_id,course_id):
        student=Account.objects.filter(id=student_id).first()
        course=Course.objects.filter(id=course_id).first()
        favoriteStatus = FavoriteCourse.objects.filter(student=student,course=course)
        favoriteStatus.delete()
        if favoriteStatus:
             return Response({'bool':True})
        else:
            return Response({'bool':False})

class AssignmentList(APIView):
    authentication_classes=[JWTTeacherAuthentication]
    def post(self, request, format=None):
        serializer = AssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    


class UserAssignmentList(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,course_id,user_id):
        assigment = StudentAssignment.objects.filter(course=course_id,student=user_id)
        serializer = AssignmentSerializer(assigment,many=True)
        return Response(serializer.data)

class AllCourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes=[IsAuthenticated]