import unittest
import unicodecsv
import cStringIO

class UnicodeCSVTestFunction(input_string):
		f = cStringIO.StringIO(input_string)
		r = self.unicodecsv.reader(f, encoding="utf-8")
		for row in r
			pass
		f.close

class HTMLParserTest(unittest.TestCase):
	def test_1(self):
		result = UnicodeCSVTestFunction("\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2(self):
		result = UnicodeCSVTestFunction("\x01\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3(self):
		result = UnicodeCSVTestFunction("\x01\x80\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4(self):
		result = UnicodeCSVTestFunction("\x01\x01\n\x01\n")
		self.assertEqual(result, expected_result)

	def test_5(self):
		result = UnicodeCSVTestFunction("\x01\x01\n\x0D\n")
		self.assertEqual(result, expected_result)

	def test_6(self):
		result = UnicodeCSVTestFunction("\x01\x01\n\x80\n")
		self.assertEqual(result, expected_result)

	def test_7(self):
		result = UnicodeCSVTestFunction("\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_8(self):
		result = UnicodeCSVTestFunction("\x01\x01\n\n\x00")
		self.assertEqual(result, expected_result)

	def test_9(self):
		result = UnicodeCSVTestFunction("\x01\x01\n\n\n")
		self.assertEqual(result, expected_result)

	def test_10(self):
		result = UnicodeCSVTestFunction("\x01,\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_11(self):
		result = UnicodeCSVTestFunction("\n\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_12(self):
		result = UnicodeCSVTestFunction("\x01\x01\n\n\x01")
		self.assertEqual(result, expected_result)

	def test_13(self):
		result = UnicodeCSVTestFunction("\x01\x01\n,\n")
		self.assertEqual(result, expected_result)

	def test_14(self):
		result = UnicodeCSVTestFunction("\x01,\n\n\x00")
		self.assertEqual(result, expected_result)

	def test_15(self):
		result = UnicodeCSVTestFunction("\x01,\n\x01\n")
		self.assertEqual(result, expected_result)

	def test_16(self):
		result = UnicodeCSVTestFunction("\x01,\n\x80\n")
		self.assertEqual(result, expected_result)

	def test_17(self):
		result = UnicodeCSVTestFunction("\x01\x01\n\n\x80")
		self.assertEqual(result, expected_result)

	def test_18(self):
		result = UnicodeCSVTestFunction("\x01,\n\x0D\n")
		self.assertEqual(result, expected_result)

	def test_19(self):
		result = UnicodeCSVTestFunction("\n\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_20(self):
		result = UnicodeCSVTestFunction("\x01,\n\n\x01")
		self.assertEqual(result, expected_result)

	def test_21(self):
		result = UnicodeCSVTestFunction("\x01\x01\n\n,")
		self.assertEqual(result, expected_result)

	def test_22(self):
		result = UnicodeCSVTestFunction("\x01,\n\n\x80")
		self.assertEqual(result, expected_result)

	def test_23(self):
		result = UnicodeCSVTestFunction("\x01,\n\n,")
		self.assertEqual(result, expected_result)

	def test_24(self):
		result = UnicodeCSVTestFunction("\x01,\n,\n")
		self.assertEqual(result, expected_result)

	def test_25(self):
		result = UnicodeCSVTestFunction("\n,\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_26(self):
		result = UnicodeCSVTestFunction("\n\x01\n\n\x00")
		self.assertEqual(result, expected_result)

	def test_27(self):
		result = UnicodeCSVTestFunction("\x01,\n\n\n")
		self.assertEqual(result, expected_result)

	def test_28(self):
		result = UnicodeCSVTestFunction("\n\x80\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_29(self):
		result = UnicodeCSVTestFunction("\n\x01\n\n\n")
		self.assertEqual(result, expected_result)

	def test_30(self):
		result = UnicodeCSVTestFunction("\n\x01\n\x01\x01")
		self.assertEqual(result, expected_result)

	def test_31(self):
		result = UnicodeCSVTestFunction("\n\x01\n\x80\x01")
		self.assertEqual(result, expected_result)

	def test_32(self):
		result = UnicodeCSVTestFunction("\n,\n\n\x00")
		self.assertEqual(result, expected_result)

	def test_33(self):
		result = UnicodeCSVTestFunction("\n,\n\n\x01")
		self.assertEqual(result, expected_result)

	def test_34(self):
		result = UnicodeCSVTestFunction("\n,\n\n,")
		self.assertEqual(result, expected_result)

	def test_35(self):
		result = UnicodeCSVTestFunction("\n\x01\n\n\x01")
		self.assertEqual(result, expected_result)

	def test_36(self):
		result = UnicodeCSVTestFunction("\n,\n\n\x0D")
		self.assertEqual(result, expected_result)

	def test_37(self):
		result = UnicodeCSVTestFunction("\n\n\"\"\x01")
		self.assertEqual(result, expected_result)

	def test_38(self):
		result = UnicodeCSVTestFunction("\n,\n\n\"")
		self.assertEqual(result, expected_result)

	def test_39(self):
		result = UnicodeCSVTestFunction("\n,\n\n\x80")
		self.assertEqual(result, expected_result)

	def test_40(self):
		result = UnicodeCSVTestFunction(",\x80\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_41(self):
		result = UnicodeCSVTestFunction("\n\n\"\"\x80")
		self.assertEqual(result, expected_result)

	def test_42(self):
		result = UnicodeCSVTestFunction("\x01\x01\n,\x80")
		self.assertEqual(result, expected_result)

	def test_43(self):
		result = UnicodeCSVTestFunction("\x01\x01\n,,")
		self.assertEqual(result, expected_result)

	def test_44(self):
		result = UnicodeCSVTestFunction("\n\x01\n\n\x80")
		self.assertEqual(result, expected_result)

	def test_45(self):
		result = UnicodeCSVTestFunction("\n\x01\n\n\"")
		self.assertEqual(result, expected_result)

	def test_46(self):
		result = UnicodeCSVTestFunction("\n\x01\n\n,")
		self.assertEqual(result, expected_result)

	def test_47(self):
		result = UnicodeCSVTestFunction("\n\x0D\n\n\x00")
		self.assertEqual(result, expected_result)

	def test_48(self):
		result = UnicodeCSVTestFunction("\n\x01\n\x01,")
		self.assertEqual(result, expected_result)

	def test_49(self):
		result = UnicodeCSVTestFunction("\n\x0D\n\n\n")
		self.assertEqual(result, expected_result)

	def test_50(self):
		result = UnicodeCSVTestFunction("\n\n\"\",")
		self.assertEqual(result, expected_result)

	def test_51(self):
		result = UnicodeCSVTestFunction("\x01\x01\n,\"")
		self.assertEqual(result, expected_result)

	def test_52(self):
		result = UnicodeCSVTestFunction("\n\x01\n,\x80")
		self.assertEqual(result, expected_result)

	def test_53(self):
		result = UnicodeCSVTestFunction("\n\n\n\n\x00")
		self.assertEqual(result, expected_result)

	def test_54(self):
		result = UnicodeCSVTestFunction(",,\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_55(self):
		result = UnicodeCSVTestFunction("\n\x01\n,\"")
		self.assertEqual(result, expected_result)

	def test_56(self):
		result = UnicodeCSVTestFunction("\n\n\n\n\x01")
		self.assertEqual(result, expected_result)

	def test_57(self):
		result = UnicodeCSVTestFunction("\n,\n\"\"")
		self.assertEqual(result, expected_result)

	def test_58(self):
		result = UnicodeCSVTestFunction("\n,\n ,")
		self.assertEqual(result, expected_result)

	def test_59(self):
		result = UnicodeCSVTestFunction("\n,\n \x80")
		self.assertEqual(result, expected_result)

	def test_60(self):
		result = UnicodeCSVTestFunction("\n\x01\n,,")
		self.assertEqual(result, expected_result)

	def test_61(self):
		result = UnicodeCSVTestFunction("\n\n\n\n\x80")
		self.assertEqual(result, expected_result)

	def test_62(self):
		result = UnicodeCSVTestFunction("\n\n\n\n\x0D")
		self.assertEqual(result, expected_result)

	def test_63(self):
		result = UnicodeCSVTestFunction("\n\x0D\n\n\x01")
		self.assertEqual(result, expected_result)

	def test_64(self):
		result = UnicodeCSVTestFunction("\n\x0D\n\n\x80")
		self.assertEqual(result, expected_result)

	def test_65(self):
		result = UnicodeCSVTestFunction(",,\n\x0D\x0D")
		self.assertEqual(result, expected_result)

	def test_66(self):
		result = UnicodeCSVTestFunction(",,\n\x01\n")
		self.assertEqual(result, expected_result)

	def test_67(self):
		result = UnicodeCSVTestFunction("\n\n\n\n,")
		self.assertEqual(result, expected_result)

	def test_68(self):
		result = UnicodeCSVTestFunction(",,\n\x80\n")
		self.assertEqual(result, expected_result)

	def test_69(self):
		result = UnicodeCSVTestFunction(",\"\n\n\"")
		self.assertEqual(result, expected_result)

	def test_70(self):
		result = UnicodeCSVTestFunction("\n\x0D\n\x0D\n")
		self.assertEqual(result, expected_result)

	def test_71(self):
		result = UnicodeCSVTestFunction(",,\n\n\x00")
		self.assertEqual(result, expected_result)

	def test_72(self):
		result = UnicodeCSVTestFunction(",,\n\n\n")
		self.assertEqual(result, expected_result)

	def test_73(self):
		result = UnicodeCSVTestFunction(",,\n\n\x01")
		self.assertEqual(result, expected_result)

	def test_74(self):
		result = UnicodeCSVTestFunction(",,\n\n\x80")
		self.assertEqual(result, expected_result)

	def test_75(self):
		result = UnicodeCSVTestFunction(",,\n\n,")
		self.assertEqual(result, expected_result)

	def test_76(self):
		result = UnicodeCSVTestFunction("\n\"\n\",")
		self.assertEqual(result, expected_result)

	def test_77(self):
		result = UnicodeCSVTestFunction("\n,\n,\x80")
		self.assertEqual(result, expected_result)

	def test_78(self):
		result = UnicodeCSVTestFunction(",,\n,\x01")
		self.assertEqual(result, expected_result)

	def test_79(self):
		result = UnicodeCSVTestFunction(",,\n,\x80")
		self.assertEqual(result, expected_result)

	def test_80(self):
		result = UnicodeCSVTestFunction("\n,\n,,")
		self.assertEqual(result, expected_result)

	def test_81(self):
		result = UnicodeCSVTestFunction(",,\n,\"")
		self.assertEqual(result, expected_result)

	def test_82(self):
		result = UnicodeCSVTestFunction("\n\x0D\n\n,")
		self.assertEqual(result, expected_result)

	def test_83(self):
		result = UnicodeCSVTestFunction(",,\n,,")
		self.assertEqual(result, expected_result)

	def test_84(self):
		result = UnicodeCSVTestFunction("\n\x0D\n,\x80")
		self.assertEqual(result, expected_result)

	def test_85(self):
		result = UnicodeCSVTestFunction("\n\x0D\n,,")
		self.assertEqual(result, expected_result)

	def test_86(self):
		result = UnicodeCSVTestFunction("\n\n\n,\x80")
		self.assertEqual(result, expected_result)

	def test_87(self):
		result = UnicodeCSVTestFunction("\n\n\n,,")
		self.assertEqual(result, expected_result)

	def test_88(self):
		result = UnicodeCSVTestFunction("\n\x0D\n,\"")
		self.assertEqual(result, expected_result)

	def test_89(self):
		result = UnicodeCSVTestFunction(",\x01,\x80\n")
		self.assertEqual(result, expected_result)

	def test_90(self):
		result = UnicodeCSVTestFunction(",\x01,,\n")
		self.assertEqual(result, expected_result)

	def test_91(self):
		result = UnicodeCSVTestFunction("\n\n\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_92(self):
		result = UnicodeCSVTestFunction(",\x0D\n,\x80")
		self.assertEqual(result, expected_result)

	def test_93(self):
		result = UnicodeCSVTestFunction("\n\n\x01\n\n")
		self.assertEqual(result, expected_result)

	def test_94(self):
		result = UnicodeCSVTestFunction("\n\n\x01\n\x01")
		self.assertEqual(result, expected_result)

	def test_95(self):
		result = UnicodeCSVTestFunction("\n\n\x01\n\x80")
		self.assertEqual(result, expected_result)

	def test_96(self):
		result = UnicodeCSVTestFunction("\n\n\x01\n,")
		self.assertEqual(result, expected_result)

	def test_97(self):
		result = UnicodeCSVTestFunction("\n\n,\n\x00")
		self.assertEqual(result, expected_result)

	def test_98(self):
		result = UnicodeCSVTestFunction("\n\n,\n\x01")
		self.assertEqual(result, expected_result)

	def test_99(self):
		result = UnicodeCSVTestFunction("\n\n,\n\x80")
		self.assertEqual(result, expected_result)

	def test_100(self):
		result = UnicodeCSVTestFunction("\n\n,\n\n")
		self.assertEqual(result, expected_result)

	def test_101(self):
		result = UnicodeCSVTestFunction("\n\n,\n,")
		self.assertEqual(result, expected_result)

	def test_102(self):
		result = UnicodeCSVTestFunction(",\x0D\n,,")
		self.assertEqual(result, expected_result)

	def test_103(self):
		result = UnicodeCSVTestFunction("\n\n,,\x80")
		self.assertEqual(result, expected_result)

	def test_104(self):
		result = UnicodeCSVTestFunction("\n,\x80\n\x00")
		self.assertEqual(result, expected_result)

	def test_105(self):
		result = UnicodeCSVTestFunction("\n,,\n\x00")
		self.assertEqual(result, expected_result)

	def test_106(self):
		result = UnicodeCSVTestFunction("\n,,\n\n")
		self.assertEqual(result, expected_result)

	def test_107(self):
		result = UnicodeCSVTestFunction("\n,,\n\x01")
		self.assertEqual(result, expected_result)

	def test_108(self):
		result = UnicodeCSVTestFunction("\n,,\n\"")
		self.assertEqual(result, expected_result)

	def test_109(self):
		result = UnicodeCSVTestFunction("\n,,\n\x80")
		self.assertEqual(result, expected_result)

	def test_110(self):
		result = UnicodeCSVTestFunction("\n\n,,,")
		self.assertEqual(result, expected_result)

	def test_111(self):
		result = UnicodeCSVTestFunction("\n,,\n,")
		self.assertEqual(result, expected_result)

	def test_112(self):
		result = UnicodeCSVTestFunction(",,,\n\x00")
		self.assertEqual(result, expected_result)

	def test_113(self):
		result = UnicodeCSVTestFunction(",,,\n\n")
		self.assertEqual(result, expected_result)

	def test_114(self):
		result = UnicodeCSVTestFunction(",,,\n\x01")
		self.assertEqual(result, expected_result)

	def test_115(self):
		result = UnicodeCSVTestFunction(",,,\n\x80")
		self.assertEqual(result, expected_result)

	def test_116(self):
		result = UnicodeCSVTestFunction(",,,\n,")
		self.assertEqual(result, expected_result)

	def test_117(self):
		result = UnicodeCSVTestFunction("\n,,\x80\n")
		self.assertEqual(result, expected_result)

	def test_118(self):
		result = UnicodeCSVTestFunction("\n\"\",\"")
		self.assertEqual(result, expected_result)

	def test_119(self):
		result = UnicodeCSVTestFunction("\n,,,\n")
		self.assertEqual(result, expected_result)

	def test_120(self):
		result = UnicodeCSVTestFunction(",,,\x80\n")
		self.assertEqual(result, expected_result)

	def test_121(self):
		result = UnicodeCSVTestFunction(",,,,\n")
		self.assertEqual(result, expected_result)

	def test_122(self):
		result = UnicodeCSVTestFunction(" \x01,,\"")
		self.assertEqual(result, expected_result)

	def test_123(self):
		result = UnicodeCSVTestFunction("\n,,,\x80")
		self.assertEqual(result, expected_result)

	def test_124(self):
		result = UnicodeCSVTestFunction("\n,,,,")
		self.assertEqual(result, expected_result)

	def test_125(self):
		result = UnicodeCSVTestFunction(",\n\n\n\x00")
		self.assertEqual(result, expected_result)

	def test_126(self):
		result = UnicodeCSVTestFunction("\x01\n\n\n\x00")
		self.assertEqual(result, expected_result)

	def test_127(self):
		result = UnicodeCSVTestFunction(",\n\n\n\x01")
		self.assertEqual(result, expected_result)

	def test_128(self):
		result = UnicodeCSVTestFunction("\x01\n\n\n\x01")
		self.assertEqual(result, expected_result)

	def test_129(self):
		result = UnicodeCSVTestFunction(",\n\n\n\x80")
		self.assertEqual(result, expected_result)

	def test_130(self):
		result = UnicodeCSVTestFunction("\x01\n\n\n\x80")
		self.assertEqual(result, expected_result)

	def test_131(self):
		result = UnicodeCSVTestFunction(",\n\n\n\n")
		self.assertEqual(result, expected_result)

	def test_132(self):
		result = UnicodeCSVTestFunction("\x01\n\n\n\x0D")
		self.assertEqual(result, expected_result)

	def test_133(self):
		result = UnicodeCSVTestFunction("\x01\n\n\n,")
		self.assertEqual(result, expected_result)

	def test_134(self):
		result = UnicodeCSVTestFunction(" \n\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_135(self):
		result = UnicodeCSVTestFunction(" \n\x01\n\x01")
		self.assertEqual(result, expected_result)

	def test_136(self):
		result = UnicodeCSVTestFunction(",\n\n,\x80")
		self.assertEqual(result, expected_result)

	def test_137(self):
		result = UnicodeCSVTestFunction(" \n\x01\n\x80")
		self.assertEqual(result, expected_result)

	def test_138(self):
		result = UnicodeCSVTestFunction(" \n\x01\n\x0D")
		self.assertEqual(result, expected_result)

	def test_139(self):
		result = UnicodeCSVTestFunction(" \n\x01\n,")
		self.assertEqual(result, expected_result)

	def test_140(self):
		result = UnicodeCSVTestFunction(",\n\n\n,")
		self.assertEqual(result, expected_result)

	def test_141(self):
		result = UnicodeCSVTestFunction(",\n\n,,")
		self.assertEqual(result, expected_result)

	def test_142(self):
		result = UnicodeCSVTestFunction(" \n,\n\x00")
		self.assertEqual(result, expected_result)

	def test_143(self):
		result = UnicodeCSVTestFunction(" \n,\n\n")
		self.assertEqual(result, expected_result)

	def test_144(self):
		result = UnicodeCSVTestFunction(" \n,\n\x01")
		self.assertEqual(result, expected_result)

	def test_145(self):
		result = UnicodeCSVTestFunction(" \n,\n\x80")
		self.assertEqual(result, expected_result)

	def test_146(self):
		result = UnicodeCSVTestFunction(",\n\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_147(self):
		result = UnicodeCSVTestFunction(",\n\x01\n\n")
		self.assertEqual(result, expected_result)

	def test_148(self):
		result = UnicodeCSVTestFunction(",\n\x01\n\x01")
		self.assertEqual(result, expected_result)

	def test_149(self):
		result = UnicodeCSVTestFunction(",\n\x01\n\x80")
		self.assertEqual(result, expected_result)

	def test_150(self):
		result = UnicodeCSVTestFunction(" \n,\n,")
		self.assertEqual(result, expected_result)

	def test_151(self):
		result = UnicodeCSVTestFunction(",\n\x01\n,")
		self.assertEqual(result, expected_result)

	def test_152(self):
		result = UnicodeCSVTestFunction("\x01\n\n,\x80")
		self.assertEqual(result, expected_result)

	def test_153(self):
		result = UnicodeCSVTestFunction("\x01\n\n,,")
		self.assertEqual(result, expected_result)

	def test_154(self):
		result = UnicodeCSVTestFunction(",\n,\n\x00")
		self.assertEqual(result, expected_result)

	def test_155(self):
		result = UnicodeCSVTestFunction(",\n,\n\x01")
		self.assertEqual(result, expected_result)

	def test_156(self):
		result = UnicodeCSVTestFunction(",\n,\n\x80")
		self.assertEqual(result, expected_result)

	def test_157(self):
		result = UnicodeCSVTestFunction(",\n,\n\n")
		self.assertEqual(result, expected_result)

	def test_158(self):
		result = UnicodeCSVTestFunction(",\n,\n,")
		self.assertEqual(result, expected_result)

	def test_159(self):
		result = UnicodeCSVTestFunction(",\n,,,")
		self.assertEqual(result, expected_result)

	def test_160(self):
		result = UnicodeCSVTestFunction(",\n,,\x80")
		self.assertEqual(result, expected_result)

	def test_161(self):
		result = UnicodeCSVTestFunction(" \n,,\x80")
		self.assertEqual(result, expected_result)

	def test_162(self):
		result = UnicodeCSVTestFunction(" \n,,,")
		self.assertEqual(result, expected_result)

	def test_163(self):
		result = UnicodeCSVTestFunction(",,,,\x80")
		self.assertEqual(result, expected_result)

	def test_164(self):
		result = UnicodeCSVTestFunction(",,,,,")
		self.assertEqual(result, expected_result)


if __name__ == '__main__':
	unittest.main()