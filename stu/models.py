from django.db import models

# Create your models here.
class Clazz(models.Model):
    cno = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=30)

    def __unicode__(self):
        return self.cname

class Course(models.Model):
    course_no = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.course_name

class Student(models.Model):
    sno = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=30)
    cls = models.ForeignKey(Clazz)
    cour = models.ManyToManyField(Course)

    def __unicode__(self):
        return self.sname

def getCls(cname):
    try:
        cls = Clazz.objects.get(cname=cname)
    except Clazz.DoesNotExist:
        cls = Clazz.objects.create(cname=cname)
    return cls

def getCourceList(*coursenames):
    courseList = []

    for cn in coursenames:
        try:
            c = Course.objects.get(course_name=cn)
        except Course.DoesNotExist:
            c = Course.objects.create(course_name=cn)
        courseList.append(c)
    return courseList
def registerStu(sname,cname,*coursenames):
#h获取班级对象
    cls = getCls(cname)
#获取课程对象列表
    courseList = getCourceList(*coursenames)
#插入学生表
    try:
        stu = Student.objects.get(sname=sname)
    except Student.DoesNotExist:
        stu = Student.objects.create(sname=sname,cls=cls)
#插入中间表数据
    stu.cour.add(*courseList)

    return True

