from django.db import models

from django_base.base_meta.models import NamedModel


class Student(NamedModel):
    parents = models.ManyToManyField(
        verbose_name='家长', to='Contact', related_name='students',
        blank=True)

    class Meta:
        verbose_name = '学生'
        verbose_name_plural = '学生'
        db_table = 'core_student'


class Contact(NamedModel):
    class Meta:
        verbose_name = '联系人'
        verbose_name_plural = '联系人'
        db_table = 'core_contact'


class Teacher(NamedModel):
    contact = models.OneToOneField(
        to='Contact', related_name='teacher', primary_key=True,
        on_delete=models.PROTECT)

    class Meta:
        verbose_name = '老师'
        verbose_name_plural = '老师'
        db_table = 'core_teacher'


class Course(NamedModel):
    # 课程介绍等信息
    class Meta:
        verbose_name = '课程'
        verbose_name_plural = '课程'
        db_table = 'core_course'


class CourseClass(NamedModel):
    # 课程
    course = models.ForeignKey(
        verbose_name='课程', to='Course', related_name='classes',
        on_delete=models.PROTECT)
    teacher = models.ForeignKey(
        verbose_name='老师', to='Teacher', related_name='classes',
        on_delete=models.PROTECT)
    students = models.ManyToManyField(
        verbose_name='学生', to='Student', related_name='classes',
        through='StudentClassRel', blank=True)

    class Meta:
        verbose_name = '班级'
        verbose_name_plural = '班级'
        db_table = 'core_course_class'


class ClassPeriod(models.Model):
    course_class = models.ForeignKey(
        verbose_name='班级', to='CourseClass', related_name='periods',
        on_delete=models.PROTECT)

    class Meta:
        verbose_name = '班级课时'
        verbose_name_plural = '班级课时'
        db_table = 'core_class_period'


class StudentClassRel(models.Model):
    course_class = models.ForeignKey(
        verbose_name='班级', to='CourseClass', related_name='students_rel',
        on_delete=models.CASCADE)
    student = models.ForeignKey(
        verbose_name='学生', to='Student', related_name='classes_rel',
        on_delete=models.CASCADE)

    # 状态
    # 加入时间
    # 退出时间
    # 课程单价

    class Meta:
        verbose_name = '学生班级记录'
        verbose_name_plural = '学生班级记录'
        db_table = 'core_student_class_rel'


class StudentClassAttendance(models.Model):
    student = models.ForeignKey(
        verbose_name='学生', to='Student', related_name='attendances',
        on_delete=models.CASCADE)
    period = models.ForeignKey(
        verbose_name='课时', to='ClassPeriod', related_name='attendances',
        on_delete=models.CASCADE)

    # 状态
    # 签到时间（弱）
    # 离开时间（弱）
    # 计费时长
    # 课时金额（不保存单价避免除不尽，动态记录兼容试课信息等临时调整）

    class Meta:
        verbose_name = '学生出勤记录'
        verbose_name_plural = '学生出勤记录'
        db_table = 'core_student_class_attendance'
