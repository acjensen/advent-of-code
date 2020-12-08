from unittest import TestCase, main


class MainTest(TestCase):
    def main_test(self):
        from .main import part_1_result, part_2_result
        self.assertEqual(part_1_result, 439)
        self.assertEqual(part_2_result, 584)

if __name__ == "__main__":
    main()
