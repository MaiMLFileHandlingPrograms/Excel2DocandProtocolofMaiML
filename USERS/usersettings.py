#####################################
##  MaiMLで使用するNameSpaceの定義
#####################################

## default
class defaultNS():
    _MAIML_ATTR = [
        'version="1.0"', 
        'features="nested-attributes"', 
        'xmlns="http://www.maiml.org/schemas"',
    	'xmlns:maiml="http://www.maiml.org/schemas"', 
        'xmlns:time="http://www.xes-standard.org/time.xesext#"',
    	'xmlns:concept="http://www.xes-standard.org/concept.xesext#"',
    	'xmlns:lifecycle="http://www.xes-standard.org/lifecycle.xesext#"',
    	'xmlns:xsd="http://www.w3.org/2001/XMLSchema"',
    	'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"', 
        'xsi:type="protocolFileRootType"',
    ]

    @property
    def MAIML_ATTR(self):
        return self._MAIML_ATTR


class filePath():
    # 入出力ファイルパス
    _INPUT_FILE_PATH = "./INPUT/excel/inprotocol.xlsx"
    _OUTPUT_FILE_PATH = "./OUTPUT/output.maiml"

    @property
    def INPUT_FILE_PATH(self):
        return self._INPUT_FILE_PATH
    @property
    def OUTPUT_FILE_PATH(self):
        return self._OUTPUT_FILE_PATH