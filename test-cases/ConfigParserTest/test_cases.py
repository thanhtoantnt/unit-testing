import unittest
import cStringIO
import ConfigParser

class ConfigParserTestFunction(input_string):
	string_file = cStringIO.StringIO(input_string)
	config = ConfigParser.ConfigParser()
	config.readfp(string_file)

	for s in config.sections():
		config.options(s)

class HTMLParserTest(unittest.TestCase):
	def test_1(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2(self):
		result = ConfigParserTestFunction("\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3(self):
		result = ConfigParserTestFunction("\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_5(self):
		result = ConfigParserTestFunction("\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_6(self):
		result = ConfigParserTestFunction("\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_7(self):
		result = ConfigParserTestFunction("\x03\x00\x00\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_8(self):
		result = ConfigParserTestFunction("\x03\x00\x00\x00\x00\x00\x00\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_9(self):
		result = ConfigParserTestFunction("\x03\x00\x00\x00\x01\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_10(self):
		result = ConfigParserTestFunction("\x03\x01\x00\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_11(self):
		result = ConfigParserTestFunction("\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_12(self):
		result = ConfigParserTestFunction("\x03\x03\x00\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_13(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_14(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_15(self):
		result = ConfigParserTestFunction("\x01\x00\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_16(self):
		result = ConfigParserTestFunction("\x00\n\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_17(self):
		result = ConfigParserTestFunction("\x03\x00\x00\x00\x00\x00\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_18(self):
		result = ConfigParserTestFunction("\x03\x01\x00\x00\x00\x00\x00\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_19(self):
		result = ConfigParserTestFunction("\x01\n\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_20(self):
		result = ConfigParserTestFunction("\x01\x00\x00\x01\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_21(self):
		result = ConfigParserTestFunction("\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_22(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_23(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_24(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_25(self):
		result = ConfigParserTestFunction("\n\x00\x01\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_26(self):
		result = ConfigParserTestFunction("\x00\x00\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_27(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_28(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_29(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_30(self):
		result = ConfigParserTestFunction("\n\n\x00\x01\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_31(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x01\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_32(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_33(self):
		result = ConfigParserTestFunction("\x00\x00\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_34(self):
		result = ConfigParserTestFunction("\n\n\n\x01\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_35(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x02\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_36(self):
		result = ConfigParserTestFunction("\x01\x02\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_37(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_38(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_39(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x01\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_40(self):
		result = ConfigParserTestFunction("\n\n\n\x01\x01\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_41(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x01\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_42(self):
		result = ConfigParserTestFunction("\n\n\n\x01\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_43(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_44(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_45(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x00\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_46(self):
		result = ConfigParserTestFunction("\x01\x00\x00\x00\x00\x00\x00\x01\x00\x01")
		self.assertEqual(result, expected_result)

	def test_47(self):
		result = ConfigParserTestFunction("\n\x00\x02\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_48(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x01\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_49(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_50(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_51(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_52(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_53(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x01\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_54(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x03\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_55(self):
		result = ConfigParserTestFunction("\n\x00\x01\x00\x00\x00\x01\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_56(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x01\x00\x01\x01\x00")
		self.assertEqual(result, expected_result)

	def test_57(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x00\x00\x01\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_58(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x01\x00\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_59(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_60(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_61(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_62(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_63(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_64(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_65(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_66(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_67(self):
		result = ConfigParserTestFunction("\n\n\x00\x01\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_68(self):
		result = ConfigParserTestFunction("\n\x00\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_69(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_70(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x01\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_71(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x00\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_72(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_73(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_74(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x02\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_75(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x01\x01\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_76(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x00\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_77(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_78(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x00\x01\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_79(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_80(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02")
		self.assertEqual(result, expected_result)

	def test_81(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_82(self):
		result = ConfigParserTestFunction("\x03\x01\x00\x00\x00\x00\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_83(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_84(self):
		result = ConfigParserTestFunction("\n\x00\x01\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_85(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x00\x00\x04\n\x00")
		self.assertEqual(result, expected_result)

	def test_86(self):
		result = ConfigParserTestFunction("\n\x00\x01\x00\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_87(self):
		result = ConfigParserTestFunction("\n\n\x01\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_88(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_89(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_90(self):
		result = ConfigParserTestFunction("\x00\x01\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_91(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_92(self):
		result = ConfigParserTestFunction("\n\n\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_93(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_94(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_95(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_96(self):
		result = ConfigParserTestFunction("\n\n\x01\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_97(self):
		result = ConfigParserTestFunction("\n\n\n\x01\x02\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_98(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_99(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_100(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_101(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_102(self):
		result = ConfigParserTestFunction("\n\x01\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_103(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_104(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_105(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_106(self):
		result = ConfigParserTestFunction("\n\x01\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_107(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_108(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_109(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_110(self):
		result = ConfigParserTestFunction("\x01\x00\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_111(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x00\x00\x00\x00\x06")
		self.assertEqual(result, expected_result)

	def test_112(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x00\x01\x05")
		self.assertEqual(result, expected_result)

	def test_113(self):
		result = ConfigParserTestFunction("\n\n\n\x01\x03\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_114(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x00")
		self.assertEqual(result, expected_result)

	def test_115(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x02\x00")
		self.assertEqual(result, expected_result)

	def test_116(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_117(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_118(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x00\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_119(self):
		result = ConfigParserTestFunction("\n\n\x01\x01\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_120(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x00\x01")
		self.assertEqual(result, expected_result)

	def test_121(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_122(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_123(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_124(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_125(self):
		result = ConfigParserTestFunction("\n\x00\x01\x00\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_126(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x00\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_127(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x00\x00\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_128(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x00\x02\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_129(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_130(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_131(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_132(self):
		result = ConfigParserTestFunction("\x01\x00\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_133(self):
		result = ConfigParserTestFunction("\x03\x01\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_134(self):
		result = ConfigParserTestFunction("\n\n\n\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_135(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x01")
		self.assertEqual(result, expected_result)

	def test_136(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_137(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_138(self):
		result = ConfigParserTestFunction("\x02\x00\x00\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_139(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_140(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x02\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_141(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x03\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_142(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x01\x00")
		self.assertEqual(result, expected_result)

	def test_143(self):
		result = ConfigParserTestFunction("\n\x01\x00\x00\x00\x00\x00\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_144(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x00\x00\x00\x00\x04")
		self.assertEqual(result, expected_result)

	def test_145(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_146(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_147(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x00\x00\x05\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_148(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_149(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x00\n")
		self.assertEqual(result, expected_result)

	def test_150(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x03\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_151(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_152(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x01\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_153(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x03\x00")
		self.assertEqual(result, expected_result)

	def test_154(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x02\x01\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_155(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\n")
		self.assertEqual(result, expected_result)

	def test_156(self):
		result = ConfigParserTestFunction("\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_157(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x06\x00")
		self.assertEqual(result, expected_result)

	def test_158(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_159(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x00\n")
		self.assertEqual(result, expected_result)

	def test_160(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x00\x04\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_161(self):
		result = ConfigParserTestFunction("\n\n\n\x01\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_162(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x03")
		self.assertEqual(result, expected_result)

	def test_163(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x01\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_164(self):
		result = ConfigParserTestFunction("\x03\x02\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_165(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_166(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x01\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_167(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_168(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_169(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_170(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x01\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_171(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x02")
		self.assertEqual(result, expected_result)

	def test_172(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x00\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_173(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x03\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_174(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x00\x00\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_175(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x02\x00")
		self.assertEqual(result, expected_result)

	def test_176(self):
		result = ConfigParserTestFunction("\x00\x01\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_177(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x00\x00\x00\x01\x06")
		self.assertEqual(result, expected_result)

	def test_178(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_179(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x03\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_180(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x00\x04")
		self.assertEqual(result, expected_result)

	def test_181(self):
		result = ConfigParserTestFunction("\x01\x00\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_182(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x07")
		self.assertEqual(result, expected_result)

	def test_183(self):
		result = ConfigParserTestFunction("\x01\x00\x01\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_184(self):
		result = ConfigParserTestFunction("\n\x00\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_185(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_186(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x00\x01\x00\n")
		self.assertEqual(result, expected_result)

	def test_187(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x02\x01")
		self.assertEqual(result, expected_result)

	def test_188(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x04\x00")
		self.assertEqual(result, expected_result)

	def test_189(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_190(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_191(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x03\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_192(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x01\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_193(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x03\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_194(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x02\x04")
		self.assertEqual(result, expected_result)

	def test_195(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_196(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_197(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_198(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x01\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_199(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x00\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_200(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x03\x00")
		self.assertEqual(result, expected_result)

	def test_201(self):
		result = ConfigParserTestFunction("\x01\x00\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_202(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x00\x00\x02\x00")
		self.assertEqual(result, expected_result)

	def test_203(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_204(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x01\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_205(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x04\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_206(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x02\x00\x00")
		self.assertEqual(result, expected_result)

	def test_207(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x00\x00\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_208(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x00\x00\x01\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_209(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x0E\x00")
		self.assertEqual(result, expected_result)

	def test_210(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_211(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x01\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_212(self):
		result = ConfigParserTestFunction("\n\n\x00\x01\x00\x00\x00\x00\x00\x06")
		self.assertEqual(result, expected_result)

	def test_213(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x02\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_214(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x04")
		self.assertEqual(result, expected_result)

	def test_215(self):
		result = ConfigParserTestFunction("\n\x01\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_216(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x01\n")
		self.assertEqual(result, expected_result)

	def test_217(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x00\x00\x01\x01")
		self.assertEqual(result, expected_result)

	def test_218(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_219(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x03\x01")
		self.assertEqual(result, expected_result)

	def test_220(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x06")
		self.assertEqual(result, expected_result)

	def test_221(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x00\x01\x00\x01")
		self.assertEqual(result, expected_result)

	def test_222(self):
		result = ConfigParserTestFunction("\n\x01\x01\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_223(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_224(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x00\\\x00")
		self.assertEqual(result, expected_result)

	def test_225(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_226(self):
		result = ConfigParserTestFunction("\x01\x01\x00\x00\x00\x00\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_227(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x03\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_228(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x01\x01")
		self.assertEqual(result, expected_result)

	def test_229(self):
		result = ConfigParserTestFunction("\n\n\n\x01\x02\x01\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_230(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x00\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_231(self):
		result = ConfigParserTestFunction("\n\n\x01\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_232(self):
		result = ConfigParserTestFunction("\n\n\x00\x02\x00\x00\x00\x00\x00\x06")
		self.assertEqual(result, expected_result)

	def test_233(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x03\x04")
		self.assertEqual(result, expected_result)

	def test_234(self):
		result = ConfigParserTestFunction("\n\x00\x02\x00\x00\x00\x00\x01\x00\x01")
		self.assertEqual(result, expected_result)

	def test_235(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\x00\n")
		self.assertEqual(result, expected_result)

	def test_236(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x05")
		self.assertEqual(result, expected_result)

	def test_237(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x01 \x00")
		self.assertEqual(result, expected_result)

	def test_238(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x08")
		self.assertEqual(result, expected_result)

	def test_239(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x03\x00\x02\x00")
		self.assertEqual(result, expected_result)

	def test_240(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x0C")
		self.assertEqual(result, expected_result)

	def test_241(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_242(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x01\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_243(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x00\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_244(self):
		result = ConfigParserTestFunction("\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_245(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x00\x01\x01\x01")
		self.assertEqual(result, expected_result)

	def test_246(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x05\n")
		self.assertEqual(result, expected_result)

	def test_247(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x00\n")
		self.assertEqual(result, expected_result)

	def test_248(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x02\x00\x00")
		self.assertEqual(result, expected_result)

	def test_249(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x0D")
		self.assertEqual(result, expected_result)

	def test_250(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x03\x05")
		self.assertEqual(result, expected_result)

	def test_251(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_252(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x00\x00\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_253(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x01\x00\x01")
		self.assertEqual(result, expected_result)

	def test_254(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x00\x02")
		self.assertEqual(result, expected_result)

	def test_255(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_256(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x01'\x00")
		self.assertEqual(result, expected_result)

	def test_257(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x03\x02")
		self.assertEqual(result, expected_result)

	def test_258(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_259(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x0E")
		self.assertEqual(result, expected_result)

	def test_260(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_261(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\x01\n")
		self.assertEqual(result, expected_result)

	def test_262(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x00\x00")
		self.assertEqual(result, expected_result)

	def test_263(self):
		result = ConfigParserTestFunction("\x01\x01\x00\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_264(self):
		result = ConfigParserTestFunction("\x01\x01\x00\x00\x01\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_265(self):
		result = ConfigParserTestFunction("\n\n\x01\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_266(self):
		result = ConfigParserTestFunction("\n\x00\x01\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_267(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x00\x00\x00\x04")
		self.assertEqual(result, expected_result)

	def test_268(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_269(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x00\x00\x02\x01")
		self.assertEqual(result, expected_result)

	def test_270(self):
		result = ConfigParserTestFunction("\n\n\x01\x01\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_271(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x00\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_272(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x00\x00\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_273(self):
		result = ConfigParserTestFunction("\x03\x00\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_274(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x01\x01\x01")
		self.assertEqual(result, expected_result)

	def test_275(self):
		result = ConfigParserTestFunction("\n\n\x00\x01\x00\x00\x00\x00\x00\x04")
		self.assertEqual(result, expected_result)

	def test_276(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x01\x01")
		self.assertEqual(result, expected_result)

	def test_277(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x01\\\x00")
		self.assertEqual(result, expected_result)

	def test_278(self):
		result = ConfigParserTestFunction("\x03\x00\x00\x01\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_279(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_280(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_281(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x02 \x00")
		self.assertEqual(result, expected_result)

	def test_282(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x01\x04")
		self.assertEqual(result, expected_result)

	def test_283(self):
		result = ConfigParserTestFunction("\n\x01\x00\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_284(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\t")
		self.assertEqual(result, expected_result)

	def test_285(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_286(self):
		result = ConfigParserTestFunction("\n\x00\x00\x01\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_287(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_288(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x01\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_289(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x00\x00\x01\x00\n")
		self.assertEqual(result, expected_result)

	def test_290(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_291(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x02\n")
		self.assertEqual(result, expected_result)

	def test_292(self):
		result = ConfigParserTestFunction("\x00\x00\x01\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_293(self):
		result = ConfigParserTestFunction("\x01\x00\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_294(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x0F")
		self.assertEqual(result, expected_result)

	def test_295(self):
		result = ConfigParserTestFunction("\n\n\n\x01\x00\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_296(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x03\x00\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_297(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_298(self):
		result = ConfigParserTestFunction("\n\x00\x02\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_299(self):
		result = ConfigParserTestFunction("\n\x01\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_300(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\x00\x00")
		self.assertEqual(result, expected_result)

	def test_301(self):
		result = ConfigParserTestFunction("\n\n\n\x07\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_302(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x00 \x00")
		self.assertEqual(result, expected_result)

	def test_303(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x00\x00\x00\x00\x07")
		self.assertEqual(result, expected_result)

	def test_304(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x01\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_305(self):
		result = ConfigParserTestFunction("\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_306(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_307(self):
		result = ConfigParserTestFunction("\x01\x01\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_308(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_309(self):
		result = ConfigParserTestFunction("\x03\x02\x00\x00\x00\x00\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_310(self):
		result = ConfigParserTestFunction("\n\n\x01\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_311(self):
		result = ConfigParserTestFunction("\n\n\n\x01\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_312(self):
		result = ConfigParserTestFunction("\n\n\x01\x00\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_313(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x03\x03")
		self.assertEqual(result, expected_result)

	def test_314(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_315(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x00'\x00")
		self.assertEqual(result, expected_result)

	def test_316(self):
		result = ConfigParserTestFunction("\n\n\x01\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_317(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x00\x0D\x00")
		self.assertEqual(result, expected_result)

	def test_318(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x05\x00")
		self.assertEqual(result, expected_result)

	def test_319(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x00\x00\x02\x00\n")
		self.assertEqual(result, expected_result)

	def test_320(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x00\x00\x00\x01\x00\x01")
		self.assertEqual(result, expected_result)

	def test_321(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x01\x00\x00\x00\x04")
		self.assertEqual(result, expected_result)

	def test_322(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x01\x00\x00\x01\x04")
		self.assertEqual(result, expected_result)

	def test_323(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x01\x04\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_324(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x02\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_325(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x02\x00\x01")
		self.assertEqual(result, expected_result)

	def test_326(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_327(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x03\x00\x00")
		self.assertEqual(result, expected_result)

	def test_328(self):
		result = ConfigParserTestFunction("\x03\x01\x00\x00\x00\x00\x00\x01\x00\x05")
		self.assertEqual(result, expected_result)

	def test_329(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x00\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_330(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_331(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x0B")
		self.assertEqual(result, expected_result)

	def test_332(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_333(self):
		result = ConfigParserTestFunction("\x03\x00\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_334(self):
		result = ConfigParserTestFunction("\x03\x00\x00\x00\x00\x00\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_335(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_336(self):
		result = ConfigParserTestFunction("\x01\x00\x00\x00\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_337(self):
		result = ConfigParserTestFunction("\n\n\x01\x02\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_338(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x02\x01\x01")
		self.assertEqual(result, expected_result)

	def test_339(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x01\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_340(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x01\x01\n")
		self.assertEqual(result, expected_result)

	def test_341(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x01\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_342(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x01\x02\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_343(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_344(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x00\x02\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_345(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x01\x01\x00")
		self.assertEqual(result, expected_result)

	def test_346(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x03'\x00")
		self.assertEqual(result, expected_result)

	def test_347(self):
		result = ConfigParserTestFunction("\n\n\x01\x00\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_348(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x00\x01\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_349(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x1D")
		self.assertEqual(result, expected_result)

	def test_350(self):
		result = ConfigParserTestFunction("\n\n\x01\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_351(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x02\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_352(self):
		result = ConfigParserTestFunction("\n\n\x02\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_353(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x01\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_354(self):
		result = ConfigParserTestFunction("\x00\x05\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_355(self):
		result = ConfigParserTestFunction("\n\n\x00\x01\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_356(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x00\x05\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_357(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x03\x01\x00")
		self.assertEqual(result, expected_result)

	def test_358(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x03\x00\x00")
		self.assertEqual(result, expected_result)

	def test_359(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x01\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_360(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x06\x00\x00")
		self.assertEqual(result, expected_result)

	def test_361(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x01\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_362(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_363(self):
		result = ConfigParserTestFunction("\x03\x01\x01\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_364(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x00\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_365(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_366(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x00\x01\x01")
		self.assertEqual(result, expected_result)

	def test_367(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x05\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_368(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x00\x01")
		self.assertEqual(result, expected_result)

	def test_369(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x01\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_370(self):
		result = ConfigParserTestFunction("\n\n\x02\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_371(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x00\x00\x00\x00E")
		self.assertEqual(result, expected_result)

	def test_372(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x01\x02\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_373(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x01\n")
		self.assertEqual(result, expected_result)

	def test_374(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_375(self):
		result = ConfigParserTestFunction("\n\n\x01\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_376(self):
		result = ConfigParserTestFunction("\n\x00\x01\x00\x00\x00\x01\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_377(self):
		result = ConfigParserTestFunction("\n\n\x01\x05\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_378(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x03\t\x00")
		self.assertEqual(result, expected_result)

	def test_379(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x03\x00\x01\x01")
		self.assertEqual(result, expected_result)

	def test_380(self):
		result = ConfigParserTestFunction("\n\x00\x03\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_381(self):
		result = ConfigParserTestFunction("\x00\x01\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_382(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x01\x00\x00\x00\x00\x04")
		self.assertEqual(result, expected_result)

	def test_383(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_384(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_385(self):
		result = ConfigParserTestFunction("\n\x01\x01\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_386(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_387(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_388(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x01\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_389(self):
		result = ConfigParserTestFunction("\n\n\n\x01\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_390(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x01\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_391(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x00\x00\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_392(self):
		result = ConfigParserTestFunction("\n\n\x02\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_393(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_394(self):
		result = ConfigParserTestFunction("\n\n\n\n\x03\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_395(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x03\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_396(self):
		result = ConfigParserTestFunction("\n\n\x02\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_397(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x00\x02\n\x00")
		self.assertEqual(result, expected_result)

	def test_398(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x04\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_399(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0E\x00\x00")
		self.assertEqual(result, expected_result)

	def test_400(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x02\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_401(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x01\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_402(self):
		result = ConfigParserTestFunction("\n\x01\x01\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_403(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0E\\\x00")
		self.assertEqual(result, expected_result)

	def test_404(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x00\x01\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_405(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x01\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_406(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x02\x05")
		self.assertEqual(result, expected_result)

	def test_407(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x02\\\x00")
		self.assertEqual(result, expected_result)

	def test_408(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x07\x00\x00")
		self.assertEqual(result, expected_result)

	def test_409(self):
		result = ConfigParserTestFunction("\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_410(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x06\\\x00")
		self.assertEqual(result, expected_result)

	def test_411(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x02\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_412(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x03\x07")
		self.assertEqual(result, expected_result)

	def test_413(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x01\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_414(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_415(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x06\x00")
		self.assertEqual(result, expected_result)

	def test_416(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x02\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_417(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x1A")
		self.assertEqual(result, expected_result)

	def test_418(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\n\x00")
		self.assertEqual(result, expected_result)

	def test_419(self):
		result = ConfigParserTestFunction("\x01\x02\x00\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_420(self):
		result = ConfigParserTestFunction("\n\n\x01\x00\x02\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_421(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x00\x00\x00\x01\x03")
		self.assertEqual(result, expected_result)

	def test_422(self):
		result = ConfigParserTestFunction("\n\n\n\x01\x04\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_423(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x00\x02\x00\n")
		self.assertEqual(result, expected_result)

	def test_424(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x07\x00\x00")
		self.assertEqual(result, expected_result)

	def test_425(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x02\x01\x00")
		self.assertEqual(result, expected_result)

	def test_426(self):
		result = ConfigParserTestFunction("\n\x00\x03\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_427(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_428(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x06\x01")
		self.assertEqual(result, expected_result)

	def test_429(self):
		result = ConfigParserTestFunction("\n\n\n\x04\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_430(self):
		result = ConfigParserTestFunction("\n\x00\x01\x00\x00\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_431(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_432(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x02\x02\x00")
		self.assertEqual(result, expected_result)

	def test_433(self):
		result = ConfigParserTestFunction("\x02\x01\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_434(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x02\x00\x00\x00\x04")
		self.assertEqual(result, expected_result)

	def test_435(self):
		result = ConfigParserTestFunction("\n\x00\x01\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_436(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x01\x00\n")
		self.assertEqual(result, expected_result)

	def test_437(self):
		result = ConfigParserTestFunction("\n\x01\x02\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_438(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_439(self):
		result = ConfigParserTestFunction("\x02\x00\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_440(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x06\x00\n")
		self.assertEqual(result, expected_result)

	def test_441(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\n\x00")
		self.assertEqual(result, expected_result)

	def test_442(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\x01\x00")
		self.assertEqual(result, expected_result)

	def test_443(self):
		result = ConfigParserTestFunction("\x02\n\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_444(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x03\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_445(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x03\x06")
		self.assertEqual(result, expected_result)

	def test_446(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_447(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x01\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_448(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x01\x02")
		self.assertEqual(result, expected_result)

	def test_449(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x07\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_450(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x07\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_451(self):
		result = ConfigParserTestFunction("\n\n\x01\x00\x00\x00\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_452(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x01\x01")
		self.assertEqual(result, expected_result)

	def test_453(self):
		result = ConfigParserTestFunction("\n\x01\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_454(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x15")
		self.assertEqual(result, expected_result)

	def test_455(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x01\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_456(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\x00\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_457(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x03\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_458(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x03\x01\x00")
		self.assertEqual(result, expected_result)

	def test_459(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_460(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_461(self):
		result = ConfigParserTestFunction("\n\x00\x01\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_462(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x01\x02\x00")
		self.assertEqual(result, expected_result)

	def test_463(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x00\x01\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_464(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_465(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x00\x00\x00\x00\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_466(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x01\x05")
		self.assertEqual(result, expected_result)

	def test_467(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x03F")
		self.assertEqual(result, expected_result)

	def test_468(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x00\x00\x02\n\x00")
		self.assertEqual(result, expected_result)

	def test_469(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x01\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_470(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x00\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_471(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x00\x00\x01\x05")
		self.assertEqual(result, expected_result)

	def test_472(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x19")
		self.assertEqual(result, expected_result)

	def test_473(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x02\t\x00")
		self.assertEqual(result, expected_result)

	def test_474(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_475(self):
		result = ConfigParserTestFunction("\n\n\x01\x03\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_476(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\x04\n")
		self.assertEqual(result, expected_result)

	def test_477(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x00\x00\x07")
		self.assertEqual(result, expected_result)

	def test_478(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x03\\\x00")
		self.assertEqual(result, expected_result)

	def test_479(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\x02\x00")
		self.assertEqual(result, expected_result)

	def test_480(self):
		result = ConfigParserTestFunction("\n\x01\x01\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_481(self):
		result = ConfigParserTestFunction("\n\n\n\x04\x00\x00\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_482(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x00\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_483(self):
		result = ConfigParserTestFunction("\n\n\x00\x01\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_484(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x02\x05")
		self.assertEqual(result, expected_result)

	def test_485(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x03\n")
		self.assertEqual(result, expected_result)

	def test_486(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x00\x03")
		self.assertEqual(result, expected_result)

	def test_487(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x03G")
		self.assertEqual(result, expected_result)

	def test_488(self):
		result = ConfigParserTestFunction("\n\n\n\x01\x01\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_489(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x01\x05")
		self.assertEqual(result, expected_result)

	def test_490(self):
		result = ConfigParserTestFunction("\n\n\n\x08\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_491(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_492(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x01\n")
		self.assertEqual(result, expected_result)

	def test_493(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x02\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_494(self):
		result = ConfigParserTestFunction("\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_495(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_496(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x06\x00\x00")
		self.assertEqual(result, expected_result)

	def test_497(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x02\x00\x01\x00\x04")
		self.assertEqual(result, expected_result)

	def test_498(self):
		result = ConfigParserTestFunction("\n\n\x03\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_499(self):
		result = ConfigParserTestFunction("\x03\x01\x01\x00\x00\x00\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_500(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x02\x01")
		self.assertEqual(result, expected_result)

	def test_501(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x11")
		self.assertEqual(result, expected_result)

	def test_502(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x02\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_503(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x1C")
		self.assertEqual(result, expected_result)

	def test_504(self):
		result = ConfigParserTestFunction("\n\n\n\n\x03\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_505(self):
		result = ConfigParserTestFunction("\n\n\n\x06\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_506(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x02\x01\x00")
		self.assertEqual(result, expected_result)

	def test_507(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x00\x00\x01\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_508(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x06 \x00")
		self.assertEqual(result, expected_result)

	def test_509(self):
		result = ConfigParserTestFunction("\n\n\n\n\x03\x01\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_510(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x07\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_511(self):
		result = ConfigParserTestFunction("\x00\x03\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_512(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x07\n")
		self.assertEqual(result, expected_result)

	def test_513(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\x01\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_514(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x1F")
		self.assertEqual(result, expected_result)

	def test_515(self):
		result = ConfigParserTestFunction("\n\n\x02\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_516(self):
		result = ConfigParserTestFunction("\n\n\x00\x01\x00\x00\x00\x02\n\x00")
		self.assertEqual(result, expected_result)

	def test_517(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_518(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x07\\\x00")
		self.assertEqual(result, expected_result)

	def test_519(self):
		result = ConfigParserTestFunction("\n\n\x03\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_520(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x06'\x00")
		self.assertEqual(result, expected_result)

	def test_521(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x03\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_522(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x1E")
		self.assertEqual(result, expected_result)

	def test_523(self):
		result = ConfigParserTestFunction("\n\n\n\x08\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_524(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x07\x00")
		self.assertEqual(result, expected_result)

	def test_525(self):
		result = ConfigParserTestFunction("\x00\x02\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_526(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x07\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_527(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x03\n")
		self.assertEqual(result, expected_result)

	def test_528(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x01\x03")
		self.assertEqual(result, expected_result)

	def test_529(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_530(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x01\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_531(self):
		result = ConfigParserTestFunction("\n\n\x03\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_532(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x01\x00\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_533(self):
		result = ConfigParserTestFunction("\x02\x02\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_534(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x07'\x00")
		self.assertEqual(result, expected_result)

	def test_535(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x00\x00\x00\x00\x01\x01")
		self.assertEqual(result, expected_result)

	def test_536(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_537(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x01\x00\x01\x01\n")
		self.assertEqual(result, expected_result)

	def test_538(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\x00\x01")
		self.assertEqual(result, expected_result)

	def test_539(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x02\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_540(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x03\x01")
		self.assertEqual(result, expected_result)

	def test_541(self):
		result = ConfigParserTestFunction("\x00\x01\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_542(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x02\x02\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_543(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x01\x00\x00\x00\x00\x06")
		self.assertEqual(result, expected_result)

	def test_544(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x03\x00\x01")
		self.assertEqual(result, expected_result)

	def test_545(self):
		result = ConfigParserTestFunction("\x01\x00\x00\x00\x00\x00\x00\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_546(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\x03\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_547(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x01\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_548(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x02\x01\x00\n")
		self.assertEqual(result, expected_result)

	def test_549(self):
		result = ConfigParserTestFunction("\n\n\n\n\x03\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_550(self):
		result = ConfigParserTestFunction("\n\x01\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_551(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_552(self):
		result = ConfigParserTestFunction("\n\x02\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_553(self):
		result = ConfigParserTestFunction("\n\x01\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_554(self):
		result = ConfigParserTestFunction("\n\n\x03\x01\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_555(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x03\x01\x00\x01")
		self.assertEqual(result, expected_result)

	def test_556(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x07\x01")
		self.assertEqual(result, expected_result)

	def test_557(self):
		result = ConfigParserTestFunction("\n\n\x00\x01\x00\x00\x00\x00\x00\x07")
		self.assertEqual(result, expected_result)

	def test_558(self):
		result = ConfigParserTestFunction("\n\n\n\x04\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_559(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x07\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_560(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_561(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x00\x01")
		self.assertEqual(result, expected_result)

	def test_562(self):
		result = ConfigParserTestFunction("\n\x01\x00\x00\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_563(self):
		result = ConfigParserTestFunction("\n\n\n\x01\x00\x02\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_564(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_565(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x04\n")
		self.assertEqual(result, expected_result)

	def test_566(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x02\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_567(self):
		result = ConfigParserTestFunction("\x02\x01\x00\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_568(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x08\x00\x00")
		self.assertEqual(result, expected_result)

	def test_569(self):
		result = ConfigParserTestFunction("\n\n\x02\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_570(self):
		result = ConfigParserTestFunction("\n\n\x03\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_571(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x17")
		self.assertEqual(result, expected_result)

	def test_572(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x1B")
		self.assertEqual(result, expected_result)

	def test_573(self):
		result = ConfigParserTestFunction("\x02\x00\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_574(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_575(self):
		result = ConfigParserTestFunction("\x02\x00\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_576(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x00\x00\x01\x02")
		self.assertEqual(result, expected_result)

	def test_577(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x03\x00\x02\x01")
		self.assertEqual(result, expected_result)

	def test_578(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x03\x05")
		self.assertEqual(result, expected_result)

	def test_579(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x00\x07")
		self.assertEqual(result, expected_result)

	def test_580(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0F\x00\x00")
		self.assertEqual(result, expected_result)

	def test_581(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0F\x00")
		self.assertEqual(result, expected_result)

	def test_582(self):
		result = ConfigParserTestFunction("\n\n\n\x07\x01\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_583(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x06\n")
		self.assertEqual(result, expected_result)

	def test_584(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x14")
		self.assertEqual(result, expected_result)

	def test_585(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x13")
		self.assertEqual(result, expected_result)

	def test_586(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0B\x00\x00")
		self.assertEqual(result, expected_result)

	def test_587(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x04\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_588(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x01\x00")
		self.assertEqual(result, expected_result)

	def test_589(self):
		result = ConfigParserTestFunction("\n\n\x00\x02\x00\x00\x00\x00\x00\x07")
		self.assertEqual(result, expected_result)

	def test_590(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x00\x00\x01\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_591(self):
		result = ConfigParserTestFunction("\n\n\x00\x01\x00\x00\x00\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_592(self):
		result = ConfigParserTestFunction("\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_593(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x18")
		self.assertEqual(result, expected_result)

	def test_594(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x03\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_595(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x01\x00\x00\x02\x04")
		self.assertEqual(result, expected_result)

	def test_596(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x00\x00\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_597(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x06\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_598(self):
		result = ConfigParserTestFunction("\n\n\x02\x01\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_599(self):
		result = ConfigParserTestFunction("\n\n\n\x04\x01\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_600(self):
		result = ConfigParserTestFunction("\x02\x00\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_601(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x12")
		self.assertEqual(result, expected_result)

	def test_602(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x00\x00\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_603(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x08'\x00")
		self.assertEqual(result, expected_result)

	def test_604(self):
		result = ConfigParserTestFunction("\n\n\n\n\x04\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_605(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x00\x02")
		self.assertEqual(result, expected_result)

	def test_606(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x01\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_607(self):
		result = ConfigParserTestFunction("\n\x00\x02\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_608(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\t\x00\x00")
		self.assertEqual(result, expected_result)

	def test_609(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x06\x01\n")
		self.assertEqual(result, expected_result)

	def test_610(self):
		result = ConfigParserTestFunction("\n\n\n\x01\x01\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_611(self):
		result = ConfigParserTestFunction("\x07\x00\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_612(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x01\x01\x00\n")
		self.assertEqual(result, expected_result)

	def test_613(self):
		result = ConfigParserTestFunction("\n\x00\x08\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_614(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x00\x01\x02\n")
		self.assertEqual(result, expected_result)

	def test_615(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x00\x00\x06")
		self.assertEqual(result, expected_result)

	def test_616(self):
		result = ConfigParserTestFunction("\x03\x02\x00\x00\x00\x00\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_617(self):
		result = ConfigParserTestFunction("\x03\x02\x00\x00\x00\x01\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_618(self):
		result = ConfigParserTestFunction("\x06\x00\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_619(self):
		result = ConfigParserTestFunction("\x03\x00\x00\x00\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_620(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x04\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_621(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x00\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_622(self):
		result = ConfigParserTestFunction("\n\n\x07\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_623(self):
		result = ConfigParserTestFunction("\n\n\x01\x01\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_624(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x01\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_625(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x01\x02")
		self.assertEqual(result, expected_result)

	def test_626(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x16")
		self.assertEqual(result, expected_result)

	def test_627(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x05\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_628(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x01\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_629(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x00\x05\n\x00")
		self.assertEqual(result, expected_result)

	def test_630(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x02\x00")
		self.assertEqual(result, expected_result)

	def test_631(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x07\x01\x00\x01")
		self.assertEqual(result, expected_result)

	def test_632(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0F\\\x00")
		self.assertEqual(result, expected_result)

	def test_633(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x00\x02")
		self.assertEqual(result, expected_result)

	def test_634(self):
		result = ConfigParserTestFunction("\n\n\x02\x00\x00\x00\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_635(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x01\x00\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_636(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x01\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_637(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x01\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_638(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0B\x00")
		self.assertEqual(result, expected_result)

	def test_639(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_640(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x00\x00\x00\x01\x01\x01")
		self.assertEqual(result, expected_result)

	def test_641(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x08\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_642(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x03\x02\x00")
		self.assertEqual(result, expected_result)

	def test_643(self):
		result = ConfigParserTestFunction("\n\x00\x01\x00\x00\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_644(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x03\x01\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_645(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x07\x01\x01\x01")
		self.assertEqual(result, expected_result)

	def test_646(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x00\x00\x00\x00\x05\n\x00")
		self.assertEqual(result, expected_result)

	def test_647(self):
		result = ConfigParserTestFunction("\n\n\x03\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_648(self):
		result = ConfigParserTestFunction("\x03\x00\x01\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_649(self):
		result = ConfigParserTestFunction("\x03\x00\x00\x00\x00\x00\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_650(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x05\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_651(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x10")
		self.assertEqual(result, expected_result)

	def test_652(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0F\x01")
		self.assertEqual(result, expected_result)

	def test_653(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x9C")
		self.assertEqual(result, expected_result)

	def test_654(self):
		result = ConfigParserTestFunction("\n\n\x08\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_655(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x00\x00\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_656(self):
		result = ConfigParserTestFunction("\n\n\n\x04\x00\x00\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_657(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x01\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_658(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x07\x00\x01")
		self.assertEqual(result, expected_result)

	def test_659(self):
		result = ConfigParserTestFunction("\x04\x00\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_660(self):
		result = ConfigParserTestFunction("\n\x03\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_661(self):
		result = ConfigParserTestFunction("\n\n\x01\x00\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_662(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_663(self):
		result = ConfigParserTestFunction("\n\x00\x01\x00\x00\x00\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_664(self):
		result = ConfigParserTestFunction("\x00\x01\x00\x00\x00\x02\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_665(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x07\x00\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_666(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x01\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_667(self):
		result = ConfigParserTestFunction("\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_668(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x03\x00\x00\x00\x04")
		self.assertEqual(result, expected_result)

	def test_669(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x02\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_670(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_671(self):
		result = ConfigParserTestFunction("\n\n\x04\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_672(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x00\x01\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_673(self):
		result = ConfigParserTestFunction("\n\n\x00\x01\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_674(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_675(self):
		result = ConfigParserTestFunction("\x02\x01\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_676(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x01\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_677(self):
		result = ConfigParserTestFunction("\x06\x00\x01\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_678(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x01\x00\x00\x02\x00")
		self.assertEqual(result, expected_result)

	def test_679(self):
		result = ConfigParserTestFunction("\n\x01\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_680(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x00\x00\x04")
		self.assertEqual(result, expected_result)

	def test_681(self):
		result = ConfigParserTestFunction("\n\x02\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_682(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x01\x00\x00\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_683(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x00\x03")
		self.assertEqual(result, expected_result)

	def test_684(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x00\x02\x00\x01")
		self.assertEqual(result, expected_result)

	def test_685(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x07\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_686(self):
		result = ConfigParserTestFunction("\x00\x02\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_687(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_688(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x03\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_689(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x07\n\x00")
		self.assertEqual(result, expected_result)

	def test_690(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x97")
		self.assertEqual(result, expected_result)

	def test_691(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x04\n\x00")
		self.assertEqual(result, expected_result)

	def test_692(self):
		result = ConfigParserTestFunction("\n\x06\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_693(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x00\x00\x00\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_694(self):
		result = ConfigParserTestFunction("\n\n\n\x01\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_695(self):
		result = ConfigParserTestFunction("\n\x03\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_696(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x08\x00")
		self.assertEqual(result, expected_result)

	def test_697(self):
		result = ConfigParserTestFunction("\n\x00\x04\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_698(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_699(self):
		result = ConfigParserTestFunction("\n\n\n\x04\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_700(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x07\x01\x00")
		self.assertEqual(result, expected_result)

	def test_701(self):
		result = ConfigParserTestFunction("\x00\x01\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_702(self):
		result = ConfigParserTestFunction("\n\n\n\x04\x01\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_703(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x03\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_704(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0B\x01\x00")
		self.assertEqual(result, expected_result)

	def test_705(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x04\x00\x00")
		self.assertEqual(result, expected_result)

	def test_706(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x00\x03")
		self.assertEqual(result, expected_result)

	def test_707(self):
		result = ConfigParserTestFunction("\n\n\n\n\x06\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_708(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_709(self):
		result = ConfigParserTestFunction("\n\n\n\n\x03\x04\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_710(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x01\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_711(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\x00\x02")
		self.assertEqual(result, expected_result)

	def test_712(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x00\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_713(self):
		result = ConfigParserTestFunction("\n\n\n\n\x06\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_714(self):
		result = ConfigParserTestFunction("\n\n\x00\x02\x00\x00\x00\x00\x00\x04")
		self.assertEqual(result, expected_result)

	def test_715(self):
		result = ConfigParserTestFunction("\n\n\x01\x00\x00\x00\x00\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_716(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x04\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_717(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x06\x00\x01")
		self.assertEqual(result, expected_result)

	def test_718(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_719(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x02\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_720(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x9B")
		self.assertEqual(result, expected_result)

	def test_721(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x01\x00\x01")
		self.assertEqual(result, expected_result)

	def test_722(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x00\x02\x05")
		self.assertEqual(result, expected_result)

	def test_723(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x04\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_724(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x02\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_725(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x02\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_726(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x00\x01\x04")
		self.assertEqual(result, expected_result)

	def test_727(self):
		result = ConfigParserTestFunction("\n\x01\x04\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_728(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_729(self):
		result = ConfigParserTestFunction("\n\n\n\x05\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_730(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_731(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x00\x05\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_732(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x05\n")
		self.assertEqual(result, expected_result)

	def test_733(self):
		result = ConfigParserTestFunction("\n\x02\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_734(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x06\x04")
		self.assertEqual(result, expected_result)

	def test_735(self):
		result = ConfigParserTestFunction("\x01\x00\x00\x00\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_736(self):
		result = ConfigParserTestFunction("\n\n\n\x01\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_737(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x06\x00\x02")
		self.assertEqual(result, expected_result)

	def test_738(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x04\n\x00")
		self.assertEqual(result, expected_result)

	def test_739(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x07\x00\n")
		self.assertEqual(result, expected_result)

	def test_740(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\x03\x00\x01\x01")
		self.assertEqual(result, expected_result)

	def test_741(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x00\x07")
		self.assertEqual(result, expected_result)

	def test_742(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x06\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_743(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x05\n\x00")
		self.assertEqual(result, expected_result)

	def test_744(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0F'\x00")
		self.assertEqual(result, expected_result)

	def test_745(self):
		result = ConfigParserTestFunction("\n\n\x00\x02\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_746(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x02\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_747(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nW")
		self.assertEqual(result, expected_result)

	def test_748(self):
		result = ConfigParserTestFunction("\x03\x00\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_749(self):
		result = ConfigParserTestFunction("\n\n\n\x04\x00\x00\x03\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_750(self):
		result = ConfigParserTestFunction("\n\n\x00\x01\x00\x00\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_751(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0E\x00")
		self.assertEqual(result, expected_result)

	def test_752(self):
		result = ConfigParserTestFunction("\n\x00\x01\x01\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_753(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x08\x00")
		self.assertEqual(result, expected_result)

	def test_754(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x02\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_755(self):
		result = ConfigParserTestFunction("\n\x01\x00\x00\x00\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_756(self):
		result = ConfigParserTestFunction("\n\n\x01\x01\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_757(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x00\x03\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_758(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x02\x01")
		self.assertEqual(result, expected_result)

	def test_759(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x03\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_760(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0E\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_761(self):
		result = ConfigParserTestFunction("\n\n\x03\x01\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_762(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x07\x01\x01")
		self.assertEqual(result, expected_result)

	def test_763(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x00\x04")
		self.assertEqual(result, expected_result)

	def test_764(self):
		result = ConfigParserTestFunction("\n\n\x00\x02\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_765(self):
		result = ConfigParserTestFunction("\n\n\n\n\x07\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_766(self):
		result = ConfigParserTestFunction("\n\x01\x01\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_767(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x06\x04\n")
		self.assertEqual(result, expected_result)

	def test_768(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0E\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_769(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x0F\x00\n")
		self.assertEqual(result, expected_result)

	def test_770(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0E\t\x00")
		self.assertEqual(result, expected_result)

	def test_771(self):
		result = ConfigParserTestFunction("\n\x07\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_772(self):
		result = ConfigParserTestFunction("\n\n\n\x05\x00\x01\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_773(self):
		result = ConfigParserTestFunction("\n\n\n\n\x06\x01\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_774(self):
		result = ConfigParserTestFunction("\n\x01\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_775(self):
		result = ConfigParserTestFunction("\x03\x02\x00\x00\x00\x00\x00\x00\x01\x02")
		self.assertEqual(result, expected_result)

	def test_776(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xDB")
		self.assertEqual(result, expected_result)

	def test_777(self):
		result = ConfigParserTestFunction("\n\n\n\x04\x02\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_778(self):
		result = ConfigParserTestFunction("\x03\x03\x00\x00\x00\x00\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_779(self):
		result = ConfigParserTestFunction("\n\x01\x01\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_780(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x07\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_781(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_782(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x07\x0D\x00")
		self.assertEqual(result, expected_result)

	def test_783(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x06\x01\x02")
		self.assertEqual(result, expected_result)

	def test_784(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x01\x02")
		self.assertEqual(result, expected_result)

	def test_785(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nX")
		self.assertEqual(result, expected_result)

	def test_786(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x00\x00\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_787(self):
		result = ConfigParserTestFunction("\n\n\x00\x02\x00\x00\x00\x01\x00\x06")
		self.assertEqual(result, expected_result)

	def test_788(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x02\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_789(self):
		result = ConfigParserTestFunction("\n\n\n\x02\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_790(self):
		result = ConfigParserTestFunction("\n\n\n\x06\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_791(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0B\x01")
		self.assertEqual(result, expected_result)

	def test_792(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_793(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\x03\x00")
		self.assertEqual(result, expected_result)

	def test_794(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0F\t\x00")
		self.assertEqual(result, expected_result)

	def test_795(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x02\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_796(self):
		result = ConfigParserTestFunction("\n\x01\x02\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_797(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x04\x00\x00")
		self.assertEqual(result, expected_result)

	def test_798(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x00\x00\x00\x01\x00\x01")
		self.assertEqual(result, expected_result)

	def test_799(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x02\x01\n")
		self.assertEqual(result, expected_result)

	def test_800(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_801(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x07\n")
		self.assertEqual(result, expected_result)

	def test_802(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x04\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_803(self):
		result = ConfigParserTestFunction("\x00\x02\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_804(self):
		result = ConfigParserTestFunction("\n\n\x01\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_805(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_806(self):
		result = ConfigParserTestFunction("\n\n\x00\x02\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_807(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x06\x01\x01")
		self.assertEqual(result, expected_result)

	def test_808(self):
		result = ConfigParserTestFunction("\n\x03\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_809(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x08\t\x00")
		self.assertEqual(result, expected_result)

	def test_810(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x0F\x01\n")
		self.assertEqual(result, expected_result)

	def test_811(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_812(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x8B")
		self.assertEqual(result, expected_result)

	def test_813(self):
		result = ConfigParserTestFunction("\n\n\x00\x03\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_814(self):
		result = ConfigParserTestFunction("\x01\x00\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_815(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x02\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_816(self):
		result = ConfigParserTestFunction("\n\x03\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_817(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x02\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_818(self):
		result = ConfigParserTestFunction("\n\n\x08\x00\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_819(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x07\x01\n")
		self.assertEqual(result, expected_result)

	def test_820(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x07\x10\x00")
		self.assertEqual(result, expected_result)

	def test_821(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x03\x01")
		self.assertEqual(result, expected_result)

	def test_822(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x01\x01\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_823(self):
		result = ConfigParserTestFunction("\n\n\n\x06\x00\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_824(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x07\x00\x02")
		self.assertEqual(result, expected_result)

	def test_825(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x01\x07")
		self.assertEqual(result, expected_result)

	def test_826(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x01\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_827(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x00\x00\x00\x02\x00\x00")
		self.assertEqual(result, expected_result)

	def test_828(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0E\x01\x00")
		self.assertEqual(result, expected_result)

	def test_829(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x02\x00\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_830(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\x00\x00\x01\x01")
		self.assertEqual(result, expected_result)

	def test_831(self):
		result = ConfigParserTestFunction("\n\x02\x00\x00\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_832(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x02\x01\x01\x00")
		self.assertEqual(result, expected_result)

	def test_833(self):
		result = ConfigParserTestFunction("\x03\x02\x00\x00\x00\x00\x00\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_834(self):
		result = ConfigParserTestFunction("\x01\x01\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_835(self):
		result = ConfigParserTestFunction("\x03\x01\x01\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_836(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x03\x11\x00")
		self.assertEqual(result, expected_result)

	def test_837(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\x00\x00\x05\n")
		self.assertEqual(result, expected_result)

	def test_838(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x08\\\x00")
		self.assertEqual(result, expected_result)

	def test_839(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x03\x00\x01\x05")
		self.assertEqual(result, expected_result)

	def test_840(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x00\x00\x00\x03\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_841(self):
		result = ConfigParserTestFunction("\x07\x00\x01\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_842(self):
		result = ConfigParserTestFunction("\n\n\x04\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_843(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x02\x00\x01\x01")
		self.assertEqual(result, expected_result)

	def test_844(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x06\n\x00")
		self.assertEqual(result, expected_result)

	def test_845(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x00\x01\x02\x01")
		self.assertEqual(result, expected_result)

	def test_846(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x00\x00\x00\x03\n")
		self.assertEqual(result, expected_result)

	def test_847(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x02\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_848(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x01\x02\n")
		self.assertEqual(result, expected_result)

	def test_849(self):
		result = ConfigParserTestFunction("\n\n\x03\x00\x00\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_850(self):
		result = ConfigParserTestFunction("\n\n\n\n\x03\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_851(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x01\x01\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_852(self):
		result = ConfigParserTestFunction("\n\n\x02\x00\x00\x00\x00\x01\x00\x01")
		self.assertEqual(result, expected_result)

	def test_853(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x07 \x00")
		self.assertEqual(result, expected_result)

	def test_854(self):
		result = ConfigParserTestFunction("\x06\x00\x02\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_855(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x08 \x00")
		self.assertEqual(result, expected_result)

	def test_856(self):
		result = ConfigParserTestFunction("\n\n\n\n\x03\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_857(self):
		result = ConfigParserTestFunction("\n\n\x02\x00\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_858(self):
		result = ConfigParserTestFunction("\n\x00\x02\x00\x00\x01\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_859(self):
		result = ConfigParserTestFunction("\x00\x01\x00\x00\x00\x00\x03\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_860(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x06\x0D\x00")
		self.assertEqual(result, expected_result)

	def test_861(self):
		result = ConfigParserTestFunction("\n\x01\x00\x00\x00\x00\x04\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_862(self):
		result = ConfigParserTestFunction("\x03\x00\x00\x00\x00\x00\x01\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_863(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0E\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_864(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x07\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_865(self):
		result = ConfigParserTestFunction("\n\n\x02\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_866(self):
		result = ConfigParserTestFunction("\n\n\x05\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_867(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x02'\x00")
		self.assertEqual(result, expected_result)

	def test_868(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x04\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_869(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x06\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_870(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x05\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_871(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_872(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0B\x02\x00")
		self.assertEqual(result, expected_result)

	def test_873(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x07\x00")
		self.assertEqual(result, expected_result)

	def test_874(self):
		result = ConfigParserTestFunction("\n\n\x01\x00\x00\x00\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_875(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0E\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_876(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n8")
		self.assertEqual(result, expected_result)

	def test_877(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x01\x00\x01\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_878(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\x01\x02")
		self.assertEqual(result, expected_result)

	def test_879(self):
		result = ConfigParserTestFunction("\n\x01\x00\x01\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_880(self):
		result = ConfigParserTestFunction("\n\n\n\n\x03\x02\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_881(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0E'\x00")
		self.assertEqual(result, expected_result)

	def test_882(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x01\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_883(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x06\x10\x00")
		self.assertEqual(result, expected_result)

	def test_884(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x07\x01\x00\n")
		self.assertEqual(result, expected_result)

	def test_885(self):
		result = ConfigParserTestFunction("\n\n\n\n\x03\x00\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_886(self):
		result = ConfigParserTestFunction("\x07\x00\x02\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_887(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_888(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0E\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_889(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_890(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x01\x05\n\x00")
		self.assertEqual(result, expected_result)

	def test_891(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\x00\n")
		self.assertEqual(result, expected_result)

	def test_892(self):
		result = ConfigParserTestFunction("\x03\x01\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_893(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x02\x02\x00\n")
		self.assertEqual(result, expected_result)

	def test_894(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x00\x00\x03\n")
		self.assertEqual(result, expected_result)

	def test_895(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x01\x00\x06")
		self.assertEqual(result, expected_result)

	def test_896(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x06\n")
		self.assertEqual(result, expected_result)

	def test_897(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x01\x00\x03")
		self.assertEqual(result, expected_result)

	def test_898(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\x01\x00")
		self.assertEqual(result, expected_result)

	def test_899(self):
		result = ConfigParserTestFunction("\x06\x00\x05\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_900(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x03\x00\x01\x00\x04")
		self.assertEqual(result, expected_result)

	def test_901(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x02\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_902(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\n\x00")
		self.assertEqual(result, expected_result)

	def test_903(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x02\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_904(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x08\x01\x00")
		self.assertEqual(result, expected_result)

	def test_905(self):
		result = ConfigParserTestFunction("\n\n\x02\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_906(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x02\x07")
		self.assertEqual(result, expected_result)

	def test_907(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0E\x0D\x00")
		self.assertEqual(result, expected_result)

	def test_908(self):
		result = ConfigParserTestFunction("\n\n\x02\x01\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_909(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x01\x00\x00\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_910(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x00\x04")
		self.assertEqual(result, expected_result)

	def test_911(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\n\n")
		self.assertEqual(result, expected_result)

	def test_912(self):
		result = ConfigParserTestFunction("\n\x02\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_913(self):
		result = ConfigParserTestFunction("\n\n\n\x07\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_914(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_915(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x03\x0D\x00")
		self.assertEqual(result, expected_result)

	def test_916(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x00\x00\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_917(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x00\x10\x00")
		self.assertEqual(result, expected_result)

	def test_918(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\n\x00")
		self.assertEqual(result, expected_result)

	def test_919(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0F\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_920(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n;")
		self.assertEqual(result, expected_result)

	def test_921(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x05\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_922(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x00\x00\x04\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_923(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x07\x01\x02")
		self.assertEqual(result, expected_result)

	def test_924(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x00\x05")
		self.assertEqual(result, expected_result)

	def test_925(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x08\n")
		self.assertEqual(result, expected_result)

	def test_926(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\x00\x00\x02\x01")
		self.assertEqual(result, expected_result)

	def test_927(self):
		result = ConfigParserTestFunction("\x01\x01\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_928(self):
		result = ConfigParserTestFunction("\n\x02\x00\x00\x00\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_929(self):
		result = ConfigParserTestFunction("\n\x00\x01\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_930(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\t\x01\x00")
		self.assertEqual(result, expected_result)

	def test_931(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x98")
		self.assertEqual(result, expected_result)

	def test_932(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x01\x03")
		self.assertEqual(result, expected_result)

	def test_933(self):
		result = ConfigParserTestFunction("\x02\x00\x01\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_934(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\x00\n")
		self.assertEqual(result, expected_result)

	def test_935(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xD8")
		self.assertEqual(result, expected_result)

	def test_936(self):
		result = ConfigParserTestFunction("\n\x00\x01\x00\x00\x00\x00\x01\x00\x01")
		self.assertEqual(result, expected_result)

	def test_937(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x03\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_938(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x02\x03")
		self.assertEqual(result, expected_result)

	def test_939(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x07\x01")
		self.assertEqual(result, expected_result)

	def test_940(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x01\x00\x01\x05")
		self.assertEqual(result, expected_result)

	def test_941(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\n\x01")
		self.assertEqual(result, expected_result)

	def test_942(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x04\x00\x00\x00\x04")
		self.assertEqual(result, expected_result)

	def test_943(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x01\x00\x00\x00\x04")
		self.assertEqual(result, expected_result)

	def test_944(self):
		result = ConfigParserTestFunction("\n\n\x00\x03\x00\x00\x00\x00\x00\x07")
		self.assertEqual(result, expected_result)

	def test_945(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x01\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_946(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x04\x01\x00")
		self.assertEqual(result, expected_result)

	def test_947(self):
		result = ConfigParserTestFunction("\x01\x01\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_948(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x02\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_949(self):
		result = ConfigParserTestFunction("\n\x04\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_950(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x06\t\x00")
		self.assertEqual(result, expected_result)

	def test_951(self):
		result = ConfigParserTestFunction("\n\x02\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_952(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_953(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x02\x00\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_954(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x01\x04")
		self.assertEqual(result, expected_result)

	def test_955(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x01\x00\x00\x00\x07")
		self.assertEqual(result, expected_result)

	def test_956(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\x01\x00")
		self.assertEqual(result, expected_result)

	def test_957(self):
		result = ConfigParserTestFunction("\n\x03\x01\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_958(self):
		result = ConfigParserTestFunction("\n\n\n\x05\x00\x00\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_959(self):
		result = ConfigParserTestFunction("\x01\x03\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_960(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nH")
		self.assertEqual(result, expected_result)

	def test_961(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x01\x01\x00\x01")
		self.assertEqual(result, expected_result)

	def test_962(self):
		result = ConfigParserTestFunction("\n\n\x0C\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_963(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x05\n\x00")
		self.assertEqual(result, expected_result)

	def test_964(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\x01\x01")
		self.assertEqual(result, expected_result)

	def test_965(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x02\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_966(self):
		result = ConfigParserTestFunction("\n\n\n\x04\x00\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_967(self):
		result = ConfigParserTestFunction("\n\x01\x00\x00\x00\x00\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_968(self):
		result = ConfigParserTestFunction("\n\x03\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_969(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\x01\x01")
		self.assertEqual(result, expected_result)

	def test_970(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x04\x00")
		self.assertEqual(result, expected_result)

	def test_971(self):
		result = ConfigParserTestFunction("\n\n\x04\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_972(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x03\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_973(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0E\x01")
		self.assertEqual(result, expected_result)

	def test_974(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x06\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_975(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x01\x03\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_976(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_977(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n[")
		self.assertEqual(result, expected_result)

	def test_978(self):
		result = ConfigParserTestFunction("\n\n\n\x01\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_979(self):
		result = ConfigParserTestFunction("\x03\x01\x00\x00\x00\x00\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_980(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x02\x02\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_981(self):
		result = ConfigParserTestFunction("\x03\x00\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_982(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\n\n")
		self.assertEqual(result, expected_result)

	def test_983(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x08\x02\x00")
		self.assertEqual(result, expected_result)

	def test_984(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x07\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_985(self):
		result = ConfigParserTestFunction("\n\n\x02\x01\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_986(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x01\x00\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_987(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x03\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_988(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x87")
		self.assertEqual(result, expected_result)

	def test_989(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nK")
		self.assertEqual(result, expected_result)

	def test_990(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x07\x00\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_991(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x04\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_992(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_993(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x00\x02\x01")
		self.assertEqual(result, expected_result)

	def test_994(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x03\x01\x01\n")
		self.assertEqual(result, expected_result)

	def test_995(self):
		result = ConfigParserTestFunction("\n\x07\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_996(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x01\x06")
		self.assertEqual(result, expected_result)

	def test_997(self):
		result = ConfigParserTestFunction("\x03\x00\x00\x00\x00\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_998(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xB8")
		self.assertEqual(result, expected_result)

	def test_999(self):
		result = ConfigParserTestFunction("\n\x02\x01\x00\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1000(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0B\x03\x00")
		self.assertEqual(result, expected_result)

	def test_1001(self):
		result = ConfigParserTestFunction("\n\n\n\x07\x00\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1002(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_1003(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\\")
		self.assertEqual(result, expected_result)

	def test_1004(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x00\x00\x02\x02")
		self.assertEqual(result, expected_result)

	def test_1005(self):
		result = ConfigParserTestFunction("\n\x01\x03\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1006(self):
		result = ConfigParserTestFunction("\x03\x01\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1007(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x02\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_1008(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x0B\x00\n")
		self.assertEqual(result, expected_result)

	def test_1009(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\t\x02\x00")
		self.assertEqual(result, expected_result)

	def test_1010(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x06\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1011(self):
		result = ConfigParserTestFunction("\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1012(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x04\n")
		self.assertEqual(result, expected_result)

	def test_1013(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x04\x00\x01")
		self.assertEqual(result, expected_result)

	def test_1014(self):
		result = ConfigParserTestFunction("\n\x02\x00\x00\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1015(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x07\x02\x02")
		self.assertEqual(result, expected_result)

	def test_1016(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_1017(self):
		result = ConfigParserTestFunction("\x0E\x00\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1018(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x08\x10\x00")
		self.assertEqual(result, expected_result)

	def test_1019(self):
		result = ConfigParserTestFunction("\n\x00\x01\x00\x03\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1020(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xB7")
		self.assertEqual(result, expected_result)

	def test_1021(self):
		result = ConfigParserTestFunction("\n\n\n\x04\x00\x02\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1022(self):
		result = ConfigParserTestFunction("\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1023(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x00\x02\x00")
		self.assertEqual(result, expected_result)

	def test_1024(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x00\x01\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1025(self):
		result = ConfigParserTestFunction("\n\n\x01\x07\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1026(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\n\x02")
		self.assertEqual(result, expected_result)

	def test_1027(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_1028(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\x02\x01")
		self.assertEqual(result, expected_result)

	def test_1029(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x02\x00\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_1030(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x00\x06")
		self.assertEqual(result, expected_result)

	def test_1031(self):
		result = ConfigParserTestFunction("\n\x00\x01\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1032(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nk")
		self.assertEqual(result, expected_result)

	def test_1033(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x0E\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1034(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x07\x01")
		self.assertEqual(result, expected_result)

	def test_1035(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x02\x02\n")
		self.assertEqual(result, expected_result)

	def test_1036(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x03 \x00")
		self.assertEqual(result, expected_result)

	def test_1037(self):
		result = ConfigParserTestFunction("\x03\x00\x00\x00\x00\x00\x03\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_1038(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x03\x00\x00\x01\x04")
		self.assertEqual(result, expected_result)

	def test_1039(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x00\x00\x05\n\x00")
		self.assertEqual(result, expected_result)

	def test_1040(self):
		result = ConfigParserTestFunction("\n\n\x06\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1041(self):
		result = ConfigParserTestFunction("\n\n\x04\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_1042(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x04\x00\x00\x01\x04")
		self.assertEqual(result, expected_result)

	def test_1043(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\x02\x00")
		self.assertEqual(result, expected_result)

	def test_1044(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x00\x02\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1045(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0E \x00")
		self.assertEqual(result, expected_result)

	def test_1046(self):
		result = ConfigParserTestFunction("\x01\x01\x00\x00\x00\x00\x00\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_1047(self):
		result = ConfigParserTestFunction("\n\n\x06\x01\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1048(self):
		result = ConfigParserTestFunction("\n\x00\x03\x00\x00\x00\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_1049(self):
		result = ConfigParserTestFunction("\x04\x00\x01\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1050(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x00\x07")
		self.assertEqual(result, expected_result)

	def test_1051(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nx")
		self.assertEqual(result, expected_result)

	def test_1052(self):
		result = ConfigParserTestFunction("\n\x06\x00\x00\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1053(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x01\x01\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_1054(self):
		result = ConfigParserTestFunction("\n\x02\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1055(self):
		result = ConfigParserTestFunction("\n\n\n\x07\x02\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1056(self):
		result = ConfigParserTestFunction("\n\x08\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1057(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0D\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1058(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x02\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1059(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x02\x00\x02\x01")
		self.assertEqual(result, expected_result)

	def test_1060(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0E\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1061(self):
		result = ConfigParserTestFunction("\n\n\x01\x01\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1062(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0F\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1063(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0C\n")
		self.assertEqual(result, expected_result)

	def test_1064(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x07\x02\x01")
		self.assertEqual(result, expected_result)

	def test_1065(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x02\x03")
		self.assertEqual(result, expected_result)

	def test_1066(self):
		result = ConfigParserTestFunction("\n\n\n\x05\x00\x00\x00\x01\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1067(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x03g")
		self.assertEqual(result, expected_result)

	def test_1068(self):
		result = ConfigParserTestFunction("\n\n\x00\x02\x01\x00\x00\x00\x00\x06")
		self.assertEqual(result, expected_result)

	def test_1069(self):
		result = ConfigParserTestFunction("\n\x03\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1070(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0F\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1071(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x00\x00\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_1072(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x04\n")
		self.assertEqual(result, expected_result)

	def test_1073(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x00\x00\x07")
		self.assertEqual(result, expected_result)

	def test_1074(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0E\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1075(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x01\x00\x02")
		self.assertEqual(result, expected_result)

	def test_1076(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_1077(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x04\x01")
		self.assertEqual(result, expected_result)

	def test_1078(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x00\x00\x00\x07\n")
		self.assertEqual(result, expected_result)

	def test_1079(self):
		result = ConfigParserTestFunction("\x00\x03\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1080(self):
		result = ConfigParserTestFunction("\n\x07\x00\x00\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1081(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xCB")
		self.assertEqual(result, expected_result)

	def test_1082(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x00\x04")
		self.assertEqual(result, expected_result)

	def test_1083(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x01\x00\x00\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_1084(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0E\x01\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1085(self):
		result = ConfigParserTestFunction("\n\n\n\n\x03\x00\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1086(self):
		result = ConfigParserTestFunction("\x03\x00\x02\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1087(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0D\n\n\x00")
		self.assertEqual(result, expected_result)

	def test_1088(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0F \x00")
		self.assertEqual(result, expected_result)

	def test_1089(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x88")
		self.assertEqual(result, expected_result)

	def test_1090(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\t\x03\x00")
		self.assertEqual(result, expected_result)

	def test_1091(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0F\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_1092(self):
		result = ConfigParserTestFunction("\x01\x00\x00\x00\x02\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1093(self):
		result = ConfigParserTestFunction("\x03\x00\x00\x00\x00\x00\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_1094(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x03&")
		self.assertEqual(result, expected_result)

	def test_1095(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x03\x03")
		self.assertEqual(result, expected_result)

	def test_1096(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\x01\x01")
		self.assertEqual(result, expected_result)

	def test_1097(self):
		result = ConfigParserTestFunction("\n\n\x02\x01\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1098(self):
		result = ConfigParserTestFunction("\x06\x00\x07\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1099(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x01\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1100(self):
		result = ConfigParserTestFunction("\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1101(self):
		result = ConfigParserTestFunction("\n\n\x00\x04\x00\x00\x00\x00\x00\x07")
		self.assertEqual(result, expected_result)

	def test_1102(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\x01\x04")
		self.assertEqual(result, expected_result)

	def test_1103(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0B\x07\x00")
		self.assertEqual(result, expected_result)

	def test_1104(self):
		result = ConfigParserTestFunction("\n\x06\x01\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1105(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\n\x01")
		self.assertEqual(result, expected_result)

	def test_1106(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0D\n\x00\n")
		self.assertEqual(result, expected_result)

	def test_1107(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x01\x00\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_1108(self):
		result = ConfigParserTestFunction("\n\n\x05\x01\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1109(self):
		result = ConfigParserTestFunction("\x0F\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1110(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x01\x00\x01\x01")
		self.assertEqual(result, expected_result)

	def test_1111(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x01\x00\x00\x00\x01\x02")
		self.assertEqual(result, expected_result)

	def test_1112(self):
		result = ConfigParserTestFunction("\x01\x00\x01\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1113(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x01\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1114(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\x00\x01")
		self.assertEqual(result, expected_result)

	def test_1115(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1116(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\n\x03")
		self.assertEqual(result, expected_result)

	def test_1117(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0D\n\n\n")
		self.assertEqual(result, expected_result)

	def test_1118(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x01\x00\x02\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1119(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0F\x0D\x00")
		self.assertEqual(result, expected_result)

	def test_1120(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x06\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1121(self):
		result = ConfigParserTestFunction("\n\x07\x00\x00\x00\x00\x04\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1122(self):
		result = ConfigParserTestFunction("\x06\x00\x00\x00\x00\x00\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1123(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x00\x11\x00")
		self.assertEqual(result, expected_result)

	def test_1124(self):
		result = ConfigParserTestFunction("\x04\x00\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1125(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x00\t\x00")
		self.assertEqual(result, expected_result)

	def test_1126(self):
		result = ConfigParserTestFunction("\n\n\x02\x00\x00\x00\x01\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1127(self):
		result = ConfigParserTestFunction("\n\n\n\x01\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1128(self):
		result = ConfigParserTestFunction("\x01\x00\x00\x00\x00\x00\x00\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_1129(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x03\x01\n")
		self.assertEqual(result, expected_result)

	def test_1130(self):
		result = ConfigParserTestFunction("\x05\x00\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1131(self):
		result = ConfigParserTestFunction("\n\n\n\n\x03\x00\x01\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1132(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x00\x00\x00\x00\x03\n")
		self.assertEqual(result, expected_result)

	def test_1133(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x01\t\x00")
		self.assertEqual(result, expected_result)

	def test_1134(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x00\x01\x03")
		self.assertEqual(result, expected_result)

	def test_1135(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x00\x00\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_1136(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x01\x03")
		self.assertEqual(result, expected_result)

	def test_1137(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x04\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1138(self):
		result = ConfigParserTestFunction("\n\n\n\n\x07\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1139(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x00\x01\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1140(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x02\x0D\x00")
		self.assertEqual(result, expected_result)

	def test_1141(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x05\n")
		self.assertEqual(result, expected_result)

	def test_1142(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x00\x05\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1143(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1144(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x07\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1145(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0E\x01\x01\x00\n")
		self.assertEqual(result, expected_result)

	def test_1146(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x07\x03")
		self.assertEqual(result, expected_result)

	def test_1147(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x02\x00\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_1148(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n{")
		self.assertEqual(result, expected_result)

	def test_1149(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x04\x01\x01")
		self.assertEqual(result, expected_result)

	def test_1150(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x07\x02\x00")
		self.assertEqual(result, expected_result)

	def test_1151(self):
		result = ConfigParserTestFunction("\x07\x00\x00\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_1152(self):
		result = ConfigParserTestFunction("\n\n\x05\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1153(self):
		result = ConfigParserTestFunction("\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1154(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x02\x02\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1155(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x01\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1156(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1157(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x07\t\x00")
		self.assertEqual(result, expected_result)

	def test_1158(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x07\x04\n")
		self.assertEqual(result, expected_result)

	def test_1159(self):
		result = ConfigParserTestFunction("\n\x04\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1160(self):
		result = ConfigParserTestFunction("\n\n\x03\x02\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1161(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0F\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1162(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x03\x00")
		self.assertEqual(result, expected_result)

	def test_1163(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x07\x80\x00")
		self.assertEqual(result, expected_result)

	def test_1164(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\x01\n")
		self.assertEqual(result, expected_result)

	def test_1165(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x06\x05")
		self.assertEqual(result, expected_result)

	def test_1166(self):
		result = ConfigParserTestFunction("\n\n\n\x04\x00\x03\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1167(self):
		result = ConfigParserTestFunction("\x05\x00\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1168(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n(")
		self.assertEqual(result, expected_result)

	def test_1169(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x02\n")
		self.assertEqual(result, expected_result)

	def test_1170(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x01\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1171(self):
		result = ConfigParserTestFunction("\n\n\x04\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1172(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x07\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1173(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\t\x00")
		self.assertEqual(result, expected_result)

	def test_1174(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n<")
		self.assertEqual(result, expected_result)

	def test_1175(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0F\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1176(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\t\x07\x00")
		self.assertEqual(result, expected_result)

	def test_1177(self):
		result = ConfigParserTestFunction("\n\x0F\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1178(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x07\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1179(self):
		result = ConfigParserTestFunction("\n\n\x06\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1180(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x02\x02")
		self.assertEqual(result, expected_result)

	def test_1181(self):
		result = ConfigParserTestFunction("\n\n\x04\x00\x00\x00\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_1182(self):
		result = ConfigParserTestFunction("\n\n\n\x08\x01\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1183(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\n\x06")
		self.assertEqual(result, expected_result)

	def test_1184(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\x01\x01\x00\x01")
		self.assertEqual(result, expected_result)

	def test_1185(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x07\x03\x02")
		self.assertEqual(result, expected_result)

	def test_1186(self):
		result = ConfigParserTestFunction("\x00\x01\x00\x00\x00\x00\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_1187(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x06\x02\x01")
		self.assertEqual(result, expected_result)

	def test_1188(self):
		result = ConfigParserTestFunction("\n\x02\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1189(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x03\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1190(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\x00\x04")
		self.assertEqual(result, expected_result)

	def test_1191(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x01\x0D\x00")
		self.assertEqual(result, expected_result)

	def test_1192(self):
		result = ConfigParserTestFunction("\n\x03\x02\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1193(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x01\x10\x00")
		self.assertEqual(result, expected_result)

	def test_1194(self):
		result = ConfigParserTestFunction("\x02\x00\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1195(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x00\x00\x03\x02")
		self.assertEqual(result, expected_result)

	def test_1196(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x01\x00\x05")
		self.assertEqual(result, expected_result)

	def test_1197(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x07\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1198(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0E\x10\x00")
		self.assertEqual(result, expected_result)

	def test_1199(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x01\x01\n")
		self.assertEqual(result, expected_result)

	def test_1200(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x04\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1201(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x00\x01\x01")
		self.assertEqual(result, expected_result)

	def test_1202(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x02\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_1203(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x07\x04")
		self.assertEqual(result, expected_result)

	def test_1204(self):
		result = ConfigParserTestFunction("\n\n\n\x03\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1205(self):
		result = ConfigParserTestFunction("\n\n\n\x01\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_1206(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x04\x01\x00\n")
		self.assertEqual(result, expected_result)

	def test_1207(self):
		result = ConfigParserTestFunction("\n\n\x0F\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1208(self):
		result = ConfigParserTestFunction("\n\x01\x00\x00\x00\x01\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1209(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x01\x01\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1210(self):
		result = ConfigParserTestFunction("\x02\x03\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1211(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x00\x00\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1212(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x0E\x00\x01")
		self.assertEqual(result, expected_result)

	def test_1213(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x02\x04")
		self.assertEqual(result, expected_result)

	def test_1214(self):
		result = ConfigParserTestFunction("\n\x02\x00\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_1215(self):
		result = ConfigParserTestFunction("\n\n\x01\x01\x00\x00\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_1216(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x00\x00\x05\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1217(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\n\x04")
		self.assertEqual(result, expected_result)

	def test_1218(self):
		result = ConfigParserTestFunction("\x0F\x00\x00\x00\x00\x01\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1219(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x01\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_1220(self):
		result = ConfigParserTestFunction("\n\n\x05\x00\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1221(self):
		result = ConfigParserTestFunction("\n\n\n\x04\x00\x00\x01\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1222(self):
		result = ConfigParserTestFunction("\x01\x00\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1223(self):
		result = ConfigParserTestFunction("\n\n\n\n\x04\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1224(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x02\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1225(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0D\n\n\x01")
		self.assertEqual(result, expected_result)

	def test_1226(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0E\x04")
		self.assertEqual(result, expected_result)

	def test_1227(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x02\x01\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1228(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0F\x04")
		self.assertEqual(result, expected_result)

	def test_1229(self):
		result = ConfigParserTestFunction("\x02\x06\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1230(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0D\x00")
		self.assertEqual(result, expected_result)

	def test_1231(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x01\x01\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1232(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\n\n\x00")
		self.assertEqual(result, expected_result)

	def test_1233(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x00\x00\x00\x03\n")
		self.assertEqual(result, expected_result)

	def test_1234(self):
		result = ConfigParserTestFunction("\n\x01\x00\x00\x00\x01\x01\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1235(self):
		result = ConfigParserTestFunction("\n\n\n\x06\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1236(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\n\n\n")
		self.assertEqual(result, expected_result)

	def test_1237(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\n\x0E")
		self.assertEqual(result, expected_result)

	def test_1238(self):
		result = ConfigParserTestFunction("\n\x00\x02\x00\x00\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_1239(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x02\x00\x00\x00\x07")
		self.assertEqual(result, expected_result)

	def test_1240(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nh")
		self.assertEqual(result, expected_result)

	def test_1241(self):
		result = ConfigParserTestFunction("\n\n\x02\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1242(self):
		result = ConfigParserTestFunction("\x07\x00\x03\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1243(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\n\x00\n")
		self.assertEqual(result, expected_result)

	def test_1244(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x0E\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1245(self):
		result = ConfigParserTestFunction("\n\n\x01\x02\x00\x00\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_1246(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x03\x01\x00\x00\x04")
		self.assertEqual(result, expected_result)

	def test_1247(self):
		result = ConfigParserTestFunction("\n\n\n\x01\x01\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1248(self):
		result = ConfigParserTestFunction("\x07\x01\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1249(self):
		result = ConfigParserTestFunction("\n\n\x00\x01\x00\x01\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_1250(self):
		result = ConfigParserTestFunction("\n\n\x06\x01\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1251(self):
		result = ConfigParserTestFunction("\n\n\x04\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1252(self):
		result = ConfigParserTestFunction("\n\n\x06\x00\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1253(self):
		result = ConfigParserTestFunction("\x03\x00\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1254(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x06\x02\x02")
		self.assertEqual(result, expected_result)

	def test_1255(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0F\x00\x01\x01")
		self.assertEqual(result, expected_result)

	def test_1256(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x01\x02\x00")
		self.assertEqual(result, expected_result)

	def test_1257(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x07\x00\x01\x01")
		self.assertEqual(result, expected_result)

	def test_1258(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1259(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x07\x90\x00")
		self.assertEqual(result, expected_result)

	def test_1260(self):
		result = ConfigParserTestFunction("\n\x00\x04\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1261(self):
		result = ConfigParserTestFunction("\n\x06\x01\x00\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1262(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x07\x00\x03")
		self.assertEqual(result, expected_result)

	def test_1263(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x02\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1264(self):
		result = ConfigParserTestFunction("\x06\x00\x03\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1265(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x04\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1266(self):
		result = ConfigParserTestFunction("\n\x00\x03\x00\x00\x00\x01\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1267(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x03\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1268(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x1B\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1269(self):
		result = ConfigParserTestFunction("\n\n\x02\x00\x00\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1270(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0E\x11\x00")
		self.assertEqual(result, expected_result)

	def test_1271(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xEB")
		self.assertEqual(result, expected_result)

	def test_1272(self):
		result = ConfigParserTestFunction("\n\n\x0E\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1273(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x01\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1274(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x01\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1275(self):
		result = ConfigParserTestFunction("\n\x01\x01\x01\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1276(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x04\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1277(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x00\x01\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1278(self):
		result = ConfigParserTestFunction("\x05\x00\x00\x00\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_1279(self):
		result = ConfigParserTestFunction("\n\x00\x01\x01\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1280(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x01\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_1281(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1282(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0D\x01")
		self.assertEqual(result, expected_result)

	def test_1283(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x03\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_1284(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x04\x02\x01")
		self.assertEqual(result, expected_result)

	def test_1285(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1286(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x07\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1287(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x08\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1288(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\t\x01")
		self.assertEqual(result, expected_result)

	def test_1289(self):
		result = ConfigParserTestFunction("\n\n\x01\x01\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1290(self):
		result = ConfigParserTestFunction("\x04\x00\x00\x00\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_1291(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0D\n\n\x02")
		self.assertEqual(result, expected_result)

	def test_1292(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1293(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xD7")
		self.assertEqual(result, expected_result)

	def test_1294(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\n\x05")
		self.assertEqual(result, expected_result)

	def test_1295(self):
		result = ConfigParserTestFunction("\n\n\n\n\x04\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1296(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x01\x00\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_1297(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0B\x06\x00")
		self.assertEqual(result, expected_result)

	def test_1298(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x00\x01\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1299(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0F\x00\x01\x00\n")
		self.assertEqual(result, expected_result)

	def test_1300(self):
		result = ConfigParserTestFunction("\n\n\n\n\x04\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1301(self):
		result = ConfigParserTestFunction("\x06\x01\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1302(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xFB")
		self.assertEqual(result, expected_result)

	def test_1303(self):
		result = ConfigParserTestFunction("\n\x03\x00\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_1304(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x04\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1305(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x0B\x00")
		self.assertEqual(result, expected_result)

	def test_1306(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1307(self):
		result = ConfigParserTestFunction("\n\n\n\n\x03\x01\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1308(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x0E\n\x00")
		self.assertEqual(result, expected_result)

	def test_1309(self):
		result = ConfigParserTestFunction("\n\x02\x00\x00\x00\x00\x04\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1310(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x02\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1311(self):
		result = ConfigParserTestFunction("\n\n\n\x08\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1312(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\x01\n")
		self.assertEqual(result, expected_result)

	def test_1313(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x00\x00\x00\x07")
		self.assertEqual(result, expected_result)

	def test_1314(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x02\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1315(self):
		result = ConfigParserTestFunction("\n\n\x00\x01\x00\x00\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_1316(self):
		result = ConfigParserTestFunction("\n\n\n\n\x06\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1317(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x04\x01")
		self.assertEqual(result, expected_result)

	def test_1318(self):
		result = ConfigParserTestFunction("\n\x03\x01\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1319(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0E\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_1320(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x00\x00\x00\x01\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1321(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x02\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_1322(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x07\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_1323(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x08\x11\x00")
		self.assertEqual(result, expected_result)

	def test_1324(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x02\x02")
		self.assertEqual(result, expected_result)

	def test_1325(self):
		result = ConfigParserTestFunction("\n\x01\x01\x00\x00\x00\x04\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1326(self):
		result = ConfigParserTestFunction("\n\n\n\x07\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1327(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0E\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1328(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x03\x03\x00")
		self.assertEqual(result, expected_result)

	def test_1329(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x04\x02\x00")
		self.assertEqual(result, expected_result)

	def test_1330(self):
		result = ConfigParserTestFunction("\n\n\n\n\x04\x04\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1331(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x08\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1332(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x00\x00\x01\x02\n")
		self.assertEqual(result, expected_result)

	def test_1333(self):
		result = ConfigParserTestFunction("\n\n\x03\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1334(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x08\x0D\x00")
		self.assertEqual(result, expected_result)

	def test_1335(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x03\x01\x00\n")
		self.assertEqual(result, expected_result)

	def test_1336(self):
		result = ConfigParserTestFunction("\n\x00\x01\x00\x00\x00\x00\x01\x00\x02")
		self.assertEqual(result, expected_result)

	def test_1337(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_1338(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x03\x00\x03\n")
		self.assertEqual(result, expected_result)

	def test_1339(self):
		result = ConfigParserTestFunction("\n\x00\x02\x00\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1340(self):
		result = ConfigParserTestFunction("\x04\x00\x00\x00\x00\x00\x00\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_1341(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xA8")
		self.assertEqual(result, expected_result)

	def test_1342(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x01\x07")
		self.assertEqual(result, expected_result)

	def test_1343(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x08\x01")
		self.assertEqual(result, expected_result)

	def test_1344(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x00\x01\x02")
		self.assertEqual(result, expected_result)

	def test_1345(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x1A\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1346(self):
		result = ConfigParserTestFunction("\n\x00\x02\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1347(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x01\x00\x02\x00")
		self.assertEqual(result, expected_result)

	def test_1348(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\t\x06\x00")
		self.assertEqual(result, expected_result)

	def test_1349(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x01\x00\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_1350(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x00\x02\x02")
		self.assertEqual(result, expected_result)

	def test_1351(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00G\n")
		self.assertEqual(result, expected_result)

	def test_1352(self):
		result = ConfigParserTestFunction("\n\x01\x00\x00\x00\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1353(self):
		result = ConfigParserTestFunction("\n\x02\x00\x00\x01\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1354(self):
		result = ConfigParserTestFunction("\n\n\x07\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1355(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0F\x02\x00")
		self.assertEqual(result, expected_result)

	def test_1356(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x04\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1357(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x01\x05\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1358(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x02\x10\x00")
		self.assertEqual(result, expected_result)

	def test_1359(self):
		result = ConfigParserTestFunction("\x03\x01\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1360(self):
		result = ConfigParserTestFunction("\x03\n\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1361(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x07\x05")
		self.assertEqual(result, expected_result)

	def test_1362(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x03\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1363(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x00\x06")
		self.assertEqual(result, expected_result)

	def test_1364(self):
		result = ConfigParserTestFunction("\n\n\n\x05\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1365(self):
		result = ConfigParserTestFunction("\n\n\x04\x00\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_1366(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x06\x80\x00")
		self.assertEqual(result, expected_result)

	def test_1367(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1368(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x06\x03")
		self.assertEqual(result, expected_result)

	def test_1369(self):
		result = ConfigParserTestFunction("\n\x03\x00\x00\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1370(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x08\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1371(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x01\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1372(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x07\x11\x00")
		self.assertEqual(result, expected_result)

	def test_1373(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x1F\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1374(self):
		result = ConfigParserTestFunction("\n\x07\x01\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1375(self):
		result = ConfigParserTestFunction("\n\n\n\x08\x01\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_1376(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x07\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1377(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x00\x00\x03\n\x00")
		self.assertEqual(result, expected_result)

	def test_1378(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x08\x12\x00")
		self.assertEqual(result, expected_result)

	def test_1379(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1380(self):
		result = ConfigParserTestFunction("\x03\x00\x00\x00\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_1381(self):
		result = ConfigParserTestFunction("\x02\x03\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1382(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x06\x03\x01")
		self.assertEqual(result, expected_result)

	def test_1383(self):
		result = ConfigParserTestFunction("\n\n\n\x01\x00\x01\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1384(self):
		result = ConfigParserTestFunction("\n\n\n\x0E\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1385(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x07\x00\x01\x03")
		self.assertEqual(result, expected_result)

	def test_1386(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x00\x07\n\x00")
		self.assertEqual(result, expected_result)

	def test_1387(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x01\x05\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1388(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x00\x00\x00\x02\n\x00")
		self.assertEqual(result, expected_result)

	def test_1389(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x18\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1390(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x08\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1391(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x08\x01\x00\n")
		self.assertEqual(result, expected_result)

	def test_1392(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n+")
		self.assertEqual(result, expected_result)

	def test_1393(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x02\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1394(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xE8")
		self.assertEqual(result, expected_result)

	def test_1395(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1396(self):
		result = ConfigParserTestFunction("\x01\x00\x00\x00\x00\x00\x00\x00\x03\n")
		self.assertEqual(result, expected_result)

	def test_1397(self):
		result = ConfigParserTestFunction("\n\n\x0F\x00\x00\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_1398(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x01G")
		self.assertEqual(result, expected_result)

	def test_1399(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1400(self):
		result = ConfigParserTestFunction("\x04\x01\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1401(self):
		result = ConfigParserTestFunction("\n\x03\x01\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_1402(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x00\x01\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_1403(self):
		result = ConfigParserTestFunction("\n\x03\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1404(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x02\x02\x01\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1405(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x00\x00\x02\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1406(self):
		result = ConfigParserTestFunction("\n\x01\x00\x00\x01\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1407(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x02\x01\x00\x01")
		self.assertEqual(result, expected_result)

	def test_1408(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0F\x11\x00")
		self.assertEqual(result, expected_result)

	def test_1409(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x00\x01\x01\n")
		self.assertEqual(result, expected_result)

	def test_1410(self):
		result = ConfigParserTestFunction("\n\n\n\n\x05\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1411(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\x02\n")
		self.assertEqual(result, expected_result)

	def test_1412(self):
		result = ConfigParserTestFunction("\x04\x01\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1413(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x00\x00\x02\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1414(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x00\x00\x00\x01\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1415(self):
		result = ConfigParserTestFunction("\n\n\x07\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1416(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x03\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1417(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x05\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1418(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0E\x05")
		self.assertEqual(result, expected_result)

	def test_1419(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x02\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1420(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x03\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1421(self):
		result = ConfigParserTestFunction("\n\n\n\x07\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_1422(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x00\x00G")
		self.assertEqual(result, expected_result)

	def test_1423(self):
		result = ConfigParserTestFunction("\n\x01\x01\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1424(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0E\x03")
		self.assertEqual(result, expected_result)

	def test_1425(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x04\x03\x01")
		self.assertEqual(result, expected_result)

	def test_1426(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\t\x02")
		self.assertEqual(result, expected_result)

	def test_1427(self):
		result = ConfigParserTestFunction("\n\x08\x00\x00\x00\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1428(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x08\x00\x01\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1429(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\x03\x00")
		self.assertEqual(result, expected_result)

	def test_1430(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x07\x01\x03")
		self.assertEqual(result, expected_result)

	def test_1431(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x07\x03\x00")
		self.assertEqual(result, expected_result)

	def test_1432(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\x04\x00")
		self.assertEqual(result, expected_result)

	def test_1433(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x05\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1434(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x03\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_1435(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nG")
		self.assertEqual(result, expected_result)

	def test_1436(self):
		result = ConfigParserTestFunction("\n\x00\x01\x00\x01\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1437(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x03\x02\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1438(self):
		result = ConfigParserTestFunction("\n\n\x00\x01\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1439(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x04\n")
		self.assertEqual(result, expected_result)

	def test_1440(self):
		result = ConfigParserTestFunction("\x02\x00\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1441(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0E\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1442(self):
		result = ConfigParserTestFunction("\x03\x03\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1443(self):
		result = ConfigParserTestFunction("\n\x07\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1444(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x04\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1445(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_1446(self):
		result = ConfigParserTestFunction("\n\x01\x00\x00\x00\x00\x05\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1447(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x02\x11\x00")
		self.assertEqual(result, expected_result)

	def test_1448(self):
		result = ConfigParserTestFunction("\n\n\n\x06\x00\x02\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1449(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\x02\x00")
		self.assertEqual(result, expected_result)

	def test_1450(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x07\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1451(self):
		result = ConfigParserTestFunction("\n\x01\x07\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1452(self):
		result = ConfigParserTestFunction("\n\n\x08\x00\x02\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1453(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0F\x01\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1454(self):
		result = ConfigParserTestFunction("\n\n\x06\x00\x00\x00\x01\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1455(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x04\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1456(self):
		result = ConfigParserTestFunction("\n\x06\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1457(self):
		result = ConfigParserTestFunction("\n\x01\x00\x00\x01\x00\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1458(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x02\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_1459(self):
		result = ConfigParserTestFunction("\n\n\n\x04\x02\x00\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1460(self):
		result = ConfigParserTestFunction("\n\n\x01\x00\x00\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_1461(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x0E\x02\x00")
		self.assertEqual(result, expected_result)

	def test_1462(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xA7")
		self.assertEqual(result, expected_result)

	def test_1463(self):
		result = ConfigParserTestFunction("\n\n\x01\x03\x00\x01\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1464(self):
		result = ConfigParserTestFunction("\n\x03\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1465(self):
		result = ConfigParserTestFunction("\n\x03\x00\x00\x01\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_1466(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x00\x05")
		self.assertEqual(result, expected_result)

	def test_1467(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0E\x81\x00")
		self.assertEqual(result, expected_result)

	def test_1468(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0E\x02\x00")
		self.assertEqual(result, expected_result)

	def test_1469(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x01\x04\n\x00")
		self.assertEqual(result, expected_result)

	def test_1470(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x02\x00\x00\x01\x05")
		self.assertEqual(result, expected_result)

	def test_1471(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x05\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1472(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0F\x10\x00")
		self.assertEqual(result, expected_result)

	def test_1473(self):
		result = ConfigParserTestFunction("\n\x0B\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1474(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x03\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1475(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x00\x07\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1476(self):
		result = ConfigParserTestFunction("\n\x02\x01\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1477(self):
		result = ConfigParserTestFunction("\n\x01\x01\x00\x00\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_1478(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0E\x00\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1479(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0B\x02")
		self.assertEqual(result, expected_result)

	def test_1480(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x00\x01\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1481(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_1482(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1483(self):
		result = ConfigParserTestFunction("\n\n\n\n\x03\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1484(self):
		result = ConfigParserTestFunction("\n\x00\x00\x01\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1485(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x00\x12\x00")
		self.assertEqual(result, expected_result)

	def test_1486(self):
		result = ConfigParserTestFunction("\n\n\x02\x00\x00\x00\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_1487(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1488(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x06\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1489(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x04\x00\x00\x02\x04")
		self.assertEqual(result, expected_result)

	def test_1490(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x01\x01\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1491(self):
		result = ConfigParserTestFunction("\x00\x01\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1492(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x00\x02\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1493(self):
		result = ConfigParserTestFunction("\n\x03\x00\x00\x01\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1494(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0E\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_1495(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x03\x02")
		self.assertEqual(result, expected_result)

	def test_1496(self):
		result = ConfigParserTestFunction("\n\n\x01\x00\x00\x00\x00\x01\x00\x03")
		self.assertEqual(result, expected_result)

	def test_1497(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x00\x00\x03\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1498(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x06\x03\x02")
		self.assertEqual(result, expected_result)

	def test_1499(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xBB")
		self.assertEqual(result, expected_result)

	def test_1500(self):
		result = ConfigParserTestFunction("\n\n\x03\x01\x00\x00\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1501(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x01\x00\x00\x01\x07")
		self.assertEqual(result, expected_result)

	def test_1502(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0F\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1503(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x06\x11\x00")
		self.assertEqual(result, expected_result)

	def test_1504(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x01\x00\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1505(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x07\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1506(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x02\x01\n")
		self.assertEqual(result, expected_result)

	def test_1507(self):
		result = ConfigParserTestFunction("\x03\x00\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1508(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x03\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1509(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x03\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1510(self):
		result = ConfigParserTestFunction("\n\x00\x04\x00\x00\x01\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1511(self):
		result = ConfigParserTestFunction("\n\n\x05\x00\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_1512(self):
		result = ConfigParserTestFunction("\n\x00\x01\x01\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1513(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x04\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_1514(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x00\x00\x00\x05\n")
		self.assertEqual(result, expected_result)

	def test_1515(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x03\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1516(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x00\x01\x06")
		self.assertEqual(result, expected_result)

	def test_1517(self):
		result = ConfigParserTestFunction("\n\n\x00\x01\x00\x00\x00\x00\x00E")
		self.assertEqual(result, expected_result)

	def test_1518(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0C\x00")
		self.assertEqual(result, expected_result)

	def test_1519(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x01\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_1520(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x07\x81\x00")
		self.assertEqual(result, expected_result)

	def test_1521(self):
		result = ConfigParserTestFunction("\n\x0E\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1522(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_1523(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x01\x00\x05\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1524(self):
		result = ConfigParserTestFunction("\n\n\x06\x01\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1525(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x01\x00\x01\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1526(self):
		result = ConfigParserTestFunction("\n\x07\x01\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1527(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\x02\n")
		self.assertEqual(result, expected_result)

	def test_1528(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\x01\x00\x05\n")
		self.assertEqual(result, expected_result)

	def test_1529(self):
		result = ConfigParserTestFunction("\n\x02\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1530(self):
		result = ConfigParserTestFunction("\n\n\x03\x00\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1531(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x01\x00\x01\x01\x00\n")
		self.assertEqual(result, expected_result)

	def test_1532(self):
		result = ConfigParserTestFunction("\n\n\x00\x02\x00\x00\x00\x01\x00\x01")
		self.assertEqual(result, expected_result)

	def test_1533(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x0E\x00\x02")
		self.assertEqual(result, expected_result)

	def test_1534(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x07\x03")
		self.assertEqual(result, expected_result)

	def test_1535(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x06\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1536(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x01\x02\n\x00")
		self.assertEqual(result, expected_result)

	def test_1537(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1538(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x07\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_1539(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x07\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1540(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0B\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1541(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x00\x01\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1542(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\n\n\x01")
		self.assertEqual(result, expected_result)

	def test_1543(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xC7")
		self.assertEqual(result, expected_result)

	def test_1544(self):
		result = ConfigParserTestFunction("\n\n\n\x0C\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1545(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x00\x00\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_1546(self):
		result = ConfigParserTestFunction("\n\x00\x02\x00\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1547(self):
		result = ConfigParserTestFunction("\x02\x00\x01\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1548(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0B\x08\x00")
		self.assertEqual(result, expected_result)

	def test_1549(self):
		result = ConfigParserTestFunction("\x02\x03\x00\x00\x00\x00\x00\x01\x00\n")
		self.assertEqual(result, expected_result)

	def test_1550(self):
		result = ConfigParserTestFunction("\n\n\x07\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1551(self):
		result = ConfigParserTestFunction("\n\n\n\n\x03\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1552(self):
		result = ConfigParserTestFunction("\n\x02\x00\x00\x00\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_1553(self):
		result = ConfigParserTestFunction("\n\n\x06\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1554(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x01\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_1555(self):
		result = ConfigParserTestFunction("\x00\x00\x01\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1556(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x01\x00\x02")
		self.assertEqual(result, expected_result)

	def test_1557(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0F\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1558(self):
		result = ConfigParserTestFunction("\x01\x04\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1559(self):
		result = ConfigParserTestFunction("\n\n\n\n\x05\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1560(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x00\x01\x00\x01")
		self.assertEqual(result, expected_result)

	def test_1561(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n,")
		self.assertEqual(result, expected_result)

	def test_1562(self):
		result = ConfigParserTestFunction("\n\x05\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1563(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x03\x01\n")
		self.assertEqual(result, expected_result)

	def test_1564(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x02\x00\n")
		self.assertEqual(result, expected_result)

	def test_1565(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\x07\x00")
		self.assertEqual(result, expected_result)

	def test_1566(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x03\x02\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1567(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x08\x03\x00")
		self.assertEqual(result, expected_result)

	def test_1568(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x07\x00")
		self.assertEqual(result, expected_result)

	def test_1569(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x06\x07\x01")
		self.assertEqual(result, expected_result)

	def test_1570(self):
		result = ConfigParserTestFunction("\n\x00\x01\x00\x00\x00\x00\x00\x03\n")
		self.assertEqual(result, expected_result)

	def test_1571(self):
		result = ConfigParserTestFunction("\n\n\n\x07\x01\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1572(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x00\x00\x00\x02\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1573(self):
		result = ConfigParserTestFunction("\n\x0F\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1574(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0E\x01\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1575(self):
		result = ConfigParserTestFunction("\x05\x01\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1576(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x01\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1577(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x00\x04\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1578(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x00\x01\x01\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1579(self):
		result = ConfigParserTestFunction("\n\x04\x00\x00\x00\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1580(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x02\x03\x00")
		self.assertEqual(result, expected_result)

	def test_1581(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x00\x01\x03")
		self.assertEqual(result, expected_result)

	def test_1582(self):
		result = ConfigParserTestFunction("\n\n\n\n\x07\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1583(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1584(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x06\x03")
		self.assertEqual(result, expected_result)

	def test_1585(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0E\x01\x01\n")
		self.assertEqual(result, expected_result)

	def test_1586(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x01\x11\x00")
		self.assertEqual(result, expected_result)

	def test_1587(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x00\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1588(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x07\x02\x00")
		self.assertEqual(result, expected_result)

	def test_1589(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x04\x07\x01")
		self.assertEqual(result, expected_result)

	def test_1590(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x03\x10\x00")
		self.assertEqual(result, expected_result)

	def test_1591(self):
		result = ConfigParserTestFunction("\x01\x01\x00\x00\x01\x00\x00\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1592(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x02\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1593(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x03\x02\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1594(self):
		result = ConfigParserTestFunction("\n\n\x03\x00\x01\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1595(self):
		result = ConfigParserTestFunction("\x04\x00\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1596(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0E\x07")
		self.assertEqual(result, expected_result)

	def test_1597(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1598(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x00\x00\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1599(self):
		result = ConfigParserTestFunction("\n\n\n\x04\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1600(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x00\x02\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1601(self):
		result = ConfigParserTestFunction("\n\n\n\n\x08\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1602(self):
		result = ConfigParserTestFunction("\n\x01\x05\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1603(self):
		result = ConfigParserTestFunction("\n\x00\x01\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1604(self):
		result = ConfigParserTestFunction("\n\x07\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1605(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0F\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1606(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x00\x05")
		self.assertEqual(result, expected_result)

	def test_1607(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\x02\n")
		self.assertEqual(result, expected_result)

	def test_1608(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x01\x00\x00\x03\n")
		self.assertEqual(result, expected_result)

	def test_1609(self):
		result = ConfigParserTestFunction("\n\n\x01\x00\x00\x00\x00\x00\x03\n")
		self.assertEqual(result, expected_result)

	def test_1610(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x02\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_1611(self):
		result = ConfigParserTestFunction("\n\n\n\x01\x02\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1612(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x9E")
		self.assertEqual(result, expected_result)

	def test_1613(self):
		result = ConfigParserTestFunction("\n\n\x0E\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1614(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x03\x00\x01")
		self.assertEqual(result, expected_result)

	def test_1615(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\x00\x03")
		self.assertEqual(result, expected_result)

	def test_1616(self):
		result = ConfigParserTestFunction("\x03\x01\x00\x00\x00\x00\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_1617(self):
		result = ConfigParserTestFunction("\n\n\x04\x00\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1618(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1619(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0F\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1620(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x07\x05\n")
		self.assertEqual(result, expected_result)

	def test_1621(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x03\x80\x00")
		self.assertEqual(result, expected_result)

	def test_1622(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x02\x01\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_1623(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x07\x00\x04")
		self.assertEqual(result, expected_result)

	def test_1624(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xC8")
		self.assertEqual(result, expected_result)

	def test_1625(self):
		result = ConfigParserTestFunction("\n\n\n\n\x07\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1626(self):
		result = ConfigParserTestFunction("\n\n\x0F\x00\x00\x00\x01\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_1627(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\ng")
		self.assertEqual(result, expected_result)

	def test_1628(self):
		result = ConfigParserTestFunction("\x05\x00\x00\x00\x00\x00\x00\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_1629(self):
		result = ConfigParserTestFunction("\n\n\n\x01\x00\x00\x00\x01\x00\n")
		self.assertEqual(result, expected_result)

	def test_1630(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x01\x81\x00")
		self.assertEqual(result, expected_result)

	def test_1631(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x00\x02\x01\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1632(self):
		result = ConfigParserTestFunction("\n\n\x0B\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1633(self):
		result = ConfigParserTestFunction("\n\n\x00\x01\x00\x00\x00\x00\x01\x06")
		self.assertEqual(result, expected_result)

	def test_1634(self):
		result = ConfigParserTestFunction("\n\n\x01\x00\x00\x00\x00\x00\x04\n")
		self.assertEqual(result, expected_result)

	def test_1635(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0D\n")
		self.assertEqual(result, expected_result)

	def test_1636(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x01\x01\x03")
		self.assertEqual(result, expected_result)

	def test_1637(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x07\x00\x00\x07")
		self.assertEqual(result, expected_result)

	def test_1638(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x07\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1639(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x01\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_1640(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n|")
		self.assertEqual(result, expected_result)

	def test_1641(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x03\x01\x02\n")
		self.assertEqual(result, expected_result)

	def test_1642(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0D\n\n\x03")
		self.assertEqual(result, expected_result)

	def test_1643(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0E\x01\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_1644(self):
		result = ConfigParserTestFunction("\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1645(self):
		result = ConfigParserTestFunction("\x00\x00\x01\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1646(self):
		result = ConfigParserTestFunction("\n\n\x04\x00\x02\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1647(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x07\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1648(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\x00\x00\x03\x01")
		self.assertEqual(result, expected_result)

	def test_1649(self):
		result = ConfigParserTestFunction("\x01\x00\x00\x01\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1650(self):
		result = ConfigParserTestFunction("\n\x0B\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1651(self):
		result = ConfigParserTestFunction("\n\n\n\x0E\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1652(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x08\x81\x00")
		self.assertEqual(result, expected_result)

	def test_1653(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x01\x00\x07")
		self.assertEqual(result, expected_result)

	def test_1654(self):
		result = ConfigParserTestFunction("\n\x03\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1655(self):
		result = ConfigParserTestFunction("\n\n\x0B\x01\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1656(self):
		result = ConfigParserTestFunction("\n\n\n\x08\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1657(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xDE")
		self.assertEqual(result, expected_result)

	def test_1658(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1659(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x02\n\x00")
		self.assertEqual(result, expected_result)

	def test_1660(self):
		result = ConfigParserTestFunction("\n\n\n\x01\x02\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1661(self):
		result = ConfigParserTestFunction("\n\n\n\n\x06\x02\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1662(self):
		result = ConfigParserTestFunction("\n\n\x07\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1663(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x94")
		self.assertEqual(result, expected_result)

	def test_1664(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x01\x04")
		self.assertEqual(result, expected_result)

	def test_1665(self):
		result = ConfigParserTestFunction("\n\n\x04\x01\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1666(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\t\x04\x00")
		self.assertEqual(result, expected_result)

	def test_1667(self):
		result = ConfigParserTestFunction("\x03\x00\x00\x00\x00\x00\x03\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1668(self):
		result = ConfigParserTestFunction("\n\n\x01\x01\x01\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1669(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x93")
		self.assertEqual(result, expected_result)

	def test_1670(self):
		result = ConfigParserTestFunction("\n\n\n\n\x08\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1671(self):
		result = ConfigParserTestFunction("\n\n\x00\x02\x00\x00\x00\x02\n\x00")
		self.assertEqual(result, expected_result)

	def test_1672(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x02\x00\x05")
		self.assertEqual(result, expected_result)

	def test_1673(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xAB")
		self.assertEqual(result, expected_result)

	def test_1674(self):
		result = ConfigParserTestFunction("\n\x0E\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1675(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x06\x00")
		self.assertEqual(result, expected_result)

	def test_1676(self):
		result = ConfigParserTestFunction("\n\n\n\x06\x01\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1677(self):
		result = ConfigParserTestFunction("\x03\x02\x01\x00\x00\x00\x00\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_1678(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\x02\x02")
		self.assertEqual(result, expected_result)

	def test_1679(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x07\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_1680(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0F\x80\x00")
		self.assertEqual(result, expected_result)

	def test_1681(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x00\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_1682(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x03\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1683(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x0B\x01\n")
		self.assertEqual(result, expected_result)

	def test_1684(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xE7")
		self.assertEqual(result, expected_result)

	def test_1685(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x07\x12\x00")
		self.assertEqual(result, expected_result)

	def test_1686(self):
		result = ConfigParserTestFunction("\n\x01\x01\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1687(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x04\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_1688(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x01\x01\x01\x01")
		self.assertEqual(result, expected_result)

	def test_1689(self):
		result = ConfigParserTestFunction("\n\n\n\x04\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1690(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0C\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1691(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x01\x00\x01")
		self.assertEqual(result, expected_result)

	def test_1692(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x07\x00\x01\x05")
		self.assertEqual(result, expected_result)

	def test_1693(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x07\x02\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1694(self):
		result = ConfigParserTestFunction("\n\n\n\x05\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1695(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\x03\n")
		self.assertEqual(result, expected_result)

	def test_1696(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x02\x05\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1697(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1698(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1699(self):
		result = ConfigParserTestFunction("\n\x01\x03\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1700(self):
		result = ConfigParserTestFunction("\x0F\x01\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1701(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nJ")
		self.assertEqual(result, expected_result)

	def test_1702(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\x02\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1703(self):
		result = ConfigParserTestFunction("\x06\x00\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1704(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0B\x04\x00")
		self.assertEqual(result, expected_result)

	def test_1705(self):
		result = ConfigParserTestFunction("\n\n\n\n\x05\x01\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1706(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0B\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1707(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\t\x03")
		self.assertEqual(result, expected_result)

	def test_1708(self):
		result = ConfigParserTestFunction("\n\n\x04\x00\x01\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1709(self):
		result = ConfigParserTestFunction("\n\n\n\x06\x01\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1710(self):
		result = ConfigParserTestFunction("\n\n\n\x01\x03\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1711(self):
		result = ConfigParserTestFunction("\n\n\x08\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1712(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x03\x04")
		self.assertEqual(result, expected_result)

	def test_1713(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x00\x80\x00")
		self.assertEqual(result, expected_result)

	def test_1714(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\x06\x00")
		self.assertEqual(result, expected_result)

	def test_1715(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x08\x04")
		self.assertEqual(result, expected_result)

	def test_1716(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x00\x03\x02")
		self.assertEqual(result, expected_result)

	def test_1717(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07")
		self.assertEqual(result, expected_result)

	def test_1718(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x02\x01\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1719(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x0E\x01\x01")
		self.assertEqual(result, expected_result)

	def test_1720(self):
		result = ConfigParserTestFunction("\x03\x02\x00\x00\x00\x00\x00\x00\x01\x05")
		self.assertEqual(result, expected_result)

	def test_1721(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x00\x02\x06")
		self.assertEqual(result, expected_result)

	def test_1722(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x07\x03\x00")
		self.assertEqual(result, expected_result)

	def test_1723(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\x01\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1724(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x01\x00\x03\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1725(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x05\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1726(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1727(self):
		result = ConfigParserTestFunction("\n\n\x07\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1728(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n^")
		self.assertEqual(result, expected_result)

	def test_1729(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\x02\x00\x05\n")
		self.assertEqual(result, expected_result)

	def test_1730(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\x00\x02\n\x00")
		self.assertEqual(result, expected_result)

	def test_1731(self):
		result = ConfigParserTestFunction("\n\x0B\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1732(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\x03\x01")
		self.assertEqual(result, expected_result)

	def test_1733(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0D\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1734(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x07\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1735(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0E\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1736(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x07\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1737(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\n\n\x02")
		self.assertEqual(result, expected_result)

	def test_1738(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x01\x07\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1739(self):
		result = ConfigParserTestFunction("\n\n\n\x0E\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1740(self):
		result = ConfigParserTestFunction("\n\n\n\x04\x01\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1741(self):
		result = ConfigParserTestFunction("\n\n\x03\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1742(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xF8")
		self.assertEqual(result, expected_result)

	def test_1743(self):
		result = ConfigParserTestFunction("\n\n\n\n\x04\x05\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1744(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x01\x05\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1745(self):
		result = ConfigParserTestFunction("\n\x06\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1746(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0D\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1747(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x03\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1748(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x07\x00\x05")
		self.assertEqual(result, expected_result)

	def test_1749(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x01\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_1750(self):
		result = ConfigParserTestFunction("\n\x0E\x01\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1751(self):
		result = ConfigParserTestFunction("\n\n\n\x07\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1752(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x0B\x02\n")
		self.assertEqual(result, expected_result)

	def test_1753(self):
		result = ConfigParserTestFunction("\n\x0E\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1754(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0F\x12\x00")
		self.assertEqual(result, expected_result)

	def test_1755(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x01\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_1756(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x06\x05\n")
		self.assertEqual(result, expected_result)

	def test_1757(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x02\x07")
		self.assertEqual(result, expected_result)

	def test_1758(self):
		result = ConfigParserTestFunction("\n\n\n\n\x06\x03\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1759(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x08\n\x00")
		self.assertEqual(result, expected_result)

	def test_1760(self):
		result = ConfigParserTestFunction("\n\n\n\n\x07\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1761(self):
		result = ConfigParserTestFunction("\n\n\x00\x03\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_1762(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\x00\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1763(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x07\x01\x05")
		self.assertEqual(result, expected_result)

	def test_1764(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x08\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1765(self):
		result = ConfigParserTestFunction("\x06\x02\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1766(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x00\x00\x00\x06")
		self.assertEqual(result, expected_result)

	def test_1767(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x00\x01\x00\x03")
		self.assertEqual(result, expected_result)

	def test_1768(self):
		result = ConfigParserTestFunction("\n\x03\x00\x00\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_1769(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0F\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1770(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x04\x04")
		self.assertEqual(result, expected_result)

	def test_1771(self):
		result = ConfigParserTestFunction("\n\n\x02\x00\x00\x00\x02\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1772(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x00\x01\x00\x01\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_1773(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0B\x03")
		self.assertEqual(result, expected_result)

	def test_1774(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x00\x00\x00\x02\x02\x00")
		self.assertEqual(result, expected_result)

	def test_1775(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0E\x12\x00")
		self.assertEqual(result, expected_result)

	def test_1776(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x02\x00\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_1777(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x0B\x03\n")
		self.assertEqual(result, expected_result)

	def test_1778(self):
		result = ConfigParserTestFunction("\n\x0B\x01\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1779(self):
		result = ConfigParserTestFunction("\n\x01\x01\x01\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1780(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x07\x00\x02\x03")
		self.assertEqual(result, expected_result)

	def test_1781(self):
		result = ConfigParserTestFunction("\n\n\x03\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1782(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x07\x13\x00")
		self.assertEqual(result, expected_result)

	def test_1783(self):
		result = ConfigParserTestFunction("\n\n\n\n\x06\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1784(self):
		result = ConfigParserTestFunction("\n\n\x01\x04\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1785(self):
		result = ConfigParserTestFunction("\n\x00\x04\x00\x00\x00\x00\x01\x00\n")
		self.assertEqual(result, expected_result)

	def test_1786(self):
		result = ConfigParserTestFunction("\n\n\n\n\x07\x01\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1787(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n7")
		self.assertEqual(result, expected_result)

	def test_1788(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_1789(self):
		result = ConfigParserTestFunction("\n\n\n\x0C\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1790(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\x07\n")
		self.assertEqual(result, expected_result)

	def test_1791(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x05\x02\x00")
		self.assertEqual(result, expected_result)

	def test_1792(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x02\x00\x01")
		self.assertEqual(result, expected_result)

	def test_1793(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x04\x00")
		self.assertEqual(result, expected_result)

	def test_1794(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\t\x07")
		self.assertEqual(result, expected_result)

	def test_1795(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x03\x00\n")
		self.assertEqual(result, expected_result)

	def test_1796(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x01\x00\x04")
		self.assertEqual(result, expected_result)

	def test_1797(self):
		result = ConfigParserTestFunction("\n\x03\x04\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1798(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x02\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1799(self):
		result = ConfigParserTestFunction("\n\n\x04\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1800(self):
		result = ConfigParserTestFunction("\n\x02\x00\x00\x00\x00\x00\x02\n\x00")
		self.assertEqual(result, expected_result)

	def test_1801(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x08\x13\x00")
		self.assertEqual(result, expected_result)

	def test_1802(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0C\x01")
		self.assertEqual(result, expected_result)

	def test_1803(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x02\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1804(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04")
		self.assertEqual(result, expected_result)

	def test_1805(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0B\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_1806(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x00\x01\x00\x03\n")
		self.assertEqual(result, expected_result)

	def test_1807(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xAC")
		self.assertEqual(result, expected_result)

	def test_1808(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x02\x04")
		self.assertEqual(result, expected_result)

	def test_1809(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\x01\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1810(self):
		result = ConfigParserTestFunction("\n\n\n\x04\x00\x01\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1811(self):
		result = ConfigParserTestFunction("\n\n\x01\x01\x00\x01\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1812(self):
		result = ConfigParserTestFunction("\n\x0B\x02\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1813(self):
		result = ConfigParserTestFunction("\x02\x00\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1814(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0F\x02\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1815(self):
		result = ConfigParserTestFunction("\n\n\x04\x01\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_1816(self):
		result = ConfigParserTestFunction("\n\n\n\x06\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1817(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x01\x01\x05")
		self.assertEqual(result, expected_result)

	def test_1818(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x02\x01\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_1819(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x01\x00\x00\x06")
		self.assertEqual(result, expected_result)

	def test_1820(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x05\x03\x00")
		self.assertEqual(result, expected_result)

	def test_1821(self):
		result = ConfigParserTestFunction("\n\n\n\n\x06\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_1822(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x00\x07\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1823(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x01\x00\x02\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1824(self):
		result = ConfigParserTestFunction("\n\n\n\n\x08\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1825(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\x03\x01")
		self.assertEqual(result, expected_result)

	def test_1826(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0E\x00\x00\x05\n")
		self.assertEqual(result, expected_result)

	def test_1827(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\x03\x00\x05\n")
		self.assertEqual(result, expected_result)

	def test_1828(self):
		result = ConfigParserTestFunction("\n\n\x06\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1829(self):
		result = ConfigParserTestFunction("\x03\x00\x00\x00\x00\x00\x00\x00\x00\x07")
		self.assertEqual(result, expected_result)

	def test_1830(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x01\x01\x07")
		self.assertEqual(result, expected_result)

	def test_1831(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x04\x03")
		self.assertEqual(result, expected_result)

	def test_1832(self):
		result = ConfigParserTestFunction("\n\n\n\x0E\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1833(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x06\x02\x00")
		self.assertEqual(result, expected_result)

	def test_1834(self):
		result = ConfigParserTestFunction("\x02\x00\x00\x00\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1835(self):
		result = ConfigParserTestFunction("\n\x01\x01\x00\x00\x00\x01\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_1836(self):
		result = ConfigParserTestFunction("\n\x00\x02\x00\x03\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1837(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1838(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x02\x00\x03\n")
		self.assertEqual(result, expected_result)

	def test_1839(self):
		result = ConfigParserTestFunction("\x05\x01\x00\x00\x00\x00\x00\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_1840(self):
		result = ConfigParserTestFunction("\n\n\n\x08\x00\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1841(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x04\x05")
		self.assertEqual(result, expected_result)

	def test_1842(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x03\x81\x00")
		self.assertEqual(result, expected_result)

	def test_1843(self):
		result = ConfigParserTestFunction("\n\n\n\n\x04\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1844(self):
		result = ConfigParserTestFunction("\x00\x01\x00\x00\x00\x00\x00\x00\x00\x04")
		self.assertEqual(result, expected_result)

	def test_1845(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x01\x01\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1846(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x0F\x00")
		self.assertEqual(result, expected_result)

	def test_1847(self):
		result = ConfigParserTestFunction("\x00\x01\x00\x01\x00\x00\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_1848(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x08\x80\x00")
		self.assertEqual(result, expected_result)

	def test_1849(self):
		result = ConfigParserTestFunction("\x01\x00\x00\x00\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1850(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0D\n\n\x07")
		self.assertEqual(result, expected_result)

	def test_1851(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x00\x01\x07")
		self.assertEqual(result, expected_result)

	def test_1852(self):
		result = ConfigParserTestFunction("\n\n\x0F\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1853(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0E\x01\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1854(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x01\x00\x01\x06")
		self.assertEqual(result, expected_result)

	def test_1855(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x03\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1856(self):
		result = ConfigParserTestFunction("\n\n\x0B\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1857(self):
		result = ConfigParserTestFunction("\n\n\n\n\x04\x01\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1858(self):
		result = ConfigParserTestFunction("\n\n\n\n\x04\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1859(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\x00\x04\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1860(self):
		result = ConfigParserTestFunction("\n\n\n\x08\x01\x00\x00\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1861(self):
		result = ConfigParserTestFunction("\n\n\n\n\x06\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1862(self):
		result = ConfigParserTestFunction("\n\x03\x01\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1863(self):
		result = ConfigParserTestFunction("\x03\x00\x00\x01\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1864(self):
		result = ConfigParserTestFunction("\x04\x01\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1865(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x00\x00\x00\x01\x02")
		self.assertEqual(result, expected_result)

	def test_1866(self):
		result = ConfigParserTestFunction("\x03\x00\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1867(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\n\x08")
		self.assertEqual(result, expected_result)

	def test_1868(self):
		result = ConfigParserTestFunction("\x04\x00\x02\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1869(self):
		result = ConfigParserTestFunction("\n\x03\x01\x01\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_1870(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x01\x02\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1871(self):
		result = ConfigParserTestFunction("\n\x01\x00\x00\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1872(self):
		result = ConfigParserTestFunction("\n\n\n\n\x06\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1873(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0C\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1874(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0D\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1875(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x05\x00")
		self.assertEqual(result, expected_result)

	def test_1876(self):
		result = ConfigParserTestFunction("\n\x03\x00\x01\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1877(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x01\x07")
		self.assertEqual(result, expected_result)

	def test_1878(self):
		result = ConfigParserTestFunction("\n\n\x07\x00\x01\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1879(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\x01\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1880(self):
		result = ConfigParserTestFunction("\n\n\x0D\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1881(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x01\x01\x00\x01")
		self.assertEqual(result, expected_result)

	def test_1882(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\x03\x00")
		self.assertEqual(result, expected_result)

	def test_1883(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x00\x00\x06")
		self.assertEqual(result, expected_result)

	def test_1884(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1885(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0B\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1886(self):
		result = ConfigParserTestFunction("\x00\x01\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1887(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1888(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\n\x07")
		self.assertEqual(result, expected_result)

	def test_1889(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\n\n\x00")
		self.assertEqual(result, expected_result)

	def test_1890(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\n\x00\n")
		self.assertEqual(result, expected_result)

	def test_1891(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x08\x05")
		self.assertEqual(result, expected_result)

	def test_1892(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\n\n\n")
		self.assertEqual(result, expected_result)

	def test_1893(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x00B")
		self.assertEqual(result, expected_result)

	def test_1894(self):
		result = ConfigParserTestFunction("\n\n\x0C\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1895(self):
		result = ConfigParserTestFunction("\x02\x00\x00\x00\x02\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1896(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x00\x00\x00\x00\x01\x02")
		self.assertEqual(result, expected_result)

	def test_1897(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x02\x03\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1898(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x04\x06\x01")
		self.assertEqual(result, expected_result)

	def test_1899(self):
		result = ConfigParserTestFunction("\x03\x00\x00\x01\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1900(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x02\x03")
		self.assertEqual(result, expected_result)

	def test_1901(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x07\x01\x02\x01")
		self.assertEqual(result, expected_result)

	def test_1902(self):
		result = ConfigParserTestFunction("\n\x02\x01\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1903(self):
		result = ConfigParserTestFunction("\n\n\x02\x00\x01\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1904(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x01\x00\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_1905(self):
		result = ConfigParserTestFunction("\n\n\x04\x00\x00\x01\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1906(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x0E\x03\x00")
		self.assertEqual(result, expected_result)

	def test_1907(self):
		result = ConfigParserTestFunction("\n\n\n\x04\x02\x00\x03\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1908(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1909(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0D\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1910(self):
		result = ConfigParserTestFunction("\n\n\n\x06\x00\x03\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1911(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x07\x02\x03")
		self.assertEqual(result, expected_result)

	def test_1912(self):
		result = ConfigParserTestFunction("\n\n\n\x06\x01\x01\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1913(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0F\x03\x00")
		self.assertEqual(result, expected_result)

	def test_1914(self):
		result = ConfigParserTestFunction("\n\n\n\x07\x00\x00\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_1915(self):
		result = ConfigParserTestFunction("\x02\x00\x00\x00\x00\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_1916(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\n\x02")
		self.assertEqual(result, expected_result)

	def test_1917(self):
		result = ConfigParserTestFunction("\n\x0E\x01\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1918(self):
		result = ConfigParserTestFunction("\n\x04\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1919(self):
		result = ConfigParserTestFunction("\n\n\n\x08\x01\x00\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1920(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x07\x04")
		self.assertEqual(result, expected_result)

	def test_1921(self):
		result = ConfigParserTestFunction("\x01\x00\x00\x00\x00\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1922(self):
		result = ConfigParserTestFunction("\x01\x00\x00\x00\x01\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_1923(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xF7")
		self.assertEqual(result, expected_result)

	def test_1924(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0F\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1925(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_1926(self):
		result = ConfigParserTestFunction("\n\n\n\n\x05\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1927(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0E\x91\x00")
		self.assertEqual(result, expected_result)

	def test_1928(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1929(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\n\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1930(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_1931(self):
		result = ConfigParserTestFunction("\x00\x03\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1932(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x00\x00\x01\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1933(self):
		result = ConfigParserTestFunction("\x02\x01\x01\x01\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1934(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1935(self):
		result = ConfigParserTestFunction("\x05\x03\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1936(self):
		result = ConfigParserTestFunction("\n\n\x0B\x00\x00\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_1937(self):
		result = ConfigParserTestFunction("\n\n\x0B\x02\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1938(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x03\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_1939(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x07\x03\n")
		self.assertEqual(result, expected_result)

	def test_1940(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x00\x00\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_1941(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\x03\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1942(self):
		result = ConfigParserTestFunction("\n\n\x04\x01\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1943(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nl")
		self.assertEqual(result, expected_result)

	def test_1944(self):
		result = ConfigParserTestFunction("\n\n\n\n\x03\x00\x00\x01\x00\n")
		self.assertEqual(result, expected_result)

	def test_1945(self):
		result = ConfigParserTestFunction("\n\x01\x00\x00\x00\x00\x03\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1946(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\n\n\x03")
		self.assertEqual(result, expected_result)

	def test_1947(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1948(self):
		result = ConfigParserTestFunction("\n\x02\x00\x00\x00\x00\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_1949(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\x01\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1950(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x1E\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1951(self):
		result = ConfigParserTestFunction("\n\n\x05\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1952(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x07\x00\x01")
		self.assertEqual(result, expected_result)

	def test_1953(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x06\x12\x00")
		self.assertEqual(result, expected_result)

	def test_1954(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x02\x02")
		self.assertEqual(result, expected_result)

	def test_1955(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xCE")
		self.assertEqual(result, expected_result)

	def test_1956(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x04\x03")
		self.assertEqual(result, expected_result)

	def test_1957(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x07\x00\x01\x07")
		self.assertEqual(result, expected_result)

	def test_1958(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\n\x0B")
		self.assertEqual(result, expected_result)

	def test_1959(self):
		result = ConfigParserTestFunction("\n\n\x06\x02\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1960(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x08\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1961(self):
		result = ConfigParserTestFunction("\n\x06\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1962(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\x04\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1963(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x07\x01\x00\x05")
		self.assertEqual(result, expected_result)

	def test_1964(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x00\x00'")
		self.assertEqual(result, expected_result)

	def test_1965(self):
		result = ConfigParserTestFunction("\n\n\n\x04\x01\x00\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1966(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nz")
		self.assertEqual(result, expected_result)

	def test_1967(self):
		result = ConfigParserTestFunction("\n\x0B\x03\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1968(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0E\n")
		self.assertEqual(result, expected_result)

	def test_1969(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x03\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1970(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x01\x01\x01")
		self.assertEqual(result, expected_result)

	def test_1971(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\x03\n")
		self.assertEqual(result, expected_result)

	def test_1972(self):
		result = ConfigParserTestFunction("\n\x00\x02\x00\x00\x00\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_1973(self):
		result = ConfigParserTestFunction("\x00\x01\x00\x00\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_1974(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x05\x00\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1975(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\n\n\x01")
		self.assertEqual(result, expected_result)

	def test_1976(self):
		result = ConfigParserTestFunction("\n\n\x00\x01\x00\x00\x00\x00\x07\n")
		self.assertEqual(result, expected_result)

	def test_1977(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xEE")
		self.assertEqual(result, expected_result)

	def test_1978(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\x04\x01")
		self.assertEqual(result, expected_result)

	def test_1979(self):
		result = ConfigParserTestFunction("\x07\n\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1980(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x00\x00\x03\n\x00")
		self.assertEqual(result, expected_result)

	def test_1981(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x03\x04")
		self.assertEqual(result, expected_result)

	def test_1982(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0D\x02")
		self.assertEqual(result, expected_result)

	def test_1983(self):
		result = ConfigParserTestFunction("\n\n\n\x01\x02\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1984(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x01\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_1985(self):
		result = ConfigParserTestFunction("\n\n\n\x0C\x01\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1986(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x05\x03")
		self.assertEqual(result, expected_result)

	def test_1987(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x00\x81\x00")
		self.assertEqual(result, expected_result)

	def test_1988(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0F\x13\x00")
		self.assertEqual(result, expected_result)

	def test_1989(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x06\x90\x00")
		self.assertEqual(result, expected_result)

	def test_1990(self):
		result = ConfigParserTestFunction("\x01\x01\x00\x00\x00\x00\x00\x00\x01\x05")
		self.assertEqual(result, expected_result)

	def test_1991(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1992(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x01\x01\x00\x02")
		self.assertEqual(result, expected_result)

	def test_1993(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x00E")
		self.assertEqual(result, expected_result)

	def test_1994(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\x01\x00\x01")
		self.assertEqual(result, expected_result)

	def test_1995(self):
		result = ConfigParserTestFunction("\x00\x03\x00\x00\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_1996(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x07\x01\n")
		self.assertEqual(result, expected_result)

	def test_1997(self):
		result = ConfigParserTestFunction("\x0F\x02\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1998(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x06\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1999(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x02\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2000(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0D\x02\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2001(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\n\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2002(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x01F")
		self.assertEqual(result, expected_result)

	def test_2003(self):
		result = ConfigParserTestFunction("\n\x0B\x03\x00\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2004(self):
		result = ConfigParserTestFunction("\x01\x01\x00\x00\x00\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2005(self):
		result = ConfigParserTestFunction("\n\n\x03\x00\x00\x00\x00\x01\x00\n")
		self.assertEqual(result, expected_result)

	def test_2006(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\x00\x05\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2007(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x03\x03")
		self.assertEqual(result, expected_result)

	def test_2008(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0D\n\n\x06")
		self.assertEqual(result, expected_result)

	def test_2009(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x0F\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2010(self):
		result = ConfigParserTestFunction("\x02\x00\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2011(self):
		result = ConfigParserTestFunction("\n\x01\x01\x00\x00\x00\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2012(self):
		result = ConfigParserTestFunction("\n\x08\x00\x00\x00\x02\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2013(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\x03\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_2014(self):
		result = ConfigParserTestFunction("\n\n\x0C\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2015(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x05\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_2016(self):
		result = ConfigParserTestFunction("\n\n\x00\x02\x00\x00\x00\x00\x00E")
		self.assertEqual(result, expected_result)

	def test_2017(self):
		result = ConfigParserTestFunction("\n\x03\x02\x00\x01\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2018(self):
		result = ConfigParserTestFunction("\n\x03\x02\x00\x00\x01\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2019(self):
		result = ConfigParserTestFunction("\n\x0B\x01\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2020(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\x00\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2021(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xBC")
		self.assertEqual(result, expected_result)

	def test_2022(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x01\x00\x00\x00\x01\x02")
		self.assertEqual(result, expected_result)

	def test_2023(self):
		result = ConfigParserTestFunction("\n\n\n\x01\x01\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2024(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x00\x02\x03")
		self.assertEqual(result, expected_result)

	def test_2025(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x02\x01\x02\x00")
		self.assertEqual(result, expected_result)

	def test_2026(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0E\xA1\x00")
		self.assertEqual(result, expected_result)

	def test_2027(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\x01\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2028(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n'")
		self.assertEqual(result, expected_result)

	def test_2029(self):
		result = ConfigParserTestFunction("\n\n\n\x0C\x02\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2030(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2031(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x05\x07\x00")
		self.assertEqual(result, expected_result)

	def test_2032(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x06\x01")
		self.assertEqual(result, expected_result)

	def test_2033(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x02\x00\x07")
		self.assertEqual(result, expected_result)

	def test_2034(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\x04\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2035(self):
		result = ConfigParserTestFunction("\n\n\n\n\t\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2036(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0F\x02\x01\x00")
		self.assertEqual(result, expected_result)

	def test_2037(self):
		result = ConfigParserTestFunction("\n\x04\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2038(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x04\x07")
		self.assertEqual(result, expected_result)

	def test_2039(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0E\x80\x00")
		self.assertEqual(result, expected_result)

	def test_2040(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0F\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_2041(self):
		result = ConfigParserTestFunction("\n\x0B\x01\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2042(self):
		result = ConfigParserTestFunction("\n\n\x0C\x01\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2043(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x01\x00'")
		self.assertEqual(result, expected_result)

	def test_2044(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x00\x00\x01\x01\n")
		self.assertEqual(result, expected_result)

	def test_2045(self):
		result = ConfigParserTestFunction("\n\n\n\n\t\x01\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2046(self):
		result = ConfigParserTestFunction("\x03\x00\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2047(self):
		result = ConfigParserTestFunction("\n\n\x02\x00\x02\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2048(self):
		result = ConfigParserTestFunction("\x04\x00\x00\x00\x00\x00\x00\x00\x03\n")
		self.assertEqual(result, expected_result)

	def test_2049(self):
		result = ConfigParserTestFunction("\n\n\x05\x00\x00\x00\x00\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_2050(self):
		result = ConfigParserTestFunction("\n\x0B\x02\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2051(self):
		result = ConfigParserTestFunction("\n\n\x0B\x00\x01\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2052(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\ny")
		self.assertEqual(result, expected_result)

	def test_2053(self):
		result = ConfigParserTestFunction("\n\x0E\x00\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2054(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0D\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2055(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nw")
		self.assertEqual(result, expected_result)

	def test_2056(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x02\x01\x01\x01")
		self.assertEqual(result, expected_result)

	def test_2057(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x07\x83\x00")
		self.assertEqual(result, expected_result)

	def test_2058(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\x03\x04")
		self.assertEqual(result, expected_result)

	def test_2059(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x02\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2060(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x02\x03\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2061(self):
		result = ConfigParserTestFunction("\n\x00\x01\x00\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_2062(self):
		result = ConfigParserTestFunction("\n\n\x06\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2063(self):
		result = ConfigParserTestFunction("\n\n\x03\x02\x01\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2064(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\t\n")
		self.assertEqual(result, expected_result)

	def test_2065(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x03\x91\x00")
		self.assertEqual(result, expected_result)

	def test_2066(self):
		result = ConfigParserTestFunction("\n\n\n\n\x08\x00\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2067(self):
		result = ConfigParserTestFunction("\x04\x04\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2068(self):
		result = ConfigParserTestFunction("\n\n\x04\x01\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2069(self):
		result = ConfigParserTestFunction("\x04\x01\x02\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2070(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x07\x07\x02")
		self.assertEqual(result, expected_result)

	def test_2071(self):
		result = ConfigParserTestFunction("\x02\x00\x00\x00\x00\x00\x00\x00\x01\x01")
		self.assertEqual(result, expected_result)

	def test_2072(self):
		result = ConfigParserTestFunction("\n\n\x0C\x01\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2073(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n?")
		self.assertEqual(result, expected_result)

	def test_2074(self):
		result = ConfigParserTestFunction("\n\n\x02\x01\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2075(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\n\x01\n")
		self.assertEqual(result, expected_result)

	def test_2076(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x08\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_2077(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x00\x00\x07\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2078(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x08\x00")
		self.assertEqual(result, expected_result)

	def test_2079(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0D\n\n\x0E")
		self.assertEqual(result, expected_result)

	def test_2080(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x92")
		self.assertEqual(result, expected_result)

	def test_2081(self):
		result = ConfigParserTestFunction("\n\x00\x01\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2082(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_2083(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\x00\x04")
		self.assertEqual(result, expected_result)

	def test_2084(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\x00\x05")
		self.assertEqual(result, expected_result)

	def test_2085(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\x07\x00")
		self.assertEqual(result, expected_result)

	def test_2086(self):
		result = ConfigParserTestFunction("\n\n\x05\x00\x00\x00\x00\x00\x03\n")
		self.assertEqual(result, expected_result)

	def test_2087(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x02\x02\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2088(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x00\x02\x03")
		self.assertEqual(result, expected_result)

	def test_2089(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\n\n\x02")
		self.assertEqual(result, expected_result)

	def test_2090(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x02\x00\x02\n\x00")
		self.assertEqual(result, expected_result)

	def test_2091(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2092(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xF9")
		self.assertEqual(result, expected_result)

	def test_2093(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x0F\x01\x00")
		self.assertEqual(result, expected_result)

	def test_2094(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\n\x02\x00")
		self.assertEqual(result, expected_result)

	def test_2095(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nR")
		self.assertEqual(result, expected_result)

	def test_2096(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_2097(self):
		result = ConfigParserTestFunction("\n\x02\x00\x00\x00\x02\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2098(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\x0F\x00")
		self.assertEqual(result, expected_result)

	def test_2099(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x03\x00\x04\n")
		self.assertEqual(result, expected_result)

	def test_2100(self):
		result = ConfigParserTestFunction("\n\x02\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2101(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x9A")
		self.assertEqual(result, expected_result)

	def test_2102(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\x00\x04\n")
		self.assertEqual(result, expected_result)

	def test_2103(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xD2")
		self.assertEqual(result, expected_result)

	def test_2104(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\x01\x00\n")
		self.assertEqual(result, expected_result)

	def test_2105(self):
		result = ConfigParserTestFunction("\x0E\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2106(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\x0B\x00")
		self.assertEqual(result, expected_result)

	def test_2107(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x08\x00\x02\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2108(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nI")
		self.assertEqual(result, expected_result)

	def test_2109(self):
		result = ConfigParserTestFunction("\n\x0C\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2110(self):
		result = ConfigParserTestFunction("\n\t\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2111(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x01\x00\x03\n")
		self.assertEqual(result, expected_result)

	def test_2112(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x01\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2113(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0E\xD1\x00")
		self.assertEqual(result, expected_result)

	def test_2114(self):
		result = ConfigParserTestFunction("\n\n\n\x05\x00\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2115(self):
		result = ConfigParserTestFunction("\n\n\n\x05\x00\x01\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2116(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x01\x05")
		self.assertEqual(result, expected_result)

	def test_2117(self):
		result = ConfigParserTestFunction("\n\n\n\n\x05\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2118(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x0B\x07\n")
		self.assertEqual(result, expected_result)

	def test_2119(self):
		result = ConfigParserTestFunction("\n\n\n\x07\x00\x00\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_2120(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x00\x06\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2121(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x00\x00\x00\x00\x01\x01")
		self.assertEqual(result, expected_result)

	def test_2122(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nB")
		self.assertEqual(result, expected_result)

	def test_2123(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\x00\x01\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2124(self):
		result = ConfigParserTestFunction("\n\x03\x00\x00\x00\x01\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2125(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x02\x04\n\x00")
		self.assertEqual(result, expected_result)

	def test_2126(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x05\x01\x00\n")
		self.assertEqual(result, expected_result)

	def test_2127(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x02\x00\x01\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_2128(self):
		result = ConfigParserTestFunction("\n\n\n\n\x08\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2129(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0E\xC1\x00")
		self.assertEqual(result, expected_result)

	def test_2130(self):
		result = ConfigParserTestFunction("\x07\x01\x00\x00\x00\x00\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2131(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x00\x00\x00\x02\x06")
		self.assertEqual(result, expected_result)

	def test_2132(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2133(self):
		result = ConfigParserTestFunction("\x03\x00\x00\x00\x00\x00\x01\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2134(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\x03\x02")
		self.assertEqual(result, expected_result)

	def test_2135(self):
		result = ConfigParserTestFunction("\n\x0B\x01\x00\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2136(self):
		result = ConfigParserTestFunction("\n\x07\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2137(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\x01\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2138(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x08\x03")
		self.assertEqual(result, expected_result)

	def test_2139(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\x03\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2140(self):
		result = ConfigParserTestFunction("\n\x01\x00\x00\x00\x00\x00\x00\x02\x00")
		self.assertEqual(result, expected_result)

	def test_2141(self):
		result = ConfigParserTestFunction("\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2142(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x00\x00\x00\x01\x00\n")
		self.assertEqual(result, expected_result)

	def test_2143(self):
		result = ConfigParserTestFunction("\n\x03\x01\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2144(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x00\x00\x00\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_2145(self):
		result = ConfigParserTestFunction("\x04\x00\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2146(self):
		result = ConfigParserTestFunction("\x00\x01\x00\x00\x00\x00\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2147(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0D\n\x01\n")
		self.assertEqual(result, expected_result)

	def test_2148(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x01\x00\x04\n")
		self.assertEqual(result, expected_result)

	def test_2149(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x01\x01\x00")
		self.assertEqual(result, expected_result)

	def test_2150(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\x02\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2151(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x01\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2152(self):
		result = ConfigParserTestFunction("\n\x00\x01\x01\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_2153(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x02\x05")
		self.assertEqual(result, expected_result)

	def test_2154(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_2155(self):
		result = ConfigParserTestFunction("\n\x03\x00\x00\x00\x00\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_2156(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x02\x07")
		self.assertEqual(result, expected_result)

	def test_2157(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x9F")
		self.assertEqual(result, expected_result)

	def test_2158(self):
		result = ConfigParserTestFunction("\n\n\n\n\x05\x01\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2159(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x01\x00\x00\x01\x05")
		self.assertEqual(result, expected_result)

	def test_2160(self):
		result = ConfigParserTestFunction("\n\n\n\n\x1A\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2161(self):
		result = ConfigParserTestFunction("\x06\x00\x06\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2162(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x07\x07")
		self.assertEqual(result, expected_result)

	def test_2163(self):
		result = ConfigParserTestFunction("\n\n\n\x0C\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2164(self):
		result = ConfigParserTestFunction("\x08\x00\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2165(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x02\x02\x01")
		self.assertEqual(result, expected_result)

	def test_2166(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x00\x03\x05")
		self.assertEqual(result, expected_result)

	def test_2167(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x01\x00")
		self.assertEqual(result, expected_result)

	def test_2168(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0B\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2169(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x07\x02")
		self.assertEqual(result, expected_result)

	def test_2170(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\n\x03")
		self.assertEqual(result, expected_result)

	def test_2171(self):
		result = ConfigParserTestFunction("\n\n\n\n\x07\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2172(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x00\x00\x01\x03\n")
		self.assertEqual(result, expected_result)

	def test_2173(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0E\x00\x03\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2174(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x01\x00\x01\x01\n")
		self.assertEqual(result, expected_result)

	def test_2175(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x06\xA0\x00")
		self.assertEqual(result, expected_result)

	def test_2176(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x08\x90\x00")
		self.assertEqual(result, expected_result)

	def test_2177(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x01\x00\x01\x01")
		self.assertEqual(result, expected_result)

	def test_2178(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x01\x01\x03\n")
		self.assertEqual(result, expected_result)

	def test_2179(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0E\x00\x00\x03\n")
		self.assertEqual(result, expected_result)

	def test_2180(self):
		result = ConfigParserTestFunction("\n\n\n\x08\x01\x00\x01\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2181(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x00\x00\x00\x03\n\x00")
		self.assertEqual(result, expected_result)

	def test_2182(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xC2")
		self.assertEqual(result, expected_result)

	def test_2183(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x00\x00\x03\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2184(self):
		result = ConfigParserTestFunction("\n\n\n\x0C\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2185(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\x01\x04")
		self.assertEqual(result, expected_result)

	def test_2186(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0D\x02\x00")
		self.assertEqual(result, expected_result)

	def test_2187(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x01\x00\x03\n")
		self.assertEqual(result, expected_result)

	def test_2188(self):
		result = ConfigParserTestFunction("\n\n\x02\x00\x00\x05\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2189(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nL")
		self.assertEqual(result, expected_result)

	def test_2190(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_2191(self):
		result = ConfigParserTestFunction("\n\n\t\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2192(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x00\x01\x02\x00")
		self.assertEqual(result, expected_result)

	def test_2193(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\n\x02\x01")
		self.assertEqual(result, expected_result)

	def test_2194(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xE2")
		self.assertEqual(result, expected_result)

	def test_2195(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x01\x01\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2196(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n/")
		self.assertEqual(result, expected_result)

	def test_2197(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\x01\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_2198(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\t\x00")
		self.assertEqual(result, expected_result)

	def test_2199(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0B\x07")
		self.assertEqual(result, expected_result)

	def test_2200(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x01\x00\x05\n\x00")
		self.assertEqual(result, expected_result)

	def test_2201(self):
		result = ConfigParserTestFunction("\n\n\n\x08\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2202(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x06\x06\x01")
		self.assertEqual(result, expected_result)

	def test_2203(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0B\x06")
		self.assertEqual(result, expected_result)

	def test_2204(self):
		result = ConfigParserTestFunction("\x01\x02\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2205(self):
		result = ConfigParserTestFunction("\n\x02\x02\x00\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2206(self):
		result = ConfigParserTestFunction("\n\n\x0C\x01\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2207(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x04\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2208(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\n\n\x03")
		self.assertEqual(result, expected_result)

	def test_2209(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nF")
		self.assertEqual(result, expected_result)

	def test_2210(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x04\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2211(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x01\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2212(self):
		result = ConfigParserTestFunction("\n\n\x01\x00\x00\x00\x00\x00\x00\x07")
		self.assertEqual(result, expected_result)

	def test_2213(self):
		result = ConfigParserTestFunction("\n\x06\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2214(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x02\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_2215(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x06\x81\x00")
		self.assertEqual(result, expected_result)

	def test_2216(self):
		result = ConfigParserTestFunction("\x01\x01\x00\x00\x00\x00\x00\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_2217(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x01\x01\x02")
		self.assertEqual(result, expected_result)

	def test_2218(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0E\x00\x00\x00\x00\x04")
		self.assertEqual(result, expected_result)

	def test_2219(self):
		result = ConfigParserTestFunction("\n\x06\x00\x00\x00\x00\x04\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2220(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xFA")
		self.assertEqual(result, expected_result)

	def test_2221(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x00\x00\x00\x04\n")
		self.assertEqual(result, expected_result)

	def test_2222(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2223(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x01\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_2224(self):
		result = ConfigParserTestFunction("\n\n\x0C\x01\x00\x00\x00\x01\x00\n")
		self.assertEqual(result, expected_result)

	def test_2225(self):
		result = ConfigParserTestFunction("\n\n\x0B\x00\x00\x00\x00\x02\n\x00")
		self.assertEqual(result, expected_result)

	def test_2226(self):
		result = ConfigParserTestFunction("\x04\x02\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2227(self):
		result = ConfigParserTestFunction("\n\n\n\x0D\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2228(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x02\x00'")
		self.assertEqual(result, expected_result)

	def test_2229(self):
		result = ConfigParserTestFunction("\n\n\n\x06\x01\x00\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2230(self):
		result = ConfigParserTestFunction("\x03\x06\x00\x00\x00\x00\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_2231(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\x03\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2232(self):
		result = ConfigParserTestFunction("\x03\x00\x00\x00\x00\x00\x00\x00\x00\x06")
		self.assertEqual(result, expected_result)

	def test_2233(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x00\x02\x00\x03")
		self.assertEqual(result, expected_result)

	def test_2234(self):
		result = ConfigParserTestFunction("\x06\x01\x06\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2235(self):
		result = ConfigParserTestFunction("\x07\x02\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2236(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x04\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2237(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\n\n\x07")
		self.assertEqual(result, expected_result)

	def test_2238(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xC6")
		self.assertEqual(result, expected_result)

	def test_2239(self):
		result = ConfigParserTestFunction("\x01\x02\x00\x00\x00\x00\x00\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_2240(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x03\x01\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2241(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\x0F\x01")
		self.assertEqual(result, expected_result)

	def test_2242(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x02\x01\x00\x05")
		self.assertEqual(result, expected_result)

	def test_2243(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0F\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_2244(self):
		result = ConfigParserTestFunction("\x07\x00\x00\x00\x00\x00\x00\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_2245(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x0C\x00")
		self.assertEqual(result, expected_result)

	def test_2246(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x00\x82\x00")
		self.assertEqual(result, expected_result)

	def test_2247(self):
		result = ConfigParserTestFunction("\x01\x00\x02\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2248(self):
		result = ConfigParserTestFunction("\n\n\x0B\x03\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2249(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x00\x01\x06")
		self.assertEqual(result, expected_result)

	def test_2250(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x02\x03\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_2251(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n_")
		self.assertEqual(result, expected_result)

	def test_2252(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\x03\x01\x00")
		self.assertEqual(result, expected_result)

	def test_2253(self):
		result = ConfigParserTestFunction("\n\n\n\x0F\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2254(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x00\x02\x00")
		self.assertEqual(result, expected_result)

	def test_2255(self):
		result = ConfigParserTestFunction("\n\x06\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2256(self):
		result = ConfigParserTestFunction("\n\x01\x01\x00\x00\x00\x05\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2257(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x00B\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2258(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x02\x80\x00")
		self.assertEqual(result, expected_result)

	def test_2259(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x06\x04")
		self.assertEqual(result, expected_result)

	def test_2260(self):
		result = ConfigParserTestFunction("\x06\x00\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2261(self):
		result = ConfigParserTestFunction("\n\n\n\x07\x01\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2262(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x00\x00\x00\x02\x03\x00")
		self.assertEqual(result, expected_result)

	def test_2263(self):
		result = ConfigParserTestFunction("\x03\x00\x00\x00\x00\x00\x00\x00\x00\x04")
		self.assertEqual(result, expected_result)

	def test_2264(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x02\x81\x00")
		self.assertEqual(result, expected_result)

	def test_2265(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x0D\x03")
		self.assertEqual(result, expected_result)

	def test_2266(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\x01\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2267(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x02\x01\x07")
		self.assertEqual(result, expected_result)

	def test_2268(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\n\x02\n")
		self.assertEqual(result, expected_result)

	def test_2269(self):
		result = ConfigParserTestFunction("\x00\x03\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2270(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x00\x00\x02\x05")
		self.assertEqual(result, expected_result)

	def test_2271(self):
		result = ConfigParserTestFunction("\n\n\x04\x00\x00\x01\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2272(self):
		result = ConfigParserTestFunction("\n\n\n\x08\x01\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2273(self):
		result = ConfigParserTestFunction("\x05\x00\x00\x00\x00\x00\x00\x00\x03\n")
		self.assertEqual(result, expected_result)

	def test_2274(self):
		result = ConfigParserTestFunction("\n\n\x08\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2275(self):
		result = ConfigParserTestFunction("\n\n\n\x0C\x01\x00\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2276(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x02\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2277(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\x04\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_2278(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x01f")
		self.assertEqual(result, expected_result)

	def test_2279(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\x01\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_2280(self):
		result = ConfigParserTestFunction("\n\n\x0C\x01\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2281(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x00\x00\x01\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_2282(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0F\x01\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_2283(self):
		result = ConfigParserTestFunction("\n\n\n\n\x04\x00\x00\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_2284(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0E\x03\x00")
		self.assertEqual(result, expected_result)

	def test_2285(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2286(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x02\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_2287(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x0B\x00")
		self.assertEqual(result, expected_result)

	def test_2288(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0F\x01\x01\x00")
		self.assertEqual(result, expected_result)

	def test_2289(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x00\x00\x00\x06\n")
		self.assertEqual(result, expected_result)

	def test_2290(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xF2")
		self.assertEqual(result, expected_result)

	def test_2291(self):
		result = ConfigParserTestFunction("\n\n\x0D\x01\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2292(self):
		result = ConfigParserTestFunction("\n\x04\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2293(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\x02\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2294(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nO")
		self.assertEqual(result, expected_result)

	def test_2295(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x02\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_2296(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x05\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2297(self):
		result = ConfigParserTestFunction("\x03\x01\x00\x00\x00\x00\x00\x00\x00\x07")
		self.assertEqual(result, expected_result)

	def test_2298(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x00\x00\x00\x00\x01\x00\n")
		self.assertEqual(result, expected_result)

	def test_2299(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x03\x01\x01")
		self.assertEqual(result, expected_result)

	def test_2300(self):
		result = ConfigParserTestFunction("\n\n\n\x0C\x01\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2301(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x06\x04\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2302(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x07\x02\x00\x05")
		self.assertEqual(result, expected_result)

	def test_2303(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\x02\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2304(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\x03\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2305(self):
		result = ConfigParserTestFunction("\n\n\n\n\x07\x01\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2306(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\n\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2307(self):
		result = ConfigParserTestFunction("\n\n\x0B\x01\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2308(self):
		result = ConfigParserTestFunction("\n\n\n\n\x04\x01\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2309(self):
		result = ConfigParserTestFunction("\n\x02\x04\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2310(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x00'")
		self.assertEqual(result, expected_result)

	def test_2311(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0F\x05")
		self.assertEqual(result, expected_result)

	def test_2312(self):
		result = ConfigParserTestFunction("\n\x02\x00\x01\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2313(self):
		result = ConfigParserTestFunction("\n\n\x0E\x00\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2314(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nb")
		self.assertEqual(result, expected_result)

	def test_2315(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x01\x01\x00\x02")
		self.assertEqual(result, expected_result)

	def test_2316(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x03f")
		self.assertEqual(result, expected_result)

	def test_2317(self):
		result = ConfigParserTestFunction("\x07\x00\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2318(self):
		result = ConfigParserTestFunction("\x0E\x00\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2319(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x00\x02\x02\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2320(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x00\x01\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2321(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x0E\x01\x02")
		self.assertEqual(result, expected_result)

	def test_2322(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x08\x02\x00")
		self.assertEqual(result, expected_result)

	def test_2323(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x05\x0D\x00")
		self.assertEqual(result, expected_result)

	def test_2324(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\x02\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2325(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\x02\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2326(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\x00\x00\x03\n")
		self.assertEqual(result, expected_result)

	def test_2327(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x00\x00\x04\n")
		self.assertEqual(result, expected_result)

	def test_2328(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x04\x02")
		self.assertEqual(result, expected_result)

	def test_2329(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x00\x00\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_2330(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\x02\x01")
		self.assertEqual(result, expected_result)

	def test_2331(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x04\x04")
		self.assertEqual(result, expected_result)

	def test_2332(self):
		result = ConfigParserTestFunction("\n\x08\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2333(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2334(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\n\x01\x00")
		self.assertEqual(result, expected_result)

	def test_2335(self):
		result = ConfigParserTestFunction("\x0C\x00\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2336(self):
		result = ConfigParserTestFunction("\n\n\x06\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2337(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n*")
		self.assertEqual(result, expected_result)

	def test_2338(self):
		result = ConfigParserTestFunction("\x02\x01\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2339(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x02\x06")
		self.assertEqual(result, expected_result)

	def test_2340(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x03\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_2341(self):
		result = ConfigParserTestFunction("\n\n\n\n\x08\x00\x03\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2342(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x02\x00\x02")
		self.assertEqual(result, expected_result)

	def test_2343(self):
		result = ConfigParserTestFunction("\n\n\n\x0D\x01\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2344(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0C\x02")
		self.assertEqual(result, expected_result)

	def test_2345(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\t\x05\x00")
		self.assertEqual(result, expected_result)

	def test_2346(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x0F\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2347(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xA2")
		self.assertEqual(result, expected_result)

	def test_2348(self):
		result = ConfigParserTestFunction("\n\n\n\x0C\x02\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2349(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\x04\x00")
		self.assertEqual(result, expected_result)

	def test_2350(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0C\x02\x00")
		self.assertEqual(result, expected_result)

	def test_2351(self):
		result = ConfigParserTestFunction("\n\n\n\x04\x02\x00\x01\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2352(self):
		result = ConfigParserTestFunction("\n\x0B\x03\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2353(self):
		result = ConfigParserTestFunction("\x05\x00\x00\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2354(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x05\\\x00")
		self.assertEqual(result, expected_result)

	def test_2355(self):
		result = ConfigParserTestFunction("\n\n\x00\x03\x00\x00\x00\x00\x00\x04")
		self.assertEqual(result, expected_result)

	def test_2356(self):
		result = ConfigParserTestFunction("\n\x07\x04\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2357(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x02\x00")
		self.assertEqual(result, expected_result)

	def test_2358(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x04\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2359(self):
		result = ConfigParserTestFunction("\n\n\n\x07\x00\x00\x01\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2360(self):
		result = ConfigParserTestFunction("\n\x00\x03\x00\x01\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2361(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_2362(self):
		result = ConfigParserTestFunction("\n\x06\x00\x00\x00\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2363(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0D\x03")
		self.assertEqual(result, expected_result)

	def test_2364(self):
		result = ConfigParserTestFunction("\n\n\x0B\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2365(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0E\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2366(self):
		result = ConfigParserTestFunction("\n\n\x08\x01\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2367(self):
		result = ConfigParserTestFunction("\n\x0B\x01\x01\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2368(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2369(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x01\x00\x00\x04\n")
		self.assertEqual(result, expected_result)

	def test_2370(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\x03\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_2371(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x01\x00\x01\x00\x05")
		self.assertEqual(result, expected_result)

	def test_2372(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x05\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2373(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x03\x00\x01\x01\x04")
		self.assertEqual(result, expected_result)

	def test_2374(self):
		result = ConfigParserTestFunction("\n\n\n\x0D\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2375(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\x01\x02\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2376(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0B\x0C\x00")
		self.assertEqual(result, expected_result)

	def test_2377(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nM")
		self.assertEqual(result, expected_result)

	def test_2378(self):
		result = ConfigParserTestFunction("\n\x03\x00\x00\x00\x00\x04\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2379(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x05 \x00")
		self.assertEqual(result, expected_result)

	def test_2380(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x0E\x00\x03")
		self.assertEqual(result, expected_result)

	def test_2381(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0B\x01\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2382(self):
		result = ConfigParserTestFunction("\x03\x02\x00\x00\x00\x00\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_2383(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\n\n\x06")
		self.assertEqual(result, expected_result)

	def test_2384(self):
		result = ConfigParserTestFunction("\n\x00\x03\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2385(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\x07\x02")
		self.assertEqual(result, expected_result)

	def test_2386(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x03\x02\x01\n")
		self.assertEqual(result, expected_result)

	def test_2387(self):
		result = ConfigParserTestFunction("\n\t\x01\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2388(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2389(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x05\t\x00")
		self.assertEqual(result, expected_result)

	def test_2390(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x03\x00\x05\n")
		self.assertEqual(result, expected_result)

	def test_2391(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0E\x13\x00")
		self.assertEqual(result, expected_result)

	def test_2392(self):
		result = ConfigParserTestFunction("\n\x00\x02\x01\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2393(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0D\x03\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2394(self):
		result = ConfigParserTestFunction("\x04\x01\x00\x00\x00\x00\x00\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_2395(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\x00\x03\n\x00")
		self.assertEqual(result, expected_result)

	def test_2396(self):
		result = ConfigParserTestFunction("\x01\x00\x00\x00\x00\x00\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2397(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0F\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2398(self):
		result = ConfigParserTestFunction("\n\n\x00\x01\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2399(self):
		result = ConfigParserTestFunction("\n\n\x0B\x07\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2400(self):
		result = ConfigParserTestFunction("\n\x02\x00\x00\x00\x03\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2401(self):
		result = ConfigParserTestFunction("\n\n\n\x07\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2402(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0D\x03\x00")
		self.assertEqual(result, expected_result)

	def test_2403(self):
		result = ConfigParserTestFunction("\x06\x00\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2404(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\x01\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_2405(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0B\x01\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_2406(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\x07\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2407(self):
		result = ConfigParserTestFunction("\n\n\x06\x01\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2408(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x05'\x00")
		self.assertEqual(result, expected_result)

	def test_2409(self):
		result = ConfigParserTestFunction("\x04\x00\x03\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2410(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x04\x03\x00")
		self.assertEqual(result, expected_result)

	def test_2411(self):
		result = ConfigParserTestFunction("\n\n\x0C\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2412(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x02\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_2413(self):
		result = ConfigParserTestFunction("\n\x00\x01\x00\x00\x00\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2414(self):
		result = ConfigParserTestFunction("\n\n\x00\x01\x01\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2415(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x06\x04\x01")
		self.assertEqual(result, expected_result)

	def test_2416(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x03\x00\x03\x01")
		self.assertEqual(result, expected_result)

	def test_2417(self):
		result = ConfigParserTestFunction("\n\x00\x01\x00\x00\x00\x03\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2418(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x03\x00")
		self.assertEqual(result, expected_result)

	def test_2419(self):
		result = ConfigParserTestFunction("\x02\x01\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2420(self):
		result = ConfigParserTestFunction("\n\n\n\x07\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2421(self):
		result = ConfigParserTestFunction("\n\n\n\x04\x01\x03\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2422(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\x00\x04\n\x00")
		self.assertEqual(result, expected_result)

	def test_2423(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\n\x02\x00")
		self.assertEqual(result, expected_result)

	def test_2424(self):
		result = ConfigParserTestFunction("\n\n\x0C\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2425(self):
		result = ConfigParserTestFunction("\n\n\n\x0C\x03\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2426(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x01'")
		self.assertEqual(result, expected_result)

	def test_2427(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x01\x01\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2428(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\"")
		self.assertEqual(result, expected_result)

	def test_2429(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x07\x02\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2430(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x96")
		self.assertEqual(result, expected_result)

	def test_2431(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x05\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2432(self):
		result = ConfigParserTestFunction("\x03\x00\x01\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2433(self):
		result = ConfigParserTestFunction("\x0C\x01\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2434(self):
		result = ConfigParserTestFunction("\n\n\x02\x01\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2435(self):
		result = ConfigParserTestFunction("\x07\x00\x00\x00\x00\x00\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_2436(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x00\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_2437(self):
		result = ConfigParserTestFunction("\n\n\n\x0E\x04\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2438(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x0E\x02\x01")
		self.assertEqual(result, expected_result)

	def test_2439(self):
		result = ConfigParserTestFunction("\n\n\n\n\x07\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2440(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x04\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2441(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x00\x00\x01\x03")
		self.assertEqual(result, expected_result)

	def test_2442(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x01\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2443(self):
		result = ConfigParserTestFunction("\n\n\n\x04\x03\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2444(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x01\x00\x00\x00\x00\x01\x03")
		self.assertEqual(result, expected_result)

	def test_2445(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\n\x0F")
		self.assertEqual(result, expected_result)

	def test_2446(self):
		result = ConfigParserTestFunction("\n\n\x04\x00\x03\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2447(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x04\x02\x00\n")
		self.assertEqual(result, expected_result)

	def test_2448(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nN")
		self.assertEqual(result, expected_result)

	def test_2449(self):
		result = ConfigParserTestFunction("\n\x02\x00\x00\x00\x00\x01\x02\n\x00")
		self.assertEqual(result, expected_result)

	def test_2450(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x00\x00\x00\x01\x01")
		self.assertEqual(result, expected_result)

	def test_2451(self):
		result = ConfigParserTestFunction("\n\n\n\x07\x02\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2452(self):
		result = ConfigParserTestFunction("\n\n\n\x0C\x02\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2453(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2454(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\t\x0D\x00")
		self.assertEqual(result, expected_result)

	def test_2455(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xB5")
		self.assertEqual(result, expected_result)

	def test_2456(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x0C\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2457(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x00\x03\x03")
		self.assertEqual(result, expected_result)

	def test_2458(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x01\x02\x03")
		self.assertEqual(result, expected_result)

	def test_2459(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\x01\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2460(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0E\x01\x00\x05\n")
		self.assertEqual(result, expected_result)

	def test_2461(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\x02\x04")
		self.assertEqual(result, expected_result)

	def test_2462(self):
		result = ConfigParserTestFunction("\n\x07\x00\x00\x00\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2463(self):
		result = ConfigParserTestFunction("\x06\x00\x00\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2464(self):
		result = ConfigParserTestFunction("\n\n\n\n\x08\x01\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2465(self):
		result = ConfigParserTestFunction("\n\n\n\x0C\x02\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2466(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\x00\x06")
		self.assertEqual(result, expected_result)

	def test_2467(self):
		result = ConfigParserTestFunction("\n\n\t\x01\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2468(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\t\t\x00")
		self.assertEqual(result, expected_result)

	def test_2469(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\t\x04")
		self.assertEqual(result, expected_result)

	def test_2470(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0F\x04\n\x00")
		self.assertEqual(result, expected_result)

	def test_2471(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x06\x05\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2472(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2473(self):
		result = ConfigParserTestFunction("\x05\x00\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2474(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x00\x00\x00\x00\x01\x02")
		self.assertEqual(result, expected_result)

	def test_2475(self):
		result = ConfigParserTestFunction("\n\n\x01\x00\x00\x00\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_2476(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x83")
		self.assertEqual(result, expected_result)

	def test_2477(self):
		result = ConfigParserTestFunction("\n\n\x08\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2478(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x04\x0D\x00")
		self.assertEqual(result, expected_result)

	def test_2479(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x00\x01\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2480(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0D\x07\x00")
		self.assertEqual(result, expected_result)

	def test_2481(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\n\n\x07")
		self.assertEqual(result, expected_result)

	def test_2482(self):
		result = ConfigParserTestFunction("\n\n\n\n\x05\x00\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2483(self):
		result = ConfigParserTestFunction("\n\x0B\x07\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2484(self):
		result = ConfigParserTestFunction("\x00\x01\x01\x00\x00\x00\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2485(self):
		result = ConfigParserTestFunction("\x05\x01\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2486(self):
		result = ConfigParserTestFunction("\x00\x01\x00\x00\x00\x01\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2487(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x07\x06")
		self.assertEqual(result, expected_result)

	def test_2488(self):
		result = ConfigParserTestFunction("\x04\x00\x00\x01\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2489(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\x05\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2490(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x07\x04")
		self.assertEqual(result, expected_result)

	def test_2491(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x03\x00\x07\x01")
		self.assertEqual(result, expected_result)

	def test_2492(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\x03\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2493(self):
		result = ConfigParserTestFunction("\n\n\x03\x00\x00\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2494(self):
		result = ConfigParserTestFunction("\n\n\x0C\x01\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2495(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0F\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2496(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0B\x03\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2497(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0E\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2498(self):
		result = ConfigParserTestFunction("\n\x08\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2499(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x02\x01\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2500(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x06\x01")
		self.assertEqual(result, expected_result)

	def test_2501(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0C\x03\x00")
		self.assertEqual(result, expected_result)

	def test_2502(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x05\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2503(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\x00\x01\x01")
		self.assertEqual(result, expected_result)

	def test_2504(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\t\x06")
		self.assertEqual(result, expected_result)

	def test_2505(self):
		result = ConfigParserTestFunction("\x07\x00\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2506(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x08\x03")
		self.assertEqual(result, expected_result)

	def test_2507(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\x02\n\x00")
		self.assertEqual(result, expected_result)

	def test_2508(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x04\t\x00")
		self.assertEqual(result, expected_result)

	def test_2509(self):
		result = ConfigParserTestFunction("\n\n\n\x07\x04\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2510(self):
		result = ConfigParserTestFunction("\n\x03\x00\x00\x00\x01\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2511(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x05\x10\x00")
		self.assertEqual(result, expected_result)

	def test_2512(self):
		result = ConfigParserTestFunction("\n\n\n\n\x07\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_2513(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0F\x03")
		self.assertEqual(result, expected_result)

	def test_2514(self):
		result = ConfigParserTestFunction("\n\n\n\n\t\x01\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2515(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x04\\\x00")
		self.assertEqual(result, expected_result)

	def test_2516(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x02\x01'")
		self.assertEqual(result, expected_result)

	def test_2517(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\x01\x01\x01\n")
		self.assertEqual(result, expected_result)

	def test_2518(self):
		result = ConfigParserTestFunction("\n\x00\x01\x00\x00\x00\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2519(self):
		result = ConfigParserTestFunction("\n\n\x02\x00\x00\x00\x01\x02\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2520(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x0E\x02\x02")
		self.assertEqual(result, expected_result)

	def test_2521(self):
		result = ConfigParserTestFunction("\n\n\x00\x03\x00\x00\x00\x00\x00E")
		self.assertEqual(result, expected_result)

	def test_2522(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\t\x05")
		self.assertEqual(result, expected_result)

	def test_2523(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\x06\x00")
		self.assertEqual(result, expected_result)

	def test_2524(self):
		result = ConfigParserTestFunction("\n\n\x01\x03\x00\x01\x00\x01\x00\n")
		self.assertEqual(result, expected_result)

	def test_2525(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x05\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2526(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\n\x07")
		self.assertEqual(result, expected_result)

	def test_2527(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x01\x00\x01\x01")
		self.assertEqual(result, expected_result)

	def test_2528(self):
		result = ConfigParserTestFunction("\n\n\n\x07\x00\x00\x01\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_2529(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x07\x01\x03\x01")
		self.assertEqual(result, expected_result)

	def test_2530(self):
		result = ConfigParserTestFunction("\n\n\x03\x02\x01\x00\x01\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2531(self):
		result = ConfigParserTestFunction("\x03\x00\x00\x00\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2532(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x06\xD0\x00")
		self.assertEqual(result, expected_result)

	def test_2533(self):
		result = ConfigParserTestFunction("\n\n\n\x01\x03\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2534(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x00\x00\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_2535(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x0C\x00")
		self.assertEqual(result, expected_result)

	def test_2536(self):
		result = ConfigParserTestFunction("\n\n\x00\x02\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2537(self):
		result = ConfigParserTestFunction("\n\n\x04\x00\x00\x00\x00\x00\x01\x03")
		self.assertEqual(result, expected_result)

	def test_2538(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0B\x05\x00")
		self.assertEqual(result, expected_result)

	def test_2539(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x08\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2540(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x02\x02\x01\x01")
		self.assertEqual(result, expected_result)

	def test_2541(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x00\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2542(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\x03\n\x00")
		self.assertEqual(result, expected_result)

	def test_2543(self):
		result = ConfigParserTestFunction("\x03\x01\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2544(self):
		result = ConfigParserTestFunction("\n\n\x03\x01\x00\x01\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2545(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0E\x02")
		self.assertEqual(result, expected_result)

	def test_2546(self):
		result = ConfigParserTestFunction("\n\n\x01\x00\x00\x00\x00\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_2547(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nr")
		self.assertEqual(result, expected_result)

	def test_2548(self):
		result = ConfigParserTestFunction("\n\x02\x01\x00\x00\x01\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2549(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x07\x00\x03\x03")
		self.assertEqual(result, expected_result)

	def test_2550(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0C\x07\x00")
		self.assertEqual(result, expected_result)

	def test_2551(self):
		result = ConfigParserTestFunction("\n\n\n\x0C\x03\x00\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2552(self):
		result = ConfigParserTestFunction("\x0C\x02\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2553(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x08\x04\x00")
		self.assertEqual(result, expected_result)

	def test_2554(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2555(self):
		result = ConfigParserTestFunction("\n\n\x01\x03\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2556(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x01\x02\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2557(self):
		result = ConfigParserTestFunction("\n\x07\x00\x00\x00\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_2558(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0B\x0D\x00")
		self.assertEqual(result, expected_result)

	def test_2559(self):
		result = ConfigParserTestFunction("\n\n\x01\x00\x00\x00\x00\x04\n\x00")
		self.assertEqual(result, expected_result)

	def test_2560(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0E\x06")
		self.assertEqual(result, expected_result)

	def test_2561(self):
		result = ConfigParserTestFunction("\n\n\x0B\x00\x00\x01\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2562(self):
		result = ConfigParserTestFunction("\n\n\x00\x03\x00\x00\x00\x00\x00\x06")
		self.assertEqual(result, expected_result)

	def test_2563(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\x0E\x00")
		self.assertEqual(result, expected_result)

	def test_2564(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x01\x03\x03")
		self.assertEqual(result, expected_result)

	def test_2565(self):
		result = ConfigParserTestFunction("\x03\x01\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2566(self):
		result = ConfigParserTestFunction("\n\x08\x00\x01\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2567(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0F\x04\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2568(self):
		result = ConfigParserTestFunction("\x03\x02\x01\x00\x00\x01\x00\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_2569(self):
		result = ConfigParserTestFunction("\x0E\x01\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2570(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0E\x02\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2571(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x07\x00\x02\x00")
		self.assertEqual(result, expected_result)

	def test_2572(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0D\x04\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2573(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0F\x04\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2574(self):
		result = ConfigParserTestFunction("\n\x03\x01\x00\x00\x00\x00\x00\x01\x01")
		self.assertEqual(result, expected_result)

	def test_2575(self):
		result = ConfigParserTestFunction("\n\n\x0B\x01\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2576(self):
		result = ConfigParserTestFunction("\n\n\n\n\x08\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2577(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0D\x05\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2578(self):
		result = ConfigParserTestFunction("\n\n\x0B\x00\x00\x00\x01\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_2579(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2580(self):
		result = ConfigParserTestFunction("\n\x07\x00\x00\x00\x00\x01\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_2581(self):
		result = ConfigParserTestFunction("\n\n\n\x07\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2582(self):
		result = ConfigParserTestFunction("\n\x0B\x06\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2583(self):
		result = ConfigParserTestFunction("\n\x04\x00\x00\x00\x02\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2584(self):
		result = ConfigParserTestFunction("\n\n\n\x06\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2585(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x04\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2586(self):
		result = ConfigParserTestFunction("\n\x0C\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2587(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\x02\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_2588(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x00$")
		self.assertEqual(result, expected_result)

	def test_2589(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x00\x00\x01\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2590(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x04 \x00")
		self.assertEqual(result, expected_result)

	def test_2591(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x00\x01\x05")
		self.assertEqual(result, expected_result)

	def test_2592(self):
		result = ConfigParserTestFunction("\n\x0C\x01\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2593(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0F\x07")
		self.assertEqual(result, expected_result)

	def test_2594(self):
		result = ConfigParserTestFunction("\n\x02\x01\x00\x01\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2595(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x01\x01\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2596(self):
		result = ConfigParserTestFunction("\n\n\x03\x02\x00\x00\x01\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2597(self):
		result = ConfigParserTestFunction("\n\x08\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2598(self):
		result = ConfigParserTestFunction("\n\n\n\n\x08\x01\x03\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2599(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\t\x08\x00")
		self.assertEqual(result, expected_result)

	def test_2600(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x02\x00\x03\n\x00")
		self.assertEqual(result, expected_result)

	def test_2601(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x05\x01\x01")
		self.assertEqual(result, expected_result)

	def test_2602(self):
		result = ConfigParserTestFunction("\x0F\x00\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2603(self):
		result = ConfigParserTestFunction("\n\n\n\x06\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2604(self):
		result = ConfigParserTestFunction("\x08\x00\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2605(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xCC")
		self.assertEqual(result, expected_result)

	def test_2606(self):
		result = ConfigParserTestFunction("\n\n\x06\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2607(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x01\x05")
		self.assertEqual(result, expected_result)

	def test_2608(self):
		result = ConfigParserTestFunction("\x04\x00\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2609(self):
		result = ConfigParserTestFunction("\x0C\x03\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2610(self):
		result = ConfigParserTestFunction("\n\n\x0C\x00\x00\x00\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_2611(self):
		result = ConfigParserTestFunction("\n\n\n\n\x1C\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2612(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x95")
		self.assertEqual(result, expected_result)

	def test_2613(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x05\x80\x00")
		self.assertEqual(result, expected_result)

	def test_2614(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x04'\x00")
		self.assertEqual(result, expected_result)

	def test_2615(self):
		result = ConfigParserTestFunction("\n\n\n\x0C\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2616(self):
		result = ConfigParserTestFunction("\n\n\x0C\x00\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_2617(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\n\x01\n")
		self.assertEqual(result, expected_result)

	def test_2618(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\x02\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2619(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x08\x14\x00")
		self.assertEqual(result, expected_result)

	def test_2620(self):
		result = ConfigParserTestFunction("\x03\x06\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2621(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x01\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_2622(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x04\x07\x00")
		self.assertEqual(result, expected_result)

	def test_2623(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x00\x01\x00\x05\n")
		self.assertEqual(result, expected_result)

	def test_2624(self):
		result = ConfigParserTestFunction("\n\n\n\n\x1B\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2625(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x03\x05")
		self.assertEqual(result, expected_result)

	def test_2626(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xDA")
		self.assertEqual(result, expected_result)

	def test_2627(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x01\x01\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_2628(self):
		result = ConfigParserTestFunction("\x0C\x06\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2629(self):
		result = ConfigParserTestFunction("\n\n\x0B\x06\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2630(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x07\x01\x01\x05")
		self.assertEqual(result, expected_result)

	def test_2631(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\x06\n")
		self.assertEqual(result, expected_result)

	def test_2632(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x03\x00\x00\x04\n")
		self.assertEqual(result, expected_result)

	def test_2633(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x07\x82\x00")
		self.assertEqual(result, expected_result)

	def test_2634(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0E$")
		self.assertEqual(result, expected_result)

	def test_2635(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x06\x02\x00")
		self.assertEqual(result, expected_result)

	def test_2636(self):
		result = ConfigParserTestFunction("\n\n\x01\x03\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2637(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\n\x00\x04")
		self.assertEqual(result, expected_result)

	def test_2638(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0E\x00\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_2639(self):
		result = ConfigParserTestFunction("\n\n\n\n\x06\x01\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2640(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\x08\x00")
		self.assertEqual(result, expected_result)

	def test_2641(self):
		result = ConfigParserTestFunction("\x06\x02\x06\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2642(self):
		result = ConfigParserTestFunction("\x03\x02\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2643(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x19\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2644(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x07\x05")
		self.assertEqual(result, expected_result)

	def test_2645(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x00\x00\x01\x00\x03\n")
		self.assertEqual(result, expected_result)

	def test_2646(self):
		result = ConfigParserTestFunction("\n\n\x08\x01\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2647(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x03\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2648(self):
		result = ConfigParserTestFunction("\n\n\n\x04\x07\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2649(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0E\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2650(self):
		result = ConfigParserTestFunction("\x04\x00\x00\x05\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2651(self):
		result = ConfigParserTestFunction("\n\n\n\x01\x00\x00\x00\x00\x04\n")
		self.assertEqual(result, expected_result)

	def test_2652(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x07$")
		self.assertEqual(result, expected_result)

	def test_2653(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x07\x01\x00\x07")
		self.assertEqual(result, expected_result)

	def test_2654(self):
		result = ConfigParserTestFunction("\n\x02\x01\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2655(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2656(self):
		result = ConfigParserTestFunction("\n\x0C\x02\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2657(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0D\n\x02\n")
		self.assertEqual(result, expected_result)

	def test_2658(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2659(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x04\x04\n\x00")
		self.assertEqual(result, expected_result)

	def test_2660(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2661(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x01\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_2662(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0F\x00\x00\x05\n")
		self.assertEqual(result, expected_result)

	def test_2663(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x00\x00\x03\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2664(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\x03\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_2665(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\n\x02\n")
		self.assertEqual(result, expected_result)

	def test_2666(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x0C\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2667(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\x01\x01\x01\x00")
		self.assertEqual(result, expected_result)

	def test_2668(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_2669(self):
		result = ConfigParserTestFunction("\n\n\n\n\x08\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2670(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x03\x90\x00")
		self.assertEqual(result, expected_result)

	def test_2671(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\x0F\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2672(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0D\x07")
		self.assertEqual(result, expected_result)

	def test_2673(self):
		result = ConfigParserTestFunction("\n\n\n\x0D\x02\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2674(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2675(self):
		result = ConfigParserTestFunction("\n\n\n\x0C\x03\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2676(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\n\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2677(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0E\x00\x00\x01\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2678(self):
		result = ConfigParserTestFunction("\n\x07\x01\x00\x00\x00\x04\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2679(self):
		result = ConfigParserTestFunction("\n\n\n\x0F\x01\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2680(self):
		result = ConfigParserTestFunction("\n\x08\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2681(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x01\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2682(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\x03\x01\x01\n")
		self.assertEqual(result, expected_result)

	def test_2683(self):
		result = ConfigParserTestFunction("\n\n\x04\x00\x00\x00\x00\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_2684(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x01\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2685(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x00\x00\x00\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_2686(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x06\x07")
		self.assertEqual(result, expected_result)

	def test_2687(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\n\x02\x01")
		self.assertEqual(result, expected_result)

	def test_2688(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2689(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\n\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2690(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x02\x01\x02")
		self.assertEqual(result, expected_result)

	def test_2691(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\x0F\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2692(self):
		result = ConfigParserTestFunction("\n\n\n\n\x04\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2693(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x08\x05\x00")
		self.assertEqual(result, expected_result)

	def test_2694(self):
		result = ConfigParserTestFunction("\n\n\n\n\x05\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_2695(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_2696(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\x0E\n")
		self.assertEqual(result, expected_result)

	def test_2697(self):
		result = ConfigParserTestFunction("\n\x04\x00\x00\x00\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_2698(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0E\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2699(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\x07\n")
		self.assertEqual(result, expected_result)

	def test_2700(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2701(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x02\x00\x00\x05\n")
		self.assertEqual(result, expected_result)

	def test_2702(self):
		result = ConfigParserTestFunction("\n\n\n\n\x08\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_2703(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x01\x00\x00\x00\x01\x01")
		self.assertEqual(result, expected_result)

	def test_2704(self):
		result = ConfigParserTestFunction("\n\n\x08\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2705(self):
		result = ConfigParserTestFunction("\n\n\x0B\x04\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2706(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\x07\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2707(self):
		result = ConfigParserTestFunction("\n\n\x0B\x01\x00\x01\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2708(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2709(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x0B\n\x00")
		self.assertEqual(result, expected_result)

	def test_2710(self):
		result = ConfigParserTestFunction("\n\n\n\x0C\x03\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2711(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x04\x10\x00")
		self.assertEqual(result, expected_result)

	def test_2712(self):
		result = ConfigParserTestFunction("\n\n\x01\x01\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2713(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x82")
		self.assertEqual(result, expected_result)

	def test_2714(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0D\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2715(self):
		result = ConfigParserTestFunction("\n\x00\x01\x00\x00\x01\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_2716(self):
		result = ConfigParserTestFunction("\x04\x00\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2717(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0B\x04")
		self.assertEqual(result, expected_result)

	def test_2718(self):
		result = ConfigParserTestFunction("\n\n\x0D\x03\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2719(self):
		result = ConfigParserTestFunction("\n\x0E\x04\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2720(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xFE")
		self.assertEqual(result, expected_result)

	def test_2721(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\n\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2722(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\x00\x01\x00\x02")
		self.assertEqual(result, expected_result)

	def test_2723(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\x02\x04")
		self.assertEqual(result, expected_result)

	def test_2724(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x00\x00\x00\x06\n")
		self.assertEqual(result, expected_result)

	def test_2725(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x0B\n\n")
		self.assertEqual(result, expected_result)

	def test_2726(self):
		result = ConfigParserTestFunction("\x01\x00\x00\x00\x00\x00\x00\x02\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2727(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x01\x00\x01\x00\n")
		self.assertEqual(result, expected_result)

	def test_2728(self):
		result = ConfigParserTestFunction("\x05\x03\x00\x00\x00\x00\x00\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_2729(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x01\x01")
		self.assertEqual(result, expected_result)

	def test_2730(self):
		result = ConfigParserTestFunction("\x0C\x06\x00\x00\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_2731(self):
		result = ConfigParserTestFunction("\n\x0B\x00\x00\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2732(self):
		result = ConfigParserTestFunction("\x05\x00\x00\x00\x00\x00\x00\x01\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2733(self):
		result = ConfigParserTestFunction("\n\x02\x01\x00\x00\x00\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2734(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x02&")
		self.assertEqual(result, expected_result)

	def test_2735(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x00%")
		self.assertEqual(result, expected_result)

	def test_2736(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x03\n\x00")
		self.assertEqual(result, expected_result)

	def test_2737(self):
		result = ConfigParserTestFunction("\x00\x03\x00\x00\x01\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2738(self):
		result = ConfigParserTestFunction("\n\n\x02\x01\x00\x00\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_2739(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x1C\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2740(self):
		result = ConfigParserTestFunction("\x07\x00\x00\x00\x00\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_2741(self):
		result = ConfigParserTestFunction("\n\n\x0C\x00\x00\x01\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2742(self):
		result = ConfigParserTestFunction("\n\x02\x01\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2743(self):
		result = ConfigParserTestFunction("\n\x0C\x02\x00\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2744(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\x07\x00\x02")
		self.assertEqual(result, expected_result)

	def test_2745(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n6")
		self.assertEqual(result, expected_result)

	def test_2746(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\x07\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2747(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\x07\x01\x00")
		self.assertEqual(result, expected_result)

	def test_2748(self):
		result = ConfigParserTestFunction("\n\n\t\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2749(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x01g")
		self.assertEqual(result, expected_result)

	def test_2750(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x00\x00\x01\x00\n")
		self.assertEqual(result, expected_result)

	def test_2751(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0D\n\x01\x00")
		self.assertEqual(result, expected_result)

	def test_2752(self):
		result = ConfigParserTestFunction("\n\n\n\x06\x01\x03\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2753(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2754(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x08\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2755(self):
		result = ConfigParserTestFunction("\n\n\n\x0C\x00\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2756(self):
		result = ConfigParserTestFunction("\n\n\x0D\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2757(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\x0E\x01")
		self.assertEqual(result, expected_result)

	def test_2758(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x01\x01\x00\x06")
		self.assertEqual(result, expected_result)

	def test_2759(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\n\n\n\x00")
		self.assertEqual(result, expected_result)

	def test_2760(self):
		result = ConfigParserTestFunction("\n\n\n\x0E\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2761(self):
		result = ConfigParserTestFunction("\n\n\n\x07\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2762(self):
		result = ConfigParserTestFunction("\n\n\x0C\x00\x01\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2763(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\n\n\x00\n")
		self.assertEqual(result, expected_result)

	def test_2764(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x03\x07")
		self.assertEqual(result, expected_result)

	def test_2765(self):
		result = ConfigParserTestFunction("\n\x0B\x04\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2766(self):
		result = ConfigParserTestFunction("\n\x04\x00\x00\x00\x00\x01\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_2767(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x00\x01\x01\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2768(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x08\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2769(self):
		result = ConfigParserTestFunction("\x05\x02\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2770(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x08\x07")
		self.assertEqual(result, expected_result)

	def test_2771(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x04\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_2772(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x03\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2773(self):
		result = ConfigParserTestFunction("\n\x08\x00\x00\x00\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_2774(self):
		result = ConfigParserTestFunction("\x06\x03\x06\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2775(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xB2")
		self.assertEqual(result, expected_result)

	def test_2776(self):
		result = ConfigParserTestFunction("\x03\x01\x00\x01\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2777(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\n\n\n\n")
		self.assertEqual(result, expected_result)

	def test_2778(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x06\x91\x00")
		self.assertEqual(result, expected_result)

	def test_2779(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x03\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2780(self):
		result = ConfigParserTestFunction("\n\n\x00\x01\x00\x01\x00\x00\x00\x06")
		self.assertEqual(result, expected_result)

	def test_2781(self):
		result = ConfigParserTestFunction("\n\x01\x01\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2782(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x06\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2783(self):
		result = ConfigParserTestFunction("\n\n\n\x08\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2784(self):
		result = ConfigParserTestFunction("\n\n\x0C\x01\x01\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2785(self):
		result = ConfigParserTestFunction("\n\n\n\x0E\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2786(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x00\x00\x00\x00\x00\x04")
		self.assertEqual(result, expected_result)

	def test_2787(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\x01\x00\x02")
		self.assertEqual(result, expected_result)

	def test_2788(self):
		result = ConfigParserTestFunction("\n\x04\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2789(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x01\x00\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2790(self):
		result = ConfigParserTestFunction("\x00\x02\x00\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2791(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\n\x00\x05")
		self.assertEqual(result, expected_result)

	def test_2792(self):
		result = ConfigParserTestFunction("\x02\x01\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2793(self):
		result = ConfigParserTestFunction("\n\n\n\n\x08\x01\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2794(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x07\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2795(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x01\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_2796(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x02\x01\x05")
		self.assertEqual(result, expected_result)

	def test_2797(self):
		result = ConfigParserTestFunction("\n\x04\x00\x00\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_2798(self):
		result = ConfigParserTestFunction("\n\x06\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2799(self):
		result = ConfigParserTestFunction("\n\n\x07\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2800(self):
		result = ConfigParserTestFunction("\n\n\n\x0D\x02\x00\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2801(self):
		result = ConfigParserTestFunction("\n\x02\x05\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2802(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x00\x02\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2803(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x01\x02\x05")
		self.assertEqual(result, expected_result)

	def test_2804(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x03\x01\x01\x00")
		self.assertEqual(result, expected_result)

	def test_2805(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x03\x00\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_2806(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x08\x02")
		self.assertEqual(result, expected_result)

	def test_2807(self):
		result = ConfigParserTestFunction("\n\n\x04\x00\x00\x00\x01\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2808(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0F\x04\x00")
		self.assertEqual(result, expected_result)

	def test_2809(self):
		result = ConfigParserTestFunction("\n\n\n\x01\x02\x01\x00\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_2810(self):
		result = ConfigParserTestFunction("\n\n\n\x04\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2811(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x02\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_2812(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x04\x00\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_2813(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\n\n\x06")
		self.assertEqual(result, expected_result)

	def test_2814(self):
		result = ConfigParserTestFunction("\n\n\n\n\x08\x00\x01\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2815(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\n\x06")
		self.assertEqual(result, expected_result)

	def test_2816(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xAF")
		self.assertEqual(result, expected_result)

	def test_2817(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\x01\x01\x00")
		self.assertEqual(result, expected_result)

	def test_2818(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x02\x02'")
		self.assertEqual(result, expected_result)

	def test_2819(self):
		result = ConfigParserTestFunction("\n\n\x0B\x03\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2820(self):
		result = ConfigParserTestFunction("\n\n\x02\x00\x00\x00\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2821(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x01\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2822(self):
		result = ConfigParserTestFunction("\n\n\n\n\x06\x00\x01\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2823(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x05\x06\x00")
		self.assertEqual(result, expected_result)

	def test_2824(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0E\x00\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2825(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x00\x00\x01\x06\n")
		self.assertEqual(result, expected_result)

	def test_2826(self):
		result = ConfigParserTestFunction("\n\n\n\n\x04\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2827(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x03\x00\x01\x03")
		self.assertEqual(result, expected_result)

	def test_2828(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0F\x81\x00")
		self.assertEqual(result, expected_result)

	def test_2829(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\n\n\x04")
		self.assertEqual(result, expected_result)

	def test_2830(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x06\x00\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_2831(self):
		result = ConfigParserTestFunction("\n\n\n\n\x07\x03\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2832(self):
		result = ConfigParserTestFunction("\n\x00\x01\x00\x00\x01\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2833(self):
		result = ConfigParserTestFunction("\x08\x00\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2834(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\x04\x01")
		self.assertEqual(result, expected_result)

	def test_2835(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2836(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0F\x14\x00")
		self.assertEqual(result, expected_result)

	def test_2837(self):
		result = ConfigParserTestFunction("\n\n\n\x05\x01\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2838(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n2")
		self.assertEqual(result, expected_result)

	def test_2839(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x01B\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2840(self):
		result = ConfigParserTestFunction("\x07\x00\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2841(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x05\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2842(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x00\x01\x01\x03\n")
		self.assertEqual(result, expected_result)

	def test_2843(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x0C\x01\x00")
		self.assertEqual(result, expected_result)

	def test_2844(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x06\x02\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2845(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x01\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_2846(self):
		result = ConfigParserTestFunction("\x06\x00\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2847(self):
		result = ConfigParserTestFunction("\x06\x00\x00\x00\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_2848(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x03\x00\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2849(self):
		result = ConfigParserTestFunction("\n\x04\x01\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2850(self):
		result = ConfigParserTestFunction("\n\x03\x00\x00\x00\x00\x01\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_2851(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x08\x15\x00")
		self.assertEqual(result, expected_result)

	def test_2852(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x00\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2853(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x01\x00\x05\n")
		self.assertEqual(result, expected_result)

	def test_2854(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x90")
		self.assertEqual(result, expected_result)

	def test_2855(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nv")
		self.assertEqual(result, expected_result)

	def test_2856(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x05\x00")
		self.assertEqual(result, expected_result)

	def test_2857(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\n\n\x01\n")
		self.assertEqual(result, expected_result)

	def test_2858(self):
		result = ConfigParserTestFunction("\x01\x01\x01\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2859(self):
		result = ConfigParserTestFunction("\n\x02\x00\x00\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_2860(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x07\x01\x01\x07")
		self.assertEqual(result, expected_result)

	def test_2861(self):
		result = ConfigParserTestFunction("\x0F\x02\x00\x00\x00\x00\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2862(self):
		result = ConfigParserTestFunction("\n\n\x0D\x00\x01\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2863(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0D\x08\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2864(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\x01\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2865(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x16\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2866(self):
		result = ConfigParserTestFunction("\n\n\n\x07\x01\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2867(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x02\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2868(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x00\x00\x00G")
		self.assertEqual(result, expected_result)

	def test_2869(self):
		result = ConfigParserTestFunction("\n\x01\x00\x00\x00\x00\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2870(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0D\x04\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2871(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x06\x05")
		self.assertEqual(result, expected_result)

	def test_2872(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x81")
		self.assertEqual(result, expected_result)

	def test_2873(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x04\x01")
		self.assertEqual(result, expected_result)

	def test_2874(self):
		result = ConfigParserTestFunction("\n\n\n\x0B\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2875(self):
		result = ConfigParserTestFunction("\n\n\x0E\x00\x00\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_2876(self):
		result = ConfigParserTestFunction("\n\n\n\x04\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2877(self):
		result = ConfigParserTestFunction("\n\n\n\n\x14\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2878(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\ns")
		self.assertEqual(result, expected_result)

	def test_2879(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\x03\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2880(self):
		result = ConfigParserTestFunction("\n\x00\x02\x00\x00\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2881(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\x07\x00\x03")
		self.assertEqual(result, expected_result)

	def test_2882(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x1E\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2883(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x00\x00\x00\x00\x00\x04")
		self.assertEqual(result, expected_result)

	def test_2884(self):
		result = ConfigParserTestFunction("\n\x04\x01\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2885(self):
		result = ConfigParserTestFunction("\x04\x01\x00\x05\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2886(self):
		result = ConfigParserTestFunction("\n\n\n\n\x04\x01\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2887(self):
		result = ConfigParserTestFunction("\n\x0B\x04\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2888(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x04\x01\n")
		self.assertEqual(result, expected_result)

	def test_2889(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x02\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2890(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x00\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2891(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x0C\x01\x01")
		self.assertEqual(result, expected_result)

	def test_2892(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2893(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x01\x80\x00")
		self.assertEqual(result, expected_result)

	def test_2894(self):
		result = ConfigParserTestFunction("\n\n\x0C\x00\x00\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_2895(self):
		result = ConfigParserTestFunction("\x01\x00\x00\x00\x00\x01\x00\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_2896(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x1E\\\x00")
		self.assertEqual(result, expected_result)

	def test_2897(self):
		result = ConfigParserTestFunction("\n\n\n\n\x07\x02\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2898(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x04\x06")
		self.assertEqual(result, expected_result)

	def test_2899(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x06\x03\x00")
		self.assertEqual(result, expected_result)

	def test_2900(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nc")
		self.assertEqual(result, expected_result)

	def test_2901(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x07\x00\x02")
		self.assertEqual(result, expected_result)

	def test_2902(self):
		result = ConfigParserTestFunction("\n\n\n\x0C\x04\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2903(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x04\x04\x01")
		self.assertEqual(result, expected_result)

	def test_2904(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x16 \x00")
		self.assertEqual(result, expected_result)

	def test_2905(self):
		result = ConfigParserTestFunction("\x02\x00\x00\x01\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2906(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0F\x01\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2907(self):
		result = ConfigParserTestFunction("\x04\n\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2908(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x03\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_2909(self):
		result = ConfigParserTestFunction("\n\n\n\x0E\x01\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2910(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2911(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\x00\x00\x07\n")
		self.assertEqual(result, expected_result)

	def test_2912(self):
		result = ConfigParserTestFunction("\n\n\x02\x02\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2913(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xC3")
		self.assertEqual(result, expected_result)

	def test_2914(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x02\x00\x04\n\x00")
		self.assertEqual(result, expected_result)

	def test_2915(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x00\x03\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2916(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x03\x00\x01\x01\n")
		self.assertEqual(result, expected_result)

	def test_2917(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x01\x01\x02")
		self.assertEqual(result, expected_result)

	def test_2918(self):
		result = ConfigParserTestFunction("\n\n\n\x07\x03\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2919(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nC")
		self.assertEqual(result, expected_result)

	def test_2920(self):
		result = ConfigParserTestFunction("\n\x03\x00\x00\x00\x00\x00\x00\x03\n")
		self.assertEqual(result, expected_result)

	def test_2921(self):
		result = ConfigParserTestFunction("\n\x05\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2922(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\x0C\x00")
		self.assertEqual(result, expected_result)

	def test_2923(self):
		result = ConfigParserTestFunction("\x08\n\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2924(self):
		result = ConfigParserTestFunction("\n\n\x0C\x03\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2925(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x01\x03")
		self.assertEqual(result, expected_result)

	def test_2926(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0F\x01\x02\x00")
		self.assertEqual(result, expected_result)

	def test_2927(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x00\x00\x00\x02\x07\x00")
		self.assertEqual(result, expected_result)

	def test_2928(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x00\x03\x00")
		self.assertEqual(result, expected_result)

	def test_2929(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x02\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2930(self):
		result = ConfigParserTestFunction("\n\n\x06\x02\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2931(self):
		result = ConfigParserTestFunction("\n\n\n\n\x04\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2932(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\n\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_2933(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x03\x00\x07\n")
		self.assertEqual(result, expected_result)

	def test_2934(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nV")
		self.assertEqual(result, expected_result)

	def test_2935(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x02\x01\x03\n\x00")
		self.assertEqual(result, expected_result)

	def test_2936(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x01\x00\x00\x00\x02\x01")
		self.assertEqual(result, expected_result)

	def test_2937(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x16\x0D\x00")
		self.assertEqual(result, expected_result)

	def test_2938(self):
		result = ConfigParserTestFunction("\x0F\x01\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2939(self):
		result = ConfigParserTestFunction("\x05\n\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2940(self):
		result = ConfigParserTestFunction("\n\x03\x00\x00\x00\x00\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2941(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nU")
		self.assertEqual(result, expected_result)

	def test_2942(self):
		result = ConfigParserTestFunction("\x03\x02\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2943(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x00\x01\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2944(self):
		result = ConfigParserTestFunction("\x05\x00\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2945(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x0D\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2946(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x02G")
		self.assertEqual(result, expected_result)

	def test_2947(self):
		result = ConfigParserTestFunction("\n\n\x00\x01\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2948(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x0D\x00")
		self.assertEqual(result, expected_result)

	def test_2949(self):
		result = ConfigParserTestFunction("\x07\x00\x00\x01\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2950(self):
		result = ConfigParserTestFunction("\n\n\x0E\x00\x00\x00\x00\x04\n\x00")
		self.assertEqual(result, expected_result)

	def test_2951(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nZ")
		self.assertEqual(result, expected_result)

	def test_2952(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x05\x04\x00")
		self.assertEqual(result, expected_result)

	def test_2953(self):
		result = ConfigParserTestFunction("\n\x01\x02\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2954(self):
		result = ConfigParserTestFunction("\n\x0B\x02\x00\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2955(self):
		result = ConfigParserTestFunction("\n\n\n\x04\x00\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_2956(self):
		result = ConfigParserTestFunction("\x01\x00\x01\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2957(self):
		result = ConfigParserTestFunction("\n\n\x00\x07\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_2958(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0D\x04\x01\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2959(self):
		result = ConfigParserTestFunction("\n\x05\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2960(self):
		result = ConfigParserTestFunction("\n\x01\x01\x01\x00\x00\x01\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_2961(self):
		result = ConfigParserTestFunction("\n\x0B\x06\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2962(self):
		result = ConfigParserTestFunction("\x06\x00\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2963(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x0C\x02\x00")
		self.assertEqual(result, expected_result)

	def test_2964(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x03\x02\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2965(self):
		result = ConfigParserTestFunction("\n\n\n\x04\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_2966(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x01\x02")
		self.assertEqual(result, expected_result)

	def test_2967(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\n\n\x01\x00")
		self.assertEqual(result, expected_result)

	def test_2968(self):
		result = ConfigParserTestFunction("\x01\x00\x00\x01\x00\x01\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2969(self):
		result = ConfigParserTestFunction("\n\x07\x02\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2970(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x00F")
		self.assertEqual(result, expected_result)

	def test_2971(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0E\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2972(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x01\x01\x01")
		self.assertEqual(result, expected_result)

	def test_2973(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x0B\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2974(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\x04\x00")
		self.assertEqual(result, expected_result)

	def test_2975(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x01\x03\x00")
		self.assertEqual(result, expected_result)

	def test_2976(self):
		result = ConfigParserTestFunction("\n\n\x0D\x02\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2977(self):
		result = ConfigParserTestFunction("\x0F\x00\x00\x00\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2978(self):
		result = ConfigParserTestFunction("\n\n\x0B\x00\x01\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_2979(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_2980(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x16\\\x00")
		self.assertEqual(result, expected_result)

	def test_2981(self):
		result = ConfigParserTestFunction("\n\n\x0E\x00\x00\x00\x00\x05\n\x00")
		self.assertEqual(result, expected_result)

	def test_2982(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x01\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_2983(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x00e")
		self.assertEqual(result, expected_result)

	def test_2984(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\x01\x00\x03")
		self.assertEqual(result, expected_result)

	def test_2985(self):
		result = ConfigParserTestFunction("\n\n\t\x03\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2986(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x00\x05\n\x00")
		self.assertEqual(result, expected_result)

	def test_2987(self):
		result = ConfigParserTestFunction("\n\x0C\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2988(self):
		result = ConfigParserTestFunction("\n\t\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2989(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x01\x02\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2990(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x07\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2991(self):
		result = ConfigParserTestFunction("\n\n\n\n\x03\x00\x01\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2992(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x02\n\x00")
		self.assertEqual(result, expected_result)

	def test_2993(self):
		result = ConfigParserTestFunction("\n\x0B\x00\x01\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2994(self):
		result = ConfigParserTestFunction("\n\n\n\n\x05\x01\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2995(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2996(self):
		result = ConfigParserTestFunction("\n\n\x0C\x00\x00\x01\x01\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_2997(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x02\x02\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2998(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x00\x01\x01\x00\x01\x01")
		self.assertEqual(result, expected_result)

	def test_2999(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x07\x01\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3000(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x9D")
		self.assertEqual(result, expected_result)

	def test_3001(self):
		result = ConfigParserTestFunction("\n\n\n\x06\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3002(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0D\x04\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3003(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x01\x00\x01\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_3004(self):
		result = ConfigParserTestFunction("\n\x02\x00\x00\x00\x00\x00\x03\n\x00")
		self.assertEqual(result, expected_result)

	def test_3005(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x07\"")
		self.assertEqual(result, expected_result)

	def test_3006(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x02\x00\x03")
		self.assertEqual(result, expected_result)

	def test_3007(self):
		result = ConfigParserTestFunction("\x03\x00\x00\x00\x01\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3008(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x00\x01'")
		self.assertEqual(result, expected_result)

	def test_3009(self):
		result = ConfigParserTestFunction("\n\x0B\x02\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_3010(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0D\n\x01\x01")
		self.assertEqual(result, expected_result)

	def test_3011(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x04\x80\x00")
		self.assertEqual(result, expected_result)

	def test_3012(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0E\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3013(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x07\x03")
		self.assertEqual(result, expected_result)

	def test_3014(self):
		result = ConfigParserTestFunction("\n\n\x06\x00\x01\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3015(self):
		result = ConfigParserTestFunction("\n\n\x05\x01\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_3016(self):
		result = ConfigParserTestFunction("\n\n\x08\x00\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_3017(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x16\t\x00")
		self.assertEqual(result, expected_result)

	def test_3018(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x04\x05\x01")
		self.assertEqual(result, expected_result)

	def test_3019(self):
		result = ConfigParserTestFunction("\n\n\x0C\x01\x00\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_3020(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xD3")
		self.assertEqual(result, expected_result)

	def test_3021(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x0D\x01\x00")
		self.assertEqual(result, expected_result)

	def test_3022(self):
		result = ConfigParserTestFunction("\x07\x00\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3023(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x00\x01\x02")
		self.assertEqual(result, expected_result)

	def test_3024(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\x0D\x00")
		self.assertEqual(result, expected_result)

	def test_3025(self):
		result = ConfigParserTestFunction("\n\n\x0B\x00\x00\x00\x02\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_3026(self):
		result = ConfigParserTestFunction("\x02\x00\x00\x00\x00\x00\x00\x05\n\x00")
		self.assertEqual(result, expected_result)

	def test_3027(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\n\x0C")
		self.assertEqual(result, expected_result)

	def test_3028(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x86")
		self.assertEqual(result, expected_result)

	def test_3029(self):
		result = ConfigParserTestFunction("\n\n\n\x01\x00\x00\x01\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_3030(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\t\x0B\x00")
		self.assertEqual(result, expected_result)

	def test_3031(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x08\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3032(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x0C\x03")
		self.assertEqual(result, expected_result)

	def test_3033(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x01\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3034(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x02\x03\x00\n")
		self.assertEqual(result, expected_result)

	def test_3035(self):
		result = ConfigParserTestFunction("\n\n\x0D\x00\x00\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_3036(self):
		result = ConfigParserTestFunction("\n\n\n\x0E\x01\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3037(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nP")
		self.assertEqual(result, expected_result)

	def test_3038(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x03\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_3039(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x00\x00\x00\x00\x02\n\x00")
		self.assertEqual(result, expected_result)

	def test_3040(self):
		result = ConfigParserTestFunction("\x08\x00\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3041(self):
		result = ConfigParserTestFunction("\n\n\x0B\x04\x01\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3042(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x1E\t\x00")
		self.assertEqual(result, expected_result)

	def test_3043(self):
		result = ConfigParserTestFunction("\x00\x01\x00\x00\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3044(self):
		result = ConfigParserTestFunction("\x06\x00\x00\x01\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3045(self):
		result = ConfigParserTestFunction("\n\x0B\x02\x00\x00\x00\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3046(self):
		result = ConfigParserTestFunction("\n\n\n\n\x04\x01\x00\x01\x01\x00")
		self.assertEqual(result, expected_result)

	def test_3047(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x01\x00\x02\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3048(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0B\x07\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3049(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x05\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3050(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x06\xA1\x00")
		self.assertEqual(result, expected_result)

	def test_3051(self):
		result = ConfigParserTestFunction("\n\x07\x00\x00\x00\x02\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3052(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\n\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_3053(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x04$")
		self.assertEqual(result, expected_result)

	def test_3054(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x01\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_3055(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x01\x00\x03\x00")
		self.assertEqual(result, expected_result)

	def test_3056(self):
		result = ConfigParserTestFunction("\x02\x01\x01\x00\x00\x00\x00\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_3057(self):
		result = ConfigParserTestFunction("\n\n\x0B\x07\x00\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_3058(self):
		result = ConfigParserTestFunction("\n\n\n\x01\x01\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3059(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\x0B\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3060(self):
		result = ConfigParserTestFunction("\n\x0C\x00\x00\x00\x00\x00\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_3061(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x16\x10\x00")
		self.assertEqual(result, expected_result)

	def test_3062(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x05\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3063(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\x02\x00\n")
		self.assertEqual(result, expected_result)

	def test_3064(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x01\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3065(self):
		result = ConfigParserTestFunction("\n\x0B\x07\x00\x00\x01\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3066(self):
		result = ConfigParserTestFunction("\n\n\x0D\x01\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3067(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x04\x00\x02")
		self.assertEqual(result, expected_result)

	def test_3068(self):
		result = ConfigParserTestFunction("\n\n\n\n\x03\x02\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3069(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x16'\x00")
		self.assertEqual(result, expected_result)

	def test_3070(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0D\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3071(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x1E\x10\x00")
		self.assertEqual(result, expected_result)

	def test_3072(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x08\x06")
		self.assertEqual(result, expected_result)

	def test_3073(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_3074(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x07\x07")
		self.assertEqual(result, expected_result)

	def test_3075(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xF3")
		self.assertEqual(result, expected_result)

	def test_3076(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x00\x00\x00\x00F")
		self.assertEqual(result, expected_result)

	def test_3077(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x06\x00\x03")
		self.assertEqual(result, expected_result)

	def test_3078(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\t\n\x00")
		self.assertEqual(result, expected_result)

	def test_3079(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\n\n\x04")
		self.assertEqual(result, expected_result)

	def test_3080(self):
		result = ConfigParserTestFunction("\x00\x02\x00\x00\x00\x00\x01\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_3081(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\n\x00\x02\x00")
		self.assertEqual(result, expected_result)

	def test_3082(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nS")
		self.assertEqual(result, expected_result)

	def test_3083(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x05\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_3084(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\x01\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3085(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xD6")
		self.assertEqual(result, expected_result)

	def test_3086(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\x01\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3087(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x01\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3088(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_3089(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n&")
		self.assertEqual(result, expected_result)

	def test_3090(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\n\n\x05")
		self.assertEqual(result, expected_result)

	def test_3091(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0E\x00\x00\x00\x01\x01")
		self.assertEqual(result, expected_result)

	def test_3092(self):
		result = ConfigParserTestFunction("\n\n\x00\x02\x00\x01\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_3093(self):
		result = ConfigParserTestFunction("\n\n\x01\x02\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3094(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x00\x01\x00\n")
		self.assertEqual(result, expected_result)

	def test_3095(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x0F\n\x00")
		self.assertEqual(result, expected_result)

	def test_3096(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x02\x02\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3097(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0D\n\n\x04")
		self.assertEqual(result, expected_result)

	def test_3098(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\x01\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_3099(self):
		result = ConfigParserTestFunction("\n\x0E\x03\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3100(self):
		result = ConfigParserTestFunction("\n\n\n\x0C\x01\x01\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3101(self):
		result = ConfigParserTestFunction("\n\n\x0B\x06\x01\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3102(self):
		result = ConfigParserTestFunction("\n\n\x0C\x01\x01\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_3103(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x01\x01'")
		self.assertEqual(result, expected_result)

	def test_3104(self):
		result = ConfigParserTestFunction("\x07\x02\x00\x01\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3105(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0D\x02\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_3106(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\x05\x00")
		self.assertEqual(result, expected_result)

	def test_3107(self):
		result = ConfigParserTestFunction("\n\n\n\n\t\x02\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3108(self):
		result = ConfigParserTestFunction("\n\n\t\x01\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_3109(self):
		result = ConfigParserTestFunction("\n\n\n\n\x03\x02\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3110(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0E\x02\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_3111(self):
		result = ConfigParserTestFunction("\n\n\n\t\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3112(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x05\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_3113(self):
		result = ConfigParserTestFunction("\n\n\n\x05\x00\x00\x00\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_3114(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x01\x07\n\x00")
		self.assertEqual(result, expected_result)

	def test_3115(self):
		result = ConfigParserTestFunction("\n\x04\x00\x00\x00\x01\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_3116(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x01\x01\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_3117(self):
		result = ConfigParserTestFunction("\n\n\x03\x01\x01\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3118(self):
		result = ConfigParserTestFunction("\n\n\x04\x01\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3119(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x01\x01\x05\n")
		self.assertEqual(result, expected_result)

	def test_3120(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3121(self):
		result = ConfigParserTestFunction("\x02\x00\x00\x00\x00\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3122(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0F\x05\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3123(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x07\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3124(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\n\n\x05")
		self.assertEqual(result, expected_result)

	def test_3125(self):
		result = ConfigParserTestFunction("\n\n\n\n\x08\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3126(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x7F")
		self.assertEqual(result, expected_result)

	def test_3127(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x01\x07\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3128(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x01\x01\x05\n\x00")
		self.assertEqual(result, expected_result)

	def test_3129(self):
		result = ConfigParserTestFunction("\n\n\n\x05\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3130(self):
		result = ConfigParserTestFunction("\n\n\x01\x00\x00\x00\x03\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3131(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x07g")
		self.assertEqual(result, expected_result)

	def test_3132(self):
		result = ConfigParserTestFunction("\n\n\x0D\x03\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_3133(self):
		result = ConfigParserTestFunction("\x06\x07\x06\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3134(self):
		result = ConfigParserTestFunction("\n\n\x0C\x02\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3135(self):
		result = ConfigParserTestFunction("\x04\x00\x00\x03\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3136(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x00\x01\x00\x03")
		self.assertEqual(result, expected_result)

	def test_3137(self):
		result = ConfigParserTestFunction("\x03\x00\x00\x00\x00\x04\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3138(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\n\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3139(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x06\xC0\x00")
		self.assertEqual(result, expected_result)

	def test_3140(self):
		result = ConfigParserTestFunction("\x07\x01\x01\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3141(self):
		result = ConfigParserTestFunction("\n\n\x0D\x02\x00\x00\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3142(self):
		result = ConfigParserTestFunction("\x0C\x02\x00\x00\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_3143(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x1E'\x00")
		self.assertEqual(result, expected_result)

	def test_3144(self):
		result = ConfigParserTestFunction("\n\n\x0C\x02\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3145(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x00\x13\x00")
		self.assertEqual(result, expected_result)

	def test_3146(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xF6")
		self.assertEqual(result, expected_result)

	def test_3147(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xE6")
		self.assertEqual(result, expected_result)

	def test_3148(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\n\x03\n")
		self.assertEqual(result, expected_result)

	def test_3149(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x06\x07\x00")
		self.assertEqual(result, expected_result)

	def test_3150(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\x06\x02")
		self.assertEqual(result, expected_result)

	def test_3151(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x1E \x00")
		self.assertEqual(result, expected_result)

	def test_3152(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\x06\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3153(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\x01\x00\x04")
		self.assertEqual(result, expected_result)

	def test_3154(self):
		result = ConfigParserTestFunction("\n\n\x0B\x05\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3155(self):
		result = ConfigParserTestFunction("\n\n\n\x0D\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3156(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x06\xD1\x00")
		self.assertEqual(result, expected_result)

	def test_3157(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\x03\x00\x01")
		self.assertEqual(result, expected_result)

	def test_3158(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n>")
		self.assertEqual(result, expected_result)

	def test_3159(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x06\x03")
		self.assertEqual(result, expected_result)

	def test_3160(self):
		result = ConfigParserTestFunction("\n\x03\x03\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3161(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x0B\x06\n")
		self.assertEqual(result, expected_result)

	def test_3162(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x07\x06\x02")
		self.assertEqual(result, expected_result)

	def test_3163(self):
		result = ConfigParserTestFunction("\x02\x00\x00\x00\x00\x04\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3164(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x03\x07")
		self.assertEqual(result, expected_result)

	def test_3165(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x06\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_3166(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x00\x03\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3167(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x04\"")
		self.assertEqual(result, expected_result)

	def test_3168(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x02\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_3169(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\n\n\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3170(self):
		result = ConfigParserTestFunction("\n\n\x04\x01\x00\x00\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_3171(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\np")
		self.assertEqual(result, expected_result)

	def test_3172(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x05\x04")
		self.assertEqual(result, expected_result)

	def test_3173(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x04\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_3174(self):
		result = ConfigParserTestFunction("\n\n\n\x05\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3175(self):
		result = ConfigParserTestFunction("\n\x02\x01\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3176(self):
		result = ConfigParserTestFunction("\n\n\n\n\x07\x00\x00\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_3177(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x01\x90\x00")
		self.assertEqual(result, expected_result)

	def test_3178(self):
		result = ConfigParserTestFunction("\n\n\x06\x00\x02\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3179(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0F\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_3180(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\x02\x01\n")
		self.assertEqual(result, expected_result)

	def test_3181(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x07G")
		self.assertEqual(result, expected_result)

	def test_3182(self):
		result = ConfigParserTestFunction("\n\n\x0D\x02\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3183(self):
		result = ConfigParserTestFunction("\n\n\t\x00\x00\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_3184(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\n\n\n\x00\n")
		self.assertEqual(result, expected_result)

	def test_3185(self):
		result = ConfigParserTestFunction("\x04\x00\x04\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3186(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0C\x06\x00")
		self.assertEqual(result, expected_result)

	def test_3187(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x08\x82\x00")
		self.assertEqual(result, expected_result)

	def test_3188(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0EG")
		self.assertEqual(result, expected_result)

	def test_3189(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x06\x00\x04")
		self.assertEqual(result, expected_result)

	def test_3190(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\t\n\n")
		self.assertEqual(result, expected_result)

	def test_3191(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x1E\x80\x00")
		self.assertEqual(result, expected_result)

	def test_3192(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\x02\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3193(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\x01\x03")
		self.assertEqual(result, expected_result)

	def test_3194(self):
		result = ConfigParserTestFunction("\n\x01\x00\x00\x01\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3195(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\n\n\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3196(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x00\x00\x02\x06\n")
		self.assertEqual(result, expected_result)

	def test_3197(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\n\n\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3198(self):
		result = ConfigParserTestFunction("\n\n\n\x07\x01\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3199(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\n\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3200(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x0C\x00\x01")
		self.assertEqual(result, expected_result)

	def test_3201(self):
		result = ConfigParserTestFunction("\n\n\n\n\x05\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3202(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x03\x02\x00")
		self.assertEqual(result, expected_result)

	def test_3203(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\x02\x01")
		self.assertEqual(result, expected_result)

	def test_3204(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0EF")
		self.assertEqual(result, expected_result)

	def test_3205(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x03\x12\x00")
		self.assertEqual(result, expected_result)

	def test_3206(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x00\x02\x07")
		self.assertEqual(result, expected_result)

	def test_3207(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\n\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3208(self):
		result = ConfigParserTestFunction("\n\x00\x01\x00\x00\x00\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_3209(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\n\n\n\n\x00")
		self.assertEqual(result, expected_result)

	def test_3210(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x04\x03")
		self.assertEqual(result, expected_result)

	def test_3211(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\x01\x02\x00")
		self.assertEqual(result, expected_result)

	def test_3212(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x05\x02\x01")
		self.assertEqual(result, expected_result)

	def test_3213(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\x03\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3214(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\n\n\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_3215(self):
		result = ConfigParserTestFunction("\n\n\n\x01\x00\x00\x00\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_3216(self):
		result = ConfigParserTestFunction("\x08\x00\x00\x01\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3217(self):
		result = ConfigParserTestFunction("\x01\x02\x00\x00\x00\x01\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_3218(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\x01\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_3219(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n@")
		self.assertEqual(result, expected_result)

	def test_3220(self):
		result = ConfigParserTestFunction("\n\t\x00\x00\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3221(self):
		result = ConfigParserTestFunction("\n\n\x00\x02\x00\x00\x00\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_3222(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\x02\x04")
		self.assertEqual(result, expected_result)

	def test_3223(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x01\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3224(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\x01\x05")
		self.assertEqual(result, expected_result)

	def test_3225(self):
		result = ConfigParserTestFunction("\n\n\x0C\x02\x01\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3226(self):
		result = ConfigParserTestFunction("\n\n\x02\x04\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3227(self):
		result = ConfigParserTestFunction("\n\x01\x00\x00\x01\x00\x03\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3228(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x03\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3229(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x1E\x0D\x00")
		self.assertEqual(result, expected_result)

	def test_3230(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\n\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3231(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x08$")
		self.assertEqual(result, expected_result)

	def test_3232(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x02\x00\x00\x03\n")
		self.assertEqual(result, expected_result)

	def test_3233(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x07\x00")
		self.assertEqual(result, expected_result)

	def test_3234(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0F\x84\x00")
		self.assertEqual(result, expected_result)

	def test_3235(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x00\x00\x04")
		self.assertEqual(result, expected_result)

	def test_3236(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0F\x02")
		self.assertEqual(result, expected_result)

	def test_3237(self):
		result = ConfigParserTestFunction("\n\x0C\x01\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3238(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n5")
		self.assertEqual(result, expected_result)

	def test_3239(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x02\x01\x00\x01\x01")
		self.assertEqual(result, expected_result)

	def test_3240(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x03\x00\x02")
		self.assertEqual(result, expected_result)

	def test_3241(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\x01\x01\x02")
		self.assertEqual(result, expected_result)

	def test_3242(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x02\x02\x00")
		self.assertEqual(result, expected_result)

	def test_3243(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x00\x00\x00\x00\x00\x03\n")
		self.assertEqual(result, expected_result)

	def test_3244(self):
		result = ConfigParserTestFunction("\n\n\x04\x02\x00\x00\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_3245(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\x04\x02")
		self.assertEqual(result, expected_result)

	def test_3246(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x01\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3247(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x01B")
		self.assertEqual(result, expected_result)

	def test_3248(self):
		result = ConfigParserTestFunction("\n\n\n\n\x06\x00\x00\x00\x01\x01")
		self.assertEqual(result, expected_result)

	def test_3249(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x02\x05\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3250(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\n\n\n\n\n")
		self.assertEqual(result, expected_result)

	def test_3251(self):
		result = ConfigParserTestFunction("\x06\x00\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3252(self):
		result = ConfigParserTestFunction("\n\x0B\x02\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3253(self):
		result = ConfigParserTestFunction("\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3254(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3255(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\x02\x05")
		self.assertEqual(result, expected_result)

	def test_3256(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x8A")
		self.assertEqual(result, expected_result)

	def test_3257(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xA6")
		self.assertEqual(result, expected_result)

	def test_3258(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x07\x02\x01\x00")
		self.assertEqual(result, expected_result)

	def test_3259(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\n\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3260(self):
		result = ConfigParserTestFunction("\n\n\n\x06\x01\x01\x00\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_3261(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x05\x03")
		self.assertEqual(result, expected_result)

	def test_3262(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x00\x00\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3263(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x01\x00\x07\x00")
		self.assertEqual(result, expected_result)

	def test_3264(self):
		result = ConfigParserTestFunction("\x04\x00\x00\x00\x00\x00\x00\x01\x00\n")
		self.assertEqual(result, expected_result)

	def test_3265(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\x0D\x00")
		self.assertEqual(result, expected_result)

	def test_3266(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x02\x12\x00")
		self.assertEqual(result, expected_result)

	def test_3267(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\x05\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3268(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x02F")
		self.assertEqual(result, expected_result)

	def test_3269(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x02\x02")
		self.assertEqual(result, expected_result)

	def test_3270(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\n\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3271(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x01\x02\x02")
		self.assertEqual(result, expected_result)

	def test_3272(self):
		result = ConfigParserTestFunction("\x06\x00\x00\x00\x01\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3273(self):
		result = ConfigParserTestFunction("\x02\x02\x00\x00\x00\x01\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3274(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0D\n\x01\x04")
		self.assertEqual(result, expected_result)

	def test_3275(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\n\x02\n\x00")
		self.assertEqual(result, expected_result)

	def test_3276(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\n\n\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3277(self):
		result = ConfigParserTestFunction("\n\x03\x00\x00\x00\x00\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_3278(self):
		result = ConfigParserTestFunction("\x03\x00\x00\x00\x00\x00\x00\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_3279(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x04\x01\x02")
		self.assertEqual(result, expected_result)

	def test_3280(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n:")
		self.assertEqual(result, expected_result)

	def test_3281(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\x01\x01\x01")
		self.assertEqual(result, expected_result)

	def test_3282(self):
		result = ConfigParserTestFunction("\x01\x03\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3283(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\n\n\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3284(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\n\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3285(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x05\x01\x00")
		self.assertEqual(result, expected_result)

	def test_3286(self):
		result = ConfigParserTestFunction("\n\x04\x00\x00\x00\x00\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3287(self):
		result = ConfigParserTestFunction("\n\n\n\x0F\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3288(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x02B")
		self.assertEqual(result, expected_result)

	def test_3289(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x02\x03'")
		self.assertEqual(result, expected_result)

	def test_3290(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\n\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3291(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x15\x00")
		self.assertEqual(result, expected_result)

	def test_3292(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\x01\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_3293(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\n\n\n\n\x00")
		self.assertEqual(result, expected_result)

	def test_3294(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\n\n\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3295(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x05\x11\x00")
		self.assertEqual(result, expected_result)

	def test_3296(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_3297(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\x04\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_3298(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\n\n\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_3299(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\n\n\n\n\n")
		self.assertEqual(result, expected_result)

	def test_3300(self):
		result = ConfigParserTestFunction("\x02\x00\x00\x00\x00\x02\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3301(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x1A\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3302(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\n\x01\x00\n")
		self.assertEqual(result, expected_result)

	def test_3303(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\t\x00")
		self.assertEqual(result, expected_result)

	def test_3304(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0C\x03")
		self.assertEqual(result, expected_result)

	def test_3305(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\x04\x01\x00\x05")
		self.assertEqual(result, expected_result)

	def test_3306(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3307(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0F\x05\n\x00")
		self.assertEqual(result, expected_result)

	def test_3308(self):
		result = ConfigParserTestFunction("\n\n\n\n\t\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3309(self):
		result = ConfigParserTestFunction("\n\x0E\x00\x00\x00\x00\x01\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_3310(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x1A\\\x00")
		self.assertEqual(result, expected_result)

	def test_3311(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3312(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x01\x01\x02\x01")
		self.assertEqual(result, expected_result)

	def test_3313(self):
		result = ConfigParserTestFunction("\n\x04\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3314(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x0E\x01\x03")
		self.assertEqual(result, expected_result)

	def test_3315(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\x01\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3316(self):
		result = ConfigParserTestFunction("\n\n\x08\x00\x00\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_3317(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_3318(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n3")
		self.assertEqual(result, expected_result)

	def test_3319(self):
		result = ConfigParserTestFunction("\n\n\x0D\x00\x01\x00\x00\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_3320(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nf")
		self.assertEqual(result, expected_result)

	def test_3321(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x02\x01\x00\x05\n")
		self.assertEqual(result, expected_result)

	def test_3322(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x03\x00\x01\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_3323(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x01\x00\x00\x04\n\x00")
		self.assertEqual(result, expected_result)

	def test_3324(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x03\x00\x03")
		self.assertEqual(result, expected_result)

	def test_3325(self):
		result = ConfigParserTestFunction("\n\n\n\n\x04\x03\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3326(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x00\x00\x00\x02\n\x00")
		self.assertEqual(result, expected_result)

	def test_3327(self):
		result = ConfigParserTestFunction("\n\n\x06\x00\x00\x00\x02\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3328(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x03\x00\x00\x07")
		self.assertEqual(result, expected_result)

	def test_3329(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xFC")
		self.assertEqual(result, expected_result)

	def test_3330(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x05\x01")
		self.assertEqual(result, expected_result)

	def test_3331(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x1A\x0D\x00")
		self.assertEqual(result, expected_result)

	def test_3332(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\n\n\n\x00\n")
		self.assertEqual(result, expected_result)

	def test_3333(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xB6")
		self.assertEqual(result, expected_result)

	def test_3334(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x08\"")
		self.assertEqual(result, expected_result)

	def test_3335(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x1A\x10\x00")
		self.assertEqual(result, expected_result)

	def test_3336(self):
		result = ConfigParserTestFunction("\n\x03\x00\x00\x00\x00\x00\x00\x07\n")
		self.assertEqual(result, expected_result)

	def test_3337(self):
		result = ConfigParserTestFunction("\n\x0B\x07\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3338(self):
		result = ConfigParserTestFunction("\n\n\x01\x00\x00\x00\x01\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_3339(self):
		result = ConfigParserTestFunction("\n\n\n\x05\x01\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3340(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x00\x02\x05")
		self.assertEqual(result, expected_result)

	def test_3341(self):
		result = ConfigParserTestFunction("\n\n\n\x07\x00\x02\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3342(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x08\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3343(self):
		result = ConfigParserTestFunction("\n\n\x0F\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3344(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x00\x01\x00\x02\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_3345(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x1A\t\x00")
		self.assertEqual(result, expected_result)

	def test_3346(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x1A \x00")
		self.assertEqual(result, expected_result)

	def test_3347(self):
		result = ConfigParserTestFunction("\n\x06\x01\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3348(self):
		result = ConfigParserTestFunction("\n\n\n\n\x07\x00\x00\x01\x02\n")
		self.assertEqual(result, expected_result)

	def test_3349(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x01\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_3350(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x00\x00\x00\x02\x00\n")
		self.assertEqual(result, expected_result)

	def test_3351(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\t\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3352(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x08\x01\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_3353(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\x00\x04\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3354(self):
		result = ConfigParserTestFunction("\n\x00\x06\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3355(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\n\n\x00\x01")
		self.assertEqual(result, expected_result)

	def test_3356(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\x01\x03")
		self.assertEqual(result, expected_result)

	def test_3357(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x03\x01\x02\x00")
		self.assertEqual(result, expected_result)

	def test_3358(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x06\x02")
		self.assertEqual(result, expected_result)

	def test_3359(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x05\x01")
		self.assertEqual(result, expected_result)

	def test_3360(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x05\x00\x02")
		self.assertEqual(result, expected_result)

	def test_3361(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x05\x04")
		self.assertEqual(result, expected_result)

	def test_3362(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x07\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3363(self):
		result = ConfigParserTestFunction("\n\x0C\x00\x01\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3364(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x02\x02\x00")
		self.assertEqual(result, expected_result)

	def test_3365(self):
		result = ConfigParserTestFunction("\x07\x03\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3366(self):
		result = ConfigParserTestFunction("\n\n\n\x0C\x00\x00\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3367(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xF1")
		self.assertEqual(result, expected_result)

	def test_3368(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x07\x03\x01")
		self.assertEqual(result, expected_result)

	def test_3369(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x05\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_3370(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x01\x06\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3371(self):
		result = ConfigParserTestFunction("\n\n\x00\x03\x00\x00\x01\x00\x00\x04")
		self.assertEqual(result, expected_result)

	def test_3372(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x00\x00\x00\x00e")
		self.assertEqual(result, expected_result)

	def test_3373(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\n\n\x08")
		self.assertEqual(result, expected_result)

	def test_3374(self):
		result = ConfigParserTestFunction("\n\n\x00\x01\x00\x01\x01\x00\x00\x06")
		self.assertEqual(result, expected_result)

	def test_3375(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\x02\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3376(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x02\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_3377(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x00\x01\x00\x00\x00\x04")
		self.assertEqual(result, expected_result)

	def test_3378(self):
		result = ConfigParserTestFunction("\x04\x00\x00\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_3379(self):
		result = ConfigParserTestFunction("\n\n\n\x0B\x01\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3380(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\n\x03\n")
		self.assertEqual(result, expected_result)

	def test_3381(self):
		result = ConfigParserTestFunction("\n\n\n\n\x08\x01\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3382(self):
		result = ConfigParserTestFunction("\n\x02\x00\x02\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3383(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x02g")
		self.assertEqual(result, expected_result)

	def test_3384(self):
		result = ConfigParserTestFunction("\x00\x01\x00\x00\x00\x00\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_3385(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x03\x00\x01\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_3386(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x00\x01\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_3387(self):
		result = ConfigParserTestFunction("\n\n\t\x00\x01\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3388(self):
		result = ConfigParserTestFunction("\n\n\x0B\x02\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3389(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x06\x00")
		self.assertEqual(result, expected_result)

	def test_3390(self):
		result = ConfigParserTestFunction("\n\n\x05\x01\x00\x00\x00\x00\x03\n")
		self.assertEqual(result, expected_result)

	def test_3391(self):
		result = ConfigParserTestFunction("\n\n\n\n\x14\x01\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3392(self):
		result = ConfigParserTestFunction("\n\n\x03\x00\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_3393(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0F\x00\x01\x05\n")
		self.assertEqual(result, expected_result)

	def test_3394(self):
		result = ConfigParserTestFunction("\n\n\n\n\x05\x01\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3395(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0E\x01\x01\x01\n")
		self.assertEqual(result, expected_result)

	def test_3396(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x02f")
		self.assertEqual(result, expected_result)

	def test_3397(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\n\x03\n\x00")
		self.assertEqual(result, expected_result)

	def test_3398(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x1A'\x00")
		self.assertEqual(result, expected_result)

	def test_3399(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x07\x00\x01\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_3400(self):
		result = ConfigParserTestFunction("\x02\x01\x00\x00\x00\x04\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3401(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_3402(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_3403(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x02\x05\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3404(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x06\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3405(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x02\x02\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3406(self):
		result = ConfigParserTestFunction("\n\x01\x02\x00\x00\x00\x04\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3407(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x07\x00\x00\x06")
		self.assertEqual(result, expected_result)

	def test_3408(self):
		result = ConfigParserTestFunction("\n\n\x02\x00\x00\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_3409(self):
		result = ConfigParserTestFunction("\n\n\n\x0D\x00\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3410(self):
		result = ConfigParserTestFunction("\n\n\x00\x03\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3411(self):
		result = ConfigParserTestFunction("\n\n\x0B\x07\x00\x00\x00\x02\n\x00")
		self.assertEqual(result, expected_result)

	def test_3412(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x00\x00\x00\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_3413(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xA5")
		self.assertEqual(result, expected_result)

	def test_3414(self):
		result = ConfigParserTestFunction("\n\n\x02\x00\x00\x01\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_3415(self):
		result = ConfigParserTestFunction("\n\n\n\x07\x03\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_3416(self):
		result = ConfigParserTestFunction("\n\x0C\x02\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3417(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x00\x00\x06\n")
		self.assertEqual(result, expected_result)

	def test_3418(self):
		result = ConfigParserTestFunction("\n\n\x07\x00\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3419(self):
		result = ConfigParserTestFunction("\n\n\n\x07\x00\x00\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3420(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\x07\x01")
		self.assertEqual(result, expected_result)

	def test_3421(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x16\x01\x00")
		self.assertEqual(result, expected_result)

	def test_3422(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0E\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_3423(self):
		result = ConfigParserTestFunction("\x0C\x01\x00\x00\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_3424(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\n\n\n\n\x01")
		self.assertEqual(result, expected_result)

	def test_3425(self):
		result = ConfigParserTestFunction("\n\x00\x00\x01\x00\x00\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_3426(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\n\x07\n")
		self.assertEqual(result, expected_result)

	def test_3427(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0D\x06\x00")
		self.assertEqual(result, expected_result)

	def test_3428(self):
		result = ConfigParserTestFunction("\x0E\x00\x00\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_3429(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\x0B\x01\x00")
		self.assertEqual(result, expected_result)

	def test_3430(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3431(self):
		result = ConfigParserTestFunction("\n\n\n\n\x04\x00\x00\x01\x00\n")
		self.assertEqual(result, expected_result)

	def test_3432(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x02\x01\x02\x01")
		self.assertEqual(result, expected_result)

	def test_3433(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0F\x05\x00")
		self.assertEqual(result, expected_result)

	def test_3434(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xAA")
		self.assertEqual(result, expected_result)

	def test_3435(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x00\x02\x00\n")
		self.assertEqual(result, expected_result)

	def test_3436(self):
		result = ConfigParserTestFunction("\n\n\n\n\x1B\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3437(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x00\x00\x00\x00\x01\x03")
		self.assertEqual(result, expected_result)

	def test_3438(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x05\x03\x01")
		self.assertEqual(result, expected_result)

	def test_3439(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x00\x83\x00")
		self.assertEqual(result, expected_result)

	def test_3440(self):
		result = ConfigParserTestFunction("\x01\x00\x00\x00\x00\x01\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3441(self):
		result = ConfigParserTestFunction("\n\x05\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3442(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x15\x01")
		self.assertEqual(result, expected_result)

	def test_3443(self):
		result = ConfigParserTestFunction("\n\n\n\n\x07\x00\x00\x00\x00\x04")
		self.assertEqual(result, expected_result)

	def test_3444(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x01\x00\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3445(self):
		result = ConfigParserTestFunction("\n\n\x0D\x02\x00\x01\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3446(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x02\x01\x01\x05\n")
		self.assertEqual(result, expected_result)

	def test_3447(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x00\x01\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_3448(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0F\x06")
		self.assertEqual(result, expected_result)

	def test_3449(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xCA")
		self.assertEqual(result, expected_result)

	def test_3450(self):
		result = ConfigParserTestFunction("\n\n\n\x05\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3451(self):
		result = ConfigParserTestFunction("\n\n\n\x04\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_3452(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\n\x01\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3453(self):
		result = ConfigParserTestFunction("\n\n\x02\x00\x00\x02\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3454(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x00\x00\x00\x00\x01\x05")
		self.assertEqual(result, expected_result)

	def test_3455(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0C\x04\x00")
		self.assertEqual(result, expected_result)

	def test_3456(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0E\x00\x02\x00")
		self.assertEqual(result, expected_result)

	def test_3457(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0D\n\x03\n")
		self.assertEqual(result, expected_result)

	def test_3458(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x06\x07")
		self.assertEqual(result, expected_result)

	def test_3459(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x03\x01\x00")
		self.assertEqual(result, expected_result)

	def test_3460(self):
		result = ConfigParserTestFunction("\n\n\n\x0C\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3461(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x07\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_3462(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0E\x83\x00")
		self.assertEqual(result, expected_result)

	def test_3463(self):
		result = ConfigParserTestFunction("\x05\x00\x00\x00\x01\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3464(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x00\x00\x01\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3465(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x00\x00\x02\x01\n")
		self.assertEqual(result, expected_result)

	def test_3466(self):
		result = ConfigParserTestFunction("\n\x02\x00\x05\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3467(self):
		result = ConfigParserTestFunction("\n\n\n\x0D\x01\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3468(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x02\x02\x05")
		self.assertEqual(result, expected_result)

	def test_3469(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x00\x91\x00")
		self.assertEqual(result, expected_result)

	def test_3470(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x08D")
		self.assertEqual(result, expected_result)

	def test_3471(self):
		result = ConfigParserTestFunction("\x0E\x00\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3472(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x16\x11\x00")
		self.assertEqual(result, expected_result)

	def test_3473(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\n\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_3474(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\n\x00\x03")
		self.assertEqual(result, expected_result)

	def test_3475(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x01\x07\x03")
		self.assertEqual(result, expected_result)

	def test_3476(self):
		result = ConfigParserTestFunction("\n\n\n\n\x07\x00\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_3477(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x01\x01\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3478(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0D\x08\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_3479(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n]")
		self.assertEqual(result, expected_result)

	def test_3480(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0F\x83\x00")
		self.assertEqual(result, expected_result)

	def test_3481(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x06\x01\x03")
		self.assertEqual(result, expected_result)

	def test_3482(self):
		result = ConfigParserTestFunction("\n\n\x07\x00\x00\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3483(self):
		result = ConfigParserTestFunction("\x02\x03\x00\x00\x01\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3484(self):
		result = ConfigParserTestFunction("\n\n\n\x0E\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3485(self):
		result = ConfigParserTestFunction("\n\n\n\x0F\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3486(self):
		result = ConfigParserTestFunction("\n\n\n\x0C\x00\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_3487(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0B\t\x00")
		self.assertEqual(result, expected_result)

	def test_3488(self):
		result = ConfigParserTestFunction("\x03\x00\x00\x00\x00\x00\x00\x00\x00D")
		self.assertEqual(result, expected_result)

	def test_3489(self):
		result = ConfigParserTestFunction("\n\t\x01\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3490(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x05\n")
		self.assertEqual(result, expected_result)

	def test_3491(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\x00\x05")
		self.assertEqual(result, expected_result)

	def test_3492(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x03\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3493(self):
		result = ConfigParserTestFunction("\x00\x01\x00\x00\x00\x02\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3494(self):
		result = ConfigParserTestFunction("\n\n\n\x0C\x01\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3495(self):
		result = ConfigParserTestFunction("\n\n\x01\x01\x00\x00\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3496(self):
		result = ConfigParserTestFunction("\n\x01\x01\x00\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3497(self):
		result = ConfigParserTestFunction("\n\n\x05\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3498(self):
		result = ConfigParserTestFunction("\n\x06\x00\x00\x00\x00\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3499(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x02\x00\x01\x00\x03")
		self.assertEqual(result, expected_result)

	def test_3500(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0Eg")
		self.assertEqual(result, expected_result)

	def test_3501(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\x0F\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3502(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x06\x07\x02")
		self.assertEqual(result, expected_result)

	def test_3503(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\n\n\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3504(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x04\x06\x00")
		self.assertEqual(result, expected_result)

	def test_3505(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x00\x00\x04")
		self.assertEqual(result, expected_result)

	def test_3506(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\x03\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3507(self):
		result = ConfigParserTestFunction("\x05\x00\x00\x00\x00\x00\x00\x02\x00\x01")
		self.assertEqual(result, expected_result)

	def test_3508(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0C\x05\x00")
		self.assertEqual(result, expected_result)

	def test_3509(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x1A\x80\x00")
		self.assertEqual(result, expected_result)

	def test_3510(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x03\x02")
		self.assertEqual(result, expected_result)

	def test_3511(self):
		result = ConfigParserTestFunction("\n\n\x02\x01\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3512(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x05\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3513(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x07\x07\x01")
		self.assertEqual(result, expected_result)

	def test_3514(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0C\x0D\x00")
		self.assertEqual(result, expected_result)

	def test_3515(self):
		result = ConfigParserTestFunction("\n\n\n\x0E\x02\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_3516(self):
		result = ConfigParserTestFunction("\n\x0B\x06\x00\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3517(self):
		result = ConfigParserTestFunction("\n\n\n\n\x19\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3518(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x00\x00\x00\x03\n\x00")
		self.assertEqual(result, expected_result)

	def test_3519(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x01\xA0\x00")
		self.assertEqual(result, expected_result)

	def test_3520(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\x04\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3521(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\n\n\t")
		self.assertEqual(result, expected_result)

	def test_3522(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xC5")
		self.assertEqual(result, expected_result)

	def test_3523(self):
		result = ConfigParserTestFunction("\x01\x00\x00\x00\x00\x00\x00\x00\x01\x01")
		self.assertEqual(result, expected_result)

	def test_3524(self):
		result = ConfigParserTestFunction("\n\n\x0B\x05\x00\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_3525(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x03\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3526(self):
		result = ConfigParserTestFunction("\n\n\x02\x02\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3527(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x06\x06")
		self.assertEqual(result, expected_result)

	def test_3528(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x0B\x01\x00")
		self.assertEqual(result, expected_result)

	def test_3529(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x03'")
		self.assertEqual(result, expected_result)

	def test_3530(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x00\x00\x00\x00\x02\x02")
		self.assertEqual(result, expected_result)

	def test_3531(self):
		result = ConfigParserTestFunction("\n\n\n\n\x03\x00\x01\x01\x01\x00")
		self.assertEqual(result, expected_result)

	def test_3532(self):
		result = ConfigParserTestFunction("\n\n\x01\x01\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_3533(self):
		result = ConfigParserTestFunction("\n\n\x02\x02\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3534(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\n\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3535(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0F\x00\x02\x00")
		self.assertEqual(result, expected_result)

	def test_3536(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0F\x15\x00")
		self.assertEqual(result, expected_result)

	def test_3537(self):
		result = ConfigParserTestFunction("\x0C\x04\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3538(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nT")
		self.assertEqual(result, expected_result)

	def test_3539(self):
		result = ConfigParserTestFunction("\n\n\x05\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3540(self):
		result = ConfigParserTestFunction("\x0C\x07\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3541(self):
		result = ConfigParserTestFunction("\x01\x06\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3542(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n#")
		self.assertEqual(result, expected_result)

	def test_3543(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x03\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_3544(self):
		result = ConfigParserTestFunction("\n\n\x01\x01\x00\x00\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_3545(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0D\x01\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_3546(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x08\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_3547(self):
		result = ConfigParserTestFunction("\n\n\x01\x00\x00\x00\x00\x00\x05\n")
		self.assertEqual(result, expected_result)

	def test_3548(self):
		result = ConfigParserTestFunction("\n\n\x0F\x00\x00\x00\x00\x04\n\x00")
		self.assertEqual(result, expected_result)

	def test_3549(self):
		result = ConfigParserTestFunction("\n\x0C\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3550(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0D\n\n\x08")
		self.assertEqual(result, expected_result)

	def test_3551(self):
		result = ConfigParserTestFunction("\n\x00\x02\x01\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3552(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0F\x00\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3553(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xC4")
		self.assertEqual(result, expected_result)

	def test_3554(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0F\x91\x00")
		self.assertEqual(result, expected_result)

	def test_3555(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x01\x91\x00")
		self.assertEqual(result, expected_result)

	def test_3556(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0D\x04\x00")
		self.assertEqual(result, expected_result)

	def test_3557(self):
		result = ConfigParserTestFunction("\x04\x01\x00\x00\x00\x01\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3558(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nj")
		self.assertEqual(result, expected_result)

	def test_3559(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0F\x01\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3560(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x01&")
		self.assertEqual(result, expected_result)

	def test_3561(self):
		result = ConfigParserTestFunction("\n\x02\x02\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3562(self):
		result = ConfigParserTestFunction("\n\n\n\n\t\x03\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3563(self):
		result = ConfigParserTestFunction("\x08\x00\x01\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3564(self):
		result = ConfigParserTestFunction("\x03\x01\x03\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_3565(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x01\x07\x00")
		self.assertEqual(result, expected_result)

	def test_3566(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x02\x01\x01\x01\x00")
		self.assertEqual(result, expected_result)

	def test_3567(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\x03\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3568(self):
		result = ConfigParserTestFunction("\n\n\n\n\x07\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3569(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x1E\x90\x00")
		self.assertEqual(result, expected_result)

	def test_3570(self):
		result = ConfigParserTestFunction("\n\n\x0B\x00\x03\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3571(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x00\x02\x06")
		self.assertEqual(result, expected_result)

	def test_3572(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\x02\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3573(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x01\x02\x07")
		self.assertEqual(result, expected_result)

	def test_3574(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\n\n\n\x00\x01")
		self.assertEqual(result, expected_result)

	def test_3575(self):
		result = ConfigParserTestFunction("\x0D\x00\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3576(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x00\x02\x02\n")
		self.assertEqual(result, expected_result)

	def test_3577(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x02\x00\x01\x01\x03")
		self.assertEqual(result, expected_result)

	def test_3578(self):
		result = ConfigParserTestFunction("\n\n\x0F\x01\x00\x00\x00\x04\n\x00")
		self.assertEqual(result, expected_result)

	def test_3579(self):
		result = ConfigParserTestFunction("\n\n\x04\x00\x01\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_3580(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\x0F\x04")
		self.assertEqual(result, expected_result)

	def test_3581(self):
		result = ConfigParserTestFunction("\x0F\x00\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3582(self):
		result = ConfigParserTestFunction("\n\n\t\x03\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_3583(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x00\x00\x00\x00\x00\x04")
		self.assertEqual(result, expected_result)

	def test_3584(self):
		result = ConfigParserTestFunction("\x0C\x07\x00\x00\x00\x01\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3585(self):
		result = ConfigParserTestFunction("\n\x0D\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3586(self):
		result = ConfigParserTestFunction("\x0C\n\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3587(self):
		result = ConfigParserTestFunction("\n\n\x07\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_3588(self):
		result = ConfigParserTestFunction("\n\x06\x01\x00\x00\x00\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3589(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n9")
		self.assertEqual(result, expected_result)

	def test_3590(self):
		result = ConfigParserTestFunction("\n\n\n\n\x07\x01\x01\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3591(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x05\x00\x02")
		self.assertEqual(result, expected_result)

	def test_3592(self):
		result = ConfigParserTestFunction("\n\n\x0B\x00\x02\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3593(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xFF")
		self.assertEqual(result, expected_result)

	def test_3594(self):
		result = ConfigParserTestFunction("\n\n\x02\x02\x00\x00\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_3595(self):
		result = ConfigParserTestFunction("\x0C\x0E\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3596(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x0D\x00")
		self.assertEqual(result, expected_result)

	def test_3597(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x06\x82\x00")
		self.assertEqual(result, expected_result)

	def test_3598(self):
		result = ConfigParserTestFunction("\x00\x00\x00\x00\x00\x00\x01\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_3599(self):
		result = ConfigParserTestFunction("\x0C\n\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3600(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x03\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_3601(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x0C\x00\x04")
		self.assertEqual(result, expected_result)

	def test_3602(self):
		result = ConfigParserTestFunction("\x01\x01\x01\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3603(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x00G")
		self.assertEqual(result, expected_result)

	def test_3604(self):
		result = ConfigParserTestFunction("\n\x03\x00\x00\x01\x00\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_3605(self):
		result = ConfigParserTestFunction("\x03\x01\x00\x00\x01\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3606(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x07\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_3607(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x0D\n\x00")
		self.assertEqual(result, expected_result)

	def test_3608(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nu")
		self.assertEqual(result, expected_result)

	def test_3609(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\x0F\x01\x01")
		self.assertEqual(result, expected_result)

	def test_3610(self):
		result = ConfigParserTestFunction("\x00\x02\x00\x00\x00\x00\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_3611(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x0E\x02\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3612(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\x02\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3613(self):
		result = ConfigParserTestFunction("\n\x06\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3614(self):
		result = ConfigParserTestFunction("\x04\x00\x00\x00\x01\x00\x00\x00\x03\n")
		self.assertEqual(result, expected_result)

	def test_3615(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0E\x01\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3616(self):
		result = ConfigParserTestFunction("\x0C\n\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3617(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xF5")
		self.assertEqual(result, expected_result)

	def test_3618(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\x0B\x01")
		self.assertEqual(result, expected_result)

	def test_3619(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n%")
		self.assertEqual(result, expected_result)

	def test_3620(self):
		result = ConfigParserTestFunction("\x0C\n\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3621(self):
		result = ConfigParserTestFunction("\n\n\n\x0F\x00\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3622(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\t\x0E")
		self.assertEqual(result, expected_result)

	def test_3623(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\n\n\n\n\x02")
		self.assertEqual(result, expected_result)

	def test_3624(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xEA")
		self.assertEqual(result, expected_result)

	def test_3625(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x02\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3626(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x03\xA0\x00")
		self.assertEqual(result, expected_result)

	def test_3627(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x03\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_3628(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xD5")
		self.assertEqual(result, expected_result)

	def test_3629(self):
		result = ConfigParserTestFunction("\n\n\n\n\x04\x00\x00\x00\x00\x04")
		self.assertEqual(result, expected_result)

	def test_3630(self):
		result = ConfigParserTestFunction("\x05\x00\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3631(self):
		result = ConfigParserTestFunction("\x00\x01\x00\x00\x00\x00\x00\x00\x00\x07")
		self.assertEqual(result, expected_result)

	def test_3632(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xBA")
		self.assertEqual(result, expected_result)

	def test_3633(self):
		result = ConfigParserTestFunction("\n\n\n\n\x08\x01\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3634(self):
		result = ConfigParserTestFunction("\n\n\n\n\x04\x00\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3635(self):
		result = ConfigParserTestFunction("\n\n\x02\x00\x00\x00\x01\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_3636(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\x0F\x02\x01")
		self.assertEqual(result, expected_result)

	def test_3637(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x0D\n\n")
		self.assertEqual(result, expected_result)

	def test_3638(self):
		result = ConfigParserTestFunction("\n\n\n\n\t\x03\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3639(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x02\x00\x00\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_3640(self):
		result = ConfigParserTestFunction("\n\n\x06\x00\x01\x01\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3641(self):
		result = ConfigParserTestFunction("\n\x01\x01\x00\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3642(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0D\x06")
		self.assertEqual(result, expected_result)

	def test_3643(self):
		result = ConfigParserTestFunction("\n\x06\x00\x00\x00\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_3644(self):
		result = ConfigParserTestFunction("\n\x02\x01\x00\x00\x02\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3645(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x08\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_3646(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0C\t\x00")
		self.assertEqual(result, expected_result)

	def test_3647(self):
		result = ConfigParserTestFunction("\x0C\n\n\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3648(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\t\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_3649(self):
		result = ConfigParserTestFunction("\x07\x02\x01\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3650(self):
		result = ConfigParserTestFunction("\n\n\n\n\x14\x02\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3651(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x02\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3652(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\x04\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3653(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\x01\x07")
		self.assertEqual(result, expected_result)

	def test_3654(self):
		result = ConfigParserTestFunction("\x0C\n\n\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3655(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x16\x81\x00")
		self.assertEqual(result, expected_result)

	def test_3656(self):
		result = ConfigParserTestFunction("\x01\x01\x00\x01\x00\x00\x00\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_3657(self):
		result = ConfigParserTestFunction("\n\x00\x01\x00\x00\x02\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_3658(self):
		result = ConfigParserTestFunction("\n\n\n\x05\x01\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3659(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x08\x85\x00")
		self.assertEqual(result, expected_result)

	def test_3660(self):
		result = ConfigParserTestFunction("\n\n\n\x07\x05\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3661(self):
		result = ConfigParserTestFunction("\n\n\x01\x00\x00\x00\x00\x01\x05\n")
		self.assertEqual(result, expected_result)

	def test_3662(self):
		result = ConfigParserTestFunction("\x0C\n\n\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3663(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\n\n\n\x01")
		self.assertEqual(result, expected_result)

	def test_3664(self):
		result = ConfigParserTestFunction("\n\n\n\n\x03\x05\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3665(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3666(self):
		result = ConfigParserTestFunction("\n\n\x02\x00\x00\x03\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3667(self):
		result = ConfigParserTestFunction("\n\n\n\n\x07\x01\x00\x01\x00\n")
		self.assertEqual(result, expected_result)

	def test_3668(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0F\x07\x00")
		self.assertEqual(result, expected_result)

	def test_3669(self):
		result = ConfigParserTestFunction("\n\n\x03\x00\x00\x00\x00\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_3670(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\x01\x00\n")
		self.assertEqual(result, expected_result)

	def test_3671(self):
		result = ConfigParserTestFunction("\n\x08\x01\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3672(self):
		result = ConfigParserTestFunction("\n\n\n\x0F\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3673(self):
		result = ConfigParserTestFunction("\n\n\n\x0B\x02\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3674(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x00\x00\x00\x01\x00\x03")
		self.assertEqual(result, expected_result)

	def test_3675(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x04\x04\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3676(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\x04\x04")
		self.assertEqual(result, expected_result)

	def test_3677(self):
		result = ConfigParserTestFunction("\x0C\n\n\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3678(self):
		result = ConfigParserTestFunction("\n\n\n\n\x08\x01\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_3679(self):
		result = ConfigParserTestFunction("\x05\x02\x00\x00\x00\x00\x00\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_3680(self):
		result = ConfigParserTestFunction("\n\n\n\x04\x07\x00\x00\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_3681(self):
		result = ConfigParserTestFunction("\x07\x00\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3682(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\t\x03")
		self.assertEqual(result, expected_result)

	def test_3683(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x02\x03\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3684(self):
		result = ConfigParserTestFunction("\n\n\x02\x00\x00\x07\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3685(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\x01\x01\x03")
		self.assertEqual(result, expected_result)

	def test_3686(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x04\x00\x01")
		self.assertEqual(result, expected_result)

	def test_3687(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x0D\n\x01")
		self.assertEqual(result, expected_result)

	def test_3688(self):
		result = ConfigParserTestFunction("\x02\x00\x00\x00\x00\x01\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3689(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_3690(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\t\x0C\x00")
		self.assertEqual(result, expected_result)

	def test_3691(self):
		result = ConfigParserTestFunction("\n\x0E\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3692(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x06\x04")
		self.assertEqual(result, expected_result)

	def test_3693(self):
		result = ConfigParserTestFunction("\n\x01\x03\x00\x00\x01\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3694(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x00\x07\x02")
		self.assertEqual(result, expected_result)

	def test_3695(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0D\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3696(self):
		result = ConfigParserTestFunction("\n\n\x08\x01\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3697(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x04D")
		self.assertEqual(result, expected_result)

	def test_3698(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\x0F\x01\x00")
		self.assertEqual(result, expected_result)

	def test_3699(self):
		result = ConfigParserTestFunction("\x03\x02\x00\x01\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3700(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x00\x01\x00\x00\x01\x04")
		self.assertEqual(result, expected_result)

	def test_3701(self):
		result = ConfigParserTestFunction("\n\n\n\n\x06\x00\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3702(self):
		result = ConfigParserTestFunction("\x0C\n\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3703(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x01\x02\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3704(self):
		result = ConfigParserTestFunction("\n\x01\x02\x00\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3705(self):
		result = ConfigParserTestFunction("\n\n\n\n\t\x03\x04\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3706(self):
		result = ConfigParserTestFunction("\n\t\x02\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3707(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x07\x00\x01\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3708(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x05\x01\x01\n")
		self.assertEqual(result, expected_result)

	def test_3709(self):
		result = ConfigParserTestFunction("\n\n\n\n\x06\x00\x00\x00\x00\x04")
		self.assertEqual(result, expected_result)

	def test_3710(self):
		result = ConfigParserTestFunction("\n\n\n\x0F\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3711(self):
		result = ConfigParserTestFunction("\n\n\t\x01\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3712(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x05\x01")
		self.assertEqual(result, expected_result)

	def test_3713(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x0F\x03")
		self.assertEqual(result, expected_result)

	def test_3714(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3715(self):
		result = ConfigParserTestFunction("\x0C\n\n\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3716(self):
		result = ConfigParserTestFunction("\n\x0B\x03\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3717(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\n\n\n\n\x03")
		self.assertEqual(result, expected_result)

	def test_3718(self):
		result = ConfigParserTestFunction("\n\n\n\x04\x07\x00\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3719(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3720(self):
		result = ConfigParserTestFunction("\n\n\n\n\x1A\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3721(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x05\x01\x02")
		self.assertEqual(result, expected_result)

	def test_3722(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\n\n\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_3723(self):
		result = ConfigParserTestFunction("\n\x07\x00\x00\x00\x03\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3724(self):
		result = ConfigParserTestFunction("\x00\x01\x00\x00\x01\x02\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3725(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\n\n\x0D")
		self.assertEqual(result, expected_result)

	def test_3726(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x02\x00\x06")
		self.assertEqual(result, expected_result)

	def test_3727(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0F\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3728(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3729(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x01\x05\n\x00")
		self.assertEqual(result, expected_result)

	def test_3730(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0D\x08\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_3731(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\x03\x00\x03\n")
		self.assertEqual(result, expected_result)

	def test_3732(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x15\x04")
		self.assertEqual(result, expected_result)

	def test_3733(self):
		result = ConfigParserTestFunction("\x02\x01\x00\x00\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3734(self):
		result = ConfigParserTestFunction("\x0C\n\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3735(self):
		result = ConfigParserTestFunction("\x0C\n\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3736(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0F\x17\x00")
		self.assertEqual(result, expected_result)

	def test_3737(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0D\x05\x00")
		self.assertEqual(result, expected_result)

	def test_3738(self):
		result = ConfigParserTestFunction("\x0C\n\x01\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3739(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\x0B\x02")
		self.assertEqual(result, expected_result)

	def test_3740(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3741(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x17\x00")
		self.assertEqual(result, expected_result)

	def test_3742(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3743(self):
		result = ConfigParserTestFunction("\x0C\n\n\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3744(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x0D\x02\x00")
		self.assertEqual(result, expected_result)

	def test_3745(self):
		result = ConfigParserTestFunction("\x0C\x06\x01\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3746(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x00\x92\x00")
		self.assertEqual(result, expected_result)

	def test_3747(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0D\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3748(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x00\x01\x04\n\x00")
		self.assertEqual(result, expected_result)

	def test_3749(self):
		result = ConfigParserTestFunction("\x00\x03\x01\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3750(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3751(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\x02\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_3752(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x02\x03\x01")
		self.assertEqual(result, expected_result)

	def test_3753(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\x03\x05")
		self.assertEqual(result, expected_result)

	def test_3754(self):
		result = ConfigParserTestFunction("\x0C\n\n\x01\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3755(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\t\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3756(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x85")
		self.assertEqual(result, expected_result)

	def test_3757(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0E\x04\x00")
		self.assertEqual(result, expected_result)

	def test_3758(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x01G")
		self.assertEqual(result, expected_result)

	def test_3759(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\x06\x01")
		self.assertEqual(result, expected_result)

	def test_3760(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\x0E\x00")
		self.assertEqual(result, expected_result)

	def test_3761(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xA4")
		self.assertEqual(result, expected_result)

	def test_3762(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\x03\x03")
		self.assertEqual(result, expected_result)

	def test_3763(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x17\x01")
		self.assertEqual(result, expected_result)

	def test_3764(self):
		result = ConfigParserTestFunction("\n\n\x0D\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3765(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xE5")
		self.assertEqual(result, expected_result)

	def test_3766(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00D\n")
		self.assertEqual(result, expected_result)

	def test_3767(self):
		result = ConfigParserTestFunction("\x01\x03\x00\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_3768(self):
		result = ConfigParserTestFunction("\n\n\n\x01\x00\x03\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3769(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x02\x03")
		self.assertEqual(result, expected_result)

	def test_3770(self):
		result = ConfigParserTestFunction("\n\x0E\x00\x00\x00\x00\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_3771(self):
		result = ConfigParserTestFunction("\n\n\n\n\x04\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_3772(self):
		result = ConfigParserTestFunction("\n\n\x05\x00\x00\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_3773(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x00\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3774(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\n\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3775(self):
		result = ConfigParserTestFunction("\x0C\n\x01\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3776(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x06\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3777(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\x03\n")
		self.assertEqual(result, expected_result)

	def test_3778(self):
		result = ConfigParserTestFunction("\x0C\x0E\x01\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3779(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x01\x00\x00\x02\n\x00")
		self.assertEqual(result, expected_result)

	def test_3780(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\n\x03\x00")
		self.assertEqual(result, expected_result)

	def test_3781(self):
		result = ConfigParserTestFunction("\t\x00\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3782(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x04\x01\x00")
		self.assertEqual(result, expected_result)

	def test_3783(self):
		result = ConfigParserTestFunction("\n\n\x0B\x03\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3784(self):
		result = ConfigParserTestFunction("\n\n\x01\x01\x01\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3785(self):
		result = ConfigParserTestFunction("\n\n\n\x07\x02\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3786(self):
		result = ConfigParserTestFunction("\n\n\x02\x00\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_3787(self):
		result = ConfigParserTestFunction("\x0C\n\x01\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3788(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0E\x14\x00")
		self.assertEqual(result, expected_result)

	def test_3789(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\x0B\x03")
		self.assertEqual(result, expected_result)

	def test_3790(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\n\n\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3791(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x07\x07\x00")
		self.assertEqual(result, expected_result)

	def test_3792(self):
		result = ConfigParserTestFunction("\n\x00\x01\x00\x01\x00\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3793(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\n\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3794(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0B\x00\x01\x00\n")
		self.assertEqual(result, expected_result)

	def test_3795(self):
		result = ConfigParserTestFunction("\n\n\n\x0D\x03\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3796(self):
		result = ConfigParserTestFunction("\n\n\x0F\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3797(self):
		result = ConfigParserTestFunction("\x0C\n\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3798(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\x0B\x01\x01")
		self.assertEqual(result, expected_result)

	def test_3799(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0E\x01\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3800(self):
		result = ConfigParserTestFunction("\x01\x01\x00\x00\x00\x00\x00\x00\x03\n")
		self.assertEqual(result, expected_result)

	def test_3801(self):
		result = ConfigParserTestFunction("\n\x01\x01\x01\x00\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_3802(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xD4")
		self.assertEqual(result, expected_result)

	def test_3803(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_3804(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x00\x01\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3805(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0D\x0D\x00")
		self.assertEqual(result, expected_result)

	def test_3806(self):
		result = ConfigParserTestFunction("\x02\x02\x00\x00\x00\x04\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3807(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\n\n\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3808(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x07\x04\x02")
		self.assertEqual(result, expected_result)

	def test_3809(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\x0E\x04")
		self.assertEqual(result, expected_result)

	def test_3810(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x8C")
		self.assertEqual(result, expected_result)

	def test_3811(self):
		result = ConfigParserTestFunction("\n\x0C\x00\x00\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3812(self):
		result = ConfigParserTestFunction("\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3813(self):
		result = ConfigParserTestFunction("\n\n\x01\x00\x00\x00\x00\x00\x00\x06")
		self.assertEqual(result, expected_result)

	def test_3814(self):
		result = ConfigParserTestFunction("\n\x00\x02\x00\x00\x01\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3815(self):
		result = ConfigParserTestFunction("\n\x0C\x01\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3816(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\n\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_3817(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\n\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3818(self):
		result = ConfigParserTestFunction("\n\n\n\n\x07\x00\x00\x00\x01\x01")
		self.assertEqual(result, expected_result)

	def test_3819(self):
		result = ConfigParserTestFunction("\x0C\n\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3820(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n.")
		self.assertEqual(result, expected_result)

	def test_3821(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\n\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3822(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\t\x08")
		self.assertEqual(result, expected_result)

	def test_3823(self):
		result = ConfigParserTestFunction("\x02\x00\x00\x00\x03\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3824(self):
		result = ConfigParserTestFunction("\n\n\n\x0B\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3825(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x0B\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3826(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\x01\x01\n")
		self.assertEqual(result, expected_result)

	def test_3827(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x00\x01\x00\x02\n\x00")
		self.assertEqual(result, expected_result)

	def test_3828(self):
		result = ConfigParserTestFunction("\n\x05\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3829(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0D\x00\x02\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3830(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0F\n")
		self.assertEqual(result, expected_result)

	def test_3831(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\x02\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3832(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\x01\x00\x02")
		self.assertEqual(result, expected_result)

	def test_3833(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\n\x04")
		self.assertEqual(result, expected_result)

	def test_3834(self):
		result = ConfigParserTestFunction("\n\n\x0B\x00\x01\x00\x00\x02\n\x00")
		self.assertEqual(result, expected_result)

	def test_3835(self):
		result = ConfigParserTestFunction("\x07\x00\x00\x00\x00\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3836(self):
		result = ConfigParserTestFunction("\n\n\x08\x01\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3837(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nE")
		self.assertEqual(result, expected_result)

	def test_3838(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x08\x03\x00")
		self.assertEqual(result, expected_result)

	def test_3839(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x04\x04\x00")
		self.assertEqual(result, expected_result)

	def test_3840(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x1A\x01\x00")
		self.assertEqual(result, expected_result)

	def test_3841(self):
		result = ConfigParserTestFunction("\n\n\n\n\x08\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3842(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0E\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_3843(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\n\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3844(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x07\x04\n\x00")
		self.assertEqual(result, expected_result)

	def test_3845(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x00\x03\x03")
		self.assertEqual(result, expected_result)

	def test_3846(self):
		result = ConfigParserTestFunction("\n\x0D\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3847(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x06\xC1\x00")
		self.assertEqual(result, expected_result)

	def test_3848(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x00\x04\x00")
		self.assertEqual(result, expected_result)

	def test_3849(self):
		result = ConfigParserTestFunction("\x03\x00\x00\x05\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3850(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0B\x06\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3851(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_3852(self):
		result = ConfigParserTestFunction("\n\n\n\x07\x01\x01\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3853(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x08\x83\x00")
		self.assertEqual(result, expected_result)

	def test_3854(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x04\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3855(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x1A\x11\x00")
		self.assertEqual(result, expected_result)

	def test_3856(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x01\x01\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3857(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\x01\x04\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3858(self):
		result = ConfigParserTestFunction("\n\x03\x01\x00\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3859(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\x02\x03")
		self.assertEqual(result, expected_result)

	def test_3860(self):
		result = ConfigParserTestFunction("\n\n\x08\x02\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3861(self):
		result = ConfigParserTestFunction("\x02\x00\x00\x00\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_3862(self):
		result = ConfigParserTestFunction("\x02\x01\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3863(self):
		result = ConfigParserTestFunction("\x0E\x01\x00\x00\x01\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3864(self):
		result = ConfigParserTestFunction("\n\n\t\x02\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3865(self):
		result = ConfigParserTestFunction("\n\n\n\x01\x02\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3866(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x8E")
		self.assertEqual(result, expected_result)

	def test_3867(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\x05\x02")
		self.assertEqual(result, expected_result)

	def test_3868(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\n\x01\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3869(self):
		result = ConfigParserTestFunction("\n\n\t\x02\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3870(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x01\x06")
		self.assertEqual(result, expected_result)

	def test_3871(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0D\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3872(self):
		result = ConfigParserTestFunction("\x0C\x07\x00\x00\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_3873(self):
		result = ConfigParserTestFunction("\n\n\n\n\x18\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3874(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x01\x00\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_3875(self):
		result = ConfigParserTestFunction("\x07\x01\x00\x00\x00\x00\x00\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_3876(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\n\n\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3877(self):
		result = ConfigParserTestFunction("\n\x00\x02\x00\x00\x00\x00\x00\x03\n")
		self.assertEqual(result, expected_result)

	def test_3878(self):
		result = ConfigParserTestFunction("\n\x05\x00\x00\x00\x01\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3879(self):
		result = ConfigParserTestFunction("\n\x00\x01\x00\x04\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3880(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\x00\x00\x01\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3881(self):
		result = ConfigParserTestFunction("\x0C\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3882(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\n\n\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3883(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\n\n\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3884(self):
		result = ConfigParserTestFunction("\n\x0B\x01\x01\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3885(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n$")
		self.assertEqual(result, expected_result)

	def test_3886(self):
		result = ConfigParserTestFunction("\n\x02\x01\x00\x00\x00\x00\x02\n\x00")
		self.assertEqual(result, expected_result)

	def test_3887(self):
		result = ConfigParserTestFunction("\n\n\n\x08\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3888(self):
		result = ConfigParserTestFunction("\n\x0C\x02\x01\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3889(self):
		result = ConfigParserTestFunction("\x03\x01\x00\x00\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3890(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x04\x00")
		self.assertEqual(result, expected_result)

	def test_3891(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0D\t\x00")
		self.assertEqual(result, expected_result)

	def test_3892(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\n\n\n\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3893(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x0F\x01\x01")
		self.assertEqual(result, expected_result)

	def test_3894(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x07\x00\x07\x03")
		self.assertEqual(result, expected_result)

	def test_3895(self):
		result = ConfigParserTestFunction("\x0D\x01\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3896(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\n\x07\n\x00")
		self.assertEqual(result, expected_result)

	def test_3897(self):
		result = ConfigParserTestFunction("\n\x02\x01\x00\x00\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_3898(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\n\x03\x01")
		self.assertEqual(result, expected_result)

	def test_3899(self):
		result = ConfigParserTestFunction("\x0C\x06\x01\x00\x01\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3900(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xAE")
		self.assertEqual(result, expected_result)

	def test_3901(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x07\x92\x00")
		self.assertEqual(result, expected_result)

	def test_3902(self):
		result = ConfigParserTestFunction("\x03\x00\x00\x00\x00\x00\x04\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3903(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0D\n\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3904(self):
		result = ConfigParserTestFunction("\n\n\n\n\t\x04\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3905(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0F\x00\x02\x01")
		self.assertEqual(result, expected_result)

	def test_3906(self):
		result = ConfigParserTestFunction("\n\n\x0B\x02\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3907(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x07\x00\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_3908(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\x02\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3909(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x03\x00\x02")
		self.assertEqual(result, expected_result)

	def test_3910(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x08\x01\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_3911(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0B\n")
		self.assertEqual(result, expected_result)

	def test_3912(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x02\x00\x05\n\x00")
		self.assertEqual(result, expected_result)

	def test_3913(self):
		result = ConfigParserTestFunction("\x01\x00\x00\x01\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3914(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0D\n\n\x01\x00")
		self.assertEqual(result, expected_result)

	def test_3915(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x06\xB1\x00")
		self.assertEqual(result, expected_result)

	def test_3916(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0D\n\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3917(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\x01\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_3918(self):
		result = ConfigParserTestFunction("\n\n\n\x01\x03\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3919(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x02\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_3920(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\n\n\n\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3921(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\n\n\n\x01\n")
		self.assertEqual(result, expected_result)

	def test_3922(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\n\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_3923(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\n\n\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3924(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x00\x06\x02")
		self.assertEqual(result, expected_result)

	def test_3925(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x00\x00\x00\x04\n\x00")
		self.assertEqual(result, expected_result)

	def test_3926(self):
		result = ConfigParserTestFunction("\n\x0B\x06\x00\x00\x00\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3927(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0D\n\n\x00\n")
		self.assertEqual(result, expected_result)

	def test_3928(self):
		result = ConfigParserTestFunction("\n\n\n\x0F\x00\x02\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3929(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3930(self):
		result = ConfigParserTestFunction("\n\n\t\x02\x00\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_3931(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x00\x01\x00\x03")
		self.assertEqual(result, expected_result)

	def test_3932(self):
		result = ConfigParserTestFunction("\n\n\x01\x01\x01\x01\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3933(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\n\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3934(self):
		result = ConfigParserTestFunction("\n\n\n\n\x04\x02\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3935(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xE4")
		self.assertEqual(result, expected_result)

	def test_3936(self):
		result = ConfigParserTestFunction("\n\n\n\n\t\x02\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3937(self):
		result = ConfigParserTestFunction("\n\n\x15\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3938(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x04\x11\x00")
		self.assertEqual(result, expected_result)

	def test_3939(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x00\x00\x01\x02")
		self.assertEqual(result, expected_result)

	def test_3940(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x01\x00\x01\x00\x03")
		self.assertEqual(result, expected_result)

	def test_3941(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\x07\n")
		self.assertEqual(result, expected_result)

	def test_3942(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\n\x02\x04")
		self.assertEqual(result, expected_result)

	def test_3943(self):
		result = ConfigParserTestFunction("\x06\x00\x00\x00\x00\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3944(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x08\x00\x01")
		self.assertEqual(result, expected_result)

	def test_3945(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0D\n\n\n\x00")
		self.assertEqual(result, expected_result)

	def test_3946(self):
		result = ConfigParserTestFunction("\x0C\n\x02\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3947(self):
		result = ConfigParserTestFunction("\x0C\n\x01\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3948(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x01\x00\x02\n\x00")
		self.assertEqual(result, expected_result)

	def test_3949(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0E\x00\x03\x00")
		self.assertEqual(result, expected_result)

	def test_3950(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x17\x04")
		self.assertEqual(result, expected_result)

	def test_3951(self):
		result = ConfigParserTestFunction("\x07\x00\x00\x00\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3952(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\x02\x03")
		self.assertEqual(result, expected_result)

	def test_3953(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\x01\x04\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3954(self):
		result = ConfigParserTestFunction("\x07\x01\x00\x00\x00\x00\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_3955(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0D\x07\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3956(self):
		result = ConfigParserTestFunction("\x01\x01\x00\x01\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3957(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x0E\x00")
		self.assertEqual(result, expected_result)

	def test_3958(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\n\n\n\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3959(self):
		result = ConfigParserTestFunction("\n\n\x00\x03\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3960(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0D\n\n\n\n")
		self.assertEqual(result, expected_result)

	def test_3961(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\n\n\n\n\x01")
		self.assertEqual(result, expected_result)

	def test_3962(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\n\n\n\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3963(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x07\x06\x01")
		self.assertEqual(result, expected_result)

	def test_3964(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x04\x04")
		self.assertEqual(result, expected_result)

	def test_3965(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\n\n\n\n\x00\n")
		self.assertEqual(result, expected_result)

	def test_3966(self):
		result = ConfigParserTestFunction("\n\n\n\x0C\x01\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3967(self):
		result = ConfigParserTestFunction("\n\x0E\x01\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_3968(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x0B\x01\x00")
		self.assertEqual(result, expected_result)

	def test_3969(self):
		result = ConfigParserTestFunction("\n\n\n\x0D\x02\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3970(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0D\x04")
		self.assertEqual(result, expected_result)

	def test_3971(self):
		result = ConfigParserTestFunction("\x01\x00\x00\x01\x00\x00\x00\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_3972(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x02\x01\x03\x00")
		self.assertEqual(result, expected_result)

	def test_3973(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x16\x02\x00")
		self.assertEqual(result, expected_result)

	def test_3974(self):
		result = ConfigParserTestFunction("\n\x08\x01\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3975(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\n\x03\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3976(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0B\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3977(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x16\x12\x00")
		self.assertEqual(result, expected_result)

	def test_3978(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x04\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_3979(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x14\x00")
		self.assertEqual(result, expected_result)

	def test_3980(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\x04\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3981(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n0")
		self.assertEqual(result, expected_result)

	def test_3982(self):
		result = ConfigParserTestFunction("\n\n\x08\x01\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_3983(self):
		result = ConfigParserTestFunction("\x08\x00\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3984(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0D\n\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3985(self):
		result = ConfigParserTestFunction("\n\x0B\x01\x02\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3986(self):
		result = ConfigParserTestFunction("\n\n\x0C\x02\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_3987(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\x01\x06")
		self.assertEqual(result, expected_result)

	def test_3988(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\n\n\x03\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3989(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\x00\x01\x00\x01")
		self.assertEqual(result, expected_result)

	def test_3990(self):
		result = ConfigParserTestFunction("\x0D\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3991(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x00\x00\x01\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_3992(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0B\n\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_3993(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x1E\x01\x00")
		self.assertEqual(result, expected_result)

	def test_3994(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\n\n\n\n\x01\x00")
		self.assertEqual(result, expected_result)

	def test_3995(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0F\x01\x01\x01\n")
		self.assertEqual(result, expected_result)

	def test_3996(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\x01\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_3997(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x06\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_3998(self):
		result = ConfigParserTestFunction("\x0D\x00\x00\x00\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_3999(self):
		result = ConfigParserTestFunction("\n\n\x0C\x01\x01\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_4000(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x00\x03\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4001(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x04\x14")
		self.assertEqual(result, expected_result)

	def test_4002(self):
		result = ConfigParserTestFunction("\x00\x02\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_4003(self):
		result = ConfigParserTestFunction("\n\n\x01\x00\x00\x00\x00\x05\n\x00")
		self.assertEqual(result, expected_result)

	def test_4004(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\x00\x01\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_4005(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x03\x01\x04\n")
		self.assertEqual(result, expected_result)

	def test_4006(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\n\n\n\n\n\x00")
		self.assertEqual(result, expected_result)

	def test_4007(self):
		result = ConfigParserTestFunction("\n\n\n\x0C\x04\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_4008(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nt")
		self.assertEqual(result, expected_result)

	def test_4009(self):
		result = ConfigParserTestFunction("\x0F\x00\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4010(self):
		result = ConfigParserTestFunction("\n\n\n\x08\x00\x01\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4011(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0B\n\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4012(self):
		result = ConfigParserTestFunction("\n\n\n\n\x06\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4013(self):
		result = ConfigParserTestFunction("\x0C\x02\x00\x00\x01\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_4014(self):
		result = ConfigParserTestFunction("\n\n\n\x0F\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_4015(self):
		result = ConfigParserTestFunction("\n\n\n\x0C\x07\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4016(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\n\n\n\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_4017(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\x01\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_4018(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x05\x05\x00")
		self.assertEqual(result, expected_result)

	def test_4019(self):
		result = ConfigParserTestFunction("\n\n\t\x00\x01\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_4020(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\n\n\n\n\n\n")
		self.assertEqual(result, expected_result)

	def test_4021(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x0D\n\x02")
		self.assertEqual(result, expected_result)

	def test_4022(self):
		result = ConfigParserTestFunction("\n\n\n\n\t\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4023(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0B\n\n\x00\n")
		self.assertEqual(result, expected_result)

	def test_4024(self):
		result = ConfigParserTestFunction("\x07\x02\x00\x00\x00\x00\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4025(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\n\n\n\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_4026(self):
		result = ConfigParserTestFunction("\n\n\x08\x01\x00\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_4027(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0D\n\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_4028(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0C\x08\x00")
		self.assertEqual(result, expected_result)

	def test_4029(self):
		result = ConfigParserTestFunction("\x0C\x00\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4030(self):
		result = ConfigParserTestFunction("\n\x0E\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4031(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x00\x01\x01\x03")
		self.assertEqual(result, expected_result)

	def test_4032(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\t\x00")
		self.assertEqual(result, expected_result)

	def test_4033(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0F\x06\x00")
		self.assertEqual(result, expected_result)

	def test_4034(self):
		result = ConfigParserTestFunction("\x04\x03\x00\x00\x00\x00\x00\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_4035(self):
		result = ConfigParserTestFunction("\x0B\x00\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4036(self):
		result = ConfigParserTestFunction("\x0C\x08\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_4037(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x02\x01\x02\n\x00")
		self.assertEqual(result, expected_result)

	def test_4038(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0B\n\n\n\x00")
		self.assertEqual(result, expected_result)

	def test_4039(self):
		result = ConfigParserTestFunction("\n\x04\x00\x00\x00\x00\x00\x00\x03\n")
		self.assertEqual(result, expected_result)

	def test_4040(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x0C\x03\x00")
		self.assertEqual(result, expected_result)

	def test_4041(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0B\n\n\n\n")
		self.assertEqual(result, expected_result)

	def test_4042(self):
		result = ConfigParserTestFunction("\n\n\x00\x03\x00\x00\x01\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_4043(self):
		result = ConfigParserTestFunction("\n\n\n\x07\x01\x00\x00\x00\x01\x01")
		self.assertEqual(result, expected_result)

	def test_4044(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x03\x00\x00\x03\n")
		self.assertEqual(result, expected_result)

	def test_4045(self):
		result = ConfigParserTestFunction("\n\x00\x03\x00\x01\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_4046(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\n\x02\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4047(self):
		result = ConfigParserTestFunction("\n\n\n\x0D\x00\x00\x00\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_4048(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0B\n\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_4049(self):
		result = ConfigParserTestFunction("\n\n\n\x0C\x06\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4050(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\n\n\x02\x00")
		self.assertEqual(result, expected_result)

	def test_4051(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\t\x0E\x00")
		self.assertEqual(result, expected_result)

	def test_4052(self):
		result = ConfigParserTestFunction("\n\n\x0C\x02\x01\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_4053(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x0F\x00\x02")
		self.assertEqual(result, expected_result)

	def test_4054(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x07\x01\x04")
		self.assertEqual(result, expected_result)

	def test_4055(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x00\x00\x00\x00\x04\n")
		self.assertEqual(result, expected_result)

	def test_4056(self):
		result = ConfigParserTestFunction("\n\n\n\x01\x02\x00\x01\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_4057(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0E\x02\x01\n")
		self.assertEqual(result, expected_result)

	def test_4058(self):
		result = ConfigParserTestFunction("\n\n\t\x03\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_4059(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\n\n\n\n\x02")
		self.assertEqual(result, expected_result)

	def test_4060(self):
		result = ConfigParserTestFunction("\n\n\x0D\x03\x00\x00\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_4061(self):
		result = ConfigParserTestFunction("\n\n\t\x02\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_4062(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x00\x00\x00\x07\n\x00")
		self.assertEqual(result, expected_result)

	def test_4063(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xD9")
		self.assertEqual(result, expected_result)

	def test_4064(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x12\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4065(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x0E\x03")
		self.assertEqual(result, expected_result)

	def test_4066(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x0D\x05")
		self.assertEqual(result, expected_result)

	def test_4067(self):
		result = ConfigParserTestFunction("\x01\x00\x00\x00\x00\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_4068(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x12\\\x00")
		self.assertEqual(result, expected_result)

	def test_4069(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\x02\x06")
		self.assertEqual(result, expected_result)

	def test_4070(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\n\t")
		self.assertEqual(result, expected_result)

	def test_4071(self):
		result = ConfigParserTestFunction("\n\x00\x05\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4072(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\n\n\n\x01\x00")
		self.assertEqual(result, expected_result)

	def test_4073(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x08\x03\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4074(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x04\x05\x00")
		self.assertEqual(result, expected_result)

	def test_4075(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x1B\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4076(self):
		result = ConfigParserTestFunction("\n\n\n\x05\x01\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4077(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0D\x00\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_4078(self):
		result = ConfigParserTestFunction("\n\n\n\n\x04\x00\x01\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_4079(self):
		result = ConfigParserTestFunction("\n\n\n\n\x03\x00\x00\x01\x01\x00")
		self.assertEqual(result, expected_result)

	def test_4080(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x01\x00\n")
		self.assertEqual(result, expected_result)

	def test_4081(self):
		result = ConfigParserTestFunction("\n\x0E\x03\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_4082(self):
		result = ConfigParserTestFunction("\n\n\n\x0B\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4083(self):
		result = ConfigParserTestFunction("\x0C\n\n\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_4084(self):
		result = ConfigParserTestFunction("\n\n\n\x0E\x02\x00\x00\x01\x00\x01")
		self.assertEqual(result, expected_result)

	def test_4085(self):
		result = ConfigParserTestFunction("\x01\x01\x01\x00\x00\x00\x01\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_4086(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\x07\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4087(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0D\n\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_4088(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x00\x00\x00\x00\x04")
		self.assertEqual(result, expected_result)

	def test_4089(self):
		result = ConfigParserTestFunction("\n\n\n\x0C\x03\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4090(self):
		result = ConfigParserTestFunction("\x00\x01\x00\x00\x00\x01\x00\x00\x00\x07")
		self.assertEqual(result, expected_result)

	def test_4091(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\x05\x00")
		self.assertEqual(result, expected_result)

	def test_4092(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x04\x02\x02")
		self.assertEqual(result, expected_result)

	def test_4093(self):
		result = ConfigParserTestFunction("\n\x05\x00\x00\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_4094(self):
		result = ConfigParserTestFunction("\n\n\x06\x01\x00\x01\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_4095(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x17\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4096(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\n\n\n\x00\x02\x00")
		self.assertEqual(result, expected_result)

	def test_4097(self):
		result = ConfigParserTestFunction("\n\n\n\x0D\x02\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4098(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x17\x05")
		self.assertEqual(result, expected_result)

	def test_4099(self):
		result = ConfigParserTestFunction("\n\n\x06\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4100(self):
		result = ConfigParserTestFunction("\n\n\n\n\x08\x01\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_4101(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0B\x00\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_4102(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n-")
		self.assertEqual(result, expected_result)

	def test_4103(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0E\x02\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_4104(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x03\x02\x01")
		self.assertEqual(result, expected_result)

	def test_4105(self):
		result = ConfigParserTestFunction("\n\n\n\x06\x00\x04\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4106(self):
		result = ConfigParserTestFunction("\x0C\n\x01\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_4107(self):
		result = ConfigParserTestFunction("\n\n\n\x07\x00\x00\x00\x01\x00\x01")
		self.assertEqual(result, expected_result)

	def test_4108(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0B\x0E\x00")
		self.assertEqual(result, expected_result)

	def test_4109(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0D\n\n\n\x01")
		self.assertEqual(result, expected_result)

	def test_4110(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x0D\x01")
		self.assertEqual(result, expected_result)

	def test_4111(self):
		result = ConfigParserTestFunction("\n\x00\x02\x01\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4112(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x02\x00\x00\x07\n")
		self.assertEqual(result, expected_result)

	def test_4113(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x0B\x02\x00")
		self.assertEqual(result, expected_result)

	def test_4114(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x00\x00\x00\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_4115(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\n\n\n\x01\x00\n")
		self.assertEqual(result, expected_result)

	def test_4116(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x02\x00\x01\x05")
		self.assertEqual(result, expected_result)

	def test_4117(self):
		result = ConfigParserTestFunction("\x03\x01\x01\x00\x01\x00\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_4118(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\x01\x05\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4119(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\n\n\n\n\n\x01")
		self.assertEqual(result, expected_result)

	def test_4120(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0D\n\x02\x00")
		self.assertEqual(result, expected_result)

	def test_4121(self):
		result = ConfigParserTestFunction("\x03\x06\x00\x01\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4122(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x01\x00\x00\x04\n")
		self.assertEqual(result, expected_result)

	def test_4123(self):
		result = ConfigParserTestFunction("\n\n\x0B\x06\x00\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_4124(self):
		result = ConfigParserTestFunction("\x0C\x0E\x02\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_4125(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\x03\x00\n")
		self.assertEqual(result, expected_result)

	def test_4126(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x07\x91\x00")
		self.assertEqual(result, expected_result)

	def test_4127(self):
		result = ConfigParserTestFunction("\x01\x00\x00\x05\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4128(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x03\x00\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_4129(self):
		result = ConfigParserTestFunction("\x01\x03\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4130(self):
		result = ConfigParserTestFunction("\x07\x00\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4131(self):
		result = ConfigParserTestFunction("\n\x02\x00\x00\x00\x00\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4132(self):
		result = ConfigParserTestFunction("\n\n\x06\x00\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4133(self):
		result = ConfigParserTestFunction("\n\x0C\x02\x02\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4134(self):
		result = ConfigParserTestFunction("\n\n\n\n\x08\x00\x00\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_4135(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x07\x05")
		self.assertEqual(result, expected_result)

	def test_4136(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x17\x0D\x00")
		self.assertEqual(result, expected_result)

	def test_4137(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x00\x04\x02")
		self.assertEqual(result, expected_result)

	def test_4138(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4139(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x06\x05\x01")
		self.assertEqual(result, expected_result)

	def test_4140(self):
		result = ConfigParserTestFunction("\t\x01\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_4141(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\x01\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4142(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x0C\x04\x00")
		self.assertEqual(result, expected_result)

	def test_4143(self):
		result = ConfigParserTestFunction("\n\n\n\x0E\x02\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4144(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\n\x04\x00")
		self.assertEqual(result, expected_result)

	def test_4145(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x02\x01\x04\n\x00")
		self.assertEqual(result, expected_result)

	def test_4146(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x01\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_4147(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\x8F")
		self.assertEqual(result, expected_result)

	def test_4148(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0E\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_4149(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_4150(self):
		result = ConfigParserTestFunction("\n\n\n\x0B\x03\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4151(self):
		result = ConfigParserTestFunction("\n\n\x00\x01\x00\x00\x00\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_4152(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x03\n\x00")
		self.assertEqual(result, expected_result)

	def test_4153(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x05\x0D\x00")
		self.assertEqual(result, expected_result)

	def test_4154(self):
		result = ConfigParserTestFunction("\x00\x01\x00\x00\x00\x00\x00\x02\n\x00")
		self.assertEqual(result, expected_result)

	def test_4155(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x15\x05")
		self.assertEqual(result, expected_result)

	def test_4156(self):
		result = ConfigParserTestFunction("\n\n\t\x02\x00\x00\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_4157(self):
		result = ConfigParserTestFunction("\n\x03\x00\x00\x00\x00\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4158(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x01\x04")
		self.assertEqual(result, expected_result)

	def test_4159(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x1B\t\x00")
		self.assertEqual(result, expected_result)

	def test_4160(self):
		result = ConfigParserTestFunction("\n\n\x00\x02\x00\x01\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4161(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\t\n\x01")
		self.assertEqual(result, expected_result)

	def test_4162(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x1B'\x00")
		self.assertEqual(result, expected_result)

	def test_4163(self):
		result = ConfigParserTestFunction("\n\n\x0D\x03\x01\x00\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_4164(self):
		result = ConfigParserTestFunction("\n\n\t\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_4165(self):
		result = ConfigParserTestFunction("\x01\x02\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4166(self):
		result = ConfigParserTestFunction("\x02\x00\x00\x00\x00\x00\x00\x03\n\x00")
		self.assertEqual(result, expected_result)

	def test_4167(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\n\x01\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_4168(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x05\x05")
		self.assertEqual(result, expected_result)

	def test_4169(self):
		result = ConfigParserTestFunction("\n\x05\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4170(self):
		result = ConfigParserTestFunction("\n\n\n\x07\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_4171(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\t\x00\x01\x00\x01")
		self.assertEqual(result, expected_result)

	def test_4172(self):
		result = ConfigParserTestFunction("\n\n\x0B\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4173(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x17'\x00")
		self.assertEqual(result, expected_result)

	def test_4174(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0E\x00\x00\x00\x02\x01")
		self.assertEqual(result, expected_result)

	def test_4175(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\ne")
		self.assertEqual(result, expected_result)

	def test_4176(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\x02\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_4177(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x0D\x03\x00")
		self.assertEqual(result, expected_result)

	def test_4178(self):
		result = ConfigParserTestFunction("\n\n\n\x04\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4179(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\x0F\x02\x00")
		self.assertEqual(result, expected_result)

	def test_4180(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x00\x01\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4181(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x01\x01\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_4182(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\n\x02\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4183(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x1D\n")
		self.assertEqual(result, expected_result)

	def test_4184(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\x05\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4185(self):
		result = ConfigParserTestFunction("\n\x05\x00\x01\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_4186(self):
		result = ConfigParserTestFunction("\n\n\n\x07\x02\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4187(self):
		result = ConfigParserTestFunction("\n\x00\x01\x00\x00\x01\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_4188(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x07\x06\x00")
		self.assertEqual(result, expected_result)

	def test_4189(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\n\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_4190(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x02\x00\x01\x03")
		self.assertEqual(result, expected_result)

	def test_4191(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x03\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_4192(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\n\x01\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_4193(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xFD")
		self.assertEqual(result, expected_result)

	def test_4194(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x01\x00\x00\x00\x00\x04")
		self.assertEqual(result, expected_result)

	def test_4195(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0E\x00\x03\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4196(self):
		result = ConfigParserTestFunction("\n\n\x04\x00\x00\x00\x00\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_4197(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0C\x0F\x00")
		self.assertEqual(result, expected_result)

	def test_4198(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\n\n\n\x01\x00")
		self.assertEqual(result, expected_result)

	def test_4199(self):
		result = ConfigParserTestFunction("\x0C\x02\x00\x00\x00\x00\x00\x00\x05\n")
		self.assertEqual(result, expected_result)

	def test_4200(self):
		result = ConfigParserTestFunction("\n\n\t\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_4201(self):
		result = ConfigParserTestFunction("\n\x03\x01\x00\x00\x00\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4202(self):
		result = ConfigParserTestFunction("\n\x04\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4203(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\n\x0D")
		self.assertEqual(result, expected_result)

	def test_4204(self):
		result = ConfigParserTestFunction("\n\n\n\x02\x00\x00\x00\x00\x01\x01")
		self.assertEqual(result, expected_result)

	def test_4205(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\n\n\x01\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_4206(self):
		result = ConfigParserTestFunction("\n\n\x0D\x03\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_4207(self):
		result = ConfigParserTestFunction("\n\n\n\x04\x01\x00\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4208(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x04\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_4209(self):
		result = ConfigParserTestFunction("\n\n\n\n\x08\x00\x04\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4210(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x08\x01\x01")
		self.assertEqual(result, expected_result)

	def test_4211(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x05\x00\x00\x01\x02")
		self.assertEqual(result, expected_result)

	def test_4212(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\x01\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_4213(self):
		result = ConfigParserTestFunction("\n\x03\x00\x01\x00\x00\x00\x00\x03\n")
		self.assertEqual(result, expected_result)

	def test_4214(self):
		result = ConfigParserTestFunction("\n\x04\x00\x00\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4215(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x01\x03\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4216(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\x06\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4217(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x04\x07")
		self.assertEqual(result, expected_result)

	def test_4218(self):
		result = ConfigParserTestFunction("\n\n\n\x0E\x01\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4219(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x17 \x00")
		self.assertEqual(result, expected_result)

	def test_4220(self):
		result = ConfigParserTestFunction("\x0F\x01\x00\x00\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4221(self):
		result = ConfigParserTestFunction("\n\n\n\n\x08\x03\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_4222(self):
		result = ConfigParserTestFunction("\n\x07\x01\x00\x00\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4223(self):
		result = ConfigParserTestFunction("\n\n\x03\x00\x00\x05\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4224(self):
		result = ConfigParserTestFunction("\n\n\t\x00\x01\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_4225(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x0C\x04\x01")
		self.assertEqual(result, expected_result)

	def test_4226(self):
		result = ConfigParserTestFunction("\n\n\n\n\x07\x00\x00\x00\x01\x04")
		self.assertEqual(result, expected_result)

	def test_4227(self):
		result = ConfigParserTestFunction("\n\n\n\x05\x00\x00\x05\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4228(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0E\x03\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_4229(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_4230(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nD")
		self.assertEqual(result, expected_result)

	def test_4231(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x12 \x00")
		self.assertEqual(result, expected_result)

	def test_4232(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x03\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4233(self):
		result = ConfigParserTestFunction("\x08\x00\x00\x00\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4234(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0F\x02\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4235(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\n\x01\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_4236(self):
		result = ConfigParserTestFunction("\x07\x01\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4237(self):
		result = ConfigParserTestFunction("\n\n\x15\x01\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_4238(self):
		result = ConfigParserTestFunction("\x07\x01\x00\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_4239(self):
		result = ConfigParserTestFunction("\x0C\n\x01\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4240(self):
		result = ConfigParserTestFunction("\x08\x00\x00\x05\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4241(self):
		result = ConfigParserTestFunction("\x07\x01\x00\x01\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4242(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x1E\x11\x00")
		self.assertEqual(result, expected_result)

	def test_4243(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nq")
		self.assertEqual(result, expected_result)

	def test_4244(self):
		result = ConfigParserTestFunction("\n\n\n\x05\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_4245(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4246(self):
		result = ConfigParserTestFunction("\n\n\n\x07\x00\x01\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_4247(self):
		result = ConfigParserTestFunction("\n\x00\x04\x00\x00\x00\x01\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_4248(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\x03\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4249(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x05\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4250(self):
		result = ConfigParserTestFunction("\x08\x00\x02\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4251(self):
		result = ConfigParserTestFunction("\x0F\x00\x00\x00\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_4252(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x02\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_4253(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x05\x00")
		self.assertEqual(result, expected_result)

	def test_4254(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x1B\x0D\x00")
		self.assertEqual(result, expected_result)

	def test_4255(self):
		result = ConfigParserTestFunction("\n\n\n\x0D\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_4256(self):
		result = ConfigParserTestFunction("\n\n\x00\x04\x00\x00\x00\x00\x00\x06")
		self.assertEqual(result, expected_result)

	def test_4257(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\x02\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_4258(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_4259(self):
		result = ConfigParserTestFunction("\n\n\x01\x00\x00\x00\x00\x03\n\x00")
		self.assertEqual(result, expected_result)

	def test_4260(self):
		result = ConfigParserTestFunction("\n\x0B\x03\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_4261(self):
		result = ConfigParserTestFunction("\n\n\x05\x02\x00\x00\x00\x00\x03\n")
		self.assertEqual(result, expected_result)

	def test_4262(self):
		result = ConfigParserTestFunction("\n\n\n\x0B\x04\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4263(self):
		result = ConfigParserTestFunction("\n\n\x0C\x00\x00\x00\x00\x02\n\x00")
		self.assertEqual(result, expected_result)

	def test_4264(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\x03\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4265(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\n\n\x00\x04\n")
		self.assertEqual(result, expected_result)

	def test_4266(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0D\n\x02\n\x00")
		self.assertEqual(result, expected_result)

	def test_4267(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x17\t\x00")
		self.assertEqual(result, expected_result)

	def test_4268(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0D\n\n\x05")
		self.assertEqual(result, expected_result)

	def test_4269(self):
		result = ConfigParserTestFunction("\x08\x00\x00\x00\x00\x01\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4270(self):
		result = ConfigParserTestFunction("\n\x07\x00\x00\x00\x04\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4271(self):
		result = ConfigParserTestFunction("\x0C\n\x02\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4272(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x02\x02\x01\x00")
		self.assertEqual(result, expected_result)

	def test_4273(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xE1")
		self.assertEqual(result, expected_result)

	def test_4274(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\n\x04\x05")
		self.assertEqual(result, expected_result)

	def test_4275(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x04\x03\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4276(self):
		result = ConfigParserTestFunction("\n\n\n\x04\x00\x00\x00\x00\x04\n")
		self.assertEqual(result, expected_result)

	def test_4277(self):
		result = ConfigParserTestFunction("\n\x03\x00\x00\x00\x00\x00\x00\x00\x04")
		self.assertEqual(result, expected_result)

	def test_4278(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x07\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4279(self):
		result = ConfigParserTestFunction("\n\n\x05\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_4280(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\n\n\n\n\n\x02")
		self.assertEqual(result, expected_result)

	def test_4281(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\t\x00\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_4282(self):
		result = ConfigParserTestFunction("\n\n\n\n\t\x02\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4283(self):
		result = ConfigParserTestFunction("\n\n\n\x05\x00\x00\x00\x00\x04\n")
		self.assertEqual(result, expected_result)

	def test_4284(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x03\x03")
		self.assertEqual(result, expected_result)

	def test_4285(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\n\n\x02\n\x00")
		self.assertEqual(result, expected_result)

	def test_4286(self):
		result = ConfigParserTestFunction("\n\n\x0D\x00\x00\x00\x00\x02\n\x00")
		self.assertEqual(result, expected_result)

	def test_4287(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\n\n\n\x02\x00\n")
		self.assertEqual(result, expected_result)

	def test_4288(self):
		result = ConfigParserTestFunction("\n\n\t\x00\x00\x00\x00\x02\n\x00")
		self.assertEqual(result, expected_result)

	def test_4289(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\x06\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_4290(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\x07\x01\x00")
		self.assertEqual(result, expected_result)

	def test_4291(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\t\x01")
		self.assertEqual(result, expected_result)

	def test_4292(self):
		result = ConfigParserTestFunction("\n\n\x00\x03\x00\x00\x00\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_4293(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0D\x04\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_4294(self):
		result = ConfigParserTestFunction("\n\n\n\x0F\x04\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4295(self):
		result = ConfigParserTestFunction("\n\n\x02\x00\x03\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4296(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x1B \x00")
		self.assertEqual(result, expected_result)

	def test_4297(self):
		result = ConfigParserTestFunction("\x02\x00\x02\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4298(self):
		result = ConfigParserTestFunction("\n\n\x01\x03\x00\x01\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4299(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x01\x03\n\x00")
		self.assertEqual(result, expected_result)

	def test_4300(self):
		result = ConfigParserTestFunction("\t\x02\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_4301(self):
		result = ConfigParserTestFunction("\n\n\n\x07\x01\x00\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_4302(self):
		result = ConfigParserTestFunction("\n\x07\x00\x00\x00\x06\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4303(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x07\x02\x04")
		self.assertEqual(result, expected_result)

	def test_4304(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x18\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4305(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0B\x01\x01\x01\n")
		self.assertEqual(result, expected_result)

	def test_4306(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\n\x01\x01\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_4307(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x05\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_4308(self):
		result = ConfigParserTestFunction("\n\x01\x00\x00\x00\x00\x00\x02\n\x00")
		self.assertEqual(result, expected_result)

	def test_4309(self):
		result = ConfigParserTestFunction("\n\n\x03\x02\x03\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_4310(self):
		result = ConfigParserTestFunction("\n\n\n\x06\x02\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4311(self):
		result = ConfigParserTestFunction("\n\n\x0F\x00\x00\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4312(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x00\x01\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_4313(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x01\x00\x00\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_4314(self):
		result = ConfigParserTestFunction("\x0F\x00\x00\x00\x00\x00\x00\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_4315(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x02\x02\x01\x01\x00")
		self.assertEqual(result, expected_result)

	def test_4316(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\n\x07\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4317(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n=")
		self.assertEqual(result, expected_result)

	def test_4318(self):
		result = ConfigParserTestFunction("\n\n\n\x0C\x06\x01\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4319(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x0B\x04\n")
		self.assertEqual(result, expected_result)

	def test_4320(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x14\x01")
		self.assertEqual(result, expected_result)

	def test_4321(self):
		result = ConfigParserTestFunction("\x0B\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4322(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x07\x02")
		self.assertEqual(result, expected_result)

	def test_4323(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x01\x03\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4324(self):
		result = ConfigParserTestFunction("\n\n\x0B\x03\x01\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4325(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\n\x01\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_4326(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x03\x00\x06")
		self.assertEqual(result, expected_result)

	def test_4327(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x18\\\x00")
		self.assertEqual(result, expected_result)

	def test_4328(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\n\x01\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_4329(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x01\x01\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_4330(self):
		result = ConfigParserTestFunction("\n\x0B\x07\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_4331(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x06\x00\x01\x00\x01")
		self.assertEqual(result, expected_result)

	def test_4332(self):
		result = ConfigParserTestFunction("\n\x02\x00\x00\x00\x00\x00\x04\n\x00")
		self.assertEqual(result, expected_result)

	def test_4333(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x02\x01\x03")
		self.assertEqual(result, expected_result)

	def test_4334(self):
		result = ConfigParserTestFunction("\n\n\x0B\x00\x00\x00\x01\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_4335(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x0F\x01")
		self.assertEqual(result, expected_result)

	def test_4336(self):
		result = ConfigParserTestFunction("\n\x03\x01\x00\x00\x00\x00\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_4337(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x0C\x02\x01")
		self.assertEqual(result, expected_result)

	def test_4338(self):
		result = ConfigParserTestFunction("\x0C\x0C\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_4339(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0D\x01\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_4340(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nm")
		self.assertEqual(result, expected_result)

	def test_4341(self):
		result = ConfigParserTestFunction("\n\n\x0C\x00\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4342(self):
		result = ConfigParserTestFunction("\x0C\n\x02\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4343(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x00\x01\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_4344(self):
		result = ConfigParserTestFunction("\n\x05\x00\x00\x00\x00\x00\x00\x03\n")
		self.assertEqual(result, expected_result)

	def test_4345(self):
		result = ConfigParserTestFunction("\n\n\n\n\x07\x01\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4346(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\x01\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4347(self):
		result = ConfigParserTestFunction("\n\x0E\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4348(self):
		result = ConfigParserTestFunction("\n\n\x03\x00\x00\x00\x00\x00\x03\n")
		self.assertEqual(result, expected_result)

	def test_4349(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\n\n\n\x02")
		self.assertEqual(result, expected_result)

	def test_4350(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\n\x01\x01\x00")
		self.assertEqual(result, expected_result)

	def test_4351(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\x07\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_4352(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\t\n\x07\x01")
		self.assertEqual(result, expected_result)

	def test_4353(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x17\x10\x00")
		self.assertEqual(result, expected_result)

	def test_4354(self):
		result = ConfigParserTestFunction("\n\x00\x01\x02\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_4355(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x02\x00\x01\x01\x00")
		self.assertEqual(result, expected_result)

	def test_4356(self):
		result = ConfigParserTestFunction("\n\n\n\x07\x00\x00\x00\x00\x01\x02")
		self.assertEqual(result, expected_result)

	def test_4357(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x00\x01\x02")
		self.assertEqual(result, expected_result)

	def test_4358(self):
		result = ConfigParserTestFunction("\n\x0E\x02\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4359(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\x00\x02\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4360(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x18\t\x00")
		self.assertEqual(result, expected_result)

	def test_4361(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x00\x03\n\x00")
		self.assertEqual(result, expected_result)

	def test_4362(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\t\x0F\x00")
		self.assertEqual(result, expected_result)

	def test_4363(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0E\x00\x01\x01\n")
		self.assertEqual(result, expected_result)

	def test_4364(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\n\x02\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_4365(self):
		result = ConfigParserTestFunction("\x06\x01\x00\x01\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4366(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0D\x01\x00\x02\x00")
		self.assertEqual(result, expected_result)

	def test_4367(self):
		result = ConfigParserTestFunction("\n\x01\x01\x00\x01\x00\x04\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4368(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x08\x95\x00")
		self.assertEqual(result, expected_result)

	def test_4369(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0D\x00\x01\x00\x01")
		self.assertEqual(result, expected_result)

	def test_4370(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\n\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4371(self):
		result = ConfigParserTestFunction("\n\n\n\n\x04\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_4372(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\n\x03\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_4373(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0B\n\n\x01\n")
		self.assertEqual(result, expected_result)

	def test_4374(self):
		result = ConfigParserTestFunction("\x0C\n\x00\x01\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4375(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x03\x00\x00\x06")
		self.assertEqual(result, expected_result)

	def test_4376(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x00\x00\x00\x07\n")
		self.assertEqual(result, expected_result)

	def test_4377(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x08F")
		self.assertEqual(result, expected_result)

	def test_4378(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x00\x00\x02\x01\x00")
		self.assertEqual(result, expected_result)

	def test_4379(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x00\x01\x03\n\x00")
		self.assertEqual(result, expected_result)

	def test_4380(self):
		result = ConfigParserTestFunction("\n\n\n\n\x06\x01\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_4381(self):
		result = ConfigParserTestFunction("\n\n\x0C\x02\x00\x01\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_4382(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xF4")
		self.assertEqual(result, expected_result)

	def test_4383(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\x07\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_4384(self):
		result = ConfigParserTestFunction("\n\n\n\n\x07\x00\x01\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_4385(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0D\n\n\x0C")
		self.assertEqual(result, expected_result)

	def test_4386(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0C\x0C\x00")
		self.assertEqual(result, expected_result)

	def test_4387(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nn")
		self.assertEqual(result, expected_result)

	def test_4388(self):
		result = ConfigParserTestFunction("\n\x00\x01\x00\x01\x00\x00\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_4389(self):
		result = ConfigParserTestFunction("\n\n\n\n\x01\x02\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4390(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x06\x03\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4391(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\n\x01\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_4392(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x17\\\x00")
		self.assertEqual(result, expected_result)

	def test_4393(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x0E\x00\n")
		self.assertEqual(result, expected_result)

	def test_4394(self):
		result = ConfigParserTestFunction("\x0C\n\x01\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4395(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\x0B\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4396(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n~")
		self.assertEqual(result, expected_result)

	def test_4397(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n)")
		self.assertEqual(result, expected_result)

	def test_4398(self):
		result = ConfigParserTestFunction("\n\n\n\x0D\x04\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4399(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0F\x03\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4400(self):
		result = ConfigParserTestFunction("\n\n\x00\x01\x02\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4401(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x04\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4402(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xE3")
		self.assertEqual(result, expected_result)

	def test_4403(self):
		result = ConfigParserTestFunction("\n\n\n\x0D\x03\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4404(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x02\x02\x00\x05\n")
		self.assertEqual(result, expected_result)

	def test_4405(self):
		result = ConfigParserTestFunction("\n\x00\x00\x00\x00\x01\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_4406(self):
		result = ConfigParserTestFunction("\x0C\n\n\x00\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_4407(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x1B\\\x00")
		self.assertEqual(result, expected_result)

	def test_4408(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x07\x00\x06\x03")
		self.assertEqual(result, expected_result)

	def test_4409(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\n\n\x00\x02\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4410(self):
		result = ConfigParserTestFunction("\x0C\n\x02\x01\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4411(self):
		result = ConfigParserTestFunction("\n\n\n\n\x06\x00\x00\x00\x00\x02")
		self.assertEqual(result, expected_result)

	def test_4412(self):
		result = ConfigParserTestFunction("\n\n\x00\x00\x00\x00\x00\x00\x01\x05")
		self.assertEqual(result, expected_result)

	def test_4413(self):
		result = ConfigParserTestFunction("\n\x05\x00\x00\x00\x00\x00\x00\x07\n")
		self.assertEqual(result, expected_result)

	def test_4414(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x05\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4415(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x03\x01\x02")
		self.assertEqual(result, expected_result)

	def test_4416(self):
		result = ConfigParserTestFunction("\x00\x01\x00\x00\x00\x00\x00\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_4417(self):
		result = ConfigParserTestFunction("\n\x03\x02\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4418(self):
		result = ConfigParserTestFunction("\x0C\n\x02\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4419(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0D\n\n\n\x02")
		self.assertEqual(result, expected_result)

	def test_4420(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x0F\x00")
		self.assertEqual(result, expected_result)

	def test_4421(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x02w")
		self.assertEqual(result, expected_result)

	def test_4422(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\n\n\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_4423(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x01\x07\x02")
		self.assertEqual(result, expected_result)

	def test_4424(self):
		result = ConfigParserTestFunction("\n\n\n\x00\x07\x01\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4425(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\x03\x06")
		self.assertEqual(result, expected_result)

	def test_4426(self):
		result = ConfigParserTestFunction("\n\n\t\x01\x01\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_4427(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x00\x02\x06")
		self.assertEqual(result, expected_result)

	def test_4428(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\x01\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4429(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\n\x0F\x00\x02")
		self.assertEqual(result, expected_result)

	def test_4430(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\n\xD0")
		self.assertEqual(result, expected_result)

	def test_4431(self):
		result = ConfigParserTestFunction("\n\n\x0D\x01\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_4432(self):
		result = ConfigParserTestFunction("\n\n\n\x0D\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4433(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\x03\x00\x02")
		self.assertEqual(result, expected_result)

	def test_4434(self):
		result = ConfigParserTestFunction("\n\x08\x00\x00\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4435(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\n\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4436(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x18 \x00")
		self.assertEqual(result, expected_result)

	def test_4437(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\n\n\x02\n")
		self.assertEqual(result, expected_result)

	def test_4438(self):
		result = ConfigParserTestFunction("\n\n\x0D\x07\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_4439(self):
		result = ConfigParserTestFunction("\n\n\n\n\x06\x00\x01\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_4440(self):
		result = ConfigParserTestFunction("\n\x06\x00\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_4441(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x12\t\x00")
		self.assertEqual(result, expected_result)

	def test_4442(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x07\x04\x00")
		self.assertEqual(result, expected_result)

	def test_4443(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x18\x0D\x00")
		self.assertEqual(result, expected_result)

	def test_4444(self):
		result = ConfigParserTestFunction("\n\n\n\x0C\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4445(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x18'\x00")
		self.assertEqual(result, expected_result)

	def test_4446(self):
		result = ConfigParserTestFunction("\x08\x01\x00\x05\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4447(self):
		result = ConfigParserTestFunction("\n\x08\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4448(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\t\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4449(self):
		result = ConfigParserTestFunction("\x03\x00\x00\x00\x00\x02\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4450(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0C\x0F\x03\x00")
		self.assertEqual(result, expected_result)

	def test_4451(self):
		result = ConfigParserTestFunction("\n\n\n\x06\x00\x07\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4452(self):
		result = ConfigParserTestFunction("\t\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4453(self):
		result = ConfigParserTestFunction("\n\n\n\x03\x01\x01\x00\x00\x01\x02")
		self.assertEqual(result, expected_result)

	def test_4454(self):
		result = ConfigParserTestFunction("\n\n\x0B\x07\x00\x00\x01\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_4455(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0B\x01\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_4456(self):
		result = ConfigParserTestFunction("\n\x00\x01\x01\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_4457(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_4458(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0B\n\n\x00\x01")
		self.assertEqual(result, expected_result)

	def test_4459(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x08\x00\x01\x00\x02")
		self.assertEqual(result, expected_result)

	def test_4460(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0D\n\x03\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4461(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x12\x10\x00")
		self.assertEqual(result, expected_result)

	def test_4462(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\n\x03\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4463(self):
		result = ConfigParserTestFunction("\n\n\n\x01\x01\x00\x01\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_4464(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nY")
		self.assertEqual(result, expected_result)

	def test_4465(self):
		result = ConfigParserTestFunction("\n\x08\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_4466(self):
		result = ConfigParserTestFunction("\n\n\n\n\x1B\x01\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4467(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x01\x02'")
		self.assertEqual(result, expected_result)

	def test_4468(self):
		result = ConfigParserTestFunction("\n\x03\x05\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4469(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x02\x01\x05")
		self.assertEqual(result, expected_result)

	def test_4470(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x05\x02\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4471(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x0C\x06\x00")
		self.assertEqual(result, expected_result)

	def test_4472(self):
		result = ConfigParserTestFunction("\n\x0B\x0E\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4473(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\t\x1F\x00")
		self.assertEqual(result, expected_result)

	def test_4474(self):
		result = ConfigParserTestFunction("\n\n\n\x0C\x00\x00\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4475(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\x03\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4476(self):
		result = ConfigParserTestFunction("\n\x0C\x01\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4477(self):
		result = ConfigParserTestFunction("\x0E\x00\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_4478(self):
		result = ConfigParserTestFunction("\x08\x00\x00\x00\x00\x00\x00\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4479(self):
		result = ConfigParserTestFunction("\x0E\x00\x00\x00\x00\x00\x00\x00\x00\x05")
		self.assertEqual(result, expected_result)

	def test_4480(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0D\x01\x00\n")
		self.assertEqual(result, expected_result)

	def test_4481(self):
		result = ConfigParserTestFunction("\n\x08\x00\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_4482(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\n\x00\x00\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_4483(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x00\x02\x07\x01")
		self.assertEqual(result, expected_result)

	def test_4484(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\x06\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4485(self):
		result = ConfigParserTestFunction("\n\x05\x00\x01\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4486(self):
		result = ConfigParserTestFunction("\x0D\x00\x01\x00\x00\x00\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_4487(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x00\x02\x02")
		self.assertEqual(result, expected_result)

	def test_4488(self):
		result = ConfigParserTestFunction("\n\n\t\x07\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_4489(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0C\x02\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_4490(self):
		result = ConfigParserTestFunction("\x01\x01\x00\x00\x02\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4491(self):
		result = ConfigParserTestFunction("\n\n\x0D\x03\x00\x00\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_4492(self):
		result = ConfigParserTestFunction("\x0C\x00\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4493(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0F\x16\x00")
		self.assertEqual(result, expected_result)

	def test_4494(self):
		result = ConfigParserTestFunction("\n\n\x0C\x01\x00\x01\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_4495(self):
		result = ConfigParserTestFunction("\n\x08\x00\x00\x01\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_4496(self):
		result = ConfigParserTestFunction("\n\n\n\n\x00\x00\x02\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4497(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x06\x03\x01\x06")
		self.assertEqual(result, expected_result)

	def test_4498(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\x01\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4499(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0B\x06\x00\x01")
		self.assertEqual(result, expected_result)

	def test_4500(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x01\xA1\x00")
		self.assertEqual(result, expected_result)

	def test_4501(self):
		result = ConfigParserTestFunction("\n\n\n\x05\x00\x01\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_4502(self):
		result = ConfigParserTestFunction("\x0C\n\x01\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_4503(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\x0D\x03")
		self.assertEqual(result, expected_result)

	def test_4504(self):
		result = ConfigParserTestFunction("\x07\x01\x00\x00\x00\x00\x00\x00\x01\x01")
		self.assertEqual(result, expected_result)

	def test_4505(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x08\x00\n")
		self.assertEqual(result, expected_result)

	def test_4506(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x01\x07\n\x00")
		self.assertEqual(result, expected_result)

	def test_4507(self):
		result = ConfigParserTestFunction("\n\n\n\x0C\x01\x04\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4508(self):
		result = ConfigParserTestFunction("\n\n\x06\x00\x00\x00\x03\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_4509(self):
		result = ConfigParserTestFunction("\n\n\n\x0D\x02\x00\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4510(self):
		result = ConfigParserTestFunction("\n\n\n\n\x05\x01\x01\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_4511(self):
		result = ConfigParserTestFunction("\n\n\x0C\x01\x02\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_4512(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x0C\x02\x00\x02\n")
		self.assertEqual(result, expected_result)

	def test_4513(self):
		result = ConfigParserTestFunction("\x01\x06\x00\x00\x00\x00\x00\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_4514(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0D\n\n\t")
		self.assertEqual(result, expected_result)

	def test_4515(self):
		result = ConfigParserTestFunction("\n\n\n\n\x04\x01\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4516(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0B\n\n\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4517(self):
		result = ConfigParserTestFunction("\n\n\n\x0C\x03\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4518(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x01\x00\x00\x01\n")
		self.assertEqual(result, expected_result)

	def test_4519(self):
		result = ConfigParserTestFunction("\n\x0B\x06\x00\x00\x00\x00\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_4520(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\nQ")
		self.assertEqual(result, expected_result)

	def test_4521(self):
		result = ConfigParserTestFunction("\n\x01\x02\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_4522(self):
		result = ConfigParserTestFunction("\n\n\x08\x01\x00\x00\x00\x01\x01\n")
		self.assertEqual(result, expected_result)

	def test_4523(self):
		result = ConfigParserTestFunction("\n\n\n\n\x0D\n\n\x00\x03\x00")
		self.assertEqual(result, expected_result)

	def test_4524(self):
		result = ConfigParserTestFunction("\x0D\x01\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4525(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x12'\x00")
		self.assertEqual(result, expected_result)

	def test_4526(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x0D\x01\x01\n")
		self.assertEqual(result, expected_result)

	def test_4527(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\n\x03\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_4528(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x18\x10\x00")
		self.assertEqual(result, expected_result)

	def test_4529(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\x00\x00\x00\x03")
		self.assertEqual(result, expected_result)

	def test_4530(self):
		result = ConfigParserTestFunction("\x07\x00\x00\x01\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4531(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\x08\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4532(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x03\t\x03")
		self.assertEqual(result, expected_result)

	def test_4533(self):
		result = ConfigParserTestFunction("\x0F\x00\x00\x00\x00\x00\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4534(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x03\x00\x07\n\x00")
		self.assertEqual(result, expected_result)

	def test_4535(self):
		result = ConfigParserTestFunction("\x0C\n\n\n\x01\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4536(self):
		result = ConfigParserTestFunction("\n\n\n\x0C\x01\x01\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_4537(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x0D\x08\x00")
		self.assertEqual(result, expected_result)

	def test_4538(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\n\x00D")
		self.assertEqual(result, expected_result)

	def test_4539(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\n\n\x04\x0D\x00")
		self.assertEqual(result, expected_result)

	def test_4540(self):
		result = ConfigParserTestFunction("\n\n\n\n\x02\x02B\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4541(self):
		result = ConfigParserTestFunction("\n\x00\x03\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4542(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x00\x14\x00")
		self.assertEqual(result, expected_result)

	def test_4543(self):
		result = ConfigParserTestFunction("\n\n\n\n\n\x00\t\x08\xA0\x00")
		self.assertEqual(result, expected_result)


if __name__ == '__main__':
	unittest.main()