import unittest
import simplejson

class SimpleJSONTestFunction(input_string):
		simplejson.loads(input_string)

class HTMLParserTest(unittest.TestCase):
	def test_1(self):
		result = SimpleJSONTestFunction("\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2(self):
		result = SimpleJSONTestFunction("\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3(self):
		result = SimpleJSONTestFunction("\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4(self):
		result = SimpleJSONTestFunction("\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_5(self):
		result = SimpleJSONTestFunction("\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_6(self):
		result = SimpleJSONTestFunction("\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_7(self):
		result = SimpleJSONTestFunction("\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_8(self):
		result = SimpleJSONTestFunction("\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_9(self):
		result = SimpleJSONTestFunction("\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_10(self):
		result = SimpleJSONTestFunction("\t\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_11(self):
		result = SimpleJSONTestFunction("\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_12(self):
		result = SimpleJSONTestFunction("\n\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_13(self):
		result = SimpleJSONTestFunction("\t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_14(self):
		result = SimpleJSONTestFunction("\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_15(self):
		result = SimpleJSONTestFunction("\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_16(self):
		result = SimpleJSONTestFunction("\t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_17(self):
		result = SimpleJSONTestFunction("\x1B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_18(self):
		result = SimpleJSONTestFunction("\t\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_19(self):
		result = SimpleJSONTestFunction("\x16\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_20(self):
		result = SimpleJSONTestFunction("\n\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_21(self):
		result = SimpleJSONTestFunction("\n\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_22(self):
		result = SimpleJSONTestFunction("\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_23(self):
		result = SimpleJSONTestFunction("\n\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_24(self):
		result = SimpleJSONTestFunction("\t\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_25(self):
		result = SimpleJSONTestFunction("\n\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_26(self):
		result = SimpleJSONTestFunction("\t\t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_27(self):
		result = SimpleJSONTestFunction("\n\t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_28(self):
		result = SimpleJSONTestFunction("\n\n\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_29(self):
		result = SimpleJSONTestFunction("\t \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_30(self):
		result = SimpleJSONTestFunction("\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_31(self):
		result = SimpleJSONTestFunction("\n \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_32(self):
		result = SimpleJSONTestFunction("\t0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_33(self):
		result = SimpleJSONTestFunction("\t\t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_34(self):
		result = SimpleJSONTestFunction("\n\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_35(self):
		result = SimpleJSONTestFunction("\t\n\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_36(self):
		result = SimpleJSONTestFunction("\n\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_37(self):
		result = SimpleJSONTestFunction("\t\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_38(self):
		result = SimpleJSONTestFunction("\t0\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_39(self):
		result = SimpleJSONTestFunction("\t0\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_40(self):
		result = SimpleJSONTestFunction("\t0\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_41(self):
		result = SimpleJSONTestFunction("\t0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_42(self):
		result = SimpleJSONTestFunction("\t0E\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_43(self):
		result = SimpleJSONTestFunction("\t0E\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_44(self):
		result = SimpleJSONTestFunction("\n\t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_45(self):
		result = SimpleJSONTestFunction("\t0E\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_46(self):
		result = SimpleJSONTestFunction("\t0\x01\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_47(self):
		result = SimpleJSONTestFunction("\t0\x00\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_48(self):
		result = SimpleJSONTestFunction("\t0\x00\x00\x00\x00\n\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_49(self):
		result = SimpleJSONTestFunction("\n\t\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_50(self):
		result = SimpleJSONTestFunction("\t\t\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_51(self):
		result = SimpleJSONTestFunction("\t\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_52(self):
		result = SimpleJSONTestFunction("\t0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_53(self):
		result = SimpleJSONTestFunction("\n\t\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_54(self):
		result = SimpleJSONTestFunction("\n\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_55(self):
		result = SimpleJSONTestFunction("\n\t\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_56(self):
		result = SimpleJSONTestFunction("\t0\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_57(self):
		result = SimpleJSONTestFunction("\t0\x03\x00\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_58(self):
		result = SimpleJSONTestFunction("\t0\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_59(self):
		result = SimpleJSONTestFunction("\t0\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_60(self):
		result = SimpleJSONTestFunction("\t0\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_61(self):
		result = SimpleJSONTestFunction("\t0e\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_62(self):
		result = SimpleJSONTestFunction("\n\t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_63(self):
		result = SimpleJSONTestFunction("\t0\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_64(self):
		result = SimpleJSONTestFunction("\t0E+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_65(self):
		result = SimpleJSONTestFunction("\t0\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_66(self):
		result = SimpleJSONTestFunction("\t0E\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_67(self):
		result = SimpleJSONTestFunction("\t0\n\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_68(self):
		result = SimpleJSONTestFunction("\t0\n\x00\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_69(self):
		result = SimpleJSONTestFunction("\t0e\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_70(self):
		result = SimpleJSONTestFunction("\n\n\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_71(self):
		result = SimpleJSONTestFunction("\t\t\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_72(self):
		result = SimpleJSONTestFunction("\t0\n\x00\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_73(self):
		result = SimpleJSONTestFunction("\t0\t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_74(self):
		result = SimpleJSONTestFunction("\t0E\x81\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_75(self):
		result = SimpleJSONTestFunction("\t\n\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_76(self):
		result = SimpleJSONTestFunction("\n\n\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_77(self):
		result = SimpleJSONTestFunction("\t\t\t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_78(self):
		result = SimpleJSONTestFunction("\t0E-\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_79(self):
		result = SimpleJSONTestFunction("\t\n\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_80(self):
		result = SimpleJSONTestFunction("\t0\t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_81(self):
		result = SimpleJSONTestFunction("\t0.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_82(self):
		result = SimpleJSONTestFunction("\t\n\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_83(self):
		result = SimpleJSONTestFunction("\t\n\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_84(self):
		result = SimpleJSONTestFunction("\t \x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_85(self):
		result = SimpleJSONTestFunction("\t \t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_86(self):
		result = SimpleJSONTestFunction("\t\t\t\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_87(self):
		result = SimpleJSONTestFunction("\t0\x01\x00\x00\n\x00\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_88(self):
		result = SimpleJSONTestFunction("\t0E+\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_89(self):
		result = SimpleJSONTestFunction("\t0E+\x80\x00\x00\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_90(self):
		result = SimpleJSONTestFunction("\t\n\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_91(self):
		result = SimpleJSONTestFunction("\t0\t\t\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_92(self):
		result = SimpleJSONTestFunction("\t\t\t\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_93(self):
		result = SimpleJSONTestFunction("\t0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_94(self):
		result = SimpleJSONTestFunction("\t0\n\x00\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_95(self):
		result = SimpleJSONTestFunction("\t\t\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_96(self):
		result = SimpleJSONTestFunction("\t \n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_97(self):
		result = SimpleJSONTestFunction("\n\t\t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_98(self):
		result = SimpleJSONTestFunction("\t0\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_99(self):
		result = SimpleJSONTestFunction("\t\n\t\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_100(self):
		result = SimpleJSONTestFunction("\t\t\t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_101(self):
		result = SimpleJSONTestFunction("\n0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_102(self):
		result = SimpleJSONTestFunction("\t \x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_103(self):
		result = SimpleJSONTestFunction("\n\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_104(self):
		result = SimpleJSONTestFunction("\t0E\x81\x00\n\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_105(self):
		result = SimpleJSONTestFunction("\t0\n\x00\n\x00\x00\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_106(self):
		result = SimpleJSONTestFunction("\t0\n\x00\n\x00\x00\n\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_107(self):
		result = SimpleJSONTestFunction("\t0\t\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_108(self):
		result = SimpleJSONTestFunction("\n\n\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_109(self):
		result = SimpleJSONTestFunction("\t\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_110(self):
		result = SimpleJSONTestFunction("\t\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_111(self):
		result = SimpleJSONTestFunction("\t0\x0E\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_112(self):
		result = SimpleJSONTestFunction("\t0\t\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_113(self):
		result = SimpleJSONTestFunction("\t0\t\t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_114(self):
		result = SimpleJSONTestFunction("\t00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_115(self):
		result = SimpleJSONTestFunction("\t0\n\x00\n\x00\x00\n\x00\n\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_116(self):
		result = SimpleJSONTestFunction("\n\t\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_117(self):
		result = SimpleJSONTestFunction("\t\t\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_118(self):
		result = SimpleJSONTestFunction("\n\n\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_119(self):
		result = SimpleJSONTestFunction("\t\t\t\t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_120(self):
		result = SimpleJSONTestFunction("\t\n\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_121(self):
		result = SimpleJSONTestFunction("\t\n\x0E\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_122(self):
		result = SimpleJSONTestFunction("\t0\n\x00\n\x00\x00\n\x00\n\x00\n\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_123(self):
		result = SimpleJSONTestFunction("\t\t\t\t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_124(self):
		result = SimpleJSONTestFunction("\t0\x0F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_125(self):
		result = SimpleJSONTestFunction("\t0\t\x00\x00\x00\x00\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_126(self):
		result = SimpleJSONTestFunction("\t0\t\t\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_127(self):
		result = SimpleJSONTestFunction("\n0E\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_128(self):
		result = SimpleJSONTestFunction("\t 0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_129(self):
		result = SimpleJSONTestFunction("\t0e\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_130(self):
		result = SimpleJSONTestFunction("\t\t\t\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_131(self):
		result = SimpleJSONTestFunction("\n\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_132(self):
		result = SimpleJSONTestFunction("\n0E+\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_133(self):
		result = SimpleJSONTestFunction("\n\t\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_134(self):
		result = SimpleJSONTestFunction("\t0E-\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_135(self):
		result = SimpleJSONTestFunction("\t0\n\x00\n\x00\x00\n\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_136(self):
		result = SimpleJSONTestFunction("\n\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_137(self):
		result = SimpleJSONTestFunction("\n0E+\x80\x00\x00\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_138(self):
		result = SimpleJSONTestFunction("\n \x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_139(self):
		result = SimpleJSONTestFunction("\t\n\t\t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_140(self):
		result = SimpleJSONTestFunction("\t\t\t\t\t\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_141(self):
		result = SimpleJSONTestFunction("\t0\n\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_142(self):
		result = SimpleJSONTestFunction("\t\t\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_143(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_144(self):
		result = SimpleJSONTestFunction("\t\t\n\t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_145(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_146(self):
		result = SimpleJSONTestFunction("\n0\t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_147(self):
		result = SimpleJSONTestFunction("\n0\t\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_148(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_149(self):
		result = SimpleJSONTestFunction("\t0e+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_150(self):
		result = SimpleJSONTestFunction("\t\n\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_151(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\t\x00\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_152(self):
		result = SimpleJSONTestFunction("\t0\t\t0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_153(self):
		result = SimpleJSONTestFunction("\n 0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_154(self):
		result = SimpleJSONTestFunction("\t\t\t\t\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_155(self):
		result = SimpleJSONTestFunction("\t0\t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_156(self):
		result = SimpleJSONTestFunction("\n0\t\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_157(self):
		result = SimpleJSONTestFunction("\t0\x04\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_158(self):
		result = SimpleJSONTestFunction("\t\t\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_159(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_160(self):
		result = SimpleJSONTestFunction("\t0\n\t\t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_161(self):
		result = SimpleJSONTestFunction("\t0\n\t\t\n\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_162(self):
		result = SimpleJSONTestFunction("\n0E-\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_163(self):
		result = SimpleJSONTestFunction("\t\t\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_164(self):
		result = SimpleJSONTestFunction("\n0\t\x0E\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_165(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\x03\x00\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_166(self):
		result = SimpleJSONTestFunction("\t0e\x81\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_167(self):
		result = SimpleJSONTestFunction("\t0E\x81\x00\x00\x00\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_168(self):
		result = SimpleJSONTestFunction("\n0e+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_169(self):
		result = SimpleJSONTestFunction("\n0E\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_170(self):
		result = SimpleJSONTestFunction("\t0E+\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_171(self):
		result = SimpleJSONTestFunction("\t\t\t\t\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_172(self):
		result = SimpleJSONTestFunction("\t0\t\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_173(self):
		result = SimpleJSONTestFunction("\t 0\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_174(self):
		result = SimpleJSONTestFunction("\t0\x10\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_175(self):
		result = SimpleJSONTestFunction("\t\t\t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_176(self):
		result = SimpleJSONTestFunction("\t\t \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_177(self):
		result = SimpleJSONTestFunction("\n0\t\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_178(self):
		result = SimpleJSONTestFunction("\t\t\t\t\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_179(self):
		result = SimpleJSONTestFunction("\t0\t\t\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_180(self):
		result = SimpleJSONTestFunction("\t0\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_181(self):
		result = SimpleJSONTestFunction("\t0\t\x03\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_182(self):
		result = SimpleJSONTestFunction("\n0\t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_183(self):
		result = SimpleJSONTestFunction("\t0\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_184(self):
		result = SimpleJSONTestFunction("\t0\t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_185(self):
		result = SimpleJSONTestFunction("\n0\t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_186(self):
		result = SimpleJSONTestFunction("\n0\t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_187(self):
		result = SimpleJSONTestFunction("\t\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_188(self):
		result = SimpleJSONTestFunction("\t0\t\t\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_189(self):
		result = SimpleJSONTestFunction("\n\n\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_190(self):
		result = SimpleJSONTestFunction("\n0E+\x80\x00\x00\x00\n\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_191(self):
		result = SimpleJSONTestFunction("\t\t \x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_192(self):
		result = SimpleJSONTestFunction("\t0e-\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_193(self):
		result = SimpleJSONTestFunction("\t0\n\x00\n\n\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_194(self):
		result = SimpleJSONTestFunction("\n0E+\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_195(self):
		result = SimpleJSONTestFunction("\t\t\t\n\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_196(self):
		result = SimpleJSONTestFunction(" \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_197(self):
		result = SimpleJSONTestFunction("\n0E+\x80\x00\x00\x00\n\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_198(self):
		result = SimpleJSONTestFunction("\t\x16\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_199(self):
		result = SimpleJSONTestFunction("\n0\t\x05\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_200(self):
		result = SimpleJSONTestFunction("\t\t \t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_201(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\t\x01\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_202(self):
		result = SimpleJSONTestFunction("\n\n\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_203(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\t\t\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_204(self):
		result = SimpleJSONTestFunction("\t 0 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_205(self):
		result = SimpleJSONTestFunction("\t\t\t\t\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_206(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_207(self):
		result = SimpleJSONTestFunction("\t0\n\t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_208(self):
		result = SimpleJSONTestFunction(" \x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_209(self):
		result = SimpleJSONTestFunction("\t 0 \x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_210(self):
		result = SimpleJSONTestFunction("\t0e+\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_211(self):
		result = SimpleJSONTestFunction("\t0\t\t \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_212(self):
		result = SimpleJSONTestFunction("\n0\t\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_213(self):
		result = SimpleJSONTestFunction("\t\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_214(self):
		result = SimpleJSONTestFunction("\t 0.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_215(self):
		result = SimpleJSONTestFunction("\t0\t\t\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_216(self):
		result = SimpleJSONTestFunction("\t0\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_217(self):
		result = SimpleJSONTestFunction("\t\n \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_218(self):
		result = SimpleJSONTestFunction("\t\n\t\t\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_219(self):
		result = SimpleJSONTestFunction("\t0\t\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_220(self):
		result = SimpleJSONTestFunction("\t0e-\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_221(self):
		result = SimpleJSONTestFunction("\t0E-\x81\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_222(self):
		result = SimpleJSONTestFunction("\t0\t\x11\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_223(self):
		result = SimpleJSONTestFunction("\n0\t\x0F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_224(self):
		result = SimpleJSONTestFunction("\t0\t8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_225(self):
		result = SimpleJSONTestFunction("\t0\t\t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_226(self):
		result = SimpleJSONTestFunction("\t\x15\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_227(self):
		result = SimpleJSONTestFunction("\t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_228(self):
		result = SimpleJSONTestFunction("\t0e\x80\x00\n\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_229(self):
		result = SimpleJSONTestFunction("\n \t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_230(self):
		result = SimpleJSONTestFunction("\t\t \x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_231(self):
		result = SimpleJSONTestFunction("\x17\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_232(self):
		result = SimpleJSONTestFunction("\t0\n\x00\n\n\x00\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_233(self):
		result = SimpleJSONTestFunction("\n0\t\x0C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_234(self):
		result = SimpleJSONTestFunction("\t0\x10\x00\x00\x00\x00\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_235(self):
		result = SimpleJSONTestFunction("\t0\t\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_236(self):
		result = SimpleJSONTestFunction("\t0E-\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_237(self):
		result = SimpleJSONTestFunction("\t0\t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_238(self):
		result = SimpleJSONTestFunction("!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_239(self):
		result = SimpleJSONTestFunction("\"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_240(self):
		result = SimpleJSONTestFunction("\t\t \t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_241(self):
		result = SimpleJSONTestFunction("\t0E+\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_242(self):
		result = SimpleJSONTestFunction("\n \x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_243(self):
		result = SimpleJSONTestFunction("\t01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_244(self):
		result = SimpleJSONTestFunction("\t\n\x17\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_245(self):
		result = SimpleJSONTestFunction("\"\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_246(self):
		result = SimpleJSONTestFunction("\n0\t\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_247(self):
		result = SimpleJSONTestFunction("\"\x10\x0D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_248(self):
		result = SimpleJSONTestFunction("\n\t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_249(self):
		result = SimpleJSONTestFunction("\" \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_250(self):
		result = SimpleJSONTestFunction("\t\t\t\t\n\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_251(self):
		result = SimpleJSONTestFunction("\t0\x0C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_252(self):
		result = SimpleJSONTestFunction("\t0\t\t\x06\x00\x00\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_253(self):
		result = SimpleJSONTestFunction("\"\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_254(self):
		result = SimpleJSONTestFunction("\t0\t\t\n\t\t\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_255(self):
		result = SimpleJSONTestFunction("'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_256(self):
		result = SimpleJSONTestFunction("\t0e+\x00\n\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_257(self):
		result = SimpleJSONTestFunction("\n\t\t\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_258(self):
		result = SimpleJSONTestFunction("\n\t\t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_259(self):
		result = SimpleJSONTestFunction("\"\x01\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_260(self):
		result = SimpleJSONTestFunction("\t\t0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_261(self):
		result = SimpleJSONTestFunction("\"\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_262(self):
		result = SimpleJSONTestFunction("\n0\t\x0B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_263(self):
		result = SimpleJSONTestFunction("\t\n\t\t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_264(self):
		result = SimpleJSONTestFunction("-\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_265(self):
		result = SimpleJSONTestFunction("\n\t\t\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_266(self):
		result = SimpleJSONTestFunction("\t 0 \t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_267(self):
		result = SimpleJSONTestFunction("\t0\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_268(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_269(self):
		result = SimpleJSONTestFunction("\t0\n\t0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_270(self):
		result = SimpleJSONTestFunction("\t0\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_271(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_272(self):
		result = SimpleJSONTestFunction("\t0\t1\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_273(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\t\x03\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_274(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\t\t\x01\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_275(self):
		result = SimpleJSONTestFunction("\t0\t\t\n\t\t\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_276(self):
		result = SimpleJSONTestFunction("\t\t \x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_277(self):
		result = SimpleJSONTestFunction("\t\t0.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_278(self):
		result = SimpleJSONTestFunction("\n\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_279(self):
		result = SimpleJSONTestFunction("\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_280(self):
		result = SimpleJSONTestFunction("\t 0.\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_281(self):
		result = SimpleJSONTestFunction("\t\t\t\t\t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_282(self):
		result = SimpleJSONTestFunction("\"\x01\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_283(self):
		result = SimpleJSONTestFunction("\" \x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_284(self):
		result = SimpleJSONTestFunction(" \t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_285(self):
		result = SimpleJSONTestFunction("\t0\t\t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_286(self):
		result = SimpleJSONTestFunction("\"  \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_287(self):
		result = SimpleJSONTestFunction("\"\n\\\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_288(self):
		result = SimpleJSONTestFunction("\"\n\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_289(self):
		result = SimpleJSONTestFunction("\t  \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_290(self):
		result = SimpleJSONTestFunction("\"  \x00\\\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_291(self):
		result = SimpleJSONTestFunction("\t\t \x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_292(self):
		result = SimpleJSONTestFunction("\"\x01\\\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_293(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\x0E\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_294(self):
		result = SimpleJSONTestFunction("\t0\t\n\t\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_295(self):
		result = SimpleJSONTestFunction("\t0\t\t \x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_296(self):
		result = SimpleJSONTestFunction("\"\n\x0D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_297(self):
		result = SimpleJSONTestFunction("\t0\t\t\n\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_298(self):
		result = SimpleJSONTestFunction("\t0\t\t \t\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_299(self):
		result = SimpleJSONTestFunction("\t0E-\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_300(self):
		result = SimpleJSONTestFunction("\t\n \t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_301(self):
		result = SimpleJSONTestFunction("\t\t\t\n\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_302(self):
		result = SimpleJSONTestFunction("\"\n\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_303(self):
		result = SimpleJSONTestFunction("\n\t0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_304(self):
		result = SimpleJSONTestFunction("\"\n\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_305(self):
		result = SimpleJSONTestFunction("\t\t \t\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_306(self):
		result = SimpleJSONTestFunction("\t\t\t0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_307(self):
		result = SimpleJSONTestFunction("\t\t\t\t\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_308(self):
		result = SimpleJSONTestFunction("\"\n'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_309(self):
		result = SimpleJSONTestFunction("\t\t\t0.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_310(self):
		result = SimpleJSONTestFunction("\" \x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_311(self):
		result = SimpleJSONTestFunction("\"  \x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_312(self):
		result = SimpleJSONTestFunction("\n0\t\t\t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_313(self):
		result = SimpleJSONTestFunction("\t\t\n\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_314(self):
		result = SimpleJSONTestFunction("\" \n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_315(self):
		result = SimpleJSONTestFunction("\t0e\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_316(self):
		result = SimpleJSONTestFunction("\t0\t\t \t\x01\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_317(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_318(self):
		result = SimpleJSONTestFunction("\t0\t\t\x03\x00\x00\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_319(self):
		result = SimpleJSONTestFunction("\" \x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_320(self):
		result = SimpleJSONTestFunction("\" \n\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_321(self):
		result = SimpleJSONTestFunction("\t\t\t\n\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_322(self):
		result = SimpleJSONTestFunction("\n\t\t\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_323(self):
		result = SimpleJSONTestFunction("\n0\t\x04\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_324(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_325(self):
		result = SimpleJSONTestFunction("\t0\n\t\t\t\x01\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_326(self):
		result = SimpleJSONTestFunction(" \x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_327(self):
		result = SimpleJSONTestFunction("\t\n\t\t\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_328(self):
		result = SimpleJSONTestFunction("\t0\n\x00\n\x00\x00\n\n\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_329(self):
		result = SimpleJSONTestFunction("-0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_330(self):
		result = SimpleJSONTestFunction("-@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_331(self):
		result = SimpleJSONTestFunction("\t0\x00\x00\x00\x00\n\x00\n\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_332(self):
		result = SimpleJSONTestFunction("\n0\t\t0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_333(self):
		result = SimpleJSONTestFunction("\t 0\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_334(self):
		result = SimpleJSONTestFunction("\"\n\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_335(self):
		result = SimpleJSONTestFunction("\"  \x10 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_336(self):
		result = SimpleJSONTestFunction("\t 0 \t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_337(self):
		result = SimpleJSONTestFunction("\" \n\\\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_338(self):
		result = SimpleJSONTestFunction("\"\x00\\\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_339(self):
		result = SimpleJSONTestFunction("\"\n\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_340(self):
		result = SimpleJSONTestFunction("\"\n\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_341(self):
		result = SimpleJSONTestFunction("\"\x10\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_342(self):
		result = SimpleJSONTestFunction("\t\t\n\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_343(self):
		result = SimpleJSONTestFunction("\"\x00\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_344(self):
		result = SimpleJSONTestFunction("\t0\t\t\n\n\t\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_345(self):
		result = SimpleJSONTestFunction("\t\t0.\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_346(self):
		result = SimpleJSONTestFunction("\"  \x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_347(self):
		result = SimpleJSONTestFunction("\"\n \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_348(self):
		result = SimpleJSONTestFunction("\t\t\t\t\t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_349(self):
		result = SimpleJSONTestFunction("\t\t\t0.\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_350(self):
		result = SimpleJSONTestFunction(" \t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_351(self):
		result = SimpleJSONTestFunction("\t0\t\t\x0C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_352(self):
		result = SimpleJSONTestFunction("\t\t \t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_353(self):
		result = SimpleJSONTestFunction("\n0e\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_354(self):
		result = SimpleJSONTestFunction(" \t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_355(self):
		result = SimpleJSONTestFunction("-0.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_356(self):
		result = SimpleJSONTestFunction("\t\t\n0.\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_357(self):
		result = SimpleJSONTestFunction(" \t\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_358(self):
		result = SimpleJSONTestFunction(" \t\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_359(self):
		result = SimpleJSONTestFunction("\t 0 \t\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_360(self):
		result = SimpleJSONTestFunction("\n0\n\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_361(self):
		result = SimpleJSONTestFunction("\t0\t\t\x0E\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_362(self):
		result = SimpleJSONTestFunction("\t\t\n\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_363(self):
		result = SimpleJSONTestFunction("\t0E+\x80\x00\x00\n\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_364(self):
		result = SimpleJSONTestFunction("\t0\t\x05\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_365(self):
		result = SimpleJSONTestFunction("\t\t \x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_366(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\n\x01\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_367(self):
		result = SimpleJSONTestFunction("\t0\n\t\t\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_368(self):
		result = SimpleJSONTestFunction("-\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_369(self):
		result = SimpleJSONTestFunction("\t\t0.\x81\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_370(self):
		result = SimpleJSONTestFunction("\"\x10\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_371(self):
		result = SimpleJSONTestFunction("-0.\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_372(self):
		result = SimpleJSONTestFunction("\"  \x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_373(self):
		result = SimpleJSONTestFunction("\t \t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_374(self):
		result = SimpleJSONTestFunction("\t0E-\x03\n\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_375(self):
		result = SimpleJSONTestFunction("\" \n\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_376(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_377(self):
		result = SimpleJSONTestFunction("\t0\t\t \t\x02\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_378(self):
		result = SimpleJSONTestFunction("\t\t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_379(self):
		result = SimpleJSONTestFunction("\"\n\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_380(self):
		result = SimpleJSONTestFunction("\"\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_381(self):
		result = SimpleJSONTestFunction("\" \n'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_382(self):
		result = SimpleJSONTestFunction("\t 0 \x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_383(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\n\x02\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_384(self):
		result = SimpleJSONTestFunction("\n0\t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_385(self):
		result = SimpleJSONTestFunction("\n\t\x0C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_386(self):
		result = SimpleJSONTestFunction("\" \x10\\\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_387(self):
		result = SimpleJSONTestFunction("\"\n\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_388(self):
		result = SimpleJSONTestFunction("\t 0 \t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_389(self):
		result = SimpleJSONTestFunction("\"  \n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_390(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\x01\x00\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_391(self):
		result = SimpleJSONTestFunction("\t\t\n\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_392(self):
		result = SimpleJSONTestFunction("\" \x00\x0D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_393(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\n\x03\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_394(self):
		result = SimpleJSONTestFunction("\n\x0F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_395(self):
		result = SimpleJSONTestFunction("\n0\t\x05\x00\x00\x00\n\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_396(self):
		result = SimpleJSONTestFunction("\t0\t\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_397(self):
		result = SimpleJSONTestFunction("\t0\n\x00\n\x00\x00\n\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_398(self):
		result = SimpleJSONTestFunction("\t0\t\t\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_399(self):
		result = SimpleJSONTestFunction("\n \x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_400(self):
		result = SimpleJSONTestFunction("\"  \x01\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_401(self):
		result = SimpleJSONTestFunction("\"\n\x90\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_402(self):
		result = SimpleJSONTestFunction("\"  \x10\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_403(self):
		result = SimpleJSONTestFunction("\t0\t\n\t\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_404(self):
		result = SimpleJSONTestFunction("\t0\t\t\x05\x00\x00\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_405(self):
		result = SimpleJSONTestFunction("\t 0 \t\t\x10\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_406(self):
		result = SimpleJSONTestFunction("\t\t\t \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_407(self):
		result = SimpleJSONTestFunction("\t\n\t\t\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_408(self):
		result = SimpleJSONTestFunction("\t\t\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_409(self):
		result = SimpleJSONTestFunction("\t0\n\t\t\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_410(self):
		result = SimpleJSONTestFunction("\" 0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_411(self):
		result = SimpleJSONTestFunction("\t\t\x15\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_412(self):
		result = SimpleJSONTestFunction("\"   \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_413(self):
		result = SimpleJSONTestFunction("\n\t\x0E\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_414(self):
		result = SimpleJSONTestFunction("\t0\t\t\x03\x00\x00\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_415(self):
		result = SimpleJSONTestFunction("\t0\t\t \x02\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_416(self):
		result = SimpleJSONTestFunction("\t0\t\t\x02\x00\x00\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_417(self):
		result = SimpleJSONTestFunction("\t 0 \t\t\x01\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_418(self):
		result = SimpleJSONTestFunction("\"  \n\\\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_419(self):
		result = SimpleJSONTestFunction("\t\t0.\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_420(self):
		result = SimpleJSONTestFunction("\n\t\t\t\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_421(self):
		result = SimpleJSONTestFunction("\t\t\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_422(self):
		result = SimpleJSONTestFunction(" \x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_423(self):
		result = SimpleJSONTestFunction("\"  \n\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_424(self):
		result = SimpleJSONTestFunction("\"   \x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_425(self):
		result = SimpleJSONTestFunction("\t0\t\x0C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_426(self):
		result = SimpleJSONTestFunction("\t0\t!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_427(self):
		result = SimpleJSONTestFunction("\t0\t'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_428(self):
		result = SimpleJSONTestFunction("\t0\t\n \t\x01\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_429(self):
		result = SimpleJSONTestFunction("\n 0 \x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_430(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\n\x07\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_431(self):
		result = SimpleJSONTestFunction("\n0\t\x04\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_432(self):
		result = SimpleJSONTestFunction("\t0\n\t\t\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_433(self):
		result = SimpleJSONTestFunction("\t0\x17\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_434(self):
		result = SimpleJSONTestFunction("\t00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_435(self):
		result = SimpleJSONTestFunction("-1\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_436(self):
		result = SimpleJSONTestFunction("\t0 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_437(self):
		result = SimpleJSONTestFunction("\t\t\n\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_438(self):
		result = SimpleJSONTestFunction("\t0\t\t\n\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_439(self):
		result = SimpleJSONTestFunction("\n\t\t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_440(self):
		result = SimpleJSONTestFunction("\" \x01\x0D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_441(self):
		result = SimpleJSONTestFunction("\"\n\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_442(self):
		result = SimpleJSONTestFunction("\" 0\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_443(self):
		result = SimpleJSONTestFunction("\t0\n\t\t\x00\n\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_444(self):
		result = SimpleJSONTestFunction("\t0\t\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_445(self):
		result = SimpleJSONTestFunction("\t0\x00\x00\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_446(self):
		result = SimpleJSONTestFunction("\t\t\t\t\x16\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_447(self):
		result = SimpleJSONTestFunction("\t0\t\t\n\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_448(self):
		result = SimpleJSONTestFunction("\" \x10\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_449(self):
		result = SimpleJSONTestFunction("\t0\t\n\t\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_450(self):
		result = SimpleJSONTestFunction("\"\x11 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_451(self):
		result = SimpleJSONTestFunction("\n\x0C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_452(self):
		result = SimpleJSONTestFunction("\t0\t\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_453(self):
		result = SimpleJSONTestFunction("\t \t\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_454(self):
		result = SimpleJSONTestFunction("\t\n\t\t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_455(self):
		result = SimpleJSONTestFunction("\n0e\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_456(self):
		result = SimpleJSONTestFunction("\t0\t\n \t\x02\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_457(self):
		result = SimpleJSONTestFunction("-3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_458(self):
		result = SimpleJSONTestFunction("-2\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_459(self):
		result = SimpleJSONTestFunction("\n0\t\x05\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_460(self):
		result = SimpleJSONTestFunction("\"   \x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_461(self):
		result = SimpleJSONTestFunction("\"  !\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_462(self):
		result = SimpleJSONTestFunction("\n\t\x0F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_463(self):
		result = SimpleJSONTestFunction("\t0\t\t \x03\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_464(self):
		result = SimpleJSONTestFunction("\t\t\t\t\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_465(self):
		result = SimpleJSONTestFunction("\n0\t\x0B\x00\x00\x00\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_466(self):
		result = SimpleJSONTestFunction("\"\x10'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_467(self):
		result = SimpleJSONTestFunction("\t \t \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_468(self):
		result = SimpleJSONTestFunction("\"  !\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_469(self):
		result = SimpleJSONTestFunction("\t \x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_470(self):
		result = SimpleJSONTestFunction("\"\x10\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_471(self):
		result = SimpleJSONTestFunction("\"   \n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_472(self):
		result = SimpleJSONTestFunction("\t 0 \t\t\t\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_473(self):
		result = SimpleJSONTestFunction("\"   \n\\\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_474(self):
		result = SimpleJSONTestFunction("\"\x11\x0D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_475(self):
		result = SimpleJSONTestFunction("\t0\t\n \t\x03\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_476(self):
		result = SimpleJSONTestFunction("\"  !\x01\n\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_477(self):
		result = SimpleJSONTestFunction("\"\x11\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_478(self):
		result = SimpleJSONTestFunction("\" \n\x0D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_479(self):
		result = SimpleJSONTestFunction("\n0\t\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_480(self):
		result = SimpleJSONTestFunction("\"   \n\x0D\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_481(self):
		result = SimpleJSONTestFunction("\" 0\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_482(self):
		result = SimpleJSONTestFunction("-4\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_483(self):
		result = SimpleJSONTestFunction("\t\t\t\n\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_484(self):
		result = SimpleJSONTestFunction("-:\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_485(self):
		result = SimpleJSONTestFunction("\"\n\x83\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_486(self):
		result = SimpleJSONTestFunction("\"\n\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_487(self):
		result = SimpleJSONTestFunction("\"\n\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_488(self):
		result = SimpleJSONTestFunction("\"  \"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_489(self):
		result = SimpleJSONTestFunction("\"\x01\x0D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_490(self):
		result = SimpleJSONTestFunction("\n\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_491(self):
		result = SimpleJSONTestFunction("\"\x00'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_492(self):
		result = SimpleJSONTestFunction("\"  \n\x0D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_493(self):
		result = SimpleJSONTestFunction("\"  \"\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_494(self):
		result = SimpleJSONTestFunction("-I\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_495(self):
		result = SimpleJSONTestFunction("\t\t \t\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_496(self):
		result = SimpleJSONTestFunction("\"  !\x01'\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_497(self):
		result = SimpleJSONTestFunction("\n\t\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_498(self):
		result = SimpleJSONTestFunction("\t\t \x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_499(self):
		result = SimpleJSONTestFunction("\n0\t\x06\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_500(self):
		result = SimpleJSONTestFunction("\t0!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_501(self):
		result = SimpleJSONTestFunction("\t \t0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_502(self):
		result = SimpleJSONTestFunction("\t\t0\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_503(self):
		result = SimpleJSONTestFunction("\"  !\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_504(self):
		result = SimpleJSONTestFunction("\"  !\n\\\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_505(self):
		result = SimpleJSONTestFunction("\"\n\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_506(self):
		result = SimpleJSONTestFunction("\"\n\x93\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_507(self):
		result = SimpleJSONTestFunction("-In\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_508(self):
		result = SimpleJSONTestFunction("\t\t \x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_509(self):
		result = SimpleJSONTestFunction("\t0 \x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_510(self):
		result = SimpleJSONTestFunction("\t\n\t\n\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_511(self):
		result = SimpleJSONTestFunction("\n0\t\x04\n\x00\x00\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_512(self):
		result = SimpleJSONTestFunction("\"  \" \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_513(self):
		result = SimpleJSONTestFunction("\"  \"0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_514(self):
		result = SimpleJSONTestFunction("\n0\t\x0B\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_515(self):
		result = SimpleJSONTestFunction("\t0\t\t\n\t\t\x00\x00\n\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_516(self):
		result = SimpleJSONTestFunction("\"   \x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_517(self):
		result = SimpleJSONTestFunction("\"\n\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_518(self):
		result = SimpleJSONTestFunction("\" @\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_519(self):
		result = SimpleJSONTestFunction("-Inf\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_520(self):
		result = SimpleJSONTestFunction("\t 0 \x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_521(self):
		result = SimpleJSONTestFunction("\"  \" \x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_522(self):
		result = SimpleJSONTestFunction("\t \t0.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_523(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\x16\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_524(self):
		result = SimpleJSONTestFunction("\t0 \x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_525(self):
		result = SimpleJSONTestFunction(" \x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_526(self):
		result = SimpleJSONTestFunction("\"  \" \x02\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_527(self):
		result = SimpleJSONTestFunction("\"\x01 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_528(self):
		result = SimpleJSONTestFunction("\t0e\x01\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_529(self):
		result = SimpleJSONTestFunction("\t \t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_530(self):
		result = SimpleJSONTestFunction("-Infi\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_531(self):
		result = SimpleJSONTestFunction("\"  \" \t\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_532(self):
		result = SimpleJSONTestFunction("\" 0\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_533(self):
		result = SimpleJSONTestFunction("\n 0 \x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_534(self):
		result = SimpleJSONTestFunction("\"  \" \n\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_535(self):
		result = SimpleJSONTestFunction("\"\x10\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_536(self):
		result = SimpleJSONTestFunction("\t\n\t\t\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_537(self):
		result = SimpleJSONTestFunction("\"  \"\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_538(self):
		result = SimpleJSONTestFunction("\"\n\x84\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_539(self):
		result = SimpleJSONTestFunction("\n\x0B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_540(self):
		result = SimpleJSONTestFunction("\"  \" \x02\x00\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_541(self):
		result = SimpleJSONTestFunction("\n0\n\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_542(self):
		result = SimpleJSONTestFunction("\t\t \x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_543(self):
		result = SimpleJSONTestFunction(" \x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_544(self):
		result = SimpleJSONTestFunction("\n0\t\x02\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_545(self):
		result = SimpleJSONTestFunction("\n\n\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_546(self):
		result = SimpleJSONTestFunction("\n\t\t0.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_547(self):
		result = SimpleJSONTestFunction("\t  \x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_548(self):
		result = SimpleJSONTestFunction("\" 0\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_549(self):
		result = SimpleJSONTestFunction("\t\n\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_550(self):
		result = SimpleJSONTestFunction("-6\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_551(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\t\t\t\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_552(self):
		result = SimpleJSONTestFunction("\t\n0\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_553(self):
		result = SimpleJSONTestFunction("\"  \n\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_554(self):
		result = SimpleJSONTestFunction("\t\t\x17\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_555(self):
		result = SimpleJSONTestFunction("\"   \x01'\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_556(self):
		result = SimpleJSONTestFunction("\t0'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_557(self):
		result = SimpleJSONTestFunction("\t0\t\t\x0F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_558(self):
		result = SimpleJSONTestFunction("\t \t\t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_559(self):
		result = SimpleJSONTestFunction("\t 0 \t\t\x00\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_560(self):
		result = SimpleJSONTestFunction("\t 0\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_561(self):
		result = SimpleJSONTestFunction("\"  \n\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_562(self):
		result = SimpleJSONTestFunction("\" 0\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_563(self):
		result = SimpleJSONTestFunction("\n0\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_564(self):
		result = SimpleJSONTestFunction("\t\t\t0\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_565(self):
		result = SimpleJSONTestFunction("\t0\n\t\t\x00\n\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_566(self):
		result = SimpleJSONTestFunction("-Infin\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_567(self):
		result = SimpleJSONTestFunction("\t\t \n\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_568(self):
		result = SimpleJSONTestFunction(" \x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_569(self):
		result = SimpleJSONTestFunction("\t0\n\t\t\t\x02\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_570(self):
		result = SimpleJSONTestFunction("\"  \"\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_571(self):
		result = SimpleJSONTestFunction("\n\t\t\t\t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_572(self):
		result = SimpleJSONTestFunction("\"  \" \x03\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_573(self):
		result = SimpleJSONTestFunction("\t \n0.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_574(self):
		result = SimpleJSONTestFunction("\t0\xA0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_575(self):
		result = SimpleJSONTestFunction("\t \t\n\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_576(self):
		result = SimpleJSONTestFunction("\"\n\x15\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_577(self):
		result = SimpleJSONTestFunction("\"   \x10\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_578(self):
		result = SimpleJSONTestFunction("\"\n\x94\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_579(self):
		result = SimpleJSONTestFunction("\"\n\x81\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_580(self):
		result = SimpleJSONTestFunction("\t0\t\t\n\x13\x00\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_581(self):
		result = SimpleJSONTestFunction("\"\x01\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_582(self):
		result = SimpleJSONTestFunction("\"  \"\t\x00\x00\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_583(self):
		result = SimpleJSONTestFunction("\t 0\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_584(self):
		result = SimpleJSONTestFunction("\t 0 \x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_585(self):
		result = SimpleJSONTestFunction("\t\t\t\n\t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_586(self):
		result = SimpleJSONTestFunction("\" \n\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_587(self):
		result = SimpleJSONTestFunction(" \t\t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_588(self):
		result = SimpleJSONTestFunction("\n \t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_589(self):
		result = SimpleJSONTestFunction("\"  !\n\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_590(self):
		result = SimpleJSONTestFunction("\"  \" \x00\x00\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_591(self):
		result = SimpleJSONTestFunction("\t0\n\t\t\x12\x00\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_592(self):
		result = SimpleJSONTestFunction("\" @\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_593(self):
		result = SimpleJSONTestFunction("\t0E\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_594(self):
		result = SimpleJSONTestFunction("\t \t0\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_595(self):
		result = SimpleJSONTestFunction("\"  0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_596(self):
		result = SimpleJSONTestFunction("\t\n\t0.\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_597(self):
		result = SimpleJSONTestFunction("\"  \"\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_598(self):
		result = SimpleJSONTestFunction("\t \n0\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_599(self):
		result = SimpleJSONTestFunction("\t \t0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_600(self):
		result = SimpleJSONTestFunction("\t0\t\t\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_601(self):
		result = SimpleJSONTestFunction(" \t\t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_602(self):
		result = SimpleJSONTestFunction("\"  \n\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_603(self):
		result = SimpleJSONTestFunction("\n\t\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_604(self):
		result = SimpleJSONTestFunction("\n\t \t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_605(self):
		result = SimpleJSONTestFunction("\n 0\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_606(self):
		result = SimpleJSONTestFunction("\t\t\n\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_607(self):
		result = SimpleJSONTestFunction("\t\n\t0\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_608(self):
		result = SimpleJSONTestFunction("\" \x01\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_609(self):
		result = SimpleJSONTestFunction("\" @\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_610(self):
		result = SimpleJSONTestFunction("\t0\t\t\n\n\t\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_611(self):
		result = SimpleJSONTestFunction("\"  0\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_612(self):
		result = SimpleJSONTestFunction("\t0 \t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_613(self):
		result = SimpleJSONTestFunction("\t \t0\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_614(self):
		result = SimpleJSONTestFunction("\t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_615(self):
		result = SimpleJSONTestFunction("\n 0\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_616(self):
		result = SimpleJSONTestFunction("\"  0\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_617(self):
		result = SimpleJSONTestFunction("\"  \"\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_618(self):
		result = SimpleJSONTestFunction("\"\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_619(self):
		result = SimpleJSONTestFunction("\n0\t\x0E\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_620(self):
		result = SimpleJSONTestFunction("\n00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_621(self):
		result = SimpleJSONTestFunction("\"\n\x91\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_622(self):
		result = SimpleJSONTestFunction("\t 0 \t\t\x02\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_623(self):
		result = SimpleJSONTestFunction("\"  \" \n\x00\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_624(self):
		result = SimpleJSONTestFunction("-Infini\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_625(self):
		result = SimpleJSONTestFunction("-7\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_626(self):
		result = SimpleJSONTestFunction("\"  \"\t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_627(self):
		result = SimpleJSONTestFunction("\t0\n\x00\n\x00\x00\n\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_628(self):
		result = SimpleJSONTestFunction("\n \x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_629(self):
		result = SimpleJSONTestFunction("\"  \"\n\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_630(self):
		result = SimpleJSONTestFunction("\"   \x11 \x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_631(self):
		result = SimpleJSONTestFunction("\t\t\t \x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_632(self):
		result = SimpleJSONTestFunction("\n\n\x0F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_633(self):
		result = SimpleJSONTestFunction("\"  \"\n\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_634(self):
		result = SimpleJSONTestFunction("-5\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_635(self):
		result = SimpleJSONTestFunction("\" 0\n \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_636(self):
		result = SimpleJSONTestFunction("\t\t\t\n\t\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_637(self):
		result = SimpleJSONTestFunction("\t0E-0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_638(self):
		result = SimpleJSONTestFunction("\"  \"\n\x01\x00\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_639(self):
		result = SimpleJSONTestFunction("\"  \"\n\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_640(self):
		result = SimpleJSONTestFunction("\t0E-0\x00\x00\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_641(self):
		result = SimpleJSONTestFunction("\n0E-0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_642(self):
		result = SimpleJSONTestFunction("\"   \x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_643(self):
		result = SimpleJSONTestFunction(" \t\t\t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_644(self):
		result = SimpleJSONTestFunction("1\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_645(self):
		result = SimpleJSONTestFunction("\"  \"\n\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_646(self):
		result = SimpleJSONTestFunction("\"  \" \x04\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_647(self):
		result = SimpleJSONTestFunction("\n\n\x0C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_648(self):
		result = SimpleJSONTestFunction("\t0\t\n \x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_649(self):
		result = SimpleJSONTestFunction("\t!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_650(self):
		result = SimpleJSONTestFunction("\"\x01\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_651(self):
		result = SimpleJSONTestFunction("\t0E-0\x00\x00\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_652(self):
		result = SimpleJSONTestFunction("\"  0\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_653(self):
		result = SimpleJSONTestFunction("\t0\t\x07\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_654(self):
		result = SimpleJSONTestFunction("\"   \n\n\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_655(self):
		result = SimpleJSONTestFunction("\t\"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_656(self):
		result = SimpleJSONTestFunction("\n0\t\x02\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_657(self):
		result = SimpleJSONTestFunction("\"\n\x85\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_658(self):
		result = SimpleJSONTestFunction("\"\n\x95\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_659(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\x1E\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_660(self):
		result = SimpleJSONTestFunction("\"  \"\t\x00\x00\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_661(self):
		result = SimpleJSONTestFunction("\n0e+\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_662(self):
		result = SimpleJSONTestFunction("\n0E-0\x00\x00\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_663(self):
		result = SimpleJSONTestFunction("\t 0\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_664(self):
		result = SimpleJSONTestFunction("\t 0E\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_665(self):
		result = SimpleJSONTestFunction("\"   \x01\t\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_666(self):
		result = SimpleJSONTestFunction("2\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_667(self):
		result = SimpleJSONTestFunction("\n0E-0\x00\x00\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_668(self):
		result = SimpleJSONTestFunction("\n0\n\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_669(self):
		result = SimpleJSONTestFunction("\"   \x11\t\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_670(self):
		result = SimpleJSONTestFunction("\"  \n\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_671(self):
		result = SimpleJSONTestFunction("-Infinit\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_672(self):
		result = SimpleJSONTestFunction("\"  \" \n\x00\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_673(self):
		result = SimpleJSONTestFunction("\t\t\n\t\t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_674(self):
		result = SimpleJSONTestFunction("\t0\t\n\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_675(self):
		result = SimpleJSONTestFunction("-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_676(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\t\t\t\x01\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_677(self):
		result = SimpleJSONTestFunction("\t \t\t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_678(self):
		result = SimpleJSONTestFunction("-0\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_679(self):
		result = SimpleJSONTestFunction("\"   !\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_680(self):
		result = SimpleJSONTestFunction("\"\n\xA1\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_681(self):
		result = SimpleJSONTestFunction(":\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_682(self):
		result = SimpleJSONTestFunction("\t\t \t\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_683(self):
		result = SimpleJSONTestFunction("-Infinity\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_684(self):
		result = SimpleJSONTestFunction("\t \t\t\t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_685(self):
		result = SimpleJSONTestFunction("\n0E-0\x00\x00\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_686(self):
		result = SimpleJSONTestFunction("\"   !\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_687(self):
		result = SimpleJSONTestFunction("\"  \" \n\x00\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_688(self):
		result = SimpleJSONTestFunction("\"\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_689(self):
		result = SimpleJSONTestFunction("\t\t \t\t\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_690(self):
		result = SimpleJSONTestFunction("\t0\t\t \x03\x00\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_691(self):
		result = SimpleJSONTestFunction("\t0E-0\x00\x00\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_692(self):
		result = SimpleJSONTestFunction("-Infinity\x01\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_693(self):
		result = SimpleJSONTestFunction("3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_694(self):
		result = SimpleJSONTestFunction("\n\"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_695(self):
		result = SimpleJSONTestFunction("\n0\n\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_696(self):
		result = SimpleJSONTestFunction("\t \t0\t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_697(self):
		result = SimpleJSONTestFunction("\t0 \x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_698(self):
		result = SimpleJSONTestFunction("-Infinity\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_699(self):
		result = SimpleJSONTestFunction("\n\t\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_700(self):
		result = SimpleJSONTestFunction("\t \t\t\t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_701(self):
		result = SimpleJSONTestFunction("\"  \"\n\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_702(self):
		result = SimpleJSONTestFunction("\t-\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_703(self):
		result = SimpleJSONTestFunction("\t0E-\x81\x00\x00\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_704(self):
		result = SimpleJSONTestFunction("\"   !\n\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_705(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\n\x06\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_706(self):
		result = SimpleJSONTestFunction("\n0E-0\x00\x00\n\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_707(self):
		result = SimpleJSONTestFunction("\t\t\t\t\x17\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_708(self):
		result = SimpleJSONTestFunction("\t0\t\x0B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_709(self):
		result = SimpleJSONTestFunction("-Infinity\t\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_710(self):
		result = SimpleJSONTestFunction("\t0\n\x00\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_711(self):
		result = SimpleJSONTestFunction(" \n\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_712(self):
		result = SimpleJSONTestFunction("\t \t0.\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_713(self):
		result = SimpleJSONTestFunction("\t0\n\t\t\t\x03\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_714(self):
		result = SimpleJSONTestFunction("\t'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_715(self):
		result = SimpleJSONTestFunction("\"  \"\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_716(self):
		result = SimpleJSONTestFunction("\n0\t\t\t\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_717(self):
		result = SimpleJSONTestFunction("\t \t0\t\x00\x00\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_718(self):
		result = SimpleJSONTestFunction("\t\"\x00\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_719(self):
		result = SimpleJSONTestFunction("\t\t8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_720(self):
		result = SimpleJSONTestFunction("\"  \"\t\x00\x00\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_721(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\n\x04\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_722(self):
		result = SimpleJSONTestFunction("\t-@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_723(self):
		result = SimpleJSONTestFunction("\"  \n\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_724(self):
		result = SimpleJSONTestFunction("\"   \"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_725(self):
		result = SimpleJSONTestFunction("\n0E-0\x00\x00\x00\x00\x00\n\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_726(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\n\x04\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_727(self):
		result = SimpleJSONTestFunction("-Infinity\x01\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_728(self):
		result = SimpleJSONTestFunction("\"  \n\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_729(self):
		result = SimpleJSONTestFunction("\"  \"\n\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_730(self):
		result = SimpleJSONTestFunction("\"  \"\n\x06\x00\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_731(self):
		result = SimpleJSONTestFunction("-Infinity\t\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_732(self):
		result = SimpleJSONTestFunction("\t\t\n\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_733(self):
		result = SimpleJSONTestFunction("\"  0\x01\x0D\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_734(self):
		result = SimpleJSONTestFunction("\"\x00\x0D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_735(self):
		result = SimpleJSONTestFunction("\n \t\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_736(self):
		result = SimpleJSONTestFunction("\n0\t\x0B\x00\x00\x00\x00\x00\n\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_737(self):
		result = SimpleJSONTestFunction("\t\"\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_738(self):
		result = SimpleJSONTestFunction("\t0\n\t\t\t\x04\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_739(self):
		result = SimpleJSONTestFunction("\"  \"\t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_740(self):
		result = SimpleJSONTestFunction("-Infinity\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_741(self):
		result = SimpleJSONTestFunction("\t0 \t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_742(self):
		result = SimpleJSONTestFunction("\t0\t\t \x07\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_743(self):
		result = SimpleJSONTestFunction("\t 0 \t\t\t\x01\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_744(self):
		result = SimpleJSONTestFunction("\t0E-0\x00\x00\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_745(self):
		result = SimpleJSONTestFunction("\t 0 \t\t\t\t\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_746(self):
		result = SimpleJSONTestFunction("\"\n\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_747(self):
		result = SimpleJSONTestFunction("-Infinity\t\x01\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_748(self):
		result = SimpleJSONTestFunction("\n-@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_749(self):
		result = SimpleJSONTestFunction("\"  !\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_750(self):
		result = SimpleJSONTestFunction("\"  \"\t\t\x10\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_751(self):
		result = SimpleJSONTestFunction("\t\n\n\t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_752(self):
		result = SimpleJSONTestFunction("\"   1\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_753(self):
		result = SimpleJSONTestFunction("\n0\t\x02\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\n")
		self.assertEqual(result, expected_result)

	def test_754(self):
		result = SimpleJSONTestFunction("\"  \" \x04\x00\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_755(self):
		result = SimpleJSONTestFunction("\n0E-0\x00\x00\x00\x00\x00\x00\n\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_756(self):
		result = SimpleJSONTestFunction("\n0E-0\x00\n\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_757(self):
		result = SimpleJSONTestFunction("\t\t\t\n\t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_758(self):
		result = SimpleJSONTestFunction("\n0 \x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_759(self):
		result = SimpleJSONTestFunction("\t\t\t \t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_760(self):
		result = SimpleJSONTestFunction("\t\t\t\n\t\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_761(self):
		result = SimpleJSONTestFunction("\t0E-0\x00\x00\x00\n\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_762(self):
		result = SimpleJSONTestFunction("-Infinity\n\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_763(self):
		result = SimpleJSONTestFunction("\"  \" \x02\x00\x00\x00\x00\n\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_764(self):
		result = SimpleJSONTestFunction("\n-\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_765(self):
		result = SimpleJSONTestFunction("\x0F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_766(self):
		result = SimpleJSONTestFunction(" \t\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_767(self):
		result = SimpleJSONTestFunction("\n\t\t0.\x00\x00\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_768(self):
		result = SimpleJSONTestFunction("\t\t\x16\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_769(self):
		result = SimpleJSONTestFunction("\"   !\x00\t\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_770(self):
		result = SimpleJSONTestFunction("\"  \"\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_771(self):
		result = SimpleJSONTestFunction("\n0E-0\x00\n\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_772(self):
		result = SimpleJSONTestFunction("-Infinity\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_773(self):
		result = SimpleJSONTestFunction("-0\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_774(self):
		result = SimpleJSONTestFunction("\"  \"\n\t\x10\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_775(self):
		result = SimpleJSONTestFunction("\n0E-0\x00\x00\x00\x00\x00\n\n\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_776(self):
		result = SimpleJSONTestFunction("\t \t \x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_777(self):
		result = SimpleJSONTestFunction("\"  \"\t\n\x10\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_778(self):
		result = SimpleJSONTestFunction("\t0\t\t\n\x11\x00\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_779(self):
		result = SimpleJSONTestFunction("\n\"\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_780(self):
		result = SimpleJSONTestFunction("\"  \"@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_781(self):
		result = SimpleJSONTestFunction("\n\t \x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_782(self):
		result = SimpleJSONTestFunction("\"  \" \t\x10\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_783(self):
		result = SimpleJSONTestFunction("\t\"\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_784(self):
		result = SimpleJSONTestFunction("\n0E-0\x00\n\x00\n\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_785(self):
		result = SimpleJSONTestFunction("\n\"\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_786(self):
		result = SimpleJSONTestFunction("\t\t\t\t\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_787(self):
		result = SimpleJSONTestFunction("\"   \"\x00\x00\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_788(self):
		result = SimpleJSONTestFunction("\x0C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_789(self):
		result = SimpleJSONTestFunction("\"  \" \x11\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_790(self):
		result = SimpleJSONTestFunction("\t\t:\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_791(self):
		result = SimpleJSONTestFunction("\n\"\x01\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_792(self):
		result = SimpleJSONTestFunction("-Infinity\n\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_793(self):
		result = SimpleJSONTestFunction("\"  \" \x05\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_794(self):
		result = SimpleJSONTestFunction("\"  \" \x03\x00\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_795(self):
		result = SimpleJSONTestFunction("\"  \"\n\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_796(self):
		result = SimpleJSONTestFunction("-Infinity\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_797(self):
		result = SimpleJSONTestFunction("\t 0 \x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_798(self):
		result = SimpleJSONTestFunction("\"  \" \t \x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_799(self):
		result = SimpleJSONTestFunction("-Infinity\n\x00\n\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_800(self):
		result = SimpleJSONTestFunction("-Infinity\x11\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_801(self):
		result = SimpleJSONTestFunction("\t0\t\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_802(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\n\t\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_803(self):
		result = SimpleJSONTestFunction("-9\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_804(self):
		result = SimpleJSONTestFunction("\"  \" \x12\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_805(self):
		result = SimpleJSONTestFunction("-Infinity\n\x00\n\n\x00\n")
		self.assertEqual(result, expected_result)

	def test_806(self):
		result = SimpleJSONTestFunction("\t\t\n0.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_807(self):
		result = SimpleJSONTestFunction("-Infinity\n\x01\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_808(self):
		result = SimpleJSONTestFunction("\n0\t\x02\x00\x00\x00\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_809(self):
		result = SimpleJSONTestFunction("\t\n\t0\x10\n\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_810(self):
		result = SimpleJSONTestFunction("\"  \"\n\x0F\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_811(self):
		result = SimpleJSONTestFunction("\t0\n\x00\x00\x00\x00\n\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_812(self):
		result = SimpleJSONTestFunction("\"  0\x00\t\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_813(self):
		result = SimpleJSONTestFunction("\"  \" \x03\x00\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_814(self):
		result = SimpleJSONTestFunction("\t\t\t\t\t\t\x01\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_815(self):
		result = SimpleJSONTestFunction("\x0B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_816(self):
		result = SimpleJSONTestFunction("\t0E-0\x00\x00\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_817(self):
		result = SimpleJSONTestFunction("\t0\t\t\x04\x00\n\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_818(self):
		result = SimpleJSONTestFunction("\"   \"\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_819(self):
		result = SimpleJSONTestFunction("\"  \"\n\x0C\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_820(self):
		result = SimpleJSONTestFunction("\"  \n \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_821(self):
		result = SimpleJSONTestFunction("\"   1\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_822(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\t\t\x03\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_823(self):
		result = SimpleJSONTestFunction("\n0E-0\x00\x00\x00\x00\x00\x00\n\x00\n\n")
		self.assertEqual(result, expected_result)

	def test_824(self):
		result = SimpleJSONTestFunction("\n\"\x00\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_825(self):
		result = SimpleJSONTestFunction("\t0 \t\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_826(self):
		result = SimpleJSONTestFunction("-Infinity\t\t\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_827(self):
		result = SimpleJSONTestFunction("\"  \"\x04\x00\x00\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_828(self):
		result = SimpleJSONTestFunction("\t0\t\n\t\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_829(self):
		result = SimpleJSONTestFunction("\"  \"\n\n\x10\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_830(self):
		result = SimpleJSONTestFunction("\t\t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_831(self):
		result = SimpleJSONTestFunction("\"   \x01\\\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_832(self):
		result = SimpleJSONTestFunction("\"   1\n\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_833(self):
		result = SimpleJSONTestFunction("-Infinity\n\t\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_834(self):
		result = SimpleJSONTestFunction("-Infinity\n\t\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_835(self):
		result = SimpleJSONTestFunction("-Infinity\t\x10\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_836(self):
		result = SimpleJSONTestFunction("\"  \"\n\x0B\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_837(self):
		result = SimpleJSONTestFunction("\t0\t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_838(self):
		result = SimpleJSONTestFunction("\t 0 \t\t\t\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_839(self):
		result = SimpleJSONTestFunction("\"  !\x01 \x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_840(self):
		result = SimpleJSONTestFunction("\n\"\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_841(self):
		result = SimpleJSONTestFunction("\"   \"\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_842(self):
		result = SimpleJSONTestFunction("\t\n\t\t\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_843(self):
		result = SimpleJSONTestFunction("\t-0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_844(self):
		result = SimpleJSONTestFunction("-Infinity\x01\x00\n\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_845(self):
		result = SimpleJSONTestFunction("-Infinity\x00\n\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_846(self):
		result = SimpleJSONTestFunction("-Infinity\x02\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_847(self):
		result = SimpleJSONTestFunction("\n0\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_848(self):
		result = SimpleJSONTestFunction("\"\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_849(self):
		result = SimpleJSONTestFunction("-Infinity\t\x03\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_850(self):
		result = SimpleJSONTestFunction("\"  0\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_851(self):
		result = SimpleJSONTestFunction("\n0\t\t\t\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_852(self):
		result = SimpleJSONTestFunction("\t 0\t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_853(self):
		result = SimpleJSONTestFunction("\"  \"\n\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_854(self):
		result = SimpleJSONTestFunction("\"  0\n \x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_855(self):
		result = SimpleJSONTestFunction("\"  \"\n\x0E\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_856(self):
		result = SimpleJSONTestFunction("\n0E-0\x00\n\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_857(self):
		result = SimpleJSONTestFunction("\n\"\n\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_858(self):
		result = SimpleJSONTestFunction("\t0\n\x00\n\x00\x00\n\x00\n\x00\n\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_859(self):
		result = SimpleJSONTestFunction("\"  \" \t\x00\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_860(self):
		result = SimpleJSONTestFunction("\" 0\x10\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_861(self):
		result = SimpleJSONTestFunction("\t0e-\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_862(self):
		result = SimpleJSONTestFunction("\"  \" \t \x10\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_863(self):
		result = SimpleJSONTestFunction("\"  \"\t\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_864(self):
		result = SimpleJSONTestFunction("\t\"\n\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_865(self):
		result = SimpleJSONTestFunction("\t\"\n\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_866(self):
		result = SimpleJSONTestFunction("\" 0\x10\x0D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_867(self):
		result = SimpleJSONTestFunction("\t 0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_868(self):
		result = SimpleJSONTestFunction("\"\x01'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_869(self):
		result = SimpleJSONTestFunction("-0E\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_870(self):
		result = SimpleJSONTestFunction("\n0E-0\x00\n\x00\n\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_871(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_872(self):
		result = SimpleJSONTestFunction("7\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_873(self):
		result = SimpleJSONTestFunction("\n0E-0\x00\n\x00\n\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_874(self):
		result = SimpleJSONTestFunction("\"   \"\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_875(self):
		result = SimpleJSONTestFunction("\"  \" \x06\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_876(self):
		result = SimpleJSONTestFunction("-Infinity\n\x01\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_877(self):
		result = SimpleJSONTestFunction("\"  \" \n \x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_878(self):
		result = SimpleJSONTestFunction("\n0E-0\x00\x00\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_879(self):
		result = SimpleJSONTestFunction("-Infinity\n\x00\n\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_880(self):
		result = SimpleJSONTestFunction("\"\x10\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_881(self):
		result = SimpleJSONTestFunction("-Infinity\n\x10\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_882(self):
		result = SimpleJSONTestFunction("\t \t \x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_883(self):
		result = SimpleJSONTestFunction("\n0\t\x02\x00\x00\x00\x00\x00\n\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_884(self):
		result = SimpleJSONTestFunction("-Infinity\t\x10\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_885(self):
		result = SimpleJSONTestFunction("\"  \"\n\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_886(self):
		result = SimpleJSONTestFunction("\"  \"p\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_887(self):
		result = SimpleJSONTestFunction("\t \t0\t\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_888(self):
		result = SimpleJSONTestFunction("-Infinity\x03\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_889(self):
		result = SimpleJSONTestFunction("-Infinity\n\x01\n\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_890(self):
		result = SimpleJSONTestFunction("\"  \"\n\x01\x00\x00\n\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_891(self):
		result = SimpleJSONTestFunction("-Infinity\t\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_892(self):
		result = SimpleJSONTestFunction("\t0E-0\x00\x00\x00\n\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_893(self):
		result = SimpleJSONTestFunction("\n\t0\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_894(self):
		result = SimpleJSONTestFunction("\t\t1\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_895(self):
		result = SimpleJSONTestFunction("\"  \"\n\x01\x00\x00\n\x00\n\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_896(self):
		result = SimpleJSONTestFunction("-Infinity\n\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_897(self):
		result = SimpleJSONTestFunction("-Infinity\n\x02\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_898(self):
		result = SimpleJSONTestFunction("-Infinity1\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_899(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\t\x02\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_900(self):
		result = SimpleJSONTestFunction("-Infinity\n\x03\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_901(self):
		result = SimpleJSONTestFunction("-Infinity\x01\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_902(self):
		result = SimpleJSONTestFunction("-Infinity\n\x04\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_903(self):
		result = SimpleJSONTestFunction("\n0E-0\x00\x00\x00\x00\x00\x00\x00\x00\n\n")
		self.assertEqual(result, expected_result)

	def test_904(self):
		result = SimpleJSONTestFunction("\t 0 \t\t\t\t\x01\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_905(self):
		result = SimpleJSONTestFunction("\"   !\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_906(self):
		result = SimpleJSONTestFunction("\t\t\t\t\t\t\t\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_907(self):
		result = SimpleJSONTestFunction("\t\"\n'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_908(self):
		result = SimpleJSONTestFunction("\t\t\n0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_909(self):
		result = SimpleJSONTestFunction("\"   \"\t\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_910(self):
		result = SimpleJSONTestFunction("\t0e-\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_911(self):
		result = SimpleJSONTestFunction("\"    \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_912(self):
		result = SimpleJSONTestFunction("\"\x00\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_913(self):
		result = SimpleJSONTestFunction("\"  \n\x82\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_914(self):
		result = SimpleJSONTestFunction("\" 0 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_915(self):
		result = SimpleJSONTestFunction("\t0\n\t\t\x00\n\n\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_916(self):
		result = SimpleJSONTestFunction("\t\"\x01'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_917(self):
		result = SimpleJSONTestFunction("\n\"\x01 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_918(self):
		result = SimpleJSONTestFunction("\n0\t\t \t\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_919(self):
		result = SimpleJSONTestFunction("\"   0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_920(self):
		result = SimpleJSONTestFunction("\t\t\t \t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_921(self):
		result = SimpleJSONTestFunction("\n\t\x0B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_922(self):
		result = SimpleJSONTestFunction("4\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_923(self):
		result = SimpleJSONTestFunction("\"   0\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_924(self):
		result = SimpleJSONTestFunction("-Infinity\x10\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_925(self):
		result = SimpleJSONTestFunction("\"   1\x01\n\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_926(self):
		result = SimpleJSONTestFunction("\"  \"P\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_927(self):
		result = SimpleJSONTestFunction("\"  \"p\x00\x00\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_928(self):
		result = SimpleJSONTestFunction("\t\t\t\n\n\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_929(self):
		result = SimpleJSONTestFunction("-Infinity\n\x06\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_930(self):
		result = SimpleJSONTestFunction("\t  \t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_931(self):
		result = SimpleJSONTestFunction("\n\"\x04\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_932(self):
		result = SimpleJSONTestFunction("-Infinity\x11\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_933(self):
		result = SimpleJSONTestFunction("\t0E-0\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_934(self):
		result = SimpleJSONTestFunction("\t0 0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_935(self):
		result = SimpleJSONTestFunction("\n0E-0\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_936(self):
		result = SimpleJSONTestFunction("\t0\t\x0E\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_937(self):
		result = SimpleJSONTestFunction("\t\x17\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_938(self):
		result = SimpleJSONTestFunction("6\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_939(self):
		result = SimpleJSONTestFunction("-Infinity\x12\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_940(self):
		result = SimpleJSONTestFunction(" \x13\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_941(self):
		result = SimpleJSONTestFunction("\t0\t\n \x01\x00\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_942(self):
		result = SimpleJSONTestFunction("\t0E-0\x00\x00\x00\x00\x00\x00\n\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_943(self):
		result = SimpleJSONTestFunction("-0 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_944(self):
		result = SimpleJSONTestFunction("\n0E-0\x00\n\x00\n\x00\n\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_945(self):
		result = SimpleJSONTestFunction("\"  \"@\x00\x00\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_946(self):
		result = SimpleJSONTestFunction("-Infinity\x11\n\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_947(self):
		result = SimpleJSONTestFunction("\"   !\n\t\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_948(self):
		result = SimpleJSONTestFunction("\n\t\t\n\t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_949(self):
		result = SimpleJSONTestFunction("\"0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_950(self):
		result = SimpleJSONTestFunction("\"  \" \n \x10\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_951(self):
		result = SimpleJSONTestFunction("\"  \" \n\x00\x00\x00\n\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_952(self):
		result = SimpleJSONTestFunction("\t 0 \t\t\t\t\x02\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_953(self):
		result = SimpleJSONTestFunction("\t0E-0\x00\x00\x00\n\x00\n\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_954(self):
		result = SimpleJSONTestFunction("-Infinity\n\x05\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_955(self):
		result = SimpleJSONTestFunction("\n0E-0\x00\x00\x00\x00\x00\x00\n\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_956(self):
		result = SimpleJSONTestFunction("5\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_957(self):
		result = SimpleJSONTestFunction("\"  \" \x13\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_958(self):
		result = SimpleJSONTestFunction("\"  \"\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_959(self):
		result = SimpleJSONTestFunction("\n\"\n\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_960(self):
		result = SimpleJSONTestFunction("8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_961(self):
		result = SimpleJSONTestFunction("\n0E-0\x00\n\x00\x00\x00\x00\x00\n\n\x00")
		self.assertEqual(result, expected_result)

	def test_962(self):
		result = SimpleJSONTestFunction("\t\t \t\t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_963(self):
		result = SimpleJSONTestFunction("\"  \" \t \x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_964(self):
		result = SimpleJSONTestFunction("\" 0 \x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_965(self):
		result = SimpleJSONTestFunction("\"    \x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_966(self):
		result = SimpleJSONTestFunction("\"\x11\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_967(self):
		result = SimpleJSONTestFunction("\t \t0E\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_968(self):
		result = SimpleJSONTestFunction("\t0\t\t\n\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_969(self):
		result = SimpleJSONTestFunction("\t \n\t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_970(self):
		result = SimpleJSONTestFunction("\n\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_971(self):
		result = SimpleJSONTestFunction("\"  \"\t\n\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_972(self):
		result = SimpleJSONTestFunction("-0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_973(self):
		result = SimpleJSONTestFunction("\t\t \n\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_974(self):
		result = SimpleJSONTestFunction("-Infinity\t\t\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_975(self):
		result = SimpleJSONTestFunction("\"  \"`\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_976(self):
		result = SimpleJSONTestFunction("\t\t\t\n\t\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_977(self):
		result = SimpleJSONTestFunction("\"  \"\n\x04\x00\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_978(self):
		result = SimpleJSONTestFunction("\t0.\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_979(self):
		result = SimpleJSONTestFunction("\n0E-0\x00\n\x00\n\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_980(self):
		result = SimpleJSONTestFunction("\t\t\t \t\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_981(self):
		result = SimpleJSONTestFunction("\t-0.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_982(self):
		result = SimpleJSONTestFunction("\t0E-0\x00\x00\x00\n\x00\n\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_983(self):
		result = SimpleJSONTestFunction("\t\"\x01\x0D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_984(self):
		result = SimpleJSONTestFunction("\t\"\n\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_985(self):
		result = SimpleJSONTestFunction("\"   \"\x00\x00\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_986(self):
		result = SimpleJSONTestFunction("-Infinity\t\t\x03\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_987(self):
		result = SimpleJSONTestFunction("-Infinity\n\x04\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_988(self):
		result = SimpleJSONTestFunction("\"   1\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_989(self):
		result = SimpleJSONTestFunction("-Infinity\t\n\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_990(self):
		result = SimpleJSONTestFunction("\t0\t\t\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_991(self):
		result = SimpleJSONTestFunction("\"  \" \n\x10\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_992(self):
		result = SimpleJSONTestFunction("\"    \x11\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_993(self):
		result = SimpleJSONTestFunction("\"   \"\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_994(self):
		result = SimpleJSONTestFunction("-0 \x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_995(self):
		result = SimpleJSONTestFunction("\"  !\n\n\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_996(self):
		result = SimpleJSONTestFunction("\"   \"\t\x01\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_997(self):
		result = SimpleJSONTestFunction("-Infinity\n\x00\n\n\n\x00")
		self.assertEqual(result, expected_result)

	def test_998(self):
		result = SimpleJSONTestFunction("\"   \"\t\t\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_999(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\t\t\t\t\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1000(self):
		result = SimpleJSONTestFunction("\t-0.\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1001(self):
		result = SimpleJSONTestFunction("\t\n\t\t\t\t\x01\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1002(self):
		result = SimpleJSONTestFunction("-Infinity\n\x07\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1003(self):
		result = SimpleJSONTestFunction("\t0\t\t\n\x16\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1004(self):
		result = SimpleJSONTestFunction("-1\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1005(self):
		result = SimpleJSONTestFunction("\t \t0e\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1006(self):
		result = SimpleJSONTestFunction("\n\x0E\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1007(self):
		result = SimpleJSONTestFunction("\t\t\t\n\n\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1008(self):
		result = SimpleJSONTestFunction("\"  \" \n\x00\x00\x00\n\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1009(self):
		result = SimpleJSONTestFunction("-Infinity\x04\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1010(self):
		result = SimpleJSONTestFunction("\"   \"\n\x01\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1011(self):
		result = SimpleJSONTestFunction("\"   \"\x00\x00\x00\n\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1012(self):
		result = SimpleJSONTestFunction("\"  \"\t\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1013(self):
		result = SimpleJSONTestFunction("\"   \"\n\x02\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1014(self):
		result = SimpleJSONTestFunction("\"  0\x10\\\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1015(self):
		result = SimpleJSONTestFunction("\"   \"\t\t\x01\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1016(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\n\x05\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1017(self):
		result = SimpleJSONTestFunction("\"   \"\t\t\x02\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1018(self):
		result = SimpleJSONTestFunction("\t\t\t\n\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1019(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\t\t\t\t\x01\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1020(self):
		result = SimpleJSONTestFunction("\" 0\n\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1021(self):
		result = SimpleJSONTestFunction("\"  \x11\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1022(self):
		result = SimpleJSONTestFunction("\t0E-0\x00\x00\x00\x00\x00\x00\x00\n\x00\n")
		self.assertEqual(result, expected_result)

	def test_1023(self):
		result = SimpleJSONTestFunction("\t\"\x00'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1024(self):
		result = SimpleJSONTestFunction("\t0\t\t\n\x12\x00\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1025(self):
		result = SimpleJSONTestFunction("-Infinity\n\t\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1026(self):
		result = SimpleJSONTestFunction("\t \t\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1027(self):
		result = SimpleJSONTestFunction("\"  \"\n\x02\x00\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1028(self):
		result = SimpleJSONTestFunction("\"    \n\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1029(self):
		result = SimpleJSONTestFunction("\" 0 \n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1030(self):
		result = SimpleJSONTestFunction("-Infinity\n\n\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1031(self):
		result = SimpleJSONTestFunction("\t\t2\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1032(self):
		result = SimpleJSONTestFunction("\t0\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1033(self):
		result = SimpleJSONTestFunction("\t\"\x00\x0D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1034(self):
		result = SimpleJSONTestFunction("\"  \" \x07\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1035(self):
		result = SimpleJSONTestFunction("\t\t\t\t\t\t\t\x01\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1036(self):
		result = SimpleJSONTestFunction("\"0\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1037(self):
		result = SimpleJSONTestFunction("-Infinity\x06\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1038(self):
		result = SimpleJSONTestFunction("\"  \" \t\x10\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1039(self):
		result = SimpleJSONTestFunction("\"   0\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1040(self):
		result = SimpleJSONTestFunction("\"   \"\x10\x00\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1041(self):
		result = SimpleJSONTestFunction("\"   \"\n\x03\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1042(self):
		result = SimpleJSONTestFunction("\t\t\t\n\t\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1043(self):
		result = SimpleJSONTestFunction("-Infinity\x13\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1044(self):
		result = SimpleJSONTestFunction("\t0\t\n\t\x16\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1045(self):
		result = SimpleJSONTestFunction("\t \t0\t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1046(self):
		result = SimpleJSONTestFunction("-1\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1047(self):
		result = SimpleJSONTestFunction("-Infinity\x13\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1048(self):
		result = SimpleJSONTestFunction("\t\t\t\t\t\n\t\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1049(self):
		result = SimpleJSONTestFunction("\"  \"\n\x04\x00\x00\x00\x00\n\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1050(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\t\x06\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1051(self):
		result = SimpleJSONTestFunction("\t0\n\t\t\t\x00\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1052(self):
		result = SimpleJSONTestFunction("-Infinity\t\n\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1053(self):
		result = SimpleJSONTestFunction("\"  \" \t \x01\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1054(self):
		result = SimpleJSONTestFunction("\"   !\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1055(self):
		result = SimpleJSONTestFunction("\"  \" \n\x10\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1056(self):
		result = SimpleJSONTestFunction("\n0\t\t\t\t\t\t\x01\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1057(self):
		result = SimpleJSONTestFunction("\"   \n\t\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1058(self):
		result = SimpleJSONTestFunction("\t  \t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1059(self):
		result = SimpleJSONTestFunction("\n0E-0\x00\n\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1060(self):
		result = SimpleJSONTestFunction("-Infinity\t\t\x02\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1061(self):
		result = SimpleJSONTestFunction("\t0\n\t\t\x11\x00\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1062(self):
		result = SimpleJSONTestFunction("-Infinity\x1B\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1063(self):
		result = SimpleJSONTestFunction("\"  \"P\x00\x00\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1064(self):
		result = SimpleJSONTestFunction("\"  \"@\x00\x00\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1065(self):
		result = SimpleJSONTestFunction("-Infinity\t\t\t\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1066(self):
		result = SimpleJSONTestFunction("\n\t3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1067(self):
		result = SimpleJSONTestFunction("\"   \"\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1068(self):
		result = SimpleJSONTestFunction("\n\"\n\\\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1069(self):
		result = SimpleJSONTestFunction("\"  \"\n\x05\x00\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1070(self):
		result = SimpleJSONTestFunction("\"  0\n\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1071(self):
		result = SimpleJSONTestFunction("-Infinity\n\n\x02\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1072(self):
		result = SimpleJSONTestFunction("-Infinity\t\x02\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1073(self):
		result = SimpleJSONTestFunction("\"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1074(self):
		result = SimpleJSONTestFunction("-0 \x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1075(self):
		result = SimpleJSONTestFunction("-Infinity\x12\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1076(self):
		result = SimpleJSONTestFunction("-Infinity\x12\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1077(self):
		result = SimpleJSONTestFunction("\" 0 \n\\\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1078(self):
		result = SimpleJSONTestFunction("\t \t0\t\t\x01\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1079(self):
		result = SimpleJSONTestFunction("\n\t \x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1080(self):
		result = SimpleJSONTestFunction("\t \t0e-\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1081(self):
		result = SimpleJSONTestFunction("\"\x10\\\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1082(self):
		result = SimpleJSONTestFunction("-Infinity\x17\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1083(self):
		result = SimpleJSONTestFunction("\t\"\x01 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1084(self):
		result = SimpleJSONTestFunction("\t \t0e\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1085(self):
		result = SimpleJSONTestFunction("\t\t \t\t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1086(self):
		result = SimpleJSONTestFunction("\"   $\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1087(self):
		result = SimpleJSONTestFunction("\t \t\n\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1088(self):
		result = SimpleJSONTestFunction("-Infinity\t\t\t\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1089(self):
		result = SimpleJSONTestFunction("-Infinity\x11\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1090(self):
		result = SimpleJSONTestFunction("\t\t\n\t\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1091(self):
		result = SimpleJSONTestFunction("\"  \"\n\x04\x00\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1092(self):
		result = SimpleJSONTestFunction("\n0E-0\x00\n\x00\n\n\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1093(self):
		result = SimpleJSONTestFunction("-Infinity\t\t\x07\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1094(self):
		result = SimpleJSONTestFunction("-Infinity\n\t\t\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1095(self):
		result = SimpleJSONTestFunction("\t \t0\t\t\x11\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1096(self):
		result = SimpleJSONTestFunction("\"  \" \x11\x00\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1097(self):
		result = SimpleJSONTestFunction("-Infinity\t\t\t\t\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1098(self):
		result = SimpleJSONTestFunction("\"  \"\n\n\x10\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1099(self):
		result = SimpleJSONTestFunction("\t\t\t\n\x16\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1100(self):
		result = SimpleJSONTestFunction("\t\t@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1101(self):
		result = SimpleJSONTestFunction("-Infinity\t\t\t\t\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1102(self):
		result = SimpleJSONTestFunction("\"\x11'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1103(self):
		result = SimpleJSONTestFunction("\t \t0.\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1104(self):
		result = SimpleJSONTestFunction("-Infinity\t\t\t\t\x03\x00")
		self.assertEqual(result, expected_result)

	def test_1105(self):
		result = SimpleJSONTestFunction("\n0E-0\x00\n\x00\n\x00\x00\x00\x00\n\n")
		self.assertEqual(result, expected_result)

	def test_1106(self):
		result = SimpleJSONTestFunction("\"   \"\t\t\t\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1107(self):
		result = SimpleJSONTestFunction("\"   0\n\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1108(self):
		result = SimpleJSONTestFunction("\t\t0\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1109(self):
		result = SimpleJSONTestFunction("-Infinity\t\x04\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1110(self):
		result = SimpleJSONTestFunction("\t \t0e+\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1111(self):
		result = SimpleJSONTestFunction("\t \n \x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1112(self):
		result = SimpleJSONTestFunction("\t0E-0\x01\x00\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1113(self):
		result = SimpleJSONTestFunction("\"  \"\n\x04\x00\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1114(self):
		result = SimpleJSONTestFunction("-Infinity\t\t\t\t\t\x00")
		self.assertEqual(result, expected_result)

	def test_1115(self):
		result = SimpleJSONTestFunction("-3\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1116(self):
		result = SimpleJSONTestFunction("\t0\n\t\t\t\x03\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1117(self):
		result = SimpleJSONTestFunction("\"   \"\t\t\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1118(self):
		result = SimpleJSONTestFunction("\"   \"\n\x01\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1119(self):
		result = SimpleJSONTestFunction("\t\t\t\n\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1120(self):
		result = SimpleJSONTestFunction("\t0 \t\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1121(self):
		result = SimpleJSONTestFunction("\"\x00\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1122(self):
		result = SimpleJSONTestFunction("-Infinity\n\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1123(self):
		result = SimpleJSONTestFunction("\t\t\t\t\t\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1124(self):
		result = SimpleJSONTestFunction("-Infinity\t\t\n\t\t\x00")
		self.assertEqual(result, expected_result)

	def test_1125(self):
		result = SimpleJSONTestFunction("\"  \"\n\x04\x00\x00\x00\x00\x00\x00\n\x00\n")
		self.assertEqual(result, expected_result)

	def test_1126(self):
		result = SimpleJSONTestFunction("-Infinity\t\x11\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1127(self):
		result = SimpleJSONTestFunction("\t0\t\n \x02\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1128(self):
		result = SimpleJSONTestFunction("\n0\t\x06\n\x00\n\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1129(self):
		result = SimpleJSONTestFunction("\t\t6\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1130(self):
		result = SimpleJSONTestFunction("\"0\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1131(self):
		result = SimpleJSONTestFunction("-Infinity\t\x05\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1132(self):
		result = SimpleJSONTestFunction("-Infinity\x14\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1133(self):
		result = SimpleJSONTestFunction("\"0\n\x0D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1134(self):
		result = SimpleJSONTestFunction("\"  \"\n\n\x10\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1135(self):
		result = SimpleJSONTestFunction("\"  \" \t\x01\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1136(self):
		result = SimpleJSONTestFunction("\"   \"\n\x04\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1137(self):
		result = SimpleJSONTestFunction("\"   \"\n\x05\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1138(self):
		result = SimpleJSONTestFunction("\"  \" \x0F\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1139(self):
		result = SimpleJSONTestFunction("\"  \"\n\x06\x00\x00\n\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1140(self):
		result = SimpleJSONTestFunction("\n\t\t\t\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1141(self):
		result = SimpleJSONTestFunction("\t0\t\n \t\x0B\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1142(self):
		result = SimpleJSONTestFunction("\t0\xA0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1143(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\n\x08\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1144(self):
		result = SimpleJSONTestFunction("\n\"\n \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1145(self):
		result = SimpleJSONTestFunction("\"  \"\t\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1146(self):
		result = SimpleJSONTestFunction("\"  \"\t\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1147(self):
		result = SimpleJSONTestFunction("\"  \" \n\x00\x00\x00\n\x00\n\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1148(self):
		result = SimpleJSONTestFunction("\t \t0\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1149(self):
		result = SimpleJSONTestFunction("\n0E-0\x00\x00\n\x00\x00\x00\x00\x00\n\n")
		self.assertEqual(result, expected_result)

	def test_1150(self):
		result = SimpleJSONTestFunction("-Infinity\n\x11\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1151(self):
		result = SimpleJSONTestFunction("-0.\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1152(self):
		result = SimpleJSONTestFunction("\t0\t\n\t\x18\x00\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1153(self):
		result = SimpleJSONTestFunction("\n\"\x01\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1154(self):
		result = SimpleJSONTestFunction("-Infinity\x00\n\n\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1155(self):
		result = SimpleJSONTestFunction("\"  \"\n\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1156(self):
		result = SimpleJSONTestFunction("-Infinity\t\n\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1157(self):
		result = SimpleJSONTestFunction("9\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1158(self):
		result = SimpleJSONTestFunction("\"  \"\t\x11\x00\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1159(self):
		result = SimpleJSONTestFunction("\"   \"\t\n\x01\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1160(self):
		result = SimpleJSONTestFunction("-3\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1161(self):
		result = SimpleJSONTestFunction("\t\t\t\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1162(self):
		result = SimpleJSONTestFunction("\n0E+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1163(self):
		result = SimpleJSONTestFunction("\n0E-0\x00\x00\x00\x00\x00\x00\n\n\n\x00")
		self.assertEqual(result, expected_result)

	def test_1164(self):
		result = SimpleJSONTestFunction("\"  !\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1165(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1166(self):
		result = SimpleJSONTestFunction("9\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1167(self):
		result = SimpleJSONTestFunction(" \t\t\t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1168(self):
		result = SimpleJSONTestFunction("-2\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1169(self):
		result = SimpleJSONTestFunction("\"  \"\n\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1170(self):
		result = SimpleJSONTestFunction("\t \t0\t\t\t\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1171(self):
		result = SimpleJSONTestFunction("\"   \"\n\x05\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1172(self):
		result = SimpleJSONTestFunction("-0 \x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1173(self):
		result = SimpleJSONTestFunction("\"   \"\t\t\t\x01\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1174(self):
		result = SimpleJSONTestFunction("\"   \"\n\x06\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1175(self):
		result = SimpleJSONTestFunction("-Infinity\t\t\t\t\t\x10")
		self.assertEqual(result, expected_result)

	def test_1176(self):
		result = SimpleJSONTestFunction("\"  \" \t \t\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1177(self):
		result = SimpleJSONTestFunction("\t0 \x02\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1178(self):
		result = SimpleJSONTestFunction("-Infinity\t\t\t\t\t\x01")
		self.assertEqual(result, expected_result)

	def test_1179(self):
		result = SimpleJSONTestFunction("-Infinity\t\x10\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1180(self):
		result = SimpleJSONTestFunction("\t\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1181(self):
		result = SimpleJSONTestFunction("\"  ( \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1182(self):
		result = SimpleJSONTestFunction("-Infinity\x11\n\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1183(self):
		result = SimpleJSONTestFunction("\"  \"\n\t\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1184(self):
		result = SimpleJSONTestFunction("\t0E-0\x00\x00\x00\n\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1185(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\x17\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1186(self):
		result = SimpleJSONTestFunction("\t\"\x00\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1187(self):
		result = SimpleJSONTestFunction("\"   0\n\x01\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1188(self):
		result = SimpleJSONTestFunction("-Infinity\t\t\t\t\x02\x00")
		self.assertEqual(result, expected_result)

	def test_1189(self):
		result = SimpleJSONTestFunction("\t\n \t\t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1190(self):
		result = SimpleJSONTestFunction("-Infinity\t\t\t\t\n\x00")
		self.assertEqual(result, expected_result)

	def test_1191(self):
		result = SimpleJSONTestFunction("-Infinity\t\t\t\t\t\x11")
		self.assertEqual(result, expected_result)

	def test_1192(self):
		result = SimpleJSONTestFunction("\"  \"\t\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1193(self):
		result = SimpleJSONTestFunction("-Infinity\n\n\x02\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1194(self):
		result = SimpleJSONTestFunction("\"  \" \x05\n\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1195(self):
		result = SimpleJSONTestFunction("\t0E-0\x01\x00\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1196(self):
		result = SimpleJSONTestFunction("\t\"\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1197(self):
		result = SimpleJSONTestFunction("\t0\n\t0\x00\n\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1198(self):
		result = SimpleJSONTestFunction("-Infinity\n\x05\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1199(self):
		result = SimpleJSONTestFunction("\t0E-0\x00\x00\x00\x00\x00\n\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1200(self):
		result = SimpleJSONTestFunction("\t \n \x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1201(self):
		result = SimpleJSONTestFunction("\t0\t\n \x03\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1202(self):
		result = SimpleJSONTestFunction("\t0E-0\x00\x00\x00\n\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1203(self):
		result = SimpleJSONTestFunction("\t0\t\n\t\x18\x00\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1204(self):
		result = SimpleJSONTestFunction("\"  \"\x02\x00\x00\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1205(self):
		result = SimpleJSONTestFunction("\"  \"\n\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1206(self):
		result = SimpleJSONTestFunction("\"   \"\t\x00\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1207(self):
		result = SimpleJSONTestFunction("\t\t7\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1208(self):
		result = SimpleJSONTestFunction("\"   0\x01 \x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1209(self):
		result = SimpleJSONTestFunction("\n\"\x00\x0D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1210(self):
		result = SimpleJSONTestFunction("\"  \"\x03\x00\x00\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1211(self):
		result = SimpleJSONTestFunction("\n0E-0\x01\x00\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1212(self):
		result = SimpleJSONTestFunction("\"  \x10\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1213(self):
		result = SimpleJSONTestFunction("\t\n\t \x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1214(self):
		result = SimpleJSONTestFunction("1\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1215(self):
		result = SimpleJSONTestFunction("\t\t0E\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1216(self):
		result = SimpleJSONTestFunction("\"  \"\x00\x00\x00\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1217(self):
		result = SimpleJSONTestFunction("-Infinity\n\t\t\x02\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1218(self):
		result = SimpleJSONTestFunction("\t0\n\t\t\t\t\t\t\x01\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1219(self):
		result = SimpleJSONTestFunction("\t\n \t\t\n\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1220(self):
		result = SimpleJSONTestFunction("\"   \"\t\x11\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1221(self):
		result = SimpleJSONTestFunction("\"   \"\t\n\t\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1222(self):
		result = SimpleJSONTestFunction("-Infinity\n\x01\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1223(self):
		result = SimpleJSONTestFunction("-Infinity \x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1224(self):
		result = SimpleJSONTestFunction("-Infinity\t\t\x03\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1225(self):
		result = SimpleJSONTestFunction("\"   \"\t\x12\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1226(self):
		result = SimpleJSONTestFunction("\n\"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1227(self):
		result = SimpleJSONTestFunction("\t \t0e0\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1228(self):
		result = SimpleJSONTestFunction("\"   !\x11'\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1229(self):
		result = SimpleJSONTestFunction("\t 0 \x10\x00\x00\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1230(self):
		result = SimpleJSONTestFunction("\t0\t\t \t\x02\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1231(self):
		result = SimpleJSONTestFunction("-Infinity\n\x12\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1232(self):
		result = SimpleJSONTestFunction("\t \n0e0\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1233(self):
		result = SimpleJSONTestFunction("\"  \"\n\x07\n\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1234(self):
		result = SimpleJSONTestFunction("-Infinity\x13\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1235(self):
		result = SimpleJSONTestFunction("\n\"\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1236(self):
		result = SimpleJSONTestFunction("-Infinity\n\x12\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1237(self):
		result = SimpleJSONTestFunction("\"  \"\n\x0C\x00\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1238(self):
		result = SimpleJSONTestFunction("\t\t0\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1239(self):
		result = SimpleJSONTestFunction("\n\"\x11 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1240(self):
		result = SimpleJSONTestFunction("\t0 \t\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1241(self):
		result = SimpleJSONTestFunction("\"@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1242(self):
		result = SimpleJSONTestFunction("-Infinity\t\t\t\t\t\x13")
		self.assertEqual(result, expected_result)

	def test_1243(self):
		result = SimpleJSONTestFunction("\t \t0\n\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1244(self):
		result = SimpleJSONTestFunction("\"    \x11\x0D\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1245(self):
		result = SimpleJSONTestFunction("\t\"\n\x0D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1246(self):
		result = SimpleJSONTestFunction("\t \t0\n\t\x01\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1247(self):
		result = SimpleJSONTestFunction("\t0\t\t\n\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1248(self):
		result = SimpleJSONTestFunction("\t  \t\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1249(self):
		result = SimpleJSONTestFunction("\t\n:\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1250(self):
		result = SimpleJSONTestFunction("-Infinity\x14\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1251(self):
		result = SimpleJSONTestFunction("-Infinity\t\t\t\t\x10\x00")
		self.assertEqual(result, expected_result)

	def test_1252(self):
		result = SimpleJSONTestFunction("-Infinity\x01\x00\n\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1253(self):
		result = SimpleJSONTestFunction("\"  \"\t\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1254(self):
		result = SimpleJSONTestFunction("\n \t0e0\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1255(self):
		result = SimpleJSONTestFunction("-Infinity\n\x03\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1256(self):
		result = SimpleJSONTestFunction("\"  ! \x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1257(self):
		result = SimpleJSONTestFunction("\t \t0\t\t\t\x01\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1258(self):
		result = SimpleJSONTestFunction("\t\t\t\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1259(self):
		result = SimpleJSONTestFunction("\n\t4\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1260(self):
		result = SimpleJSONTestFunction("\t0\t\n \t\x04\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1261(self):
		result = SimpleJSONTestFunction("\t0\n\t\t\x13\x00\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1262(self):
		result = SimpleJSONTestFunction(" \t\t\t\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1263(self):
		result = SimpleJSONTestFunction("\t0E-0\x01\x00\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1264(self):
		result = SimpleJSONTestFunction("\n0E-0\x00\x00\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1265(self):
		result = SimpleJSONTestFunction("\"  \" \t \n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1266(self):
		result = SimpleJSONTestFunction("\"  ! \n\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1267(self):
		result = SimpleJSONTestFunction("\t\xB0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1268(self):
		result = SimpleJSONTestFunction("\t0E-0\x00\x00\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1269(self):
		result = SimpleJSONTestFunction("\n \n0e0\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1270(self):
		result = SimpleJSONTestFunction("\n \t \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1271(self):
		result = SimpleJSONTestFunction("\"  \" \x07\n\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1272(self):
		result = SimpleJSONTestFunction("-Infinity\x06\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1273(self):
		result = SimpleJSONTestFunction("\t\"\n \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1274(self):
		result = SimpleJSONTestFunction("\t\t\n\t\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1275(self):
		result = SimpleJSONTestFunction("\"   1\n\\\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1276(self):
		result = SimpleJSONTestFunction("\"  !\n'\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1277(self):
		result = SimpleJSONTestFunction("\t0\n\x00\n\x00\x00\n\x00\n\x00\n\x00\n\n")
		self.assertEqual(result, expected_result)

	def test_1278(self):
		result = SimpleJSONTestFunction("\"  \" \x11\x00\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1279(self):
		result = SimpleJSONTestFunction("\t0\x15\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1280(self):
		result = SimpleJSONTestFunction("-Infinity\t\t\t\x03\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1281(self):
		result = SimpleJSONTestFunction("\"   \"\n\t\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1282(self):
		result = SimpleJSONTestFunction("\t\t0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1283(self):
		result = SimpleJSONTestFunction("\n\t5\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1284(self):
		result = SimpleJSONTestFunction("\"  \"\n\x05\x00\x00\x00\n\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1285(self):
		result = SimpleJSONTestFunction("-Infinity\n\t\t\x03\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1286(self):
		result = SimpleJSONTestFunction("\"@\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1287(self):
		result = SimpleJSONTestFunction("-Infinity\t\t\x02\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1288(self):
		result = SimpleJSONTestFunction("\t0E-0\x00\x00\x00\x00\n\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1289(self):
		result = SimpleJSONTestFunction("-Infinity\x04\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1290(self):
		result = SimpleJSONTestFunction("\t0\t\x17\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1291(self):
		result = SimpleJSONTestFunction("\t\n\t\t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1292(self):
		result = SimpleJSONTestFunction("\t 0 \t\t\t\t\x03\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1293(self):
		result = SimpleJSONTestFunction("\"  \" \t \x01\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1294(self):
		result = SimpleJSONTestFunction("-Infinity\t\t\t\t\x06\x00")
		self.assertEqual(result, expected_result)

	def test_1295(self):
		result = SimpleJSONTestFunction("\t\t\n\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1296(self):
		result = SimpleJSONTestFunction("\"@\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1297(self):
		result = SimpleJSONTestFunction(" \t\t\t\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1298(self):
		result = SimpleJSONTestFunction("\t0\x10\x00\x00\x00\x00\x00\x00\x00\x00\n\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1299(self):
		result = SimpleJSONTestFunction("\" @\x01\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1300(self):
		result = SimpleJSONTestFunction("\n0E-0\x01\x00\n\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1301(self):
		result = SimpleJSONTestFunction("-Infinity\x16\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1302(self):
		result = SimpleJSONTestFunction("-Infinity\t\x12\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1303(self):
		result = SimpleJSONTestFunction("-Infinity\t\t\t\t\t\t")
		self.assertEqual(result, expected_result)

	def test_1304(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\n\x0F\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1305(self):
		result = SimpleJSONTestFunction("\n\t5\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1306(self):
		result = SimpleJSONTestFunction("\n \t0\t\t\x11\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1307(self):
		result = SimpleJSONTestFunction("\"   \"\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1308(self):
		result = SimpleJSONTestFunction("\" \n\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1309(self):
		result = SimpleJSONTestFunction(" \t\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1310(self):
		result = SimpleJSONTestFunction("\t \t0e0\x00\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1311(self):
		result = SimpleJSONTestFunction("\t\t9\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1312(self):
		result = SimpleJSONTestFunction("\t\t\t\n\t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1313(self):
		result = SimpleJSONTestFunction("\"  \"\t\t\x01\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1314(self):
		result = SimpleJSONTestFunction("\"  \"\t\x1B\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1315(self):
		result = SimpleJSONTestFunction("-Infinity\n\t\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1316(self):
		result = SimpleJSONTestFunction("\n0\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1317(self):
		result = SimpleJSONTestFunction("-4\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1318(self):
		result = SimpleJSONTestFunction("-Infinity\n\x0F\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1319(self):
		result = SimpleJSONTestFunction("\t0\t\n \x04\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1320(self):
		result = SimpleJSONTestFunction("\t\n\n0.\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1321(self):
		result = SimpleJSONTestFunction("\"  0\n\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1322(self):
		result = SimpleJSONTestFunction("\" @\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1323(self):
		result = SimpleJSONTestFunction("\t\t\n\t\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1324(self):
		result = SimpleJSONTestFunction("\t \n0\t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1325(self):
		result = SimpleJSONTestFunction("\"\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1326(self):
		result = SimpleJSONTestFunction("\"  \n\x90\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1327(self):
		result = SimpleJSONTestFunction("\t  \t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1328(self):
		result = SimpleJSONTestFunction("\"@\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1329(self):
		result = SimpleJSONTestFunction("\t \n0e0\x00\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1330(self):
		result = SimpleJSONTestFunction("\"   \"\t\n\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1331(self):
		result = SimpleJSONTestFunction("-Infinity\x05\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1332(self):
		result = SimpleJSONTestFunction("\"   \"\n\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1333(self):
		result = SimpleJSONTestFunction("-Infinity\n\n\t\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1334(self):
		result = SimpleJSONTestFunction("\"  \"\t\t\x02\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1335(self):
		result = SimpleJSONTestFunction("-Infinity\n\n\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1336(self):
		result = SimpleJSONTestFunction("\"  \"\t\n\x00\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1337(self):
		result = SimpleJSONTestFunction("\"   \"\t\t\x03\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1338(self):
		result = SimpleJSONTestFunction("-1\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1339(self):
		result = SimpleJSONTestFunction("\t\t\t0.\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1340(self):
		result = SimpleJSONTestFunction("\t0\t\t\n\x12\x00\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1341(self):
		result = SimpleJSONTestFunction("\t\n\t\t\t\t\x02\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1342(self):
		result = SimpleJSONTestFunction("\"  \x10'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1343(self):
		result = SimpleJSONTestFunction("-Infinity\t\t\x03\n\x00\n")
		self.assertEqual(result, expected_result)

	def test_1344(self):
		result = SimpleJSONTestFunction("\t \t \x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1345(self):
		result = SimpleJSONTestFunction("\t0E-0\x00\x00\x00\x00\x00\x00\n\n\n\x00")
		self.assertEqual(result, expected_result)

	def test_1346(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\t\t\t\x03\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1347(self):
		result = SimpleJSONTestFunction("\t0E-0\x00\x00\x00\x00\n\x00\x00\n\n\x00")
		self.assertEqual(result, expected_result)

	def test_1348(self):
		result = SimpleJSONTestFunction("\"  \" \n \t\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1349(self):
		result = SimpleJSONTestFunction("\t \t \x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1350(self):
		result = SimpleJSONTestFunction("\n\t\t0\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1351(self):
		result = SimpleJSONTestFunction("\t\t\t \t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1352(self):
		result = SimpleJSONTestFunction("\n\t\t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1353(self):
		result = SimpleJSONTestFunction("\t \t\t\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1354(self):
		result = SimpleJSONTestFunction("-2\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1355(self):
		result = SimpleJSONTestFunction("\n0\t\x04\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1356(self):
		result = SimpleJSONTestFunction("-0 \x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1357(self):
		result = SimpleJSONTestFunction("-Infinity\x04\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1358(self):
		result = SimpleJSONTestFunction("\n\"\x01\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1359(self):
		result = SimpleJSONTestFunction("\t\t\n\t\t\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1360(self):
		result = SimpleJSONTestFunction("\"  \" \n\x10\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1361(self):
		result = SimpleJSONTestFunction("\t0E-0\x01\x00\n\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1362(self):
		result = SimpleJSONTestFunction("\t\n\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1363(self):
		result = SimpleJSONTestFunction("\" 0\x00\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1364(self):
		result = SimpleJSONTestFunction("2\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1365(self):
		result = SimpleJSONTestFunction("-Infinity\n\t\t\x03\x00\n")
		self.assertEqual(result, expected_result)

	def test_1366(self):
		result = SimpleJSONTestFunction("-4\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1367(self):
		result = SimpleJSONTestFunction("\"  \"\t\t\x02\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1368(self):
		result = SimpleJSONTestFunction("-Infinity\n\x00\n\n\n\n")
		self.assertEqual(result, expected_result)

	def test_1369(self):
		result = SimpleJSONTestFunction("\t 0\t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1370(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\n\x06\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1371(self):
		result = SimpleJSONTestFunction("\n\t \t\t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1372(self):
		result = SimpleJSONTestFunction("\"   \"\x00\x00\x00\n\x00\x00\n\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1373(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\t\x07\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1374(self):
		result = SimpleJSONTestFunction("\t\t\t \t\t\x01\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1375(self):
		result = SimpleJSONTestFunction("-Infinity\n\x00\n\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1376(self):
		result = SimpleJSONTestFunction("\"   \"\n\x07\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1377(self):
		result = SimpleJSONTestFunction("-0\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1378(self):
		result = SimpleJSONTestFunction("-Infinity\n\x13\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1379(self):
		result = SimpleJSONTestFunction("\n \t\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1380(self):
		result = SimpleJSONTestFunction("\"  \"\t\t\t\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1381(self):
		result = SimpleJSONTestFunction("\t0E-0\x01\x00\n\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1382(self):
		result = SimpleJSONTestFunction("\t0\x16\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1383(self):
		result = SimpleJSONTestFunction("\" 0 \n\n\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1384(self):
		result = SimpleJSONTestFunction("\t0 \x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1385(self):
		result = SimpleJSONTestFunction("\"   0\x01\n\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1386(self):
		result = SimpleJSONTestFunction("\t \t0E\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1387(self):
		result = SimpleJSONTestFunction("\"  \"\t\t\x03\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1388(self):
		result = SimpleJSONTestFunction("-Infinity \x01\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1389(self):
		result = SimpleJSONTestFunction("\t\t\n\t\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1390(self):
		result = SimpleJSONTestFunction("\t0\t\n\t\x16\x00\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1391(self):
		result = SimpleJSONTestFunction("-Infinity\t\t\t\n\x10\x00")
		self.assertEqual(result, expected_result)

	def test_1392(self):
		result = SimpleJSONTestFunction("3\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1393(self):
		result = SimpleJSONTestFunction("\n0E-0\x00\x00\x00\x00\x00\x00\x00\n\n\x00")
		self.assertEqual(result, expected_result)

	def test_1394(self):
		result = SimpleJSONTestFunction("\t0\t\t\n\x15\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1395(self):
		result = SimpleJSONTestFunction("\"  0\x01\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1396(self):
		result = SimpleJSONTestFunction("\n 0 \x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1397(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\x13\n\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1398(self):
		result = SimpleJSONTestFunction("\t\n@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1399(self):
		result = SimpleJSONTestFunction("\t\t\n\t\t\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1400(self):
		result = SimpleJSONTestFunction("\n\t\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1401(self):
		result = SimpleJSONTestFunction("-Infinity\t\x07\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1402(self):
		result = SimpleJSONTestFunction("\"   0\x01\x0D\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1403(self):
		result = SimpleJSONTestFunction("\"0\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1404(self):
		result = SimpleJSONTestFunction("\"  \"\n\n\x10\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1405(self):
		result = SimpleJSONTestFunction("\"   \"\n\x0F\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1406(self):
		result = SimpleJSONTestFunction("\"\n\xD1\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1407(self):
		result = SimpleJSONTestFunction("-Infinity\t\n\x01\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1408(self):
		result = SimpleJSONTestFunction("\t  \t\t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1409(self):
		result = SimpleJSONTestFunction("-0 \t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1410(self):
		result = SimpleJSONTestFunction("\" 00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1411(self):
		result = SimpleJSONTestFunction("\t\t\t \x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1412(self):
		result = SimpleJSONTestFunction("\n0E-0\x00\n\x00\x00\x00\x00\x00\n\n\n")
		self.assertEqual(result, expected_result)

	def test_1413(self):
		result = SimpleJSONTestFunction("\t\n\t \x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1414(self):
		result = SimpleJSONTestFunction("\n\"\x00\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1415(self):
		result = SimpleJSONTestFunction("-Infinity\n\t\t\t\t\x11")
		self.assertEqual(result, expected_result)

	def test_1416(self):
		result = SimpleJSONTestFunction("\t 0E\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1417(self):
		result = SimpleJSONTestFunction(" \t\t\t\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1418(self):
		result = SimpleJSONTestFunction("\t0\t\t \t\t\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1419(self):
		result = SimpleJSONTestFunction("\"  \"\t\t\t\x01\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1420(self):
		result = SimpleJSONTestFunction("\t\t\t0.\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1421(self):
		result = SimpleJSONTestFunction("\n\xB0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1422(self):
		result = SimpleJSONTestFunction("\t0 \t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1423(self):
		result = SimpleJSONTestFunction("\"  !\x11\t\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1424(self):
		result = SimpleJSONTestFunction("\t0\t\n\t\x12\x00\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1425(self):
		result = SimpleJSONTestFunction("\" 00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1426(self):
		result = SimpleJSONTestFunction("\"   !\n\x01\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1427(self):
		result = SimpleJSONTestFunction("-Infinity \t\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1428(self):
		result = SimpleJSONTestFunction("\t\n\t\t\t\n\x01\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1429(self):
		result = SimpleJSONTestFunction("\"  \" \n \x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1430(self):
		result = SimpleJSONTestFunction("-Infinity\n\x0F\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1431(self):
		result = SimpleJSONTestFunction("\t0E-\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1432(self):
		result = SimpleJSONTestFunction("-Infinity\n\x01\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1433(self):
		result = SimpleJSONTestFunction("\t\"\x11\x0D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1434(self):
		result = SimpleJSONTestFunction("\" 00\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1435(self):
		result = SimpleJSONTestFunction("\n\"\x11\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1436(self):
		result = SimpleJSONTestFunction("\"  \" \n \x00\x00\x00\x00\x00\n\n\x00")
		self.assertEqual(result, expected_result)

	def test_1437(self):
		result = SimpleJSONTestFunction("\t\t\t \t\t\t\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1438(self):
		result = SimpleJSONTestFunction("\"   \"\t\t\n\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1439(self):
		result = SimpleJSONTestFunction("\t\n\x15\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1440(self):
		result = SimpleJSONTestFunction("\n \t0e0\x00\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1441(self):
		result = SimpleJSONTestFunction("\"  \"\n\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1442(self):
		result = SimpleJSONTestFunction("\"   \"\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1443(self):
		result = SimpleJSONTestFunction("\"  \" \t \t\x01\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1444(self):
		result = SimpleJSONTestFunction("\"   \"\t\n\t\x01\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1445(self):
		result = SimpleJSONTestFunction("\"  \"\n\t\t\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1446(self):
		result = SimpleJSONTestFunction("-Infinity\t\x06\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1447(self):
		result = SimpleJSONTestFunction("\t \t \x13\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1448(self):
		result = SimpleJSONTestFunction("\t\"\x11'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1449(self):
		result = SimpleJSONTestFunction("\"  \"\t\n\x00\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1450(self):
		result = SimpleJSONTestFunction("\"   @\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1451(self):
		result = SimpleJSONTestFunction("-Infinity\n\t\x02\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1452(self):
		result = SimpleJSONTestFunction("\t 0E+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1453(self):
		result = SimpleJSONTestFunction("\"\n\x82\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1454(self):
		result = SimpleJSONTestFunction("-Infinity\n\n\x03\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1455(self):
		result = SimpleJSONTestFunction("\"   \"\n\x0C\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1456(self):
		result = SimpleJSONTestFunction("\"   \"\t\n\t\x02\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1457(self):
		result = SimpleJSONTestFunction("-Infinity\n\n\x04\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1458(self):
		result = SimpleJSONTestFunction("\n0\t\t\t\x03\x00\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1459(self):
		result = SimpleJSONTestFunction("\"   1\n\x0D\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1460(self):
		result = SimpleJSONTestFunction("\"  \"\n\x15\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1461(self):
		result = SimpleJSONTestFunction("\t 0 \t\t\t\t\t\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1462(self):
		result = SimpleJSONTestFunction("\t0\t\t \x04\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1463(self):
		result = SimpleJSONTestFunction("\t0E-0\x00\n\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1464(self):
		result = SimpleJSONTestFunction("\"@\n\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1465(self):
		result = SimpleJSONTestFunction("6\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1466(self):
		result = SimpleJSONTestFunction("\"   \"\t\n\n\x01\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1467(self):
		result = SimpleJSONTestFunction("\t0 \t\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1468(self):
		result = SimpleJSONTestFunction("\t \t\t\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1469(self):
		result = SimpleJSONTestFunction("-Infinity\t\x0C\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1470(self):
		result = SimpleJSONTestFunction("\"  \"\n\x16\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1471(self):
		result = SimpleJSONTestFunction("-Infinity\n\t\n\t\t\x11")
		self.assertEqual(result, expected_result)

	def test_1472(self):
		result = SimpleJSONTestFunction("\"   \x11\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1473(self):
		result = SimpleJSONTestFunction("\t  \x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1474(self):
		result = SimpleJSONTestFunction("\t \n0\t\x01\x00\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1475(self):
		result = SimpleJSONTestFunction("-Infinity\n\t\t\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1476(self):
		result = SimpleJSONTestFunction("\t\n\t\t\t\t\t\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1477(self):
		result = SimpleJSONTestFunction("\t  \t\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1478(self):
		result = SimpleJSONTestFunction("\"   \"\n\x0B\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1479(self):
		result = SimpleJSONTestFunction("\t\t\n\t\t\t\t\x01\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1480(self):
		result = SimpleJSONTestFunction("-Infinity\t\x06\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1481(self):
		result = SimpleJSONTestFunction("\"   \"\t\t\t\t\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1482(self):
		result = SimpleJSONTestFunction("\t0\n\t\t\t\x02\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1483(self):
		result = SimpleJSONTestFunction("\"  \" \n\x01\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1484(self):
		result = SimpleJSONTestFunction("-Infinity \t\x01\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1485(self):
		result = SimpleJSONTestFunction("\"   \"\t\n\x02\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1486(self):
		result = SimpleJSONTestFunction("\t\"\x00\\\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1487(self):
		result = SimpleJSONTestFunction("-Infinity\n\x05\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1488(self):
		result = SimpleJSONTestFunction("\n\t \x13\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1489(self):
		result = SimpleJSONTestFunction("\"   \"\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1490(self):
		result = SimpleJSONTestFunction("-Infinity\t\t\t\t\x10\n")
		self.assertEqual(result, expected_result)

	def test_1491(self):
		result = SimpleJSONTestFunction("\"   \"\t\t\t\x02\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1492(self):
		result = SimpleJSONTestFunction("\t0@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1493(self):
		result = SimpleJSONTestFunction("\n0E-0\x01\x00\n\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1494(self):
		result = SimpleJSONTestFunction("\t  \t\t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1495(self):
		result = SimpleJSONTestFunction("\n \t0\t\t\x13\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1496(self):
		result = SimpleJSONTestFunction("\"  \"\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1497(self):
		result = SimpleJSONTestFunction("\"  \" \x04\x00\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1498(self):
		result = SimpleJSONTestFunction("\"   0\x10\n\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1499(self):
		result = SimpleJSONTestFunction("\t\t0e\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1500(self):
		result = SimpleJSONTestFunction("\t0 \t\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1501(self):
		result = SimpleJSONTestFunction("-Infinity\t\t\t\x11\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1502(self):
		result = SimpleJSONTestFunction("-6\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1503(self):
		result = SimpleJSONTestFunction("\"  \x11\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1504(self):
		result = SimpleJSONTestFunction("\n \n0e0\x00\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1505(self):
		result = SimpleJSONTestFunction("\t\t \t\x0B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1506(self):
		result = SimpleJSONTestFunction("\t\n\x16\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1507(self):
		result = SimpleJSONTestFunction("\t  \x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1508(self):
		result = SimpleJSONTestFunction("\"  \"\n\t\t\x01\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1509(self):
		result = SimpleJSONTestFunction("\"  \" \t \x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1510(self):
		result = SimpleJSONTestFunction("\t0\t\n \n\x01\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1511(self):
		result = SimpleJSONTestFunction("\"  \"\n\x03\x00\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1512(self):
		result = SimpleJSONTestFunction("-10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1513(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\t\t\t\t\x02\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1514(self):
		result = SimpleJSONTestFunction("-Infinity\t\t\t\t\x02\n")
		self.assertEqual(result, expected_result)

	def test_1515(self):
		result = SimpleJSONTestFunction("\t0E-0\x00\x00\x00\x00\n\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1516(self):
		result = SimpleJSONTestFunction("\t0E-0\x01\x00\x00\x00\x00\x00\x00\x00\n\n")
		self.assertEqual(result, expected_result)

	def test_1517(self):
		result = SimpleJSONTestFunction("\t\t0e-\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1518(self):
		result = SimpleJSONTestFunction("-Infinity\n\t\x01\n\n\x00")
		self.assertEqual(result, expected_result)

	def test_1519(self):
		result = SimpleJSONTestFunction("\"0\x00\\\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1520(self):
		result = SimpleJSONTestFunction("-Infinity\n\t\t\t\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1521(self):
		result = SimpleJSONTestFunction("\t 0E\x81\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1522(self):
		result = SimpleJSONTestFunction("\"  \"P\x00\x00\x00\x00\n\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1523(self):
		result = SimpleJSONTestFunction("\n\"\n'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1524(self):
		result = SimpleJSONTestFunction("\t0\t\n \n\x02\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1525(self):
		result = SimpleJSONTestFunction("\"  \" \t \t\x02\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1526(self):
		result = SimpleJSONTestFunction("\" \x01\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1527(self):
		result = SimpleJSONTestFunction("\t\"\x01\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1528(self):
		result = SimpleJSONTestFunction("\t\t\t\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1529(self):
		result = SimpleJSONTestFunction("\"   \"\t\t\n\x01\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1530(self):
		result = SimpleJSONTestFunction("-Infinity\n\n\x06\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1531(self):
		result = SimpleJSONTestFunction("\"  !0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1532(self):
		result = SimpleJSONTestFunction("\n\t\n\t\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1533(self):
		result = SimpleJSONTestFunction("-Infinity\x05\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1534(self):
		result = SimpleJSONTestFunction("\t \t \t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1535(self):
		result = SimpleJSONTestFunction("\n0\t\x0B\x00\x00\x00\x00\x00\x00\n\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1536(self):
		result = SimpleJSONTestFunction("\t \t0e0\x00\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1537(self):
		result = SimpleJSONTestFunction("\t0\x1E\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1538(self):
		result = SimpleJSONTestFunction("\t\t\n\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1539(self):
		result = SimpleJSONTestFunction("-Infinity\t\t\t\n\t\x10")
		self.assertEqual(result, expected_result)

	def test_1540(self):
		result = SimpleJSONTestFunction("\t\"\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1541(self):
		result = SimpleJSONTestFunction("\"@\x11\x0D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1542(self):
		result = SimpleJSONTestFunction("-Infinity\n\x05\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1543(self):
		result = SimpleJSONTestFunction("\t 00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1544(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1545(self):
		result = SimpleJSONTestFunction("\t0E-0\x00\x00\x00\x00\n\x00\x00\n\x00\n")
		self.assertEqual(result, expected_result)

	def test_1546(self):
		result = SimpleJSONTestFunction("\t\t0\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1547(self):
		result = SimpleJSONTestFunction("\"   @\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1548(self):
		result = SimpleJSONTestFunction("-Infinity\n\x03\x00\n\n\x00")
		self.assertEqual(result, expected_result)

	def test_1549(self):
		result = SimpleJSONTestFunction("-Infinity\t\x13\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1550(self):
		result = SimpleJSONTestFunction("-Infinity\t\t\t\t\n\x01")
		self.assertEqual(result, expected_result)

	def test_1551(self):
		result = SimpleJSONTestFunction("\t \t0e \x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1552(self):
		result = SimpleJSONTestFunction("\"  \"\x10\x00\x00\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1553(self):
		result = SimpleJSONTestFunction("\t \t0\t\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1554(self):
		result = SimpleJSONTestFunction("\n\"\x01\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1555(self):
		result = SimpleJSONTestFunction("-Infinity\t\n\t\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1556(self):
		result = SimpleJSONTestFunction("-Infinity\t\t\t\n\x10\n")
		self.assertEqual(result, expected_result)

	def test_1557(self):
		result = SimpleJSONTestFunction("-Infinity\n\x0F\n\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1558(self):
		result = SimpleJSONTestFunction("\n\t\t\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1559(self):
		result = SimpleJSONTestFunction("\"   @\n\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1560(self):
		result = SimpleJSONTestFunction("\"   \n \x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1561(self):
		result = SimpleJSONTestFunction("\t0\t\n \n\x03\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1562(self):
		result = SimpleJSONTestFunction("\"   \"\n\x08\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1563(self):
		result = SimpleJSONTestFunction("\t0e+\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1564(self):
		result = SimpleJSONTestFunction("\t0E-0\x01\x00\n\x00\x00\x00\n\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1565(self):
		result = SimpleJSONTestFunction("-5\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1566(self):
		result = SimpleJSONTestFunction("\n\"\n\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1567(self):
		result = SimpleJSONTestFunction("\"   1\n\t\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1568(self):
		result = SimpleJSONTestFunction("\t\t\n \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1569(self):
		result = SimpleJSONTestFunction("\"  !\x10\x0D\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1570(self):
		result = SimpleJSONTestFunction("\t0 \t\t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1571(self):
		result = SimpleJSONTestFunction("\"  \"\n\x17\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1572(self):
		result = SimpleJSONTestFunction("-Infinity\x13\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1573(self):
		result = SimpleJSONTestFunction("\"   \"\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1574(self):
		result = SimpleJSONTestFunction("\"  \"\t\t\x00\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1575(self):
		result = SimpleJSONTestFunction("-Infinity\t\t\t!\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1576(self):
		result = SimpleJSONTestFunction("\t 0 \t\t\t\t\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1577(self):
		result = SimpleJSONTestFunction("7\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1578(self):
		result = SimpleJSONTestFunction("-Infinity\n\t\t\t\t\x00")
		self.assertEqual(result, expected_result)

	def test_1579(self):
		result = SimpleJSONTestFunction("\n\n\t\t\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1580(self):
		result = SimpleJSONTestFunction("-Infinity\n\n\x05\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1581(self):
		result = SimpleJSONTestFunction("\" @\x11\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1582(self):
		result = SimpleJSONTestFunction("-Infinity\n\x12\n\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1583(self):
		result = SimpleJSONTestFunction("\n0E-0\x00\x00\x00\x00\x00\x00\n\n\x00\n")
		self.assertEqual(result, expected_result)

	def test_1584(self):
		result = SimpleJSONTestFunction("\"  \"\t\t\n\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1585(self):
		result = SimpleJSONTestFunction("\"  \" \n\x01\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1586(self):
		result = SimpleJSONTestFunction("\"0\n'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1587(self):
		result = SimpleJSONTestFunction("\"   \"\t\x00\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1588(self):
		result = SimpleJSONTestFunction("\n0E\x80\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1589(self):
		result = SimpleJSONTestFunction("\"  \" \t\x10\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1590(self):
		result = SimpleJSONTestFunction("\t \t0\t\t\t\t\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1591(self):
		result = SimpleJSONTestFunction("-Infinity\n\x13\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1592(self):
		result = SimpleJSONTestFunction("\n\"\x11\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1593(self):
		result = SimpleJSONTestFunction("\t\t6\x00\x00\x00\x00\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1594(self):
		result = SimpleJSONTestFunction("\"p\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1595(self):
		result = SimpleJSONTestFunction("\t \n0\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1596(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\n\t\x01\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1597(self):
		result = SimpleJSONTestFunction("\t\t\n\t\t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1598(self):
		result = SimpleJSONTestFunction("\"  \"\n\x01\x00\x00\n\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1599(self):
		result = SimpleJSONTestFunction("-Infinity\t\t\t'\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1600(self):
		result = SimpleJSONTestFunction("\"  \"\n\x16\n\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1601(self):
		result = SimpleJSONTestFunction("-30\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1602(self):
		result = SimpleJSONTestFunction("\t 0E-\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1603(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\n\x0B\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1604(self):
		result = SimpleJSONTestFunction("\"  !\x11\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1605(self):
		result = SimpleJSONTestFunction("\"  \" \t\t\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1606(self):
		result = SimpleJSONTestFunction("4\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1607(self):
		result = SimpleJSONTestFunction("\n\t \x1B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1608(self):
		result = SimpleJSONTestFunction("\"\x11\\\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1609(self):
		result = SimpleJSONTestFunction("\"  !0\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1610(self):
		result = SimpleJSONTestFunction("\"  \"\n\x0C\x00\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1611(self):
		result = SimpleJSONTestFunction("\"  \" \t\t\x01\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1612(self):
		result = SimpleJSONTestFunction("-Infinity \x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1613(self):
		result = SimpleJSONTestFunction("0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1614(self):
		result = SimpleJSONTestFunction("-Infinity\t\t\x02\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1615(self):
		result = SimpleJSONTestFunction("\n \t0\t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1616(self):
		result = SimpleJSONTestFunction("\"  \"\t\t\t\t\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1617(self):
		result = SimpleJSONTestFunction("\"   \"\t\n\t\x03\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1618(self):
		result = SimpleJSONTestFunction("\t\"\x11\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1619(self):
		result = SimpleJSONTestFunction("\t \t0.\x80\x00\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1620(self):
		result = SimpleJSONTestFunction("-Infinity\t\n\x02\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1621(self):
		result = SimpleJSONTestFunction("\"  !0\n\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1622(self):
		result = SimpleJSONTestFunction("-Infinity\n\n\t\x02\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1623(self):
		result = SimpleJSONTestFunction("\t\n\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1624(self):
		result = SimpleJSONTestFunction("\"p\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1625(self):
		result = SimpleJSONTestFunction("\t\"\x01\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1626(self):
		result = SimpleJSONTestFunction("\n0\t\t\t\x0B\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1627(self):
		result = SimpleJSONTestFunction("\"   \"\t\t\n\t\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1628(self):
		result = SimpleJSONTestFunction("-Infinity\n\t\t\n\t\x11")
		self.assertEqual(result, expected_result)

	def test_1629(self):
		result = SimpleJSONTestFunction("\"\n\xA5\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1630(self):
		result = SimpleJSONTestFunction("\"  \"\n\t\t\x02\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1631(self):
		result = SimpleJSONTestFunction("\t0E-0\x00\n\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1632(self):
		result = SimpleJSONTestFunction("\"  \" \t  \x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1633(self):
		result = SimpleJSONTestFunction("\"  \" \t \t\t\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1634(self):
		result = SimpleJSONTestFunction("-Infinity\x15\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1635(self):
		result = SimpleJSONTestFunction("\"   \"\t\t\t\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1636(self):
		result = SimpleJSONTestFunction("\"  \" \t \x01\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1637(self):
		result = SimpleJSONTestFunction("-Infinity\n\n\t\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1638(self):
		result = SimpleJSONTestFunction("\t \t0\n\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1639(self):
		result = SimpleJSONTestFunction("\"  \" \t\t\t\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1640(self):
		result = SimpleJSONTestFunction("\t \t0\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1641(self):
		result = SimpleJSONTestFunction("\"p\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1642(self):
		result = SimpleJSONTestFunction("\t\t\x1F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1643(self):
		result = SimpleJSONTestFunction("\t\n\x1E\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1644(self):
		result = SimpleJSONTestFunction("\"  \"`\x00\x00\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1645(self):
		result = SimpleJSONTestFunction("\t \n \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1646(self):
		result = SimpleJSONTestFunction("\"   \"\t\t\x07\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1647(self):
		result = SimpleJSONTestFunction("-Infinity\t\n\t\x01\n\x00")
		self.assertEqual(result, expected_result)

	def test_1648(self):
		result = SimpleJSONTestFunction("\"  \"\t\t\x11\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1649(self):
		result = SimpleJSONTestFunction("-Infinity\n\t\t\x02\n\x00")
		self.assertEqual(result, expected_result)

	def test_1650(self):
		result = SimpleJSONTestFunction("\t\t0e-\x00\x00\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1651(self):
		result = SimpleJSONTestFunction("\t\t\t\t\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1652(self):
		result = SimpleJSONTestFunction("\"  \"\n\x1E\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1653(self):
		result = SimpleJSONTestFunction("\"  \"\t\t\t\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1654(self):
		result = SimpleJSONTestFunction("\n0E-0\x00\n\x00\n\x00\n\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1655(self):
		result = SimpleJSONTestFunction("\"   \"\t\n\x03\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1656(self):
		result = SimpleJSONTestFunction("-Infinity \t\x02\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1657(self):
		result = SimpleJSONTestFunction("\"  \"\n\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1658(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\t\t\t\t\t\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1659(self):
		result = SimpleJSONTestFunction("\"   \"\t\n\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1660(self):
		result = SimpleJSONTestFunction("-Infinity\t\t\t\x13\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1661(self):
		result = SimpleJSONTestFunction("\t0 \t(\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1662(self):
		result = SimpleJSONTestFunction("\"  \" \t  \x01\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1663(self):
		result = SimpleJSONTestFunction("\"  \"\t\t\t\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1664(self):
		result = SimpleJSONTestFunction("\"  \" \t \x00\n\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1665(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\n\t\x02\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1666(self):
		result = SimpleJSONTestFunction("\"   \x01\x0D\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1667(self):
		result = SimpleJSONTestFunction("\"  \"\n\t\t\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1668(self):
		result = SimpleJSONTestFunction("\t0\t\n \n\x04\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1669(self):
		result = SimpleJSONTestFunction("-Infinity \t\t\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1670(self):
		result = SimpleJSONTestFunction("\"  \"\t\x0E\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1671(self):
		result = SimpleJSONTestFunction("\n0E-0\x00\n\x00\x00\x00\x00\n\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1672(self):
		result = SimpleJSONTestFunction("\"   P\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1673(self):
		result = SimpleJSONTestFunction("\" 00\x01\x0D\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1674(self):
		result = SimpleJSONTestFunction("\t \t \x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1675(self):
		result = SimpleJSONTestFunction("\n \t0e0\x00\x00\x00\n\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1676(self):
		result = SimpleJSONTestFunction("\"  \" \t\t\t\x01\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1677(self):
		result = SimpleJSONTestFunction("\t0 \t'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1678(self):
		result = SimpleJSONTestFunction("\" 00\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1679(self):
		result = SimpleJSONTestFunction("\"   1\n\n\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1680(self):
		result = SimpleJSONTestFunction("\t \t0\t\t\x13\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1681(self):
		result = SimpleJSONTestFunction("\"  \" \t\t\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1682(self):
		result = SimpleJSONTestFunction("\t0\t\t\x0E\x00\x00\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1683(self):
		result = SimpleJSONTestFunction("\n0\t\x0C\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1684(self):
		result = SimpleJSONTestFunction("-Infinity\n\n\t\x03\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1685(self):
		result = SimpleJSONTestFunction("\"   \"\t\n\n\x02\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1686(self):
		result = SimpleJSONTestFunction("\t0\t\n \n\x01\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1687(self):
		result = SimpleJSONTestFunction("\n\"\x00'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1688(self):
		result = SimpleJSONTestFunction("\"   P\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1689(self):
		result = SimpleJSONTestFunction("\t0\t\t \t\x03\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1690(self):
		result = SimpleJSONTestFunction("\t\"\x11\\\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1691(self):
		result = SimpleJSONTestFunction("\"  \" \t  \x01\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1692(self):
		result = SimpleJSONTestFunction("\t\"\x01\\\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1693(self):
		result = SimpleJSONTestFunction("\n 0 \x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1694(self):
		result = SimpleJSONTestFunction("\t0E-0\x00\x00\x00\x00\x00\x00\n\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1695(self):
		result = SimpleJSONTestFunction("\"\x00\x81\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1696(self):
		result = SimpleJSONTestFunction("\"@\x11 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1697(self):
		result = SimpleJSONTestFunction("\"  \" \n\x02\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1698(self):
		result = SimpleJSONTestFunction("\"  0\x01\\\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1699(self):
		result = SimpleJSONTestFunction("\"  \"\t\t\t\t\x01\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1700(self):
		result = SimpleJSONTestFunction("\n\"\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1701(self):
		result = SimpleJSONTestFunction("\"  \"\t\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1702(self):
		result = SimpleJSONTestFunction("-Infinity\t\t\t\n\n\x10")
		self.assertEqual(result, expected_result)

	def test_1703(self):
		result = SimpleJSONTestFunction("\"  \" \t \t\x03\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1704(self):
		result = SimpleJSONTestFunction("\t \t0E-\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1705(self):
		result = SimpleJSONTestFunction("\t\t \n\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1706(self):
		result = SimpleJSONTestFunction("\t\"\x11\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1707(self):
		result = SimpleJSONTestFunction("-Infinity \t\x03\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1708(self):
		result = SimpleJSONTestFunction("-Infinity \x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1709(self):
		result = SimpleJSONTestFunction("-Infinity\t\x1B\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1710(self):
		result = SimpleJSONTestFunction("\"  \"\n\t\t\x03\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1711(self):
		result = SimpleJSONTestFunction("\t0E-0\x00\x00\x00\n\x00\n\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1712(self):
		result = SimpleJSONTestFunction("\"   \"\t\t\t\t\x01\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1713(self):
		result = SimpleJSONTestFunction("-0\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1714(self):
		result = SimpleJSONTestFunction("\"   P\n\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1715(self):
		result = SimpleJSONTestFunction("-Infinity\n\x11\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1716(self):
		result = SimpleJSONTestFunction("\" 00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1717(self):
		result = SimpleJSONTestFunction("\"  \" \t \x02\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1718(self):
		result = SimpleJSONTestFunction("0.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1719(self):
		result = SimpleJSONTestFunction("\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1720(self):
		result = SimpleJSONTestFunction("\t \t0e0\x00\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1721(self):
		result = SimpleJSONTestFunction("\t \t\n\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1722(self):
		result = SimpleJSONTestFunction("\" 00\"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1723(self):
		result = SimpleJSONTestFunction("\n\n\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1724(self):
		result = SimpleJSONTestFunction("\"   \"\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1725(self):
		result = SimpleJSONTestFunction("\"  \"\t\t\t\x02\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1726(self):
		result = SimpleJSONTestFunction("\t0\n\t\t\t\x04\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1727(self):
		result = SimpleJSONTestFunction("-Infinity\t\t\t\n\t\x00")
		self.assertEqual(result, expected_result)

	def test_1728(self):
		result = SimpleJSONTestFunction("\" 00!\x00\\\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1729(self):
		result = SimpleJSONTestFunction("\t0\t\t\x05\x00\x00\x00\x00\x00\x00\n\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1730(self):
		result = SimpleJSONTestFunction("\n \t0e0\x00\x00\x00\n\n\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1731(self):
		result = SimpleJSONTestFunction("\t\t\t\t\t\t\t\x02\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1732(self):
		result = SimpleJSONTestFunction("\t0\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1733(self):
		result = SimpleJSONTestFunction("\"  \"\t\t\t\t\t\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1734(self):
		result = SimpleJSONTestFunction(" \x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1735(self):
		result = SimpleJSONTestFunction("-Infinity!\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1736(self):
		result = SimpleJSONTestFunction("\"  \"\t\x15\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1737(self):
		result = SimpleJSONTestFunction("\t \t0\t\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1738(self):
		result = SimpleJSONTestFunction("\t\"\x11\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1739(self):
		result = SimpleJSONTestFunction("\n\"\x11\\\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1740(self):
		result = SimpleJSONTestFunction("\n\t\t \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1741(self):
		result = SimpleJSONTestFunction("-Infinity\n\t\t\n\t\x13")
		self.assertEqual(result, expected_result)

	def test_1742(self):
		result = SimpleJSONTestFunction("-0\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1743(self):
		result = SimpleJSONTestFunction("\"  ! \x00\\\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1744(self):
		result = SimpleJSONTestFunction("\t\t \x13\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1745(self):
		result = SimpleJSONTestFunction("-3\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1746(self):
		result = SimpleJSONTestFunction("\n0E+\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1747(self):
		result = SimpleJSONTestFunction("\"   \"\x01\x00\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1748(self):
		result = SimpleJSONTestFunction("\"  \" \t \t\x04\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1749(self):
		result = SimpleJSONTestFunction("\n 0 \x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1750(self):
		result = SimpleJSONTestFunction(" \x17\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1751(self):
		result = SimpleJSONTestFunction("\t\t\t \t\t\x02\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1752(self):
		result = SimpleJSONTestFunction("\t \t0\n\t\x02\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1753(self):
		result = SimpleJSONTestFunction("\t0E-0\x01\x00\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1754(self):
		result = SimpleJSONTestFunction("\t \t0e0\x00\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1755(self):
		result = SimpleJSONTestFunction("\t 0 \x10\x00\x00\x00\x00\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1756(self):
		result = SimpleJSONTestFunction("\"  \" \t\t\x02\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1757(self):
		result = SimpleJSONTestFunction("\t0\t\t\n\x15\x00\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1758(self):
		result = SimpleJSONTestFunction("\t  0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1759(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1760(self):
		result = SimpleJSONTestFunction("\n\t7\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1761(self):
		result = SimpleJSONTestFunction("\" @\n\\\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1762(self):
		result = SimpleJSONTestFunction("\t0\t\t\n\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1763(self):
		result = SimpleJSONTestFunction("\"   @\n\n\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1764(self):
		result = SimpleJSONTestFunction("\t\t\n \t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1765(self):
		result = SimpleJSONTestFunction("\"   \"\n\t\t\t\x01\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1766(self):
		result = SimpleJSONTestFunction("\"  \"\t\t\t\t\t\x01\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1767(self):
		result = SimpleJSONTestFunction("\t\t\t \t\t\t\x01\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1768(self):
		result = SimpleJSONTestFunction("\t  0.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1769(self):
		result = SimpleJSONTestFunction("\"   \"\t\n\t\x02\x00\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1770(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\n\x0C\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1771(self):
		result = SimpleJSONTestFunction("-Infinity\n\t\t\t\t\x12")
		self.assertEqual(result, expected_result)

	def test_1772(self):
		result = SimpleJSONTestFunction("-Infinity \t\t\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1773(self):
		result = SimpleJSONTestFunction("\n \t0\t\t\x12\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1774(self):
		result = SimpleJSONTestFunction("\t0 \t\t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1775(self):
		result = SimpleJSONTestFunction("\t \t0E+\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1776(self):
		result = SimpleJSONTestFunction("-Infinity\t\x03\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1777(self):
		result = SimpleJSONTestFunction("-Infinity\t\x14\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1778(self):
		result = SimpleJSONTestFunction("-20\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1779(self):
		result = SimpleJSONTestFunction("\t\t\n\t\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1780(self):
		result = SimpleJSONTestFunction("\t \t \x15\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1781(self):
		result = SimpleJSONTestFunction("-Infinity\x07\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1782(self):
		result = SimpleJSONTestFunction("\"  \" \t\t\t\x02\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1783(self):
		result = SimpleJSONTestFunction("-Infinity\n\x1B\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1784(self):
		result = SimpleJSONTestFunction("-Infinity \t\t\t\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1785(self):
		result = SimpleJSONTestFunction("\n0 \t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1786(self):
		result = SimpleJSONTestFunction("\t\t0e+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1787(self):
		result = SimpleJSONTestFunction("\n0\t\n\t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1788(self):
		result = SimpleJSONTestFunction("-Infinity\t\n\x01\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1789(self):
		result = SimpleJSONTestFunction("\"  \"\t\x03\x00\n\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1790(self):
		result = SimpleJSONTestFunction("\t \t0E\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1791(self):
		result = SimpleJSONTestFunction("\t0\n\t\t\t\x06\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1792(self):
		result = SimpleJSONTestFunction("-Infinity\t\t\n\t\x10\x00")
		self.assertEqual(result, expected_result)

	def test_1793(self):
		result = SimpleJSONTestFunction("-Infinity \t\t\t\x01\x00")
		self.assertEqual(result, expected_result)

	def test_1794(self):
		result = SimpleJSONTestFunction("\"  \"`\x00\x00\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1795(self):
		result = SimpleJSONTestFunction("\t0\t\t \x11\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1796(self):
		result = SimpleJSONTestFunction("\"  \" \t \t\t\x01\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1797(self):
		result = SimpleJSONTestFunction("\"\x01\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1798(self):
		result = SimpleJSONTestFunction("\t \t0\t\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1799(self):
		result = SimpleJSONTestFunction("\" 00\"\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1800(self):
		result = SimpleJSONTestFunction("\"  \"\n\t\t\t\t\x01\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1801(self):
		result = SimpleJSONTestFunction("\n 0 \x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1802(self):
		result = SimpleJSONTestFunction("\t0\t\n\t\t\t\t\t\x01\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1803(self):
		result = SimpleJSONTestFunction("\t\t\t \t\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1804(self):
		result = SimpleJSONTestFunction("\n\"\x01\\\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1805(self):
		result = SimpleJSONTestFunction("\n0\t\t\t\t\t\t\x02\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1806(self):
		result = SimpleJSONTestFunction("\n\"\x11'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1807(self):
		result = SimpleJSONTestFunction("-Infinity\n\n\x07\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1808(self):
		result = SimpleJSONTestFunction("\"  \" \x12\x00\x00\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1809(self):
		result = SimpleJSONTestFunction("\t\t\n\n\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1810(self):
		result = SimpleJSONTestFunction("\"  !0\x01\x0D\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1811(self):
		result = SimpleJSONTestFunction("\t0E-0\x01\x00\n\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1812(self):
		result = SimpleJSONTestFunction("\"P\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1813(self):
		result = SimpleJSONTestFunction("\n\t\t\t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1814(self):
		result = SimpleJSONTestFunction("\t0E-0\x00\x00\x00\n\n\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1815(self):
		result = SimpleJSONTestFunction("\t\t\t\t\t\t\t\t\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1816(self):
		result = SimpleJSONTestFunction("\t \t0e-\x80\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1817(self):
		result = SimpleJSONTestFunction("\n  \x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1818(self):
		result = SimpleJSONTestFunction("\t0.\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1819(self):
		result = SimpleJSONTestFunction("\"   \"\t\n\x0E\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1820(self):
		result = SimpleJSONTestFunction("0.\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1821(self):
		result = SimpleJSONTestFunction("\t0E-0\x01\x00\x00\x00\n\x00\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1822(self):
		result = SimpleJSONTestFunction("-0E\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1823(self):
		result = SimpleJSONTestFunction("\"\n\x17\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1824(self):
		result = SimpleJSONTestFunction("-0 \t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1825(self):
		result = SimpleJSONTestFunction("\t0E-\x03\n\n\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1826(self):
		result = SimpleJSONTestFunction("\"  \x18\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1827(self):
		result = SimpleJSONTestFunction("\"  \"\t \x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1828(self):
		result = SimpleJSONTestFunction("\t  \t\t\t\x01\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1829(self):
		result = SimpleJSONTestFunction("-Infinity\xB2\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1830(self):
		result = SimpleJSONTestFunction("-Infinity\n\x0F\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1831(self):
		result = SimpleJSONTestFunction("\"\n\x92\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1832(self):
		result = SimpleJSONTestFunction("\" @\x01\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1833(self):
		result = SimpleJSONTestFunction("-Infinity\n\t\t\t\x02\x00")
		self.assertEqual(result, expected_result)

	def test_1834(self):
		result = SimpleJSONTestFunction("\"  \" \t \t\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1835(self):
		result = SimpleJSONTestFunction("\n0E-0\x00\n\x00\n\x00\x00\x00\n\x00\n")
		self.assertEqual(result, expected_result)

	def test_1836(self):
		result = SimpleJSONTestFunction("\t \t\n\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1837(self):
		result = SimpleJSONTestFunction("\t \t@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1838(self):
		result = SimpleJSONTestFunction("\"@\n\\\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1839(self):
		result = SimpleJSONTestFunction("\t\t\t\x16\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1840(self):
		result = SimpleJSONTestFunction("-Infinity\n\x10\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1841(self):
		result = SimpleJSONTestFunction("-Infinity\n\t\t\t\t\x10")
		self.assertEqual(result, expected_result)

	def test_1842(self):
		result = SimpleJSONTestFunction("\"`\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1843(self):
		result = SimpleJSONTestFunction("\"@\x01\x0D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1844(self):
		result = SimpleJSONTestFunction("\n\t\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1845(self):
		result = SimpleJSONTestFunction("\t\n\t \x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1846(self):
		result = SimpleJSONTestFunction("\t\"\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1847(self):
		result = SimpleJSONTestFunction("\"   \"\n\x0E\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1848(self):
		result = SimpleJSONTestFunction("\t\t0.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1849(self):
		result = SimpleJSONTestFunction("\"  \" \t \n\t\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1850(self):
		result = SimpleJSONTestFunction("\t  0.\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1851(self):
		result = SimpleJSONTestFunction("\t\n\t\t\t\n\x02\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1852(self):
		result = SimpleJSONTestFunction("\t\"\x11 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1853(self):
		result = SimpleJSONTestFunction("\t\n\t\n\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1854(self):
		result = SimpleJSONTestFunction("\t \t0e0\x00\n\x00\x00\x00\n\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1855(self):
		result = SimpleJSONTestFunction("\n\"\x01'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1856(self):
		result = SimpleJSONTestFunction("\t \n0\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1857(self):
		result = SimpleJSONTestFunction("-Infinity\n\x12\x00\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_1858(self):
		result = SimpleJSONTestFunction("\t\"\n\x90\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1859(self):
		result = SimpleJSONTestFunction("\t0\t\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1860(self):
		result = SimpleJSONTestFunction("\t 0 \t\t\t\t\t\x01\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1861(self):
		result = SimpleJSONTestFunction("\"   \"\n\t\t\t\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1862(self):
		result = SimpleJSONTestFunction("-Infinity\t\t\t\t\t\x03")
		self.assertEqual(result, expected_result)

	def test_1863(self):
		result = SimpleJSONTestFunction("\"  \"\t \x01\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1864(self):
		result = SimpleJSONTestFunction("\"  \"\n\t\t\x04\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1865(self):
		result = SimpleJSONTestFunction("\"  \"\n\x10\x00\x00\n\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1866(self):
		result = SimpleJSONTestFunction("\"  \"\n\t\t\x07\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1867(self):
		result = SimpleJSONTestFunction("\"\x11\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1868(self):
		result = SimpleJSONTestFunction("-Infinity\n\x0F\x00\n\x00\n")
		self.assertEqual(result, expected_result)

	def test_1869(self):
		result = SimpleJSONTestFunction("\"P\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1870(self):
		result = SimpleJSONTestFunction("\t \n0e0\x00\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1871(self):
		result = SimpleJSONTestFunction("\n\"\x11\x0D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1872(self):
		result = SimpleJSONTestFunction("-0 \x02\x00\x00\x00\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1873(self):
		result = SimpleJSONTestFunction("\n\"\x11\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1874(self):
		result = SimpleJSONTestFunction("5\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1875(self):
		result = SimpleJSONTestFunction("\"  !0\n'\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1876(self):
		result = SimpleJSONTestFunction("\t \t\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1877(self):
		result = SimpleJSONTestFunction("\"  \"\t\t\t\t\t\x11\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1878(self):
		result = SimpleJSONTestFunction("\n \t0\t\t\x12\x00\x00\n\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1879(self):
		result = SimpleJSONTestFunction("\t0\t\t \x01\n\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1880(self):
		result = SimpleJSONTestFunction("\"P\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1881(self):
		result = SimpleJSONTestFunction("\t\"\x01\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1882(self):
		result = SimpleJSONTestFunction(" \x15\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1883(self):
		result = SimpleJSONTestFunction("\t\t0E\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1884(self):
		result = SimpleJSONTestFunction("-7\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1885(self):
		result = SimpleJSONTestFunction("\t0\n\t\t\t\x07\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1886(self):
		result = SimpleJSONTestFunction("\" 00\"\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1887(self):
		result = SimpleJSONTestFunction("\"  \"\n\t\t\x00\x00\x00\x00\x00\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1888(self):
		result = SimpleJSONTestFunction("\" 00\"\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1889(self):
		result = SimpleJSONTestFunction("\"   \x10\x0D\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1890(self):
		result = SimpleJSONTestFunction("-2\x80\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1891(self):
		result = SimpleJSONTestFunction("\"   \"\t\t\n\x02\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1892(self):
		result = SimpleJSONTestFunction("\t \n0e0\x00\x00\x00\x00\x00\n\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1893(self):
		result = SimpleJSONTestFunction("\t\t \x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1894(self):
		result = SimpleJSONTestFunction("\"  ! \x11\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1895(self):
		result = SimpleJSONTestFunction("-Infinity\n\x06\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1896(self):
		result = SimpleJSONTestFunction("\t0\t\t\t\n\x0E\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1897(self):
		result = SimpleJSONTestFunction("\n \n0e0\x00\x00\x00\x00\n\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1898(self):
		result = SimpleJSONTestFunction("-Infinity\t \x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1899(self):
		result = SimpleJSONTestFunction("\"\x10 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1900(self):
		result = SimpleJSONTestFunction("\"  \" \x12\x00\x00\x00\x00\x00\x00\x00\x00\n")
		self.assertEqual(result, expected_result)

	def test_1901(self):
		result = SimpleJSONTestFunction("\"  \"\n\t\t\t\t\x02\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1902(self):
		result = SimpleJSONTestFunction("\t0e+\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1903(self):
		result = SimpleJSONTestFunction("\t\"\n\\\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1904(self):
		result = SimpleJSONTestFunction("\"  \" \t \t\t\x10\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1905(self):
		result = SimpleJSONTestFunction("\t0\t\n\t\t\t\t\t\x02\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1906(self):
		result = SimpleJSONTestFunction("\t0\t\t\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_1907(self):
		result = SimpleJSONTestFunction("-Infinity \t\x01\n\x00\x00")
		self.assertEqual(result, expected_result)


if __name__ == '__main__':
	unittest.main()