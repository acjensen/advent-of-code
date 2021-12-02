from unittest import TestCase, main


class MainTest(TestCase):
    def main_test(self):
        from .main import part_1_result, part_2_result
        self.assertEqual(part_1_result, 444019)
        self.assertEqual(part_2_result, 29212176)


if __name__ == "__main__":
    main()
