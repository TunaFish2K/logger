import unittest,log,sys,os

class LoggerTestCase(unittest.TestCase):
    def setUp(self):
        self.logger=log.Logger()
        self.test_file=open("test.log","w+")
    
    def test_stdout_with_info_level(self):
        self.logger.add_stream(sys.stdout)
        self.logger.log("Test stdout with logging level")
        self.logger.remove_all_stream()
    
    def test_stdout_with_warning_level(self):
        self.logger.add_stream(sys.stdout)
        self.logger.log("Test stdout with warning level",level=log.default_levels["warning"])
        self.logger.remove_all_stream()
    
    def test_stdout_with_error_level(self):
        self.logger.add_stream(sys.stdout)
        self.assertRaises(log.LogWarn,log="Test stdout with warning level",level=log.default_levels["error"])
        self.logger.remove_all_stream()
    
    def test_file(self):
        self.logger.add_stream(self.test_file)
        self.logger.log(log="test_file")
        with open("test.log","r") as f:
            log=f.read()
        self.assertTrue("test_file" in log)
        self.logger.remove_all_stream()
    
    def tearDown(self) -> None:
        self.test_file.close()
        os.remove("test.log")
        return super().tearDown()

if __name__ == "__main__":
    unittest.main()