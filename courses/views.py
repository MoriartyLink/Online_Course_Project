from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Course, Lesson, Question, Choice, ExamSubmission, Answer


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})


def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    return render(request, 'courses/course_detail.html', {'course': course})


def lesson_detail(request, course_slug, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id, course__slug=course_slug)
    exam_available = lesson.questions.exists()
    return render(request, 'courses/lesson_detail.html', {
        'lesson': lesson,
        'exam_available': exam_available
    })


def take_exam(request, course_slug, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id, course__slug=course_slug)
    if not lesson.questions.exists():
        messages.warning(request, "This lesson doesn't have an exam yet.")
        return redirect('lesson_detail', course_slug=course_slug, lesson_id=lesson_id)

    return render(request, 'courses/exam.html', {
        'lesson': lesson,
        'questions': lesson.questions.all()
    })


def submit_exam(request, course_slug, lesson_id):
    if request.method == 'POST':
        lesson = get_object_or_404(Lesson, id=lesson_id, course__slug=course_slug)
        user = request.user
        score = 0

        submission = ExamSubmission.objects.create(
            student=user,
            lesson=lesson,
            score=0
        )

        for question in lesson.questions.all():
            selected_choice_id = request.POST.get(f'question_{question.id}')

            if selected_choice_id:
                try:
                    selected_choice = Choice.objects.get(id=selected_choice_id)
                    is_correct = selected_choice.is_correct

                    Answer.objects.create(
                        submission=submission,
                        question=question,
                        selected_choice=selected_choice,
                        is_correct=is_correct
                    )

                    if is_correct:
                        score += question.points

                except Choice.DoesNotExist:
                    pass

        submission.score = score
        submission.save()

        return redirect('exam_result', submission_id=submission.id)

    return redirect('lesson_detail', course_slug=course_slug, lesson_id=lesson_id)


def exam_result(request, submission_id):
    submission = get_object_or_404(ExamSubmission, id=submission_id, student=request.user)
    total_possible = sum(q.points for q in submission.lesson.questions.all())

    return render(request, 'courses/exam_result.html', {
        'submission': submission,
        'total_possible': total_possible,
        'percentage': (submission.score / total_possible * 100) if total_possible > 0 else 0
    })


from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from .models import Course, Enrollment

@login_required
def enroll(request, slug):
    course = get_object_or_404(Course, slug=slug)
    Enrollment.objects.get_or_create(
        student=request.user,
        course=course
    )
    messages.success(request, f"You've successfully enrolled in {course.title}!")
    return redirect('courses:course_detail', slug=course.slug)