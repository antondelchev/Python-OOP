from fourth.project.student_report_card import StudentReportCard
from unittest import TestCase, main


class TestStudentReportCard(TestCase):
    def setUp(self) -> None:
        self.report_card = StudentReportCard("Name", 8)

    def test_init_creates_all_attributes(self):
        self.assertEqual("Name", self.report_card.student_name)
        self.assertEqual(8, self.report_card.school_year)
        self.assertEqual({}, self.report_card.grades_by_subject)

    def test_empty_string_for_name_raises(self):
        with self.assertRaises(ValueError) as msg:
            self.report_card.student_name = ""
        expected = "Student Name cannot be an empty string!"
        self.assertEqual(expected, str(msg.exception))


if __name__ == "__main__":
    main()
