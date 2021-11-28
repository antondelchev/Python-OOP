from unittest import TestCase, main

from student.project.student import Student


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.student = Student("S1", {"c1": ["notes"]})

    def test_init_creates_all_attributes(self):
        self.assertEqual("S1", self.student.name)
        self.assertEqual({"c1": ["notes"]}, self.student.courses)

    def test_init_without_courses(self):
        self.new_student = Student("S2")
        self.assertEqual({}, self.new_student.courses)

    def test_enroll_to_course_you_already_participate_in(self):
        result = self.student.enroll("c1", ["rr"])
        self.assertEqual("Course already added. Notes have been updated.", result)
        expected_notes = list(self.student.courses.values())
        self.assertEqual(["notes", "rr"], *expected_notes)

    def test_with_empty_or_y_add_course_notes_argument(self):
        for case in ["", "Y"]:
            expected_result = {"c1": ["notes"], "c2": ["rw"]}
            message = self.student.enroll("c2", ["rw"], case)
            self.assertEqual("Course and course notes have been added.", message)
            result = self.student.courses
            self.assertEqual(expected_result, result)
            self.student.courses.pop("c2")

    def test_with_new_course_and_nonspecific_arguments_as_course_notes(self):
        result = self.student.enroll("c2", ["r"], "different notes")
        self.assertEqual("Course has been added.", result)
        expected_values_for_notes = list(self.student.courses.values())
        self.assertEqual(["notes"], *expected_values_for_notes)

    def test_add_notes_to_existing_course(self):
        result = self.student.add_notes("c1", "extra notes")
        self.assertEqual("Notes have been updated", result)
        expected_values = list(self.student.courses.values())
        self.assertEqual(["notes", "extra notes"], *expected_values)

    def test_add_notes_raises_exception(self):
        with self.assertRaises(Exception) as msg:
            self.student.add_notes("c3", "rrr")
        self.assertEqual("Cannot add notes. Course not found.", str(msg.exception))

    def test_leave_existing_course(self):
        result = self.student.leave_course("c1")
        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, self.student.courses)

    def test_leave_course_raises_exception(self):
        with self.assertRaises(Exception) as msg:
            self.student.leave_course("c3")
        self.assertEqual("Cannot remove course. Course not found.", str(msg.exception))


if __name__ == "__main__":
    main()
