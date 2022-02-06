import unittest,log,sys,os,py_lambda

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
    
    def test_favour(self):
        _l=log.Logger("[{time}/{type}]: {log} ({f})")
        _l["f"]="favour test"
        _l.add_stream(self.test_file)
        _l.log(log="test_favour")
        with open("test.log","r") as f:
            l=f.read()
        self.assertTrue("test_favour (favour test)" in l)

    def test_favour_func(self):
        _l=log.Logger("[{time}/{type}]: {log} ({f})")
        _l["f"]=py_lambda.main._def([],"""
    return "func"    

        """)
        _l.add_stream(self.test_file)
        _l.log(log="test_favour")
        with open("test.log","r") as f:
            l=f.read()
        self.assertTrue("test_favour (func)" in l)

    def tearDown(self) -> None:
        self.test_file.close()
        os.remove("test.log")
        return super().tearDown()

if __name__ == "__main__":
    unittest.main()