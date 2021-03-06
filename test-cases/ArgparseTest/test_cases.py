import unittest
import argparse

class ArgarseTestFunction(arg1_name, arg2_name, arg1, arg2):
	parser = argparse.ArgumentParser(description="Symtest")
	parser.add_argument(arg1_name)
	parser.add_argument(arg2_name)
	parser.parse_args(arg1, arg2)

class ArgparserTest(unittest.TestCase):
	def test_1(self):
		result = ArgarseTestFunction("\x00\x00\x00", "\x00\x00\x00", "\x00\x00\x00", "\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_2(self):
		result = ArgarseTestFunction("\x00\x00\x00", "\x01\x00\x00", "\x00\x00\x00", "\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_3(self):
		result = ArgarseTestFunction("\x00\x00\x01", "\x00\x00\x00", "\x00\x00\x01", "\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_4(self):
		result = ArgarseTestFunction("\n\x00\x00", "`\x00\x00", "`\x00\x00", "\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_5(self):
		result = ArgarseTestFunction("\x00\xAA`", "\x00\x00\x01", "\x00\xAA`", "\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_6(self):
		result = ArgarseTestFunction("\x00\x00\x01", "\x00\x00\x00", "\x00\x00\x00", "\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_7(self):
		result = ArgarseTestFunction("\x00\x00\x10", "\x00\x00\x00", "\x00\x00\x00", "\x00\x00\x10")
		self.assertEqual(result, expected_result)

	def test_8(self):
		result = ArgarseTestFunction("\x00\x10\x00", "\x00\x00\x00", "\x00\x00\x00", "\x00\x10\x00")
		self.assertEqual(result, expected_result)

	def test_9(self):
		result = ArgarseTestFunction("\x00\x00\x01", "8\x00\x00", "\x00\x00\x01", "8\x00\x00")
		self.assertEqual(result, expected_result)

	def test_10(self):
		result = ArgarseTestFunction("\x00\x00(", "\x00\x00\x00", "\x00\x00\x00", "\x00\x00(")
		self.assertEqual(result, expected_result)

	def test_11(self):
		result = ArgarseTestFunction("\x00\x01\x00", "\x00\x00\x00", "\x00\x00\x00", "\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_12(self):
		result = ArgarseTestFunction("\x01\x00\x00", "\x00\x00\x00", "\x00\x00\x00", "\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_13(self):
		result = ArgarseTestFunction("\x00\n\x00", "\x00\x00\x00", "\x00\x00\x00", "\x00\n\x00")
		self.assertEqual(result, expected_result)

	def test_14(self):
		result = ArgarseTestFunction("-\x00\x00", "\x00\x00\x00", "-\x00\x00", "\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_15(self):
		result = ArgarseTestFunction("-\x01-", "\x00\x00\x00", "-\x01-", "\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_16(self):
		result = ArgarseTestFunction("-\x01\x00", "\x00\x00\x00", "-\x01\x00", "\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_17(self):
		result = ArgarseTestFunction("\x00\x00 ", "\x00\x00\x00", "\x00\x00\x00", "\x00\x00 ")
		self.assertEqual(result, expected_result)

	def test_18(self):
		result = ArgarseTestFunction("\n\x00\x00", "\x00\x00\x00", "\x00\x00\x00", "\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_19(self):
		result = ArgarseTestFunction("-\x00\x00", "\x00\x00\x00", "\x00\x00\x00", "-\x00\x00")
		self.assertEqual(result, expected_result)

	def test_20(self):
		result = ArgarseTestFunction("\x00\x00@", "\x00\x00\x00", "\x00\x00\x00", "\x00\x00@")
		self.assertEqual(result, expected_result)

	def test_21(self):
		result = ArgarseTestFunction("-\x00\x00", "\x00\x00\x00", "\x00\x00\x00", "-\x00\x00")
		self.assertEqual(result, expected_result)

	def test_22(self):
		result = ArgarseTestFunction("\x00\x000", "\x00\x00\x00", "\x00\x00\x00", "\x00\x000")
		self.assertEqual(result, expected_result)

	def test_23(self):
		result = ArgarseTestFunction("-\x00\x00", "\x00\x00\x00", "\x00\x00\x00", "-\x00\x00")
		self.assertEqual(result, expected_result)

	def test_24(self):
		result = ArgarseTestFunction("--\x00", "\x00\x00\x00", "--\x00", "\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_25(self):
		result = ArgarseTestFunction("--h", "\x00\x00\x00", "--h", "\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_26(self):
		result = ArgarseTestFunction("-\x00\x00", "\x00\x00\x00", "\x00\x00\x00", "-\x00\x00")
		self.assertEqual(result, expected_result)

	def test_27(self):
		result = ArgarseTestFunction("-\x00\x01", "\x01\x00\x00", "\x01\x00\x00", "-\x00\x01")
		self.assertEqual(result, expected_result)

	def test_28(self):
		result = ArgarseTestFunction("\x00\x10 ", "\x00\x00\x00", "\x00\x00\x00", "\x00\x10 ")
		self.assertEqual(result, expected_result)

	def test_29(self):
		result = ArgarseTestFunction("-\x00\x00", "\x00\x00\x00", "\x00\x00\x00", "-\x00\x00")
		self.assertEqual(result, expected_result)

	def test_30(self):
		result = ArgarseTestFunction("-\x00\x00", "\x00\x00\x00", "\x00\x00\x00", "-\x00\x00")
		self.assertEqual(result, expected_result)

	def test_31(self):
		result = ArgarseTestFunction("-\x00\x00", "\x00\x00\x00", "\x00\x00\x00", "-\x00\x00")
		self.assertEqual(result, expected_result)

	def test_32(self):
		result = ArgarseTestFunction("-\x01 ", "\x00\x00\x00", "-\x01 ", "\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_33(self):
		result = ArgarseTestFunction("-\x01\x00", "\x00\x00\x00", "\x00\x00\x00", "-\x01\x00")
		self.assertEqual(result, expected_result)

	def test_34(self):
		result = ArgarseTestFunction("-\x01 ", "\x00\x00\x00", "\x00\x00\x00", "-\x01 ")
		self.assertEqual(result, expected_result)

	def test_35(self):
		result = ArgarseTestFunction("--\x00", "\x00\x00\x00", "\x00\x00\x00", "--\x00")
		self.assertEqual(result, expected_result)

	def test_36(self):
		result = ArgarseTestFunction("-\x01 ", "\x00\x00\x00", "\x00\x00\x00", "-\x01 ")
		self.assertEqual(result, expected_result)

	def test_37(self):
		result = ArgarseTestFunction("-\x01\x00", "\x00\x00\x00", "\x00\x00\x00", "-\x01\x00")
		self.assertEqual(result, expected_result)

	def test_38(self):
		result = ArgarseTestFunction("--h", "\x00\x00\x00", "\x00\x00\x00", "--h")
		self.assertEqual(result, expected_result)

	def test_39(self):
		result = ArgarseTestFunction("--h", "\x00\x00\x00", "\x00\x00\x00", "--h")
		self.assertEqual(result, expected_result)

	def test_40(self):
		result = ArgarseTestFunction("\x08\x00\x00", "\x00\x00\x00", "\x08\x00\x00", "\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_41(self):
		result = ArgarseTestFunction("-\x01 ", "\x00\x00\x00", "\x00\x00\x00", "-\x01 ")
		self.assertEqual(result, expected_result)

	def test_42(self):
		result = ArgarseTestFunction("-=\xFF", "\x00\x00\x00", "\x00\x00\x00", "-=\xFF")
		self.assertEqual(result, expected_result)

	def test_43(self):
		result = ArgarseTestFunction("-\x00\x03", "\x90\x00\x00", "\x90\x00\x00", "-\x00\x03")
		self.assertEqual(result, expected_result)

	def test_44(self):
		result = ArgarseTestFunction("-\x01\x00", "\x00\x00\x00", "\x00\x00\x00", "-\x01\x00")
		self.assertEqual(result, expected_result)

	def test_45(self):
		result = ArgarseTestFunction("\x01\x00\x00", "\x01\x00\x00", "\x00\x00\x00", "\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_46(self):
		result = ArgarseTestFunction("-h\x00", "\x00\x00\x00", "-h\x00", "\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_47(self):
		result = ArgarseTestFunction("-\x00\x02", "\x14\x00\x00", "\x14\x00\x00", "-\x00\x02")
		self.assertEqual(result, expected_result)

	def test_48(self):
		result = ArgarseTestFunction("\x00\x00\x00", "\x01\x00\x00", "\x00\x00\x00", "\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_49(self):
		result = ArgarseTestFunction("\x00\x00\x00", "-\x00\x00", "\x00\x00\x00", "-\x00\x00")
		self.assertEqual(result, expected_result)

	def test_50(self):
		result = ArgarseTestFunction("\x00\x00\x00", "-\x00\x00", "\x00\x00\x00", "-\x00\x00")
		self.assertEqual(result, expected_result)

	def test_51(self):
		result = ArgarseTestFunction("\x00\x00\x00", "-\x00 ", "\x00\x00\x00", "-\x00 ")
		self.assertEqual(result, expected_result)

	def test_52(self):
		result = ArgarseTestFunction("\x00\x00\x00", "--\x00", "\x00\x00\x00", "--\x00")
		self.assertEqual(result, expected_result)

	def test_53(self):
		result = ArgarseTestFunction("\x00\x00\x00", "-\x00 ", "\x00\x00\x00", "-\x00 ")
		self.assertEqual(result, expected_result)

	def test_54(self):
		result = ArgarseTestFunction("\x00\x00\x00", "--h", "\x00\x00\x00", "--h")
		self.assertEqual(result, expected_result)

	def test_55(self):
		result = ArgarseTestFunction("-hh", "\x00\x00\x00", "-hh", "\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_56(self):
		result = ArgarseTestFunction("-\x00\x00", "\x00\x00\x00", "\x00\x00\x00", "-\x00\x00")
		self.assertEqual(result, expected_result)

	def test_57(self):
		result = ArgarseTestFunction("\x1C\x00\x00", "-\xB1\x01", "\x1C\x00\x00", "-\xB1\x01")
		self.assertEqual(result, expected_result)

	def test_58(self):
		result = ArgarseTestFunction("\x00\x00\x00", "-\x00 ", "\x00\x00\x00", "-\x00 ")
		self.assertEqual(result, expected_result)

	def test_59(self):
		result = ArgarseTestFunction("-\x01 ", "\x00\x00\x00", "\x00\x00\x00", "-\x01 ")
		self.assertEqual(result, expected_result)

	def test_60(self):
		result = ArgarseTestFunction("\x01\x00\x00", "-\x00\x00", "-\x00\x00", "\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_61(self):
		result = ArgarseTestFunction("\x00\x00\x00", "-\x00 ", "\x00\x00\x00", "-\x00 ")
		self.assertEqual(result, expected_result)

	def test_62(self):
		result = ArgarseTestFunction("-\x01 ", "\x00\x00\x00", "\x00\x00\x00", "-\x01 ")
		self.assertEqual(result, expected_result)

	def test_63(self):
		result = ArgarseTestFunction("\x01\x00\x10", "-\x00\x00", "-\x00\x00", "\x01\x00\x10")
		self.assertEqual(result, expected_result)

	def test_64(self):
		result = ArgarseTestFunction("4\x00\x00", "-\x01\x01", "-\x01\x01", "4\x00\x00")
		self.assertEqual(result, expected_result)

	def test_65(self):
		result = ArgarseTestFunction("\x00\x00\x01", "-\x00\x00", "-\x00\x00", "\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_66(self):
		result = ArgarseTestFunction("\x10\x00\x00", "\x10\x00\x00", "\x00\x00\x00", "\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_67(self):
		result = ArgarseTestFunction("-\x01 ", "\x00\x00\x00", "\x00\x00\x00", "-\x01 ")
		self.assertEqual(result, expected_result)

	def test_68(self):
		result = ArgarseTestFunction("\x00\x00\x00", "-\x00 ", "\x00\x00\x00", "-\x00 ")
		self.assertEqual(result, expected_result)

	def test_69(self):
		result = ArgarseTestFunction("\n\x00\x00", "-\x01\x01", "-\x01\x01", "\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_70(self):
		result = ArgarseTestFunction("\xC1\x00@", "-\x01\x01", "-\x01\x01", "\xC1\x00@")
		self.assertEqual(result, expected_result)

	def test_71(self):
		result = ArgarseTestFunction("\n\x00\x00", "\n\x00\x00", "\x00\x00\x00", "\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_72(self):
		result = ArgarseTestFunction("\x00\x01\x00", "-\x01\x01", "-\x01\x01", "\x00\x01\x00")
		self.assertEqual(result, expected_result)

	def test_73(self):
		result = ArgarseTestFunction("-\x01 ", "-\x00\x00", "-\x01 ", "-\x00\x00")
		self.assertEqual(result, expected_result)

	def test_74(self):
		result = ArgarseTestFunction("-\x00\x00", "\x00\x00\x00", "\x00\x00\x00", "-\x00\x00")
		self.assertEqual(result, expected_result)

	def test_75(self):
		result = ArgarseTestFunction("-\x01 ", "-\x01\x00", "-\x01 ", "-\x01\x00")
		self.assertEqual(result, expected_result)

	def test_76(self):
		result = ArgarseTestFunction("\n\x00@", "-\x01\x01", "-\x01\x01", "\n\x00@")
		self.assertEqual(result, expected_result)

	def test_77(self):
		result = ArgarseTestFunction("\x00\x10\x00", "-\x00\x00", "-\x00\x00", "\x00\x10\x00")
		self.assertEqual(result, expected_result)

	def test_78(self):
		result = ArgarseTestFunction("\x01\x00\x00", "--\x00", "--\x00", "\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_79(self):
		result = ArgarseTestFunction("-\x00 ", "\x00\x00\x00", "-\x00 ", "\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_80(self):
		result = ArgarseTestFunction("-\x00\x04", "\x11\x00\x00", "\x11\x00\x00", "-\x00\x04")
		self.assertEqual(result, expected_result)

	def test_81(self):
		result = ArgarseTestFunction("\x00\x00\x01", "\x00\x00\x00", "\x00\x00\x00", "\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_82(self):
		result = ArgarseTestFunction("]\x00\x00", "-\x01\x01", "-\x01\x01", "]\x00\x00")
		self.assertEqual(result, expected_result)

	def test_83(self):
		result = ArgarseTestFunction("\x00\x00\x01", "\x00\x00\x01", "\x00\x00\x00", "\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_84(self):
		result = ArgarseTestFunction("-\x00\x00", "-\x00\x00", "\x00\x00\x00", "\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_85(self):
		result = ArgarseTestFunction("\x00\x00\x00", "-\x00 ", "\x00\x00\x00", "-\x00 ")
		self.assertEqual(result, expected_result)

	def test_86(self):
		result = ArgarseTestFunction("\x01\x00P", "-\x00\x00", "-\x00\x00", "\x01\x00P")
		self.assertEqual(result, expected_result)

	def test_87(self):
		result = ArgarseTestFunction("-\x00\x06", "\x02\x00\x00", "\x02\x00\x00", "-\x00\x06")
		self.assertEqual(result, expected_result)

	def test_88(self):
		result = ArgarseTestFunction("\x01\x00\x00", "-h\x00", "-h\x00", "\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_89(self):
		result = ArgarseTestFunction("\x01\x00\x00", "--h", "--h", "\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_90(self):
		result = ArgarseTestFunction("-\x00\x00", "\x00\x00\x00", "-\x00\x00", "\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_91(self):
		result = ArgarseTestFunction("\x01\x00\x10", "-h\x00", "-h\x00", "\x01\x00\x10")
		self.assertEqual(result, expected_result)

	def test_92(self):
		result = ArgarseTestFunction("\x01\x000", "-h\x00", "-h\x00", "\x01\x000")
		self.assertEqual(result, expected_result)

	def test_93(self):
		result = ArgarseTestFunction("\x00\x00\x10", "-\x00\x00", "-\x00\x00", "\x00\x00\x10")
		self.assertEqual(result, expected_result)

	def test_94(self):
		result = ArgarseTestFunction("\x01\x00\x00", "-h\x10", "-h\x10", "\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_95(self):
		result = ArgarseTestFunction("--\x00", "\x00\x00\x00", "\x00\x00\x00", "--\x00")
		self.assertEqual(result, expected_result)

	def test_96(self):
		result = ArgarseTestFunction("\x00\x00\x00", "-\x00 ", "\x00\x00\x00", "-\x00 ")
		self.assertEqual(result, expected_result)

	def test_97(self):
		result = ArgarseTestFunction("\x00\x00\x00", "-\x00\x00", "\x00\x00\x00", "-\x00\x00")
		self.assertEqual(result, expected_result)

	def test_98(self):
		result = ArgarseTestFunction("-h\x0D", "\x00\x00\x00", "-h\x0D", "\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_99(self):
		result = ArgarseTestFunction("\x00\x00(", "-\x00\x00", "-\x00\x00", "\x00\x00(")
		self.assertEqual(result, expected_result)

	def test_100(self):
		result = ArgarseTestFunction("\x10\x00\x10", "\x10\x00\x10", "\x00\x00\x00", "\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_101(self):
		result = ArgarseTestFunction("\n\x000", "-h\x00", "-h\x00", "\n\x000")
		self.assertEqual(result, expected_result)

	def test_102(self):
		result = ArgarseTestFunction("\x00\x00\x00", "--\x00", "\x00\x00\x00", "--\x00")
		self.assertEqual(result, expected_result)

	def test_103(self):
		result = ArgarseTestFunction("\xD1\x000", "-\x01\x01", "-\x01\x01", "\xD1\x000")
		self.assertEqual(result, expected_result)

	def test_104(self):
		result = ArgarseTestFunction("-\x10\x00", "-\x10\x00", "\x00\x00\x00", "\x00\x00\x00")
		self.assertEqual(result, expected_result)

	def test_105(self):
		result = ArgarseTestFunction("\x01\x00\x10", "\x00\x00\x00", "\x00\x00\x00", "\x01\x00\x10")
		self.assertEqual(result, expected_result)

	def test_106(self):
		result = ArgarseTestFunction("\x01\x00 ", "--h", "--h", "\x01\x00 ")
		self.assertEqual(result, expected_result)

	def test_107(self):
		result = ArgarseTestFunction("\x81\x00p", "-h\x00", "-h\x00", "\x81\x00p")
		self.assertEqual(result, expected_result)

	def test_108(self):
		result = ArgarseTestFunction("\x00\x00\x00", "-\x00 ", "\x00\x00\x00", "-\x00 ")
		self.assertEqual(result, expected_result)

	def test_109(self):
		result = ArgarseTestFunction("-\x00\x07", "\x02\x00\x00", "\x02\x00\x00", "-\x00\x07")
		self.assertEqual(result, expected_result)

	def test_110(self):
		result = ArgarseTestFunction("\x00\x00\x00", "--h", "\x00\x00\x00", "--h")
		self.assertEqual(result, expected_result)

	def test_111(self):
		result = ArgarseTestFunction("\n\x00P", "-\x00\x00", "-\x00\x00", "\n\x00P")
		self.assertEqual(result, expected_result)

	def test_112(self):
		result = ArgarseTestFunction("-\x00\x05", "\x01\x00\x00", "\x01\x00\x00", "-\x00\x05")
		self.assertEqual(result, expected_result)

	def test_113(self):
		result = ArgarseTestFunction("\x00\x00\x00", "\n\x00\x00", "\x00\x00\x00", "\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_114(self):
		result = ArgarseTestFunction("-\x01 ", "--\x00", "-\x01 ", "--\x00")
		self.assertEqual(result, expected_result)

	def test_115(self):
		result = ArgarseTestFunction("\x00\x00\x00", "-\x00\x00", "\x00\x00\x00", "-\x00\x00")
		self.assertEqual(result, expected_result)

	def test_116(self):
		result = ArgarseTestFunction("-\x01\x00", "-\x00\x00", "-\x01\x00", "-\x00\x00")
		self.assertEqual(result, expected_result)

	def test_117(self):
		result = ArgarseTestFunction("-\x01\x00", "-\x01\x00", "-\x01\x00", "-\x01\x00")
		self.assertEqual(result, expected_result)

	def test_118(self):
		result = ArgarseTestFunction("\n\x00\x10", "-h\x00", "-h\x00", "\n\x00\x10")
		self.assertEqual(result, expected_result)

	def test_119(self):
		result = ArgarseTestFunction("\x00\x00\x00", "-\x00\x00", "\x00\x00\x00", "-\x00\x00")
		self.assertEqual(result, expected_result)

	def test_120(self):
		result = ArgarseTestFunction("\xB1\x00\x10", "-\x01\x01", "-\x01\x01", "\xB1\x00\x10")
		self.assertEqual(result, expected_result)

	def test_121(self):
		result = ArgarseTestFunction("-\x01 ", "--h", "-\x01 ", "--h")
		self.assertEqual(result, expected_result)

	def test_122(self):
		result = ArgarseTestFunction("-h\x00", "\x00\x00\x00", "\x00\x00\x00", "-h\x00")
		self.assertEqual(result, expected_result)

	def test_123(self):
		result = ArgarseTestFunction("\x01\x00\x00", "-\x00=", "-\x00=", "\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_124(self):
		result = ArgarseTestFunction("\x00\x00\x01", "--\x00", "--\x00", "\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_125(self):
		result = ArgarseTestFunction("-\x01\x00", "\x00\x00\x00", "\x00\x00\x00", "-\x01\x00")
		self.assertEqual(result, expected_result)

	def test_126(self):
		result = ArgarseTestFunction("\x01\x00\x10", "--h", "--h", "\x01\x00\x10")
		self.assertEqual(result, expected_result)

	def test_127(self):
		result = ArgarseTestFunction("\x01\x00\x00", "-hh", "-hh", "\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_128(self):
		result = ArgarseTestFunction("\n\x00\x00", "-h\x10", "-h\x10", "\n\x00\x00")
		self.assertEqual(result, expected_result)

	def test_129(self):
		result = ArgarseTestFunction("\x00\x00\x01", "--h", "--h", "\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_130(self):
		result = ArgarseTestFunction("-\x00\x00", "\x00\x00\x00", "\x00\x00\x00", "-\x00\x00")
		self.assertEqual(result, expected_result)

	def test_131(self):
		result = ArgarseTestFunction("\x00\x80\x02", "--h", "--h", "\x00\x80\x02")
		self.assertEqual(result, expected_result)

	def test_132(self):
		result = ArgarseTestFunction("-\x00\x0E", "\x02\x00\x00", "\x02\x00\x00", "-\x00\x0E")
		self.assertEqual(result, expected_result)

	def test_133(self):
		result = ArgarseTestFunction("-hh", "\x00\x00\x00", "\x00\x00\x00", "-hh")
		self.assertEqual(result, expected_result)

	def test_134(self):
		result = ArgarseTestFunction("\x01\x000", "--h", "--h", "\x01\x000")
		self.assertEqual(result, expected_result)

	def test_135(self):
		result = ArgarseTestFunction("\x00\x00\x00", "--h", "\x00\x00\x00", "--h")
		self.assertEqual(result, expected_result)

	def test_136(self):
		result = ArgarseTestFunction("-\x01 ", "\x00\x00\x00", "\x00\x00\x00", "-\x01 ")
		self.assertEqual(result, expected_result)

	def test_137(self):
		result = ArgarseTestFunction(")\x00\x00", "\x00\x00\x00", "\x00\x00\x00", ")\x00\x00")
		self.assertEqual(result, expected_result)

	def test_138(self):
		result = ArgarseTestFunction("\x01\x00\x00", "-\x01\x00", "-\x01\x00", "\x01\x00\x00")
		self.assertEqual(result, expected_result)

	def test_139(self):
		result = ArgarseTestFunction("\x08\x00\x00", "-h\x00", "-h\x00", "\x08\x00\x00")
		self.assertEqual(result, expected_result)

	def test_140(self):
		result = ArgarseTestFunction("-=\x00", "\x00\x00\x00", "\x00\x00\x00", "-=\x00")
		self.assertEqual(result, expected_result)

	def test_141(self):
		result = ArgarseTestFunction("\x00\x00\x00", "--\x00", "\x00\x00\x00", "--\x00")
		self.assertEqual(result, expected_result)

	def test_142(self):
		result = ArgarseTestFunction("-\x01 ", "-h\x00", "-\x01 ", "-h\x00")
		self.assertEqual(result, expected_result)

	def test_143(self):
		result = ArgarseTestFunction("\x00\x00\x00", "-\x00 ", "\x00\x00\x00", "-\x00 ")
		self.assertEqual(result, expected_result)

	def test_144(self):
		result = ArgarseTestFunction("\x00\x00\x01", "Q\x80\x00", "\x00\x00\x01", "Q\x80\x00")
		self.assertEqual(result, expected_result)

	def test_145(self):
		result = ArgarseTestFunction("\x00\x00\x08", "\x00\x00\x00", "\x00\x00\x00", "\x00\x00\x08")
		self.assertEqual(result, expected_result)

	def test_146(self):
		result = ArgarseTestFunction("\x00\x00\x01", "-\x01\x00", "-\x01\x00", "\x00\x00\x01")
		self.assertEqual(result, expected_result)

	def test_147(self):
		result = ArgarseTestFunction("\x00\x00\x00", "-\x81\x01", "\x00\x00\x00", "-\x81\x01")
		self.assertEqual(result, expected_result)


if __name__ == '__main__':
	unittest.main()