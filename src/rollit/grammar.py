# This file was generated from grammar.peg
# See http://canopy.jcoglan.com/ for documentation.

from collections import defaultdict
import re


class TreeNode(object):
    def __init__(self, text, offset, elements):
        self.text = text
        self.offset = offset
        self.elements = elements

    def __iter__(self):
        for el in self.elements:
            yield el


class TreeNode1(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode1, self).__init__(text, offset, elements)
        self._ws = elements[2]


class TreeNode2(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode2, self).__init__(text, offset, elements)
        self._ = elements[2]
        self.statement = elements[1]


class TreeNode3(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode3, self).__init__(text, offset, elements)
        self._ = elements[0]


class TreeNode4(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode4, self).__init__(text, offset, elements)
        self._ = elements[0]


class TreeNode5(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode5, self).__init__(text, offset, elements)
        self._ = elements[0]


class TreeNode6(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode6, self).__init__(text, offset, elements)
        self._ = elements[1]


class TreeNode7(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode7, self).__init__(text, offset, elements)
        self.keyword = elements[0]


class TreeNode8(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode8, self).__init__(text, offset, elements)
        self._ws = elements[4]
        self._ = elements[5]
        self.statement = elements[3]


class TreeNode9(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode9, self).__init__(text, offset, elements)
        self._ = elements[2]
        self.statement = elements[1]


class TreeNode10(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode10, self).__init__(text, offset, elements)
        self._ = elements[2]


class TreeNode11(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode11, self).__init__(text, offset, elements)
        self._ws = elements[0]
        self._ = elements[1]


class TreeNode12(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode12, self).__init__(text, offset, elements)
        self.expression = elements[3]
        self._ = elements[2]


class TreeNode13(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode13, self).__init__(text, offset, elements)
        self._ws = elements[3]
        self._ = elements[4]


class TreeNode14(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode14, self).__init__(text, offset, elements)
        self.roll_item = elements[0]
        self._ = elements[1]
        self._ws = elements[2]


class TreeNode15(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode15, self).__init__(text, offset, elements)
        self._ = elements[3]


class TreeNode16(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode16, self).__init__(text, offset, elements)
        self._ws = elements[3]
        self.expression = elements[2]
        self._ = elements[4]


class TreeNode17(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode17, self).__init__(text, offset, elements)
        self._ = elements[1]


class TreeNode18(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode18, self).__init__(text, offset, elements)
        self._ = elements[1]


class TreeNode19(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode19, self).__init__(text, offset, elements)
        self._ = elements[3]
        self.two_sided_op = elements[1]


class TreeNode20(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode20, self).__init__(text, offset, elements)
        self._ = elements[3]
        self.two_sided_op = elements[1]


class TreeNode21(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode21, self).__init__(text, offset, elements)
        self._ = elements[3]
        self.one_sided_op = elements[1]


class TreeNode22(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode22, self).__init__(text, offset, elements)
        self.basic_name = elements[0]
        self._ = elements[1]


class TreeNode23(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode23, self).__init__(text, offset, elements)
        self._ = elements[3]
        self.special_accessor = elements[1]


class TreeNode24(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode24, self).__init__(text, offset, elements)
        self._ = elements[4]
        self.special_entry = elements[2]


class TreeNode25(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode25, self).__init__(text, offset, elements)
        self._ = elements[4]
        self.expression = elements[2]


class TreeNode26(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode26, self).__init__(text, offset, elements)
        self.reduce = elements[0]
        self._ = elements[1]


class TreeNode27(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode27, self).__init__(text, offset, elements)
        self._ = elements[4]
        self.special_entry = elements[2]


class TreeNode28(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode28, self).__init__(text, offset, elements)
        self.accessing = elements[0]


class TreeNode29(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode29, self).__init__(text, offset, elements)
        self._ws = elements[0]
        self.accessor = elements[1]


class TreeNode30(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode30, self).__init__(text, offset, elements)
        self._ = elements[4]
        self.special_entry = elements[2]


class TreeNode31(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode31, self).__init__(text, offset, elements)
        self._ = elements[0]


class TreeNode32(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode32, self).__init__(text, offset, elements)
        self._ = elements[0]


class TreeNode33(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode33, self).__init__(text, offset, elements)
        self._ = elements[6]
        self.expression = elements[7]
        self.anor = elements[4]


class TreeNode34(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode34, self).__init__(text, offset, elements)
        self._ = elements[0]
        self.anor = elements[1]


class TreeNode35(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode35, self).__init__(text, offset, elements)
        self.comparison = elements[0]
        self._ = elements[3]
        self.anor_op = elements[2]
        self.anor = elements[4]


class TreeNode36(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode36, self).__init__(text, offset, elements)
        self.roll_math = elements[0]
        self._ = elements[3]
        self.comp_op = elements[2]
        self.comparison = elements[4]


class TreeNode37(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode37, self).__init__(text, offset, elements)
        self.add_math = elements[0]
        self._ = elements[4]
        self.roll_math = elements[5]


class TreeNode38(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode38, self).__init__(text, offset, elements)
        self.mult_math = elements[0]
        self._ = elements[4]
        self.add_op = elements[2]
        self.add_math = elements[5]


class TreeNode39(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode39, self).__init__(text, offset, elements)
        self.lambda_expr = elements[0]
        self._ = elements[4]
        self.mult_op = elements[2]
        self.mult_math = elements[5]


class TreeNode40(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode40, self).__init__(text, offset, elements)
        self.first_modifier_call = elements[0]


class TreeNode41(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode41, self).__init__(text, offset, elements)
        self.reduce_expr = elements[5]
        self._ = elements[3]


class TreeNode42(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode42, self).__init__(text, offset, elements)
        self._ws = elements[2]
        self.expression = elements[1]
        self._ = elements[3]


class TreeNode43(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode43, self).__init__(text, offset, elements)
        self.access = elements[0]
        self._ = elements[1]


class TreeNode44(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode44, self).__init__(text, offset, elements)
        self.dice = elements[0]
        self._ = elements[3]
        self.modifier_tail = elements[4]


class TreeNode45(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode45, self).__init__(text, offset, elements)
        self._ws = elements[0]
        self._ = elements[1]
        self.modifier_tail = elements[2]


class TreeNode46(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode46, self).__init__(text, offset, elements)
        self._ws = elements[0]
        self._ = elements[4]


class TreeNode47(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode47, self).__init__(text, offset, elements)
        self.expression = elements[0]
        self._ = elements[1]
        self._ws = elements[2]


class TreeNode48(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode48, self).__init__(text, offset, elements)
        self.basic_name = elements[0]
        self._ = elements[1]
        self._ws = elements[2]


class TreeNode49(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode49, self).__init__(text, offset, elements)
        self.modifier_params = elements[0]
        self._ = elements[4]
        self.expression = elements[5]


class TreeNode50(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode50, self).__init__(text, offset, elements)
        self.modifier_params = elements[0]
        self._ = elements[6]
        self._ws = elements[2]


class TreeNode51(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode51, self).__init__(text, offset, elements)
        self._ = elements[3]
        self.special_entry = elements[1]


class TreeNode52(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode52, self).__init__(text, offset, elements)
        self.modifier_def_target = elements[0]
        self._ = elements[1]
        self._ws = elements[3]


class TreeNode53(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode53, self).__init__(text, offset, elements)
        self._ = elements[1]
        self._ws = elements[3]


class TreeNode54(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode54, self).__init__(text, offset, elements)
        self._ws = elements[0]
        self.stmt_or_expr = elements[1]


class TreeNode55(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode55, self).__init__(text, offset, elements)
        self._ = elements[2]
        self.expression = elements[1]
        self.then = elements[3]


class TreeNode56(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode56, self).__init__(text, offset, elements)
        self._ = elements[2]
        self.expression = elements[1]
        self.then = elements[3]


class TreeNode57(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode57, self).__init__(text, offset, elements)
        self._ws = elements[0]
        self.stmt_or_expr = elements[1]


class TreeNode58(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode58, self).__init__(text, offset, elements)
        self.basic_name = elements[0]
        self._ = elements[1]
        self._ws = elements[2]


class TreeNode59(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode59, self).__init__(text, offset, elements)
        self.access = elements[0]
        self._ = elements[1]
        self._ws = elements[2]


class TreeNode60(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode60, self).__init__(text, offset, elements)
        self._ = elements[0]
        self.access = elements[1]


class TreeNode61(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode61, self).__init__(text, offset, elements)
        self._ = elements[0]
        self.loadable = elements[1]


class TreeNode62(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode62, self).__init__(text, offset, elements)
        self._ = elements[4]
        self.load_from = elements[3]


class TreeNode63(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode63, self).__init__(text, offset, elements)
        self._ = elements[4]
        self.loadable = elements[1]
        self.load_from = elements[3]
        self.load_into = elements[5]


class TreeNode64(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode64, self).__init__(text, offset, elements)
        self._ = elements[2]
        self.loadable = elements[1]
        self.load_from = elements[3]


class TreeNode65(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode65, self).__init__(text, offset, elements)
        self._ = elements[2]
        self.loadable = elements[1]
        self.load_into = elements[3]


class TreeNode66(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode66, self).__init__(text, offset, elements)
        self._ = elements[0]
        self.loadable = elements[1]


class TreeNode67(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode67, self).__init__(text, offset, elements)
        self._ = elements[3]
        self.expression = elements[2]
        self.then = elements[4]


class TreeNode68(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode68, self).__init__(text, offset, elements)
        self._ = elements[1]


class TreeNode69(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode69, self).__init__(text, offset, elements)
        self._ = elements[1]


class TreeNode70(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode70, self).__init__(text, offset, elements)
        self._ = elements[1]


class TreeNode71(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode71, self).__init__(text, offset, elements)
        self._ = elements[1]
        self.statement = elements[2]


class TreeNode72(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode72, self).__init__(text, offset, elements)
        self.statement = elements[0]
        self._ = elements[1]


class TreeNode73(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode73, self).__init__(text, offset, elements)
        self._ = elements[0]
        self.basic_name = elements[1]


class TreeNode74(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode74, self).__init__(text, offset, elements)
        self.stmt_or_expr = elements[0]


class TreeNode75(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode75, self).__init__(text, offset, elements)
        self.expression = elements[0]
        self._ = elements[1]


class TreeNode76(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode76, self).__init__(text, offset, elements)
        self._ = elements[5]
        self.then = elements[6]


class TreeNode77(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode77, self).__init__(text, offset, elements)
        self._ = elements[0]
        self._ws = elements[1]
        self.stmt_or_expr = elements[2]


class TreeNode78(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode78, self).__init__(text, offset, elements)
        self._ws = elements[2]
        self.but_if_stmt = elements[1]
        self.always = elements[3]


class TreeNode79(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode79, self).__init__(text, offset, elements)
        self._ws = elements[2]
        self.but_if_stmt = elements[1]


class TreeNode80(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode80, self).__init__(text, offset, elements)
        self._ws = elements[0]
        self.always = elements[1]


class TreeNode81(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode81, self).__init__(text, offset, elements)
        self._ws = elements[0]
        self.but_if_stmt = elements[1]


class TreeNode82(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode82, self).__init__(text, offset, elements)
        self._ = elements[0]
        self.expression = elements[1]


class TreeNode83(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode83, self).__init__(text, offset, elements)
        self._ = elements[0]
        self.access = elements[1]


class TreeNode84(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode84, self).__init__(text, offset, elements)
        self._ = elements[0]
        self.restart_pos = elements[1]


class TreeNode85(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode85, self).__init__(text, offset, elements)
        self._ws = elements[3]
        self.block_body = elements[2]
        self._ = elements[4]


class TreeNode86(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode86, self).__init__(text, offset, elements)
        self._ws = elements[1]
        self._ = elements[2]


class TreeNode87(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode87, self).__init__(text, offset, elements)
        self._ = elements[4]
        self.access = elements[2]


class TreeNode88(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode88, self).__init__(text, offset, elements)
        self.if_then = elements[0]


class TreeNode89(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode89, self).__init__(text, offset, elements)
        self._ws = elements[0]
        self.unless = elements[1]


class TreeNode90(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode90, self).__init__(text, offset, elements)
        self._ws = elements[0]
        self.otherwise = elements[1]


class TreeNode91(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode91, self).__init__(text, offset, elements)
        self._ = elements[9]
        self.basic_name = elements[4]
        self.expression = elements[7]
        self.loop_body = elements[10]


class TreeNode92(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode92, self).__init__(text, offset, elements)
        self._ = elements[4]
        self.expression = elements[3]
        self.loop_body = elements[5]
        self._ws = elements[6]


class TreeNode93(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode93, self).__init__(text, offset, elements)
        self.except_when = elements[0]
        self._ws = elements[1]


class TreeNode94(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode94, self).__init__(text, offset, elements)
        self.access = elements[0]
        self._ = elements[2]
        self.modifier_tail = elements[3]


class TreeNode95(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode95, self).__init__(text, offset, elements)
        self.access = elements[0]
        self._ = elements[1]
        self.assign_op = elements[2]
        self._ws = elements[3]
        self.expression = elements[4]


class TreeNode96(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode96, self).__init__(text, offset, elements)
        self.expression = elements[0]
        self._ = elements[1]
        self.eos = elements[2]


class ParseError(SyntaxError):
    pass


FAILURE = object()


class Grammar(object):
    REGEX_1 = re.compile('^[^\\n\\r\\f]')
    REGEX_2 = re.compile('^[^\\n\\r\\f]')
    REGEX_3 = re.compile('^[ \\t]')
    REGEX_4 = re.compile('^[\\n\\r\\f]')
    REGEX_5 = re.compile('^[0-9a-zA-Z_]')
    REGEX_6 = re.compile('^[0-9a-zA-Z_]')
    REGEX_7 = re.compile('^[0-9a-zA-Z_]')
    REGEX_8 = re.compile('^[0-9a-zA-Z_]')
    REGEX_9 = re.compile('^[0-9a-zA-Z_]')
    REGEX_10 = re.compile('^[0-9a-zA-Z_]')
    REGEX_11 = re.compile('^[0-9a-zA-Z_]')
    REGEX_12 = re.compile('^[0-9a-zA-Z_]')
    REGEX_13 = re.compile('^[0-9a-zA-Z_]')
    REGEX_14 = re.compile('^[0-9a-zA-Z_]')
    REGEX_15 = re.compile('^[0-9a-zA-Z_]')
    REGEX_16 = re.compile('^[0-9a-zA-Z_]')
    REGEX_17 = re.compile('^[0-9a-zA-Z_]')
    REGEX_18 = re.compile('^[0-9a-zA-Z_]')
    REGEX_19 = re.compile('^[0-9a-zA-Z_]')
    REGEX_20 = re.compile('^[0-9a-zA-Z_]')
    REGEX_21 = re.compile('^[0-9a-zA-Z_]')
    REGEX_22 = re.compile('^[0-9a-zA-Z_]')
    REGEX_23 = re.compile('^[0-9a-zA-Z_]')
    REGEX_24 = re.compile('^[0-9a-zA-Z_]')
    REGEX_25 = re.compile('^[0-9a-zA-Z_]')
    REGEX_26 = re.compile('^[0-9a-zA-Z_]')
    REGEX_27 = re.compile('^[0-9a-zA-Z_]')
    REGEX_28 = re.compile('^[0-9a-zA-Z_]')
    REGEX_29 = re.compile('^[0-9a-zA-Z_]')
    REGEX_30 = re.compile('^[0-9a-zA-Z_]')
    REGEX_31 = re.compile('^[0-9a-zA-Z_]')
    REGEX_32 = re.compile('^[0-9a-zA-Z_]')
    REGEX_33 = re.compile('^[0-9a-zA-Z_]')
    REGEX_34 = re.compile('^[0-9a-zA-Z_]')
    REGEX_35 = re.compile('^[0-9a-zA-Z_]')
    REGEX_36 = re.compile('^[0-9a-zA-Z_]')
    REGEX_37 = re.compile('^[0-9a-zA-Z_]')
    REGEX_38 = re.compile('^[0-9a-zA-Z_]')
    REGEX_39 = re.compile('^[0-9a-zA-Z_]')
    REGEX_40 = re.compile('^[0-9a-zA-Z_]')
    REGEX_41 = re.compile('^[\\n\\r\\f \\t]')
    REGEX_42 = re.compile('^[\\n\\r\\f]')
    REGEX_43 = re.compile('^[0-9]')
    REGEX_44 = re.compile('^[0-9]')
    REGEX_45 = re.compile('^[0-9]')
    REGEX_46 = re.compile('^[\\\\runftvb\']')
    REGEX_47 = re.compile('^[^\']')
    REGEX_48 = re.compile('^[a-zA-Z_]')
    REGEX_49 = re.compile('^[a-zA-Z_0-9]')
    REGEX_50 = re.compile('^[a-z_A-Z]')

    def _read_start(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['start'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        index2 = self._offset
        address1 = self._read_shebang()
        if address1 is FAILURE:
            address1 = TreeNode(self._input[index2:index2], index2, [])
            self._offset = index2
        if address1 is not FAILURE:
            address2 = FAILURE
            remaining0, index3, elements1, address3 = 0, self._offset, [], True
            while address3 is not FAILURE:
                index4, elements2 = self._offset, []
                address4 = FAILURE
                address4 = self._read__()
                if address4 is not FAILURE:
                    elements2.append(address4)
                    address5 = FAILURE
                    address5 = self._read_statement()
                    if address5 is not FAILURE:
                        elements2.append(address5)
                        address6 = FAILURE
                        address6 = self._read__()
                        if address6 is not FAILURE:
                            elements2.append(address6)
                        else:
                            elements2 = None
                            self._offset = index4
                    else:
                        elements2 = None
                        self._offset = index4
                else:
                    elements2 = None
                    self._offset = index4
                if elements2 is None:
                    address3 = FAILURE
                else:
                    address3 = TreeNode2(self._input[index4:self._offset], index4, elements2)
                    self._offset = self._offset
                if address3 is not FAILURE:
                    elements1.append(address3)
                    remaining0 -= 1
            if remaining0 <= 0:
                address2 = TreeNode(self._input[index3:self._offset], index3, elements1)
                self._offset = self._offset
            else:
                address2 = FAILURE
            if address2 is not FAILURE:
                elements0.append(address2)
                address7 = FAILURE
                index5 = self._offset
                address7 = self._read_stmt_or_expr()
                if address7 is FAILURE:
                    address7 = TreeNode(self._input[index5:index5], index5, [])
                    self._offset = index5
                if address7 is not FAILURE:
                    elements0.append(address7)
                    address8 = FAILURE
                    address8 = self._read__ws()
                    if address8 is not FAILURE:
                        elements0.append(address8)
                    else:
                        elements0 = None
                        self._offset = index1
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.statements(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['start'][index0] = (address0, self._offset)
        return address0

    def _read_shebang(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['shebang'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        chunk0, max0 = None, self._offset + 2
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == '#!':
            address1 = TreeNode(self._input[self._offset:self._offset + 2], self._offset, [])
            self._offset = self._offset + 2
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'#!\'')
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            remaining0, index2, elements1, address3 = 0, self._offset, [], True
            while address3 is not FAILURE:
                chunk1, max1 = None, self._offset + 1
                if max1 <= self._input_size:
                    chunk1 = self._input[self._offset:max1]
                if chunk1 is not None and Grammar.REGEX_1.search(chunk1):
                    address3 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                    self._offset = self._offset + 1
                else:
                    address3 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('[^\\n\\r\\f]')
                if address3 is not FAILURE:
                    elements1.append(address3)
                    remaining0 -= 1
            if remaining0 <= 0:
                address2 = TreeNode(self._input[index2:self._offset], index2, elements1)
                self._offset = self._offset
            else:
                address2 = FAILURE
            if address2 is not FAILURE:
                elements0.append(address2)
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.ignore(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['shebang'][index0] = (address0, self._offset)
        return address0

    def _read_comment(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['comment'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        chunk0, max0 = None, self._offset + 2
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == '//':
            address1 = TreeNode(self._input[self._offset:self._offset + 2], self._offset, [])
            self._offset = self._offset + 2
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'//\'')
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            remaining0, index2, elements1, address3 = 0, self._offset, [], True
            while address3 is not FAILURE:
                chunk1, max1 = None, self._offset + 1
                if max1 <= self._input_size:
                    chunk1 = self._input[self._offset:max1]
                if chunk1 is not None and Grammar.REGEX_2.search(chunk1):
                    address3 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                    self._offset = self._offset + 1
                else:
                    address3 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('[^\\n\\r\\f]')
                if address3 is not FAILURE:
                    elements1.append(address3)
                    remaining0 -= 1
            if remaining0 <= 0:
                address2 = TreeNode(self._input[index2:self._offset], index2, elements1)
                self._offset = self._offset
            else:
                address2 = FAILURE
            if address2 is not FAILURE:
                elements0.append(address2)
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.ignore(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['comment'][index0] = (address0, self._offset)
        return address0

    def _read__(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['_'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        remaining0, index1, elements0, address1 = 0, self._offset, [], True
        while address1 is not FAILURE:
            chunk0, max0 = None, self._offset + 1
            if max0 <= self._input_size:
                chunk0 = self._input[self._offset:max0]
            if chunk0 is not None and Grammar.REGEX_3.search(chunk0):
                address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                self._offset = self._offset + 1
            else:
                address1 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('[ \\t]')
            if address1 is not FAILURE:
                elements0.append(address1)
                remaining0 -= 1
        if remaining0 <= 0:
            address0 = self._actions.ignore(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        else:
            address0 = FAILURE
        self._cache['_'][index0] = (address0, self._offset)
        return address0

    def _read_eol(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['eol'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        remaining0, index2, elements0, address1 = 1, self._offset, [], True
        while address1 is not FAILURE:
            address1 = self._read_comment()
            if address1 is not FAILURE:
                elements0.append(address1)
                remaining0 -= 1
        if remaining0 <= 0:
            address0 = TreeNode(self._input[index2:self._offset], index2, elements0)
            self._offset = self._offset
        else:
            address0 = FAILURE
        if address0 is FAILURE:
            self._offset = index1
            remaining1, index3, elements1, address2 = 1, self._offset, [], True
            while address2 is not FAILURE:
                chunk0, max0 = None, self._offset + 1
                if max0 <= self._input_size:
                    chunk0 = self._input[self._offset:max0]
                if chunk0 is not None and Grammar.REGEX_4.search(chunk0):
                    address2 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                    self._offset = self._offset + 1
                else:
                    address2 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('[\\n\\r\\f]')
                if address2 is not FAILURE:
                    elements1.append(address2)
                    remaining1 -= 1
            if remaining1 <= 0:
                address0 = self._actions.ignore(self._input, index3, self._offset, elements1)
                self._offset = self._offset
            else:
                address0 = FAILURE
            if address0 is FAILURE:
                self._offset = index1
        self._cache['eol'][index0] = (address0, self._offset)
        return address0

    def _read_keyword(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['keyword'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        index2, elements0 = self._offset, []
        address1 = FAILURE
        chunk0, max0 = None, self._offset + 5
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == 'leave':
            address1 = TreeNode(self._input[self._offset:self._offset + 5], self._offset, [])
            self._offset = self._offset + 5
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'leave\'')
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            index3 = self._offset
            chunk1, max1 = None, self._offset + 1
            if max1 <= self._input_size:
                chunk1 = self._input[self._offset:max1]
            if chunk1 is not None and Grammar.REGEX_5.search(chunk1):
                address2 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                self._offset = self._offset + 1
            else:
                address2 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('[0-9a-zA-Z_]')
            self._offset = index3
            if address2 is FAILURE:
                address2 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                self._offset = self._offset
            else:
                address2 = FAILURE
            if address2 is not FAILURE:
                elements0.append(address2)
            else:
                elements0 = None
                self._offset = index2
        else:
            elements0 = None
            self._offset = index2
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode(self._input[index2:self._offset], index2, elements0)
            self._offset = self._offset
        if address0 is FAILURE:
            self._offset = index1
            index4, elements1 = self._offset, []
            address3 = FAILURE
            chunk2, max2 = None, self._offset + 5
            if max2 <= self._input_size:
                chunk2 = self._input[self._offset:max2]
            if chunk2 == 'until':
                address3 = TreeNode(self._input[self._offset:self._offset + 5], self._offset, [])
                self._offset = self._offset + 5
            else:
                address3 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('\'until\'')
            if address3 is not FAILURE:
                elements1.append(address3)
                address4 = FAILURE
                index5 = self._offset
                chunk3, max3 = None, self._offset + 1
                if max3 <= self._input_size:
                    chunk3 = self._input[self._offset:max3]
                if chunk3 is not None and Grammar.REGEX_6.search(chunk3):
                    address4 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                    self._offset = self._offset + 1
                else:
                    address4 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('[0-9a-zA-Z_]')
                self._offset = index5
                if address4 is FAILURE:
                    address4 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                    self._offset = self._offset
                else:
                    address4 = FAILURE
                if address4 is not FAILURE:
                    elements1.append(address4)
                else:
                    elements1 = None
                    self._offset = index4
            else:
                elements1 = None
                self._offset = index4
            if elements1 is None:
                address0 = FAILURE
            else:
                address0 = TreeNode(self._input[index4:self._offset], index4, elements1)
                self._offset = self._offset
            if address0 is FAILURE:
                self._offset = index1
                index6, elements2 = self._offset, []
                address5 = FAILURE
                chunk4, max4 = None, self._offset + 2
                if max4 <= self._input_size:
                    chunk4 = self._input[self._offset:max4]
                if chunk4 == 'do':
                    address5 = TreeNode(self._input[self._offset:self._offset + 2], self._offset, [])
                    self._offset = self._offset + 2
                else:
                    address5 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('\'do\'')
                if address5 is not FAILURE:
                    elements2.append(address5)
                    address6 = FAILURE
                    index7 = self._offset
                    chunk5, max5 = None, self._offset + 1
                    if max5 <= self._input_size:
                        chunk5 = self._input[self._offset:max5]
                    if chunk5 is not None and Grammar.REGEX_7.search(chunk5):
                        address6 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                        self._offset = self._offset + 1
                    else:
                        address6 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('[0-9a-zA-Z_]')
                    self._offset = index7
                    if address6 is FAILURE:
                        address6 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                        self._offset = self._offset
                    else:
                        address6 = FAILURE
                    if address6 is not FAILURE:
                        elements2.append(address6)
                    else:
                        elements2 = None
                        self._offset = index6
                else:
                    elements2 = None
                    self._offset = index6
                if elements2 is None:
                    address0 = FAILURE
                else:
                    address0 = TreeNode(self._input[index6:self._offset], index6, elements2)
                    self._offset = self._offset
                if address0 is FAILURE:
                    self._offset = index1
                    index8, elements3 = self._offset, []
                    address7 = FAILURE
                    chunk6, max6 = None, self._offset + 6
                    if max6 <= self._input_size:
                        chunk6 = self._input[self._offset:max6]
                    if chunk6 == 'except':
                        address7 = TreeNode(self._input[self._offset:self._offset + 6], self._offset, [])
                        self._offset = self._offset + 6
                    else:
                        address7 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('\'except\'')
                    if address7 is not FAILURE:
                        elements3.append(address7)
                        address8 = FAILURE
                        index9 = self._offset
                        chunk7, max7 = None, self._offset + 1
                        if max7 <= self._input_size:
                            chunk7 = self._input[self._offset:max7]
                        if chunk7 is not None and Grammar.REGEX_8.search(chunk7):
                            address8 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                            self._offset = self._offset + 1
                        else:
                            address8 = FAILURE
                            if self._offset > self._failure:
                                self._failure = self._offset
                                self._expected = []
                            if self._offset == self._failure:
                                self._expected.append('[0-9a-zA-Z_]')
                        self._offset = index9
                        if address8 is FAILURE:
                            address8 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                            self._offset = self._offset
                        else:
                            address8 = FAILURE
                        if address8 is not FAILURE:
                            elements3.append(address8)
                        else:
                            elements3 = None
                            self._offset = index8
                    else:
                        elements3 = None
                        self._offset = index8
                    if elements3 is None:
                        address0 = FAILURE
                    else:
                        address0 = TreeNode(self._input[index8:self._offset], index8, elements3)
                        self._offset = self._offset
                    if address0 is FAILURE:
                        self._offset = index1
                        index10, elements4 = self._offset, []
                        address9 = FAILURE
                        chunk8, max8 = None, self._offset + 3
                        if max8 <= self._input_size:
                            chunk8 = self._input[self._offset:max8]
                        if chunk8 == 'for':
                            address9 = TreeNode(self._input[self._offset:self._offset + 3], self._offset, [])
                            self._offset = self._offset + 3
                        else:
                            address9 = FAILURE
                            if self._offset > self._failure:
                                self._failure = self._offset
                                self._expected = []
                            if self._offset == self._failure:
                                self._expected.append('\'for\'')
                        if address9 is not FAILURE:
                            elements4.append(address9)
                            address10 = FAILURE
                            index11 = self._offset
                            chunk9, max9 = None, self._offset + 1
                            if max9 <= self._input_size:
                                chunk9 = self._input[self._offset:max9]
                            if chunk9 is not None and Grammar.REGEX_9.search(chunk9):
                                address10 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                self._offset = self._offset + 1
                            else:
                                address10 = FAILURE
                                if self._offset > self._failure:
                                    self._failure = self._offset
                                    self._expected = []
                                if self._offset == self._failure:
                                    self._expected.append('[0-9a-zA-Z_]')
                            self._offset = index11
                            if address10 is FAILURE:
                                address10 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                self._offset = self._offset
                            else:
                                address10 = FAILURE
                            if address10 is not FAILURE:
                                elements4.append(address10)
                            else:
                                elements4 = None
                                self._offset = index10
                        else:
                            elements4 = None
                            self._offset = index10
                        if elements4 is None:
                            address0 = FAILURE
                        else:
                            address0 = TreeNode(self._input[index10:self._offset], index10, elements4)
                            self._offset = self._offset
                        if address0 is FAILURE:
                            self._offset = index1
                            index12, elements5 = self._offset, []
                            address11 = FAILURE
                            chunk10, max10 = None, self._offset + 5
                            if max10 <= self._input_size:
                                chunk10 = self._input[self._offset:max10]
                            if chunk10 == 'every':
                                address11 = TreeNode(self._input[self._offset:self._offset + 5], self._offset, [])
                                self._offset = self._offset + 5
                            else:
                                address11 = FAILURE
                                if self._offset > self._failure:
                                    self._failure = self._offset
                                    self._expected = []
                                if self._offset == self._failure:
                                    self._expected.append('\'every\'')
                            if address11 is not FAILURE:
                                elements5.append(address11)
                                address12 = FAILURE
                                index13 = self._offset
                                chunk11, max11 = None, self._offset + 1
                                if max11 <= self._input_size:
                                    chunk11 = self._input[self._offset:max11]
                                if chunk11 is not None and Grammar.REGEX_10.search(chunk11):
                                    address12 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                    self._offset = self._offset + 1
                                else:
                                    address12 = FAILURE
                                    if self._offset > self._failure:
                                        self._failure = self._offset
                                        self._expected = []
                                    if self._offset == self._failure:
                                        self._expected.append('[0-9a-zA-Z_]')
                                self._offset = index13
                                if address12 is FAILURE:
                                    address12 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                    self._offset = self._offset
                                else:
                                    address12 = FAILURE
                                if address12 is not FAILURE:
                                    elements5.append(address12)
                                else:
                                    elements5 = None
                                    self._offset = index12
                            else:
                                elements5 = None
                                self._offset = index12
                            if elements5 is None:
                                address0 = FAILURE
                            else:
                                address0 = TreeNode(self._input[index12:self._offset], index12, elements5)
                                self._offset = self._offset
                            if address0 is FAILURE:
                                self._offset = index1
                                index14, elements6 = self._offset, []
                                address13 = FAILURE
                                chunk12, max12 = None, self._offset + 4
                                if max12 <= self._input_size:
                                    chunk12 = self._input[self._offset:max12]
                                if chunk12 == 'that':
                                    address13 = TreeNode(self._input[self._offset:self._offset + 4], self._offset, [])
                                    self._offset = self._offset + 4
                                else:
                                    address13 = FAILURE
                                    if self._offset > self._failure:
                                        self._failure = self._offset
                                        self._expected = []
                                    if self._offset == self._failure:
                                        self._expected.append('\'that\'')
                                if address13 is not FAILURE:
                                    elements6.append(address13)
                                    address14 = FAILURE
                                    index15 = self._offset
                                    chunk13, max13 = None, self._offset + 1
                                    if max13 <= self._input_size:
                                        chunk13 = self._input[self._offset:max13]
                                    if chunk13 is not None and Grammar.REGEX_11.search(chunk13):
                                        address14 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                        self._offset = self._offset + 1
                                    else:
                                        address14 = FAILURE
                                        if self._offset > self._failure:
                                            self._failure = self._offset
                                            self._expected = []
                                        if self._offset == self._failure:
                                            self._expected.append('[0-9a-zA-Z_]')
                                    self._offset = index15
                                    if address14 is FAILURE:
                                        address14 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                        self._offset = self._offset
                                    else:
                                        address14 = FAILURE
                                    if address14 is not FAILURE:
                                        elements6.append(address14)
                                    else:
                                        elements6 = None
                                        self._offset = index14
                                else:
                                    elements6 = None
                                    self._offset = index14
                                if elements6 is None:
                                    address0 = FAILURE
                                else:
                                    address0 = TreeNode(self._input[index14:self._offset], index14, elements6)
                                    self._offset = self._offset
                                if address0 is FAILURE:
                                    self._offset = index1
                                    index16, elements7 = self._offset, []
                                    address15 = FAILURE
                                    chunk14, max14 = None, self._offset + 2
                                    if max14 <= self._input_size:
                                        chunk14 = self._input[self._offset:max14]
                                    if chunk14 == 'at':
                                        address15 = TreeNode(self._input[self._offset:self._offset + 2], self._offset, [])
                                        self._offset = self._offset + 2
                                    else:
                                        address15 = FAILURE
                                        if self._offset > self._failure:
                                            self._failure = self._offset
                                            self._expected = []
                                        if self._offset == self._failure:
                                            self._expected.append('\'at\'')
                                    if address15 is not FAILURE:
                                        elements7.append(address15)
                                        address16 = FAILURE
                                        index17 = self._offset
                                        chunk15, max15 = None, self._offset + 1
                                        if max15 <= self._input_size:
                                            chunk15 = self._input[self._offset:max15]
                                        if chunk15 is not None and Grammar.REGEX_12.search(chunk15):
                                            address16 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                            self._offset = self._offset + 1
                                        else:
                                            address16 = FAILURE
                                            if self._offset > self._failure:
                                                self._failure = self._offset
                                                self._expected = []
                                            if self._offset == self._failure:
                                                self._expected.append('[0-9a-zA-Z_]')
                                        self._offset = index17
                                        if address16 is FAILURE:
                                            address16 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                            self._offset = self._offset
                                        else:
                                            address16 = FAILURE
                                        if address16 is not FAILURE:
                                            elements7.append(address16)
                                        else:
                                            elements7 = None
                                            self._offset = index16
                                    else:
                                        elements7 = None
                                        self._offset = index16
                                    if elements7 is None:
                                        address0 = FAILURE
                                    else:
                                        address0 = TreeNode(self._input[index16:self._offset], index16, elements7)
                                        self._offset = self._offset
                                    if address0 is FAILURE:
                                        self._offset = index1
                                        index18, elements8 = self._offset, []
                                        address17 = FAILURE
                                        chunk16, max16 = None, self._offset + 5
                                        if max16 <= self._input_size:
                                            chunk16 = self._input[self._offset:max16]
                                        if chunk16 == 'after':
                                            address17 = TreeNode(self._input[self._offset:self._offset + 5], self._offset, [])
                                            self._offset = self._offset + 5
                                        else:
                                            address17 = FAILURE
                                            if self._offset > self._failure:
                                                self._failure = self._offset
                                                self._expected = []
                                            if self._offset == self._failure:
                                                self._expected.append('\'after\'')
                                        if address17 is not FAILURE:
                                            elements8.append(address17)
                                            address18 = FAILURE
                                            index19 = self._offset
                                            chunk17, max17 = None, self._offset + 1
                                            if max17 <= self._input_size:
                                                chunk17 = self._input[self._offset:max17]
                                            if chunk17 is not None and Grammar.REGEX_13.search(chunk17):
                                                address18 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                                self._offset = self._offset + 1
                                            else:
                                                address18 = FAILURE
                                                if self._offset > self._failure:
                                                    self._failure = self._offset
                                                    self._expected = []
                                                if self._offset == self._failure:
                                                    self._expected.append('[0-9a-zA-Z_]')
                                            self._offset = index19
                                            if address18 is FAILURE:
                                                address18 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                                self._offset = self._offset
                                            else:
                                                address18 = FAILURE
                                            if address18 is not FAILURE:
                                                elements8.append(address18)
                                            else:
                                                elements8 = None
                                                self._offset = index18
                                        else:
                                            elements8 = None
                                            self._offset = index18
                                        if elements8 is None:
                                            address0 = FAILURE
                                        else:
                                            address0 = TreeNode(self._input[index18:self._offset], index18, elements8)
                                            self._offset = self._offset
                                        if address0 is FAILURE:
                                            self._offset = index1
                                            index20, elements9 = self._offset, []
                                            address19 = FAILURE
                                            chunk18, max18 = None, self._offset + 7
                                            if max18 <= self._input_size:
                                                chunk18 = self._input[self._offset:max18]
                                            if chunk18 == 'restart':
                                                address19 = TreeNode(self._input[self._offset:self._offset + 7], self._offset, [])
                                                self._offset = self._offset + 7
                                            else:
                                                address19 = FAILURE
                                                if self._offset > self._failure:
                                                    self._failure = self._offset
                                                    self._expected = []
                                                if self._offset == self._failure:
                                                    self._expected.append('\'restart\'')
                                            if address19 is not FAILURE:
                                                elements9.append(address19)
                                                address20 = FAILURE
                                                index21 = self._offset
                                                chunk19, max19 = None, self._offset + 1
                                                if max19 <= self._input_size:
                                                    chunk19 = self._input[self._offset:max19]
                                                if chunk19 is not None and Grammar.REGEX_14.search(chunk19):
                                                    address20 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                                    self._offset = self._offset + 1
                                                else:
                                                    address20 = FAILURE
                                                    if self._offset > self._failure:
                                                        self._failure = self._offset
                                                        self._expected = []
                                                    if self._offset == self._failure:
                                                        self._expected.append('[0-9a-zA-Z_]')
                                                self._offset = index21
                                                if address20 is FAILURE:
                                                    address20 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                                    self._offset = self._offset
                                                else:
                                                    address20 = FAILURE
                                                if address20 is not FAILURE:
                                                    elements9.append(address20)
                                                else:
                                                    elements9 = None
                                                    self._offset = index20
                                            else:
                                                elements9 = None
                                                self._offset = index20
                                            if elements9 is None:
                                                address0 = FAILURE
                                            else:
                                                address0 = TreeNode(self._input[index20:self._offset], index20, elements9)
                                                self._offset = self._offset
                                            if address0 is FAILURE:
                                                self._offset = index1
                                                index22, elements10 = self._offset, []
                                                address21 = FAILURE
                                                chunk20, max20 = None, self._offset + 6
                                                if max20 <= self._input_size:
                                                    chunk20 = self._input[self._offset:max20]
                                                if chunk20 == 'before':
                                                    address21 = TreeNode(self._input[self._offset:self._offset + 6], self._offset, [])
                                                    self._offset = self._offset + 6
                                                else:
                                                    address21 = FAILURE
                                                    if self._offset > self._failure:
                                                        self._failure = self._offset
                                                        self._expected = []
                                                    if self._offset == self._failure:
                                                        self._expected.append('\'before\'')
                                                if address21 is not FAILURE:
                                                    elements10.append(address21)
                                                    address22 = FAILURE
                                                    index23 = self._offset
                                                    chunk21, max21 = None, self._offset + 1
                                                    if max21 <= self._input_size:
                                                        chunk21 = self._input[self._offset:max21]
                                                    if chunk21 is not None and Grammar.REGEX_15.search(chunk21):
                                                        address22 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                                        self._offset = self._offset + 1
                                                    else:
                                                        address22 = FAILURE
                                                        if self._offset > self._failure:
                                                            self._failure = self._offset
                                                            self._expected = []
                                                        if self._offset == self._failure:
                                                            self._expected.append('[0-9a-zA-Z_]')
                                                    self._offset = index23
                                                    if address22 is FAILURE:
                                                        address22 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                                        self._offset = self._offset
                                                    else:
                                                        address22 = FAILURE
                                                    if address22 is not FAILURE:
                                                        elements10.append(address22)
                                                    else:
                                                        elements10 = None
                                                        self._offset = index22
                                                else:
                                                    elements10 = None
                                                    self._offset = index22
                                                if elements10 is None:
                                                    address0 = FAILURE
                                                else:
                                                    address0 = TreeNode(self._input[index22:self._offset], index22, elements10)
                                                    self._offset = self._offset
                                                if address0 is FAILURE:
                                                    self._offset = index1
                                                    index24, elements11 = self._offset, []
                                                    address23 = FAILURE
                                                    chunk22, max22 = None, self._offset + 4
                                                    if max22 <= self._input_size:
                                                        chunk22 = self._input[self._offset:max22]
                                                    if chunk22 == 'when':
                                                        address23 = TreeNode(self._input[self._offset:self._offset + 4], self._offset, [])
                                                        self._offset = self._offset + 4
                                                    else:
                                                        address23 = FAILURE
                                                        if self._offset > self._failure:
                                                            self._failure = self._offset
                                                            self._expected = []
                                                        if self._offset == self._failure:
                                                            self._expected.append('\'when\'')
                                                    if address23 is not FAILURE:
                                                        elements11.append(address23)
                                                        address24 = FAILURE
                                                        index25 = self._offset
                                                        chunk23, max23 = None, self._offset + 1
                                                        if max23 <= self._input_size:
                                                            chunk23 = self._input[self._offset:max23]
                                                        if chunk23 is not None and Grammar.REGEX_16.search(chunk23):
                                                            address24 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                                            self._offset = self._offset + 1
                                                        else:
                                                            address24 = FAILURE
                                                            if self._offset > self._failure:
                                                                self._failure = self._offset
                                                                self._expected = []
                                                            if self._offset == self._failure:
                                                                self._expected.append('[0-9a-zA-Z_]')
                                                        self._offset = index25
                                                        if address24 is FAILURE:
                                                            address24 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                                            self._offset = self._offset
                                                        else:
                                                            address24 = FAILURE
                                                        if address24 is not FAILURE:
                                                            elements11.append(address24)
                                                        else:
                                                            elements11 = None
                                                            self._offset = index24
                                                    else:
                                                        elements11 = None
                                                        self._offset = index24
                                                    if elements11 is None:
                                                        address0 = FAILURE
                                                    else:
                                                        address0 = TreeNode(self._input[index24:self._offset], index24, elements11)
                                                        self._offset = self._offset
                                                    if address0 is FAILURE:
                                                        self._offset = index1
                                                        index26, elements12 = self._offset, []
                                                        address25 = FAILURE
                                                        chunk24, max24 = None, self._offset + 7
                                                        if max24 <= self._input_size:
                                                            chunk24 = self._input[self._offset:max24]
                                                        if chunk24 == 'attempt':
                                                            address25 = TreeNode(self._input[self._offset:self._offset + 7], self._offset, [])
                                                            self._offset = self._offset + 7
                                                        else:
                                                            address25 = FAILURE
                                                            if self._offset > self._failure:
                                                                self._failure = self._offset
                                                                self._expected = []
                                                            if self._offset == self._failure:
                                                                self._expected.append('\'attempt\'')
                                                        if address25 is not FAILURE:
                                                            elements12.append(address25)
                                                            address26 = FAILURE
                                                            index27 = self._offset
                                                            chunk25, max25 = None, self._offset + 1
                                                            if max25 <= self._input_size:
                                                                chunk25 = self._input[self._offset:max25]
                                                            if chunk25 is not None and Grammar.REGEX_17.search(chunk25):
                                                                address26 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                                                self._offset = self._offset + 1
                                                            else:
                                                                address26 = FAILURE
                                                                if self._offset > self._failure:
                                                                    self._failure = self._offset
                                                                    self._expected = []
                                                                if self._offset == self._failure:
                                                                    self._expected.append('[0-9a-zA-Z_]')
                                                            self._offset = index27
                                                            if address26 is FAILURE:
                                                                address26 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                                                self._offset = self._offset
                                                            else:
                                                                address26 = FAILURE
                                                            if address26 is not FAILURE:
                                                                elements12.append(address26)
                                                            else:
                                                                elements12 = None
                                                                self._offset = index26
                                                        else:
                                                            elements12 = None
                                                            self._offset = index26
                                                        if elements12 is None:
                                                            address0 = FAILURE
                                                        else:
                                                            address0 = TreeNode(self._input[index26:self._offset], index26, elements12)
                                                            self._offset = self._offset
                                                        if address0 is FAILURE:
                                                            self._offset = index1
                                                            index28, elements13 = self._offset, []
                                                            address27 = FAILURE
                                                            chunk26, max26 = None, self._offset + 3
                                                            if max26 <= self._input_size:
                                                                chunk26 = self._input[self._offset:max26]
                                                            if chunk26 == 'but':
                                                                address27 = TreeNode(self._input[self._offset:self._offset + 3], self._offset, [])
                                                                self._offset = self._offset + 3
                                                            else:
                                                                address27 = FAILURE
                                                                if self._offset > self._failure:
                                                                    self._failure = self._offset
                                                                    self._expected = []
                                                                if self._offset == self._failure:
                                                                    self._expected.append('\'but\'')
                                                            if address27 is not FAILURE:
                                                                elements13.append(address27)
                                                                address28 = FAILURE
                                                                index29 = self._offset
                                                                chunk27, max27 = None, self._offset + 1
                                                                if max27 <= self._input_size:
                                                                    chunk27 = self._input[self._offset:max27]
                                                                if chunk27 is not None and Grammar.REGEX_18.search(chunk27):
                                                                    address28 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                                                    self._offset = self._offset + 1
                                                                else:
                                                                    address28 = FAILURE
                                                                    if self._offset > self._failure:
                                                                        self._failure = self._offset
                                                                        self._expected = []
                                                                    if self._offset == self._failure:
                                                                        self._expected.append('[0-9a-zA-Z_]')
                                                                self._offset = index29
                                                                if address28 is FAILURE:
                                                                    address28 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                                                    self._offset = self._offset
                                                                else:
                                                                    address28 = FAILURE
                                                                if address28 is not FAILURE:
                                                                    elements13.append(address28)
                                                                else:
                                                                    elements13 = None
                                                                    self._offset = index28
                                                            else:
                                                                elements13 = None
                                                                self._offset = index28
                                                            if elements13 is None:
                                                                address0 = FAILURE
                                                            else:
                                                                address0 = TreeNode(self._input[index28:self._offset], index28, elements13)
                                                                self._offset = self._offset
                                                            if address0 is FAILURE:
                                                                self._offset = index1
                                                                index30, elements14 = self._offset, []
                                                                address29 = FAILURE
                                                                chunk28, max28 = None, self._offset + 6
                                                                if max28 <= self._input_size:
                                                                    chunk28 = self._input[self._offset:max28]
                                                                if chunk28 == 'always':
                                                                    address29 = TreeNode(self._input[self._offset:self._offset + 6], self._offset, [])
                                                                    self._offset = self._offset + 6
                                                                else:
                                                                    address29 = FAILURE
                                                                    if self._offset > self._failure:
                                                                        self._failure = self._offset
                                                                        self._expected = []
                                                                    if self._offset == self._failure:
                                                                        self._expected.append('\'always\'')
                                                                if address29 is not FAILURE:
                                                                    elements14.append(address29)
                                                                    address30 = FAILURE
                                                                    index31 = self._offset
                                                                    chunk29, max29 = None, self._offset + 1
                                                                    if max29 <= self._input_size:
                                                                        chunk29 = self._input[self._offset:max29]
                                                                    if chunk29 is not None and Grammar.REGEX_19.search(chunk29):
                                                                        address30 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                                                        self._offset = self._offset + 1
                                                                    else:
                                                                        address30 = FAILURE
                                                                        if self._offset > self._failure:
                                                                            self._failure = self._offset
                                                                            self._expected = []
                                                                        if self._offset == self._failure:
                                                                            self._expected.append('[0-9a-zA-Z_]')
                                                                    self._offset = index31
                                                                    if address30 is FAILURE:
                                                                        address30 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                                                        self._offset = self._offset
                                                                    else:
                                                                        address30 = FAILURE
                                                                    if address30 is not FAILURE:
                                                                        elements14.append(address30)
                                                                    else:
                                                                        elements14 = None
                                                                        self._offset = index30
                                                                else:
                                                                    elements14 = None
                                                                    self._offset = index30
                                                                if elements14 is None:
                                                                    address0 = FAILURE
                                                                else:
                                                                    address0 = TreeNode(self._input[index30:self._offset], index30, elements14)
                                                                    self._offset = self._offset
                                                                if address0 is FAILURE:
                                                                    self._offset = index1
                                                                    index32, elements15 = self._offset, []
                                                                    address31 = FAILURE
                                                                    chunk30, max30 = None, self._offset + 6
                                                                    if max30 <= self._input_size:
                                                                        chunk30 = self._input[self._offset:max30]
                                                                    if chunk30 == 'occurs':
                                                                        address31 = TreeNode(self._input[self._offset:self._offset + 6], self._offset, [])
                                                                        self._offset = self._offset + 6
                                                                    else:
                                                                        address31 = FAILURE
                                                                        if self._offset > self._failure:
                                                                            self._failure = self._offset
                                                                            self._expected = []
                                                                        if self._offset == self._failure:
                                                                            self._expected.append('\'occurs\'')
                                                                    if address31 is not FAILURE:
                                                                        elements15.append(address31)
                                                                        address32 = FAILURE
                                                                        index33 = self._offset
                                                                        chunk31, max31 = None, self._offset + 1
                                                                        if max31 <= self._input_size:
                                                                            chunk31 = self._input[self._offset:max31]
                                                                        if chunk31 is not None and Grammar.REGEX_20.search(chunk31):
                                                                            address32 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                                                            self._offset = self._offset + 1
                                                                        else:
                                                                            address32 = FAILURE
                                                                            if self._offset > self._failure:
                                                                                self._failure = self._offset
                                                                                self._expected = []
                                                                            if self._offset == self._failure:
                                                                                self._expected.append('[0-9a-zA-Z_]')
                                                                        self._offset = index33
                                                                        if address32 is FAILURE:
                                                                            address32 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                                                            self._offset = self._offset
                                                                        else:
                                                                            address32 = FAILURE
                                                                        if address32 is not FAILURE:
                                                                            elements15.append(address32)
                                                                        else:
                                                                            elements15 = None
                                                                            self._offset = index32
                                                                    else:
                                                                        elements15 = None
                                                                        self._offset = index32
                                                                    if elements15 is None:
                                                                        address0 = FAILURE
                                                                    else:
                                                                        address0 = TreeNode(self._input[index32:self._offset], index32, elements15)
                                                                        self._offset = self._offset
                                                                    if address0 is FAILURE:
                                                                        self._offset = index1
                                                                        index34, elements16 = self._offset, []
                                                                        address33 = FAILURE
                                                                        chunk32, max32 = None, self._offset + 4
                                                                        if max32 <= self._input_size:
                                                                            chunk32 = self._input[self._offset:max32]
                                                                        if chunk32 == 'oops':
                                                                            address33 = TreeNode(self._input[self._offset:self._offset + 4], self._offset, [])
                                                                            self._offset = self._offset + 4
                                                                        else:
                                                                            address33 = FAILURE
                                                                            if self._offset > self._failure:
                                                                                self._failure = self._offset
                                                                                self._expected = []
                                                                            if self._offset == self._failure:
                                                                                self._expected.append('\'oops\'')
                                                                        if address33 is not FAILURE:
                                                                            elements16.append(address33)
                                                                            address34 = FAILURE
                                                                            index35 = self._offset
                                                                            chunk33, max33 = None, self._offset + 1
                                                                            if max33 <= self._input_size:
                                                                                chunk33 = self._input[self._offset:max33]
                                                                            if chunk33 is not None and Grammar.REGEX_21.search(chunk33):
                                                                                address34 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                                                                self._offset = self._offset + 1
                                                                            else:
                                                                                address34 = FAILURE
                                                                                if self._offset > self._failure:
                                                                                    self._failure = self._offset
                                                                                    self._expected = []
                                                                                if self._offset == self._failure:
                                                                                    self._expected.append('[0-9a-zA-Z_]')
                                                                            self._offset = index35
                                                                            if address34 is FAILURE:
                                                                                address34 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                                                                self._offset = self._offset
                                                                            else:
                                                                                address34 = FAILURE
                                                                            if address34 is not FAILURE:
                                                                                elements16.append(address34)
                                                                            else:
                                                                                elements16 = None
                                                                                self._offset = index34
                                                                        else:
                                                                            elements16 = None
                                                                            self._offset = index34
                                                                        if elements16 is None:
                                                                            address0 = FAILURE
                                                                        else:
                                                                            address0 = TreeNode(self._input[index34:self._offset], index34, elements16)
                                                                            self._offset = self._offset
                                                                        if address0 is FAILURE:
                                                                            self._offset = index1
                                                                            index36, elements17 = self._offset, []
                                                                            address35 = FAILURE
                                                                            chunk34, max34 = None, self._offset + 4
                                                                            if max34 <= self._input_size:
                                                                                chunk34 = self._input[self._offset:max34]
                                                                            if chunk34 == 'load':
                                                                                address35 = TreeNode(self._input[self._offset:self._offset + 4], self._offset, [])
                                                                                self._offset = self._offset + 4
                                                                            else:
                                                                                address35 = FAILURE
                                                                                if self._offset > self._failure:
                                                                                    self._failure = self._offset
                                                                                    self._expected = []
                                                                                if self._offset == self._failure:
                                                                                    self._expected.append('\'load\'')
                                                                            if address35 is not FAILURE:
                                                                                elements17.append(address35)
                                                                                address36 = FAILURE
                                                                                index37 = self._offset
                                                                                chunk35, max35 = None, self._offset + 1
                                                                                if max35 <= self._input_size:
                                                                                    chunk35 = self._input[self._offset:max35]
                                                                                if chunk35 is not None and Grammar.REGEX_22.search(chunk35):
                                                                                    address36 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                                                                    self._offset = self._offset + 1
                                                                                else:
                                                                                    address36 = FAILURE
                                                                                    if self._offset > self._failure:
                                                                                        self._failure = self._offset
                                                                                        self._expected = []
                                                                                    if self._offset == self._failure:
                                                                                        self._expected.append('[0-9a-zA-Z_]')
                                                                                self._offset = index37
                                                                                if address36 is FAILURE:
                                                                                    address36 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                                                                    self._offset = self._offset
                                                                                else:
                                                                                    address36 = FAILURE
                                                                                if address36 is not FAILURE:
                                                                                    elements17.append(address36)
                                                                                else:
                                                                                    elements17 = None
                                                                                    self._offset = index36
                                                                            else:
                                                                                elements17 = None
                                                                                self._offset = index36
                                                                            if elements17 is None:
                                                                                address0 = FAILURE
                                                                            else:
                                                                                address0 = TreeNode(self._input[index36:self._offset], index36, elements17)
                                                                                self._offset = self._offset
                                                                            if address0 is FAILURE:
                                                                                self._offset = index1
                                                                                index38, elements18 = self._offset, []
                                                                                address37 = FAILURE
                                                                                chunk36, max36 = None, self._offset + 4
                                                                                if max36 <= self._input_size:
                                                                                    chunk36 = self._input[self._offset:max36]
                                                                                if chunk36 == 'from':
                                                                                    address37 = TreeNode(self._input[self._offset:self._offset + 4], self._offset, [])
                                                                                    self._offset = self._offset + 4
                                                                                else:
                                                                                    address37 = FAILURE
                                                                                    if self._offset > self._failure:
                                                                                        self._failure = self._offset
                                                                                        self._expected = []
                                                                                    if self._offset == self._failure:
                                                                                        self._expected.append('\'from\'')
                                                                                if address37 is not FAILURE:
                                                                                    elements18.append(address37)
                                                                                    address38 = FAILURE
                                                                                    index39 = self._offset
                                                                                    chunk37, max37 = None, self._offset + 1
                                                                                    if max37 <= self._input_size:
                                                                                        chunk37 = self._input[self._offset:max37]
                                                                                    if chunk37 is not None and Grammar.REGEX_23.search(chunk37):
                                                                                        address38 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                                                                        self._offset = self._offset + 1
                                                                                    else:
                                                                                        address38 = FAILURE
                                                                                        if self._offset > self._failure:
                                                                                            self._failure = self._offset
                                                                                            self._expected = []
                                                                                        if self._offset == self._failure:
                                                                                            self._expected.append('[0-9a-zA-Z_]')
                                                                                    self._offset = index39
                                                                                    if address38 is FAILURE:
                                                                                        address38 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                                                                        self._offset = self._offset
                                                                                    else:
                                                                                        address38 = FAILURE
                                                                                    if address38 is not FAILURE:
                                                                                        elements18.append(address38)
                                                                                    else:
                                                                                        elements18 = None
                                                                                        self._offset = index38
                                                                                else:
                                                                                    elements18 = None
                                                                                    self._offset = index38
                                                                                if elements18 is None:
                                                                                    address0 = FAILURE
                                                                                else:
                                                                                    address0 = TreeNode(self._input[index38:self._offset], index38, elements18)
                                                                                    self._offset = self._offset
                                                                                if address0 is FAILURE:
                                                                                    self._offset = index1
                                                                                    index40, elements19 = self._offset, []
                                                                                    address39 = FAILURE
                                                                                    chunk38, max38 = None, self._offset + 4
                                                                                    if max38 <= self._input_size:
                                                                                        chunk38 = self._input[self._offset:max38]
                                                                                    if chunk38 == 'into':
                                                                                        address39 = TreeNode(self._input[self._offset:self._offset + 4], self._offset, [])
                                                                                        self._offset = self._offset + 4
                                                                                    else:
                                                                                        address39 = FAILURE
                                                                                        if self._offset > self._failure:
                                                                                            self._failure = self._offset
                                                                                            self._expected = []
                                                                                        if self._offset == self._failure:
                                                                                            self._expected.append('\'into\'')
                                                                                    if address39 is not FAILURE:
                                                                                        elements19.append(address39)
                                                                                        address40 = FAILURE
                                                                                        index41 = self._offset
                                                                                        chunk39, max39 = None, self._offset + 1
                                                                                        if max39 <= self._input_size:
                                                                                            chunk39 = self._input[self._offset:max39]
                                                                                        if chunk39 is not None and Grammar.REGEX_24.search(chunk39):
                                                                                            address40 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                                                                            self._offset = self._offset + 1
                                                                                        else:
                                                                                            address40 = FAILURE
                                                                                            if self._offset > self._failure:
                                                                                                self._failure = self._offset
                                                                                                self._expected = []
                                                                                            if self._offset == self._failure:
                                                                                                self._expected.append('[0-9a-zA-Z_]')
                                                                                        self._offset = index41
                                                                                        if address40 is FAILURE:
                                                                                            address40 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                                                                            self._offset = self._offset
                                                                                        else:
                                                                                            address40 = FAILURE
                                                                                        if address40 is not FAILURE:
                                                                                            elements19.append(address40)
                                                                                        else:
                                                                                            elements19 = None
                                                                                            self._offset = index40
                                                                                    else:
                                                                                        elements19 = None
                                                                                        self._offset = index40
                                                                                    if elements19 is None:
                                                                                        address0 = FAILURE
                                                                                    else:
                                                                                        address0 = TreeNode(self._input[index40:self._offset], index40, elements19)
                                                                                        self._offset = self._offset
                                                                                    if address0 is FAILURE:
                                                                                        self._offset = index1
                                                                                        index42, elements20 = self._offset, []
                                                                                        address41 = FAILURE
                                                                                        chunk40, max40 = None, self._offset + 3
                                                                                        if max40 <= self._input_size:
                                                                                            chunk40 = self._input[self._offset:max40]
                                                                                        if chunk40 == 'use':
                                                                                            address41 = TreeNode(self._input[self._offset:self._offset + 3], self._offset, [])
                                                                                            self._offset = self._offset + 3
                                                                                        else:
                                                                                            address41 = FAILURE
                                                                                            if self._offset > self._failure:
                                                                                                self._failure = self._offset
                                                                                                self._expected = []
                                                                                            if self._offset == self._failure:
                                                                                                self._expected.append('\'use\'')
                                                                                        if address41 is not FAILURE:
                                                                                            elements20.append(address41)
                                                                                            address42 = FAILURE
                                                                                            index43 = self._offset
                                                                                            chunk41, max41 = None, self._offset + 1
                                                                                            if max41 <= self._input_size:
                                                                                                chunk41 = self._input[self._offset:max41]
                                                                                            if chunk41 is not None and Grammar.REGEX_25.search(chunk41):
                                                                                                address42 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                                                                                self._offset = self._offset + 1
                                                                                            else:
                                                                                                address42 = FAILURE
                                                                                                if self._offset > self._failure:
                                                                                                    self._failure = self._offset
                                                                                                    self._expected = []
                                                                                                if self._offset == self._failure:
                                                                                                    self._expected.append('[0-9a-zA-Z_]')
                                                                                            self._offset = index43
                                                                                            if address42 is FAILURE:
                                                                                                address42 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                                                                                self._offset = self._offset
                                                                                            else:
                                                                                                address42 = FAILURE
                                                                                            if address42 is not FAILURE:
                                                                                                elements20.append(address42)
                                                                                            else:
                                                                                                elements20 = None
                                                                                                self._offset = index42
                                                                                        else:
                                                                                            elements20 = None
                                                                                            self._offset = index42
                                                                                        if elements20 is None:
                                                                                            address0 = FAILURE
                                                                                        else:
                                                                                            address0 = TreeNode(self._input[index42:self._offset], index42, elements20)
                                                                                            self._offset = self._offset
                                                                                        if address0 is FAILURE:
                                                                                            self._offset = index1
                                                                                            index44, elements21 = self._offset, []
                                                                                            address43 = FAILURE
                                                                                            chunk42, max42 = None, self._offset + 2
                                                                                            if max42 <= self._input_size:
                                                                                                chunk42 = self._input[self._offset:max42]
                                                                                            if chunk42 == 'if':
                                                                                                address43 = TreeNode(self._input[self._offset:self._offset + 2], self._offset, [])
                                                                                                self._offset = self._offset + 2
                                                                                            else:
                                                                                                address43 = FAILURE
                                                                                                if self._offset > self._failure:
                                                                                                    self._failure = self._offset
                                                                                                    self._expected = []
                                                                                                if self._offset == self._failure:
                                                                                                    self._expected.append('\'if\'')
                                                                                            if address43 is not FAILURE:
                                                                                                elements21.append(address43)
                                                                                                address44 = FAILURE
                                                                                                index45 = self._offset
                                                                                                chunk43, max43 = None, self._offset + 1
                                                                                                if max43 <= self._input_size:
                                                                                                    chunk43 = self._input[self._offset:max43]
                                                                                                if chunk43 is not None and Grammar.REGEX_26.search(chunk43):
                                                                                                    address44 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                                                                                    self._offset = self._offset + 1
                                                                                                else:
                                                                                                    address44 = FAILURE
                                                                                                    if self._offset > self._failure:
                                                                                                        self._failure = self._offset
                                                                                                        self._expected = []
                                                                                                    if self._offset == self._failure:
                                                                                                        self._expected.append('[0-9a-zA-Z_]')
                                                                                                self._offset = index45
                                                                                                if address44 is FAILURE:
                                                                                                    address44 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                                                                                    self._offset = self._offset
                                                                                                else:
                                                                                                    address44 = FAILURE
                                                                                                if address44 is not FAILURE:
                                                                                                    elements21.append(address44)
                                                                                                else:
                                                                                                    elements21 = None
                                                                                                    self._offset = index44
                                                                                            else:
                                                                                                elements21 = None
                                                                                                self._offset = index44
                                                                                            if elements21 is None:
                                                                                                address0 = FAILURE
                                                                                            else:
                                                                                                address0 = TreeNode(self._input[index44:self._offset], index44, elements21)
                                                                                                self._offset = self._offset
                                                                                            if address0 is FAILURE:
                                                                                                self._offset = index1
                                                                                                index46, elements22 = self._offset, []
                                                                                                address45 = FAILURE
                                                                                                chunk44, max44 = None, self._offset + 4
                                                                                                if max44 <= self._input_size:
                                                                                                    chunk44 = self._input[self._offset:max44]
                                                                                                if chunk44 == 'then':
                                                                                                    address45 = TreeNode(self._input[self._offset:self._offset + 4], self._offset, [])
                                                                                                    self._offset = self._offset + 4
                                                                                                else:
                                                                                                    address45 = FAILURE
                                                                                                    if self._offset > self._failure:
                                                                                                        self._failure = self._offset
                                                                                                        self._expected = []
                                                                                                    if self._offset == self._failure:
                                                                                                        self._expected.append('\'then\'')
                                                                                                if address45 is not FAILURE:
                                                                                                    elements22.append(address45)
                                                                                                    address46 = FAILURE
                                                                                                    index47 = self._offset
                                                                                                    chunk45, max45 = None, self._offset + 1
                                                                                                    if max45 <= self._input_size:
                                                                                                        chunk45 = self._input[self._offset:max45]
                                                                                                    if chunk45 is not None and Grammar.REGEX_27.search(chunk45):
                                                                                                        address46 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                                                                                        self._offset = self._offset + 1
                                                                                                    else:
                                                                                                        address46 = FAILURE
                                                                                                        if self._offset > self._failure:
                                                                                                            self._failure = self._offset
                                                                                                            self._expected = []
                                                                                                        if self._offset == self._failure:
                                                                                                            self._expected.append('[0-9a-zA-Z_]')
                                                                                                    self._offset = index47
                                                                                                    if address46 is FAILURE:
                                                                                                        address46 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                                                                                        self._offset = self._offset
                                                                                                    else:
                                                                                                        address46 = FAILURE
                                                                                                    if address46 is not FAILURE:
                                                                                                        elements22.append(address46)
                                                                                                    else:
                                                                                                        elements22 = None
                                                                                                        self._offset = index46
                                                                                                else:
                                                                                                    elements22 = None
                                                                                                    self._offset = index46
                                                                                                if elements22 is None:
                                                                                                    address0 = FAILURE
                                                                                                else:
                                                                                                    address0 = TreeNode(self._input[index46:self._offset], index46, elements22)
                                                                                                    self._offset = self._offset
                                                                                                if address0 is FAILURE:
                                                                                                    self._offset = index1
                                                                                                    index48, elements23 = self._offset, []
                                                                                                    address47 = FAILURE
                                                                                                    chunk46, max46 = None, self._offset + 3
                                                                                                    if max46 <= self._input_size:
                                                                                                        chunk46 = self._input[self._offset:max46]
                                                                                                    if chunk46 == 'and':
                                                                                                        address47 = TreeNode(self._input[self._offset:self._offset + 3], self._offset, [])
                                                                                                        self._offset = self._offset + 3
                                                                                                    else:
                                                                                                        address47 = FAILURE
                                                                                                        if self._offset > self._failure:
                                                                                                            self._failure = self._offset
                                                                                                            self._expected = []
                                                                                                        if self._offset == self._failure:
                                                                                                            self._expected.append('\'and\'')
                                                                                                    if address47 is not FAILURE:
                                                                                                        elements23.append(address47)
                                                                                                        address48 = FAILURE
                                                                                                        index49 = self._offset
                                                                                                        chunk47, max47 = None, self._offset + 1
                                                                                                        if max47 <= self._input_size:
                                                                                                            chunk47 = self._input[self._offset:max47]
                                                                                                        if chunk47 is not None and Grammar.REGEX_28.search(chunk47):
                                                                                                            address48 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                                                                                            self._offset = self._offset + 1
                                                                                                        else:
                                                                                                            address48 = FAILURE
                                                                                                            if self._offset > self._failure:
                                                                                                                self._failure = self._offset
                                                                                                                self._expected = []
                                                                                                            if self._offset == self._failure:
                                                                                                                self._expected.append('[0-9a-zA-Z_]')
                                                                                                        self._offset = index49
                                                                                                        if address48 is FAILURE:
                                                                                                            address48 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                                                                                            self._offset = self._offset
                                                                                                        else:
                                                                                                            address48 = FAILURE
                                                                                                        if address48 is not FAILURE:
                                                                                                            elements23.append(address48)
                                                                                                        else:
                                                                                                            elements23 = None
                                                                                                            self._offset = index48
                                                                                                    else:
                                                                                                        elements23 = None
                                                                                                        self._offset = index48
                                                                                                    if elements23 is None:
                                                                                                        address0 = FAILURE
                                                                                                    else:
                                                                                                        address0 = TreeNode(self._input[index48:self._offset], index48, elements23)
                                                                                                        self._offset = self._offset
                                                                                                    if address0 is FAILURE:
                                                                                                        self._offset = index1
                                                                                                        index50, elements24 = self._offset, []
                                                                                                        address49 = FAILURE
                                                                                                        chunk48, max48 = None, self._offset + 2
                                                                                                        if max48 <= self._input_size:
                                                                                                            chunk48 = self._input[self._offset:max48]
                                                                                                        if chunk48 == 'or':
                                                                                                            address49 = TreeNode(self._input[self._offset:self._offset + 2], self._offset, [])
                                                                                                            self._offset = self._offset + 2
                                                                                                        else:
                                                                                                            address49 = FAILURE
                                                                                                            if self._offset > self._failure:
                                                                                                                self._failure = self._offset
                                                                                                                self._expected = []
                                                                                                            if self._offset == self._failure:
                                                                                                                self._expected.append('\'or\'')
                                                                                                        if address49 is not FAILURE:
                                                                                                            elements24.append(address49)
                                                                                                            address50 = FAILURE
                                                                                                            index51 = self._offset
                                                                                                            chunk49, max49 = None, self._offset + 1
                                                                                                            if max49 <= self._input_size:
                                                                                                                chunk49 = self._input[self._offset:max49]
                                                                                                            if chunk49 is not None and Grammar.REGEX_29.search(chunk49):
                                                                                                                address50 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                                                                                                self._offset = self._offset + 1
                                                                                                            else:
                                                                                                                address50 = FAILURE
                                                                                                                if self._offset > self._failure:
                                                                                                                    self._failure = self._offset
                                                                                                                    self._expected = []
                                                                                                                if self._offset == self._failure:
                                                                                                                    self._expected.append('[0-9a-zA-Z_]')
                                                                                                            self._offset = index51
                                                                                                            if address50 is FAILURE:
                                                                                                                address50 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                                                                                                self._offset = self._offset
                                                                                                            else:
                                                                                                                address50 = FAILURE
                                                                                                            if address50 is not FAILURE:
                                                                                                                elements24.append(address50)
                                                                                                            else:
                                                                                                                elements24 = None
                                                                                                                self._offset = index50
                                                                                                        else:
                                                                                                            elements24 = None
                                                                                                            self._offset = index50
                                                                                                        if elements24 is None:
                                                                                                            address0 = FAILURE
                                                                                                        else:
                                                                                                            address0 = TreeNode(self._input[index50:self._offset], index50, elements24)
                                                                                                            self._offset = self._offset
                                                                                                        if address0 is FAILURE:
                                                                                                            self._offset = index1
                                                                                                            index52, elements25 = self._offset, []
                                                                                                            address51 = FAILURE
                                                                                                            chunk50, max50 = None, self._offset + 3
                                                                                                            if max50 <= self._input_size:
                                                                                                                chunk50 = self._input[self._offset:max50]
                                                                                                            if chunk50 == 'not':
                                                                                                                address51 = TreeNode(self._input[self._offset:self._offset + 3], self._offset, [])
                                                                                                                self._offset = self._offset + 3
                                                                                                            else:
                                                                                                                address51 = FAILURE
                                                                                                                if self._offset > self._failure:
                                                                                                                    self._failure = self._offset
                                                                                                                    self._expected = []
                                                                                                                if self._offset == self._failure:
                                                                                                                    self._expected.append('\'not\'')
                                                                                                            if address51 is not FAILURE:
                                                                                                                elements25.append(address51)
                                                                                                                address52 = FAILURE
                                                                                                                index53 = self._offset
                                                                                                                chunk51, max51 = None, self._offset + 1
                                                                                                                if max51 <= self._input_size:
                                                                                                                    chunk51 = self._input[self._offset:max51]
                                                                                                                if chunk51 is not None and Grammar.REGEX_30.search(chunk51):
                                                                                                                    address52 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                                                                                                    self._offset = self._offset + 1
                                                                                                                else:
                                                                                                                    address52 = FAILURE
                                                                                                                    if self._offset > self._failure:
                                                                                                                        self._failure = self._offset
                                                                                                                        self._expected = []
                                                                                                                    if self._offset == self._failure:
                                                                                                                        self._expected.append('[0-9a-zA-Z_]')
                                                                                                                self._offset = index53
                                                                                                                if address52 is FAILURE:
                                                                                                                    address52 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                                                                                                    self._offset = self._offset
                                                                                                                else:
                                                                                                                    address52 = FAILURE
                                                                                                                if address52 is not FAILURE:
                                                                                                                    elements25.append(address52)
                                                                                                                else:
                                                                                                                    elements25 = None
                                                                                                                    self._offset = index52
                                                                                                            else:
                                                                                                                elements25 = None
                                                                                                                self._offset = index52
                                                                                                            if elements25 is None:
                                                                                                                address0 = FAILURE
                                                                                                            else:
                                                                                                                address0 = TreeNode(self._input[index52:self._offset], index52, elements25)
                                                                                                                self._offset = self._offset
                                                                                                            if address0 is FAILURE:
                                                                                                                self._offset = index1
                                                                                                                index54, elements26 = self._offset, []
                                                                                                                address53 = FAILURE
                                                                                                                chunk52, max52 = None, self._offset + 3
                                                                                                                if max52 <= self._input_size:
                                                                                                                    chunk52 = self._input[self._offset:max52]
                                                                                                                if chunk52 == 'has':
                                                                                                                    address53 = TreeNode(self._input[self._offset:self._offset + 3], self._offset, [])
                                                                                                                    self._offset = self._offset + 3
                                                                                                                else:
                                                                                                                    address53 = FAILURE
                                                                                                                    if self._offset > self._failure:
                                                                                                                        self._failure = self._offset
                                                                                                                        self._expected = []
                                                                                                                    if self._offset == self._failure:
                                                                                                                        self._expected.append('\'has\'')
                                                                                                                if address53 is not FAILURE:
                                                                                                                    elements26.append(address53)
                                                                                                                    address54 = FAILURE
                                                                                                                    index55 = self._offset
                                                                                                                    chunk53, max53 = None, self._offset + 1
                                                                                                                    if max53 <= self._input_size:
                                                                                                                        chunk53 = self._input[self._offset:max53]
                                                                                                                    if chunk53 is not None and Grammar.REGEX_31.search(chunk53):
                                                                                                                        address54 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                                                                                                        self._offset = self._offset + 1
                                                                                                                    else:
                                                                                                                        address54 = FAILURE
                                                                                                                        if self._offset > self._failure:
                                                                                                                            self._failure = self._offset
                                                                                                                            self._expected = []
                                                                                                                        if self._offset == self._failure:
                                                                                                                            self._expected.append('[0-9a-zA-Z_]')
                                                                                                                    self._offset = index55
                                                                                                                    if address54 is FAILURE:
                                                                                                                        address54 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                                                                                                        self._offset = self._offset
                                                                                                                    else:
                                                                                                                        address54 = FAILURE
                                                                                                                    if address54 is not FAILURE:
                                                                                                                        elements26.append(address54)
                                                                                                                    else:
                                                                                                                        elements26 = None
                                                                                                                        self._offset = index54
                                                                                                                else:
                                                                                                                    elements26 = None
                                                                                                                    self._offset = index54
                                                                                                                if elements26 is None:
                                                                                                                    address0 = FAILURE
                                                                                                                else:
                                                                                                                    address0 = TreeNode(self._input[index54:self._offset], index54, elements26)
                                                                                                                    self._offset = self._offset
                                                                                                                if address0 is FAILURE:
                                                                                                                    self._offset = index1
                                                                                                                    index56, elements27 = self._offset, []
                                                                                                                    address55 = FAILURE
                                                                                                                    chunk54, max54 = None, self._offset + 9
                                                                                                                    if max54 <= self._input_size:
                                                                                                                        chunk54 = self._input[self._offset:max54]
                                                                                                                    if chunk54 == 'otherwise':
                                                                                                                        address55 = TreeNode(self._input[self._offset:self._offset + 9], self._offset, [])
                                                                                                                        self._offset = self._offset + 9
                                                                                                                    else:
                                                                                                                        address55 = FAILURE
                                                                                                                        if self._offset > self._failure:
                                                                                                                            self._failure = self._offset
                                                                                                                            self._expected = []
                                                                                                                        if self._offset == self._failure:
                                                                                                                            self._expected.append('\'otherwise\'')
                                                                                                                    if address55 is not FAILURE:
                                                                                                                        elements27.append(address55)
                                                                                                                        address56 = FAILURE
                                                                                                                        index57 = self._offset
                                                                                                                        chunk55, max55 = None, self._offset + 1
                                                                                                                        if max55 <= self._input_size:
                                                                                                                            chunk55 = self._input[self._offset:max55]
                                                                                                                        if chunk55 is not None and Grammar.REGEX_32.search(chunk55):
                                                                                                                            address56 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                                                                                                            self._offset = self._offset + 1
                                                                                                                        else:
                                                                                                                            address56 = FAILURE
                                                                                                                            if self._offset > self._failure:
                                                                                                                                self._failure = self._offset
                                                                                                                                self._expected = []
                                                                                                                            if self._offset == self._failure:
                                                                                                                                self._expected.append('[0-9a-zA-Z_]')
                                                                                                                        self._offset = index57
                                                                                                                        if address56 is FAILURE:
                                                                                                                            address56 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                                                                                                            self._offset = self._offset
                                                                                                                        else:
                                                                                                                            address56 = FAILURE
                                                                                                                        if address56 is not FAILURE:
                                                                                                                            elements27.append(address56)
                                                                                                                        else:
                                                                                                                            elements27 = None
                                                                                                                            self._offset = index56
                                                                                                                    else:
                                                                                                                        elements27 = None
                                                                                                                        self._offset = index56
                                                                                                                    if elements27 is None:
                                                                                                                        address0 = FAILURE
                                                                                                                    else:
                                                                                                                        address0 = TreeNode(self._input[index56:self._offset], index56, elements27)
                                                                                                                        self._offset = self._offset
                                                                                                                    if address0 is FAILURE:
                                                                                                                        self._offset = index1
                                                                                                                        index58, elements28 = self._offset, []
                                                                                                                        address57 = FAILURE
                                                                                                                        chunk56, max56 = None, self._offset + 6
                                                                                                                        if max56 <= self._input_size:
                                                                                                                            chunk56 = self._input[self._offset:max56]
                                                                                                                        if chunk56 == 'unless':
                                                                                                                            address57 = TreeNode(self._input[self._offset:self._offset + 6], self._offset, [])
                                                                                                                            self._offset = self._offset + 6
                                                                                                                        else:
                                                                                                                            address57 = FAILURE
                                                                                                                            if self._offset > self._failure:
                                                                                                                                self._failure = self._offset
                                                                                                                                self._expected = []
                                                                                                                            if self._offset == self._failure:
                                                                                                                                self._expected.append('\'unless\'')
                                                                                                                        if address57 is not FAILURE:
                                                                                                                            elements28.append(address57)
                                                                                                                            address58 = FAILURE
                                                                                                                            index59 = self._offset
                                                                                                                            chunk57, max57 = None, self._offset + 1
                                                                                                                            if max57 <= self._input_size:
                                                                                                                                chunk57 = self._input[self._offset:max57]
                                                                                                                            if chunk57 is not None and Grammar.REGEX_33.search(chunk57):
                                                                                                                                address58 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                                                                                                                self._offset = self._offset + 1
                                                                                                                            else:
                                                                                                                                address58 = FAILURE
                                                                                                                                if self._offset > self._failure:
                                                                                                                                    self._failure = self._offset
                                                                                                                                    self._expected = []
                                                                                                                                if self._offset == self._failure:
                                                                                                                                    self._expected.append('[0-9a-zA-Z_]')
                                                                                                                            self._offset = index59
                                                                                                                            if address58 is FAILURE:
                                                                                                                                address58 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                                                                                                                self._offset = self._offset
                                                                                                                            else:
                                                                                                                                address58 = FAILURE
                                                                                                                            if address58 is not FAILURE:
                                                                                                                                elements28.append(address58)
                                                                                                                            else:
                                                                                                                                elements28 = None
                                                                                                                                self._offset = index58
                                                                                                                        else:
                                                                                                                            elements28 = None
                                                                                                                            self._offset = index58
                                                                                                                        if elements28 is None:
                                                                                                                            address0 = FAILURE
                                                                                                                        else:
                                                                                                                            address0 = TreeNode(self._input[index58:self._offset], index58, elements28)
                                                                                                                            self._offset = self._offset
                                                                                                                        if address0 is FAILURE:
                                                                                                                            self._offset = index1
                                                                                                                            index60, elements29 = self._offset, []
                                                                                                                            address59 = FAILURE
                                                                                                                            chunk58, max58 = None, self._offset + 3
                                                                                                                            if max58 <= self._input_size:
                                                                                                                                chunk58 = self._input[self._offset:max58]
                                                                                                                            if chunk58 == 'and':
                                                                                                                                address59 = TreeNode(self._input[self._offset:self._offset + 3], self._offset, [])
                                                                                                                                self._offset = self._offset + 3
                                                                                                                            else:
                                                                                                                                address59 = FAILURE
                                                                                                                                if self._offset > self._failure:
                                                                                                                                    self._failure = self._offset
                                                                                                                                    self._expected = []
                                                                                                                                if self._offset == self._failure:
                                                                                                                                    self._expected.append('\'and\'')
                                                                                                                            if address59 is not FAILURE:
                                                                                                                                elements29.append(address59)
                                                                                                                                address60 = FAILURE
                                                                                                                                index61 = self._offset
                                                                                                                                chunk59, max59 = None, self._offset + 1
                                                                                                                                if max59 <= self._input_size:
                                                                                                                                    chunk59 = self._input[self._offset:max59]
                                                                                                                                if chunk59 is not None and Grammar.REGEX_34.search(chunk59):
                                                                                                                                    address60 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                                                                                                                    self._offset = self._offset + 1
                                                                                                                                else:
                                                                                                                                    address60 = FAILURE
                                                                                                                                    if self._offset > self._failure:
                                                                                                                                        self._failure = self._offset
                                                                                                                                        self._expected = []
                                                                                                                                    if self._offset == self._failure:
                                                                                                                                        self._expected.append('[0-9a-zA-Z_]')
                                                                                                                                self._offset = index61
                                                                                                                                if address60 is FAILURE:
                                                                                                                                    address60 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                                                                                                                    self._offset = self._offset
                                                                                                                                else:
                                                                                                                                    address60 = FAILURE
                                                                                                                                if address60 is not FAILURE:
                                                                                                                                    elements29.append(address60)
                                                                                                                                else:
                                                                                                                                    elements29 = None
                                                                                                                                    self._offset = index60
                                                                                                                            else:
                                                                                                                                elements29 = None
                                                                                                                                self._offset = index60
                                                                                                                            if elements29 is None:
                                                                                                                                address0 = FAILURE
                                                                                                                            else:
                                                                                                                                address0 = TreeNode(self._input[index60:self._offset], index60, elements29)
                                                                                                                                self._offset = self._offset
                                                                                                                            if address0 is FAILURE:
                                                                                                                                self._offset = index1
                                                                                                                                index62, elements30 = self._offset, []
                                                                                                                                address61 = FAILURE
                                                                                                                                chunk60, max60 = None, self._offset + 3
                                                                                                                                if max60 <= self._input_size:
                                                                                                                                    chunk60 = self._input[self._offset:max60]
                                                                                                                                if chunk60 == 'has':
                                                                                                                                    address61 = TreeNode(self._input[self._offset:self._offset + 3], self._offset, [])
                                                                                                                                    self._offset = self._offset + 3
                                                                                                                                else:
                                                                                                                                    address61 = FAILURE
                                                                                                                                    if self._offset > self._failure:
                                                                                                                                        self._failure = self._offset
                                                                                                                                        self._expected = []
                                                                                                                                    if self._offset == self._failure:
                                                                                                                                        self._expected.append('\'has\'')
                                                                                                                                if address61 is not FAILURE:
                                                                                                                                    elements30.append(address61)
                                                                                                                                    address62 = FAILURE
                                                                                                                                    index63 = self._offset
                                                                                                                                    chunk61, max61 = None, self._offset + 1
                                                                                                                                    if max61 <= self._input_size:
                                                                                                                                        chunk61 = self._input[self._offset:max61]
                                                                                                                                    if chunk61 is not None and Grammar.REGEX_35.search(chunk61):
                                                                                                                                        address62 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                                                                                                                        self._offset = self._offset + 1
                                                                                                                                    else:
                                                                                                                                        address62 = FAILURE
                                                                                                                                        if self._offset > self._failure:
                                                                                                                                            self._failure = self._offset
                                                                                                                                            self._expected = []
                                                                                                                                        if self._offset == self._failure:
                                                                                                                                            self._expected.append('[0-9a-zA-Z_]')
                                                                                                                                    self._offset = index63
                                                                                                                                    if address62 is FAILURE:
                                                                                                                                        address62 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                                                                                                                        self._offset = self._offset
                                                                                                                                    else:
                                                                                                                                        address62 = FAILURE
                                                                                                                                    if address62 is not FAILURE:
                                                                                                                                        elements30.append(address62)
                                                                                                                                    else:
                                                                                                                                        elements30 = None
                                                                                                                                        self._offset = index62
                                                                                                                                else:
                                                                                                                                    elements30 = None
                                                                                                                                    self._offset = index62
                                                                                                                                if elements30 is None:
                                                                                                                                    address0 = FAILURE
                                                                                                                                else:
                                                                                                                                    address0 = TreeNode(self._input[index62:self._offset], index62, elements30)
                                                                                                                                    self._offset = self._offset
                                                                                                                                if address0 is FAILURE:
                                                                                                                                    self._offset = index1
                                                                                                                                    index64, elements31 = self._offset, []
                                                                                                                                    address63 = FAILURE
                                                                                                                                    chunk62, max62 = None, self._offset + 3
                                                                                                                                    if max62 <= self._input_size:
                                                                                                                                        chunk62 = self._input[self._offset:max62]
                                                                                                                                    if chunk62 == 'not':
                                                                                                                                        address63 = TreeNode(self._input[self._offset:self._offset + 3], self._offset, [])
                                                                                                                                        self._offset = self._offset + 3
                                                                                                                                    else:
                                                                                                                                        address63 = FAILURE
                                                                                                                                        if self._offset > self._failure:
                                                                                                                                            self._failure = self._offset
                                                                                                                                            self._expected = []
                                                                                                                                        if self._offset == self._failure:
                                                                                                                                            self._expected.append('\'not\'')
                                                                                                                                    if address63 is not FAILURE:
                                                                                                                                        elements31.append(address63)
                                                                                                                                        address64 = FAILURE
                                                                                                                                        index65 = self._offset
                                                                                                                                        chunk63, max63 = None, self._offset + 1
                                                                                                                                        if max63 <= self._input_size:
                                                                                                                                            chunk63 = self._input[self._offset:max63]
                                                                                                                                        if chunk63 is not None and Grammar.REGEX_36.search(chunk63):
                                                                                                                                            address64 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                                                                                                                            self._offset = self._offset + 1
                                                                                                                                        else:
                                                                                                                                            address64 = FAILURE
                                                                                                                                            if self._offset > self._failure:
                                                                                                                                                self._failure = self._offset
                                                                                                                                                self._expected = []
                                                                                                                                            if self._offset == self._failure:
                                                                                                                                                self._expected.append('[0-9a-zA-Z_]')
                                                                                                                                        self._offset = index65
                                                                                                                                        if address64 is FAILURE:
                                                                                                                                            address64 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                                                                                                                            self._offset = self._offset
                                                                                                                                        else:
                                                                                                                                            address64 = FAILURE
                                                                                                                                        if address64 is not FAILURE:
                                                                                                                                            elements31.append(address64)
                                                                                                                                        else:
                                                                                                                                            elements31 = None
                                                                                                                                            self._offset = index64
                                                                                                                                    else:
                                                                                                                                        elements31 = None
                                                                                                                                        self._offset = index64
                                                                                                                                    if elements31 is None:
                                                                                                                                        address0 = FAILURE
                                                                                                                                    else:
                                                                                                                                        address0 = TreeNode(self._input[index64:self._offset], index64, elements31)
                                                                                                                                        self._offset = self._offset
                                                                                                                                    if address0 is FAILURE:
                                                                                                                                        self._offset = index1
                                                                                                                                        index66, elements32 = self._offset, []
                                                                                                                                        address65 = FAILURE
                                                                                                                                        chunk64, max64 = None, self._offset + 2
                                                                                                                                        if max64 <= self._input_size:
                                                                                                                                            chunk64 = self._input[self._offset:max64]
                                                                                                                                        if chunk64 == 'or':
                                                                                                                                            address65 = TreeNode(self._input[self._offset:self._offset + 2], self._offset, [])
                                                                                                                                            self._offset = self._offset + 2
                                                                                                                                        else:
                                                                                                                                            address65 = FAILURE
                                                                                                                                            if self._offset > self._failure:
                                                                                                                                                self._failure = self._offset
                                                                                                                                                self._expected = []
                                                                                                                                            if self._offset == self._failure:
                                                                                                                                                self._expected.append('\'or\'')
                                                                                                                                        if address65 is not FAILURE:
                                                                                                                                            elements32.append(address65)
                                                                                                                                            address66 = FAILURE
                                                                                                                                            index67 = self._offset
                                                                                                                                            chunk65, max65 = None, self._offset + 1
                                                                                                                                            if max65 <= self._input_size:
                                                                                                                                                chunk65 = self._input[self._offset:max65]
                                                                                                                                            if chunk65 is not None and Grammar.REGEX_37.search(chunk65):
                                                                                                                                                address66 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                                                                                                                                self._offset = self._offset + 1
                                                                                                                                            else:
                                                                                                                                                address66 = FAILURE
                                                                                                                                                if self._offset > self._failure:
                                                                                                                                                    self._failure = self._offset
                                                                                                                                                    self._expected = []
                                                                                                                                                if self._offset == self._failure:
                                                                                                                                                    self._expected.append('[0-9a-zA-Z_]')
                                                                                                                                            self._offset = index67
                                                                                                                                            if address66 is FAILURE:
                                                                                                                                                address66 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                                                                                                                                self._offset = self._offset
                                                                                                                                            else:
                                                                                                                                                address66 = FAILURE
                                                                                                                                            if address66 is not FAILURE:
                                                                                                                                                elements32.append(address66)
                                                                                                                                            else:
                                                                                                                                                elements32 = None
                                                                                                                                                self._offset = index66
                                                                                                                                        else:
                                                                                                                                            elements32 = None
                                                                                                                                            self._offset = index66
                                                                                                                                        if elements32 is None:
                                                                                                                                            address0 = FAILURE
                                                                                                                                        else:
                                                                                                                                            address0 = TreeNode(self._input[index66:self._offset], index66, elements32)
                                                                                                                                            self._offset = self._offset
                                                                                                                                        if address0 is FAILURE:
                                                                                                                                            self._offset = index1
                                                                                                                                            index68, elements33 = self._offset, []
                                                                                                                                            address67 = FAILURE
                                                                                                                                            chunk66, max66 = None, self._offset + 3
                                                                                                                                            if max66 <= self._input_size:
                                                                                                                                                chunk66 = self._input[self._offset:max66]
                                                                                                                                            if chunk66 == 'isa':
                                                                                                                                                address67 = TreeNode(self._input[self._offset:self._offset + 3], self._offset, [])
                                                                                                                                                self._offset = self._offset + 3
                                                                                                                                            else:
                                                                                                                                                address67 = FAILURE
                                                                                                                                                if self._offset > self._failure:
                                                                                                                                                    self._failure = self._offset
                                                                                                                                                    self._expected = []
                                                                                                                                                if self._offset == self._failure:
                                                                                                                                                    self._expected.append('\'isa\'')
                                                                                                                                            if address67 is not FAILURE:
                                                                                                                                                elements33.append(address67)
                                                                                                                                                address68 = FAILURE
                                                                                                                                                index69 = self._offset
                                                                                                                                                chunk67, max67 = None, self._offset + 1
                                                                                                                                                if max67 <= self._input_size:
                                                                                                                                                    chunk67 = self._input[self._offset:max67]
                                                                                                                                                if chunk67 is not None and Grammar.REGEX_38.search(chunk67):
                                                                                                                                                    address68 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                                                                                                                                    self._offset = self._offset + 1
                                                                                                                                                else:
                                                                                                                                                    address68 = FAILURE
                                                                                                                                                    if self._offset > self._failure:
                                                                                                                                                        self._failure = self._offset
                                                                                                                                                        self._expected = []
                                                                                                                                                    if self._offset == self._failure:
                                                                                                                                                        self._expected.append('[0-9a-zA-Z_]')
                                                                                                                                                self._offset = index69
                                                                                                                                                if address68 is FAILURE:
                                                                                                                                                    address68 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                                                                                                                                    self._offset = self._offset
                                                                                                                                                else:
                                                                                                                                                    address68 = FAILURE
                                                                                                                                                if address68 is not FAILURE:
                                                                                                                                                    elements33.append(address68)
                                                                                                                                                else:
                                                                                                                                                    elements33 = None
                                                                                                                                                    self._offset = index68
                                                                                                                                            else:
                                                                                                                                                elements33 = None
                                                                                                                                                self._offset = index68
                                                                                                                                            if elements33 is None:
                                                                                                                                                address0 = FAILURE
                                                                                                                                            else:
                                                                                                                                                address0 = TreeNode(self._input[index68:self._offset], index68, elements33)
                                                                                                                                                self._offset = self._offset
                                                                                                                                            if address0 is FAILURE:
                                                                                                                                                self._offset = index1
                                                                                                                                                index70, elements34 = self._offset, []
                                                                                                                                                address69 = FAILURE
                                                                                                                                                chunk68, max68 = None, self._offset + 5
                                                                                                                                                if max68 <= self._input_size:
                                                                                                                                                    chunk68 = self._input[self._offset:max68]
                                                                                                                                                if chunk68 == 'clear':
                                                                                                                                                    address69 = TreeNode(self._input[self._offset:self._offset + 5], self._offset, [])
                                                                                                                                                    self._offset = self._offset + 5
                                                                                                                                                else:
                                                                                                                                                    address69 = FAILURE
                                                                                                                                                    if self._offset > self._failure:
                                                                                                                                                        self._failure = self._offset
                                                                                                                                                        self._expected = []
                                                                                                                                                    if self._offset == self._failure:
                                                                                                                                                        self._expected.append('\'clear\'')
                                                                                                                                                if address69 is not FAILURE:
                                                                                                                                                    elements34.append(address69)
                                                                                                                                                    address70 = FAILURE
                                                                                                                                                    index71 = self._offset
                                                                                                                                                    chunk69, max69 = None, self._offset + 1
                                                                                                                                                    if max69 <= self._input_size:
                                                                                                                                                        chunk69 = self._input[self._offset:max69]
                                                                                                                                                    if chunk69 is not None and Grammar.REGEX_39.search(chunk69):
                                                                                                                                                        address70 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                                                                                                                                        self._offset = self._offset + 1
                                                                                                                                                    else:
                                                                                                                                                        address70 = FAILURE
                                                                                                                                                        if self._offset > self._failure:
                                                                                                                                                            self._failure = self._offset
                                                                                                                                                            self._expected = []
                                                                                                                                                        if self._offset == self._failure:
                                                                                                                                                            self._expected.append('[0-9a-zA-Z_]')
                                                                                                                                                    self._offset = index71
                                                                                                                                                    if address70 is FAILURE:
                                                                                                                                                        address70 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                                                                                                                                        self._offset = self._offset
                                                                                                                                                    else:
                                                                                                                                                        address70 = FAILURE
                                                                                                                                                    if address70 is not FAILURE:
                                                                                                                                                        elements34.append(address70)
                                                                                                                                                    else:
                                                                                                                                                        elements34 = None
                                                                                                                                                        self._offset = index70
                                                                                                                                                else:
                                                                                                                                                    elements34 = None
                                                                                                                                                    self._offset = index70
                                                                                                                                                if elements34 is None:
                                                                                                                                                    address0 = FAILURE
                                                                                                                                                else:
                                                                                                                                                    address0 = TreeNode(self._input[index70:self._offset], index70, elements34)
                                                                                                                                                    self._offset = self._offset
                                                                                                                                                if address0 is FAILURE:
                                                                                                                                                    self._offset = index1
                                                                                                                                                    index72, elements35 = self._offset, []
                                                                                                                                                    address71 = FAILURE
                                                                                                                                                    chunk70, max70 = None, self._offset + 7
                                                                                                                                                    if max70 <= self._input_size:
                                                                                                                                                        chunk70 = self._input[self._offset:max70]
                                                                                                                                                    if chunk70 == 'restart':
                                                                                                                                                        address71 = TreeNode(self._input[self._offset:self._offset + 7], self._offset, [])
                                                                                                                                                        self._offset = self._offset + 7
                                                                                                                                                    else:
                                                                                                                                                        address71 = FAILURE
                                                                                                                                                        if self._offset > self._failure:
                                                                                                                                                            self._failure = self._offset
                                                                                                                                                            self._expected = []
                                                                                                                                                        if self._offset == self._failure:
                                                                                                                                                            self._expected.append('\'restart\'')
                                                                                                                                                    if address71 is not FAILURE:
                                                                                                                                                        elements35.append(address71)
                                                                                                                                                        address72 = FAILURE
                                                                                                                                                        index73 = self._offset
                                                                                                                                                        chunk71, max71 = None, self._offset + 1
                                                                                                                                                        if max71 <= self._input_size:
                                                                                                                                                            chunk71 = self._input[self._offset:max71]
                                                                                                                                                        if chunk71 is not None and Grammar.REGEX_40.search(chunk71):
                                                                                                                                                            address72 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                                                                                                                                            self._offset = self._offset + 1
                                                                                                                                                        else:
                                                                                                                                                            address72 = FAILURE
                                                                                                                                                            if self._offset > self._failure:
                                                                                                                                                                self._failure = self._offset
                                                                                                                                                                self._expected = []
                                                                                                                                                            if self._offset == self._failure:
                                                                                                                                                                self._expected.append('[0-9a-zA-Z_]')
                                                                                                                                                        self._offset = index73
                                                                                                                                                        if address72 is FAILURE:
                                                                                                                                                            address72 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                                                                                                                                            self._offset = self._offset
                                                                                                                                                        else:
                                                                                                                                                            address72 = FAILURE
                                                                                                                                                        if address72 is not FAILURE:
                                                                                                                                                            elements35.append(address72)
                                                                                                                                                        else:
                                                                                                                                                            elements35 = None
                                                                                                                                                            self._offset = index72
                                                                                                                                                    else:
                                                                                                                                                        elements35 = None
                                                                                                                                                        self._offset = index72
                                                                                                                                                    if elements35 is None:
                                                                                                                                                        address0 = FAILURE
                                                                                                                                                    else:
                                                                                                                                                        address0 = TreeNode(self._input[index72:self._offset], index72, elements35)
                                                                                                                                                        self._offset = self._offset
                                                                                                                                                    if address0 is FAILURE:
                                                                                                                                                        self._offset = index1
        self._cache['keyword'][index0] = (address0, self._offset)
        return address0

    def _read_eos(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['eos'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        address0 = self._read_eol()
        if address0 is FAILURE:
            self._offset = index1
            remaining0, index2, elements0, address1 = 1, self._offset, [], True
            while address1 is not FAILURE:
                chunk0, max0 = None, self._offset + 1
                if max0 <= self._input_size:
                    chunk0 = self._input[self._offset:max0]
                if chunk0 == '|':
                    address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                    self._offset = self._offset + 1
                else:
                    address1 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('\'|\'')
                if address1 is not FAILURE:
                    elements0.append(address1)
                    remaining0 -= 1
            if remaining0 <= 0:
                address0 = self._actions.ignore(self._input, index2, self._offset, elements0)
                self._offset = self._offset
            else:
                address0 = FAILURE
            if address0 is FAILURE:
                self._offset = index1
                index3, elements1 = self._offset, []
                address2 = FAILURE
                address2 = self._read__()
                if address2 is not FAILURE:
                    elements1.append(address2)
                    address3 = FAILURE
                    index4 = self._offset
                    chunk1, max1 = None, self._offset + 1
                    if max1 <= self._input_size:
                        chunk1 = self._input[self._offset:max1]
                    if chunk1 == ']':
                        address3 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                        self._offset = self._offset + 1
                    else:
                        address3 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('\']\'')
                    self._offset = index4
                    if address3 is not FAILURE:
                        address3 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                        self._offset = self._offset
                    else:
                        address3 = FAILURE
                    if address3 is not FAILURE:
                        elements1.append(address3)
                    else:
                        elements1 = None
                        self._offset = index3
                else:
                    elements1 = None
                    self._offset = index3
                if elements1 is None:
                    address0 = FAILURE
                else:
                    address0 = TreeNode3(self._input[index3:self._offset], index3, elements1)
                    self._offset = self._offset
                if address0 is FAILURE:
                    self._offset = index1
                    index5, elements2 = self._offset, []
                    address4 = FAILURE
                    address4 = self._read__()
                    if address4 is not FAILURE:
                        elements2.append(address4)
                        address5 = FAILURE
                        index6 = self._offset
                        chunk2, max2 = None, self._offset + 2
                        if max2 <= self._input_size:
                            chunk2 = self._input[self._offset:max2]
                        if chunk2 == ':}':
                            address5 = TreeNode(self._input[self._offset:self._offset + 2], self._offset, [])
                            self._offset = self._offset + 2
                        else:
                            address5 = FAILURE
                            if self._offset > self._failure:
                                self._failure = self._offset
                                self._expected = []
                            if self._offset == self._failure:
                                self._expected.append('\':}\'')
                        self._offset = index6
                        if address5 is not FAILURE:
                            address5 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                            self._offset = self._offset
                        else:
                            address5 = FAILURE
                        if address5 is not FAILURE:
                            elements2.append(address5)
                        else:
                            elements2 = None
                            self._offset = index5
                    else:
                        elements2 = None
                        self._offset = index5
                    if elements2 is None:
                        address0 = FAILURE
                    else:
                        address0 = TreeNode4(self._input[index5:self._offset], index5, elements2)
                        self._offset = self._offset
                    if address0 is FAILURE:
                        self._offset = index1
                        index7, elements3 = self._offset, []
                        address6 = FAILURE
                        address6 = self._read__()
                        if address6 is not FAILURE:
                            elements3.append(address6)
                            address7 = FAILURE
                            index8 = self._offset
                            chunk3, max3 = None, self._offset + 3
                            if max3 <= self._input_size:
                                chunk3 = self._input[self._offset:max3]
                            if chunk3 == 'but':
                                address7 = TreeNode(self._input[self._offset:self._offset + 3], self._offset, [])
                                self._offset = self._offset + 3
                            else:
                                address7 = FAILURE
                                if self._offset > self._failure:
                                    self._failure = self._offset
                                    self._expected = []
                                if self._offset == self._failure:
                                    self._expected.append('\'but\'')
                            self._offset = index8
                            if address7 is not FAILURE:
                                address7 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                self._offset = self._offset
                            else:
                                address7 = FAILURE
                            if address7 is not FAILURE:
                                elements3.append(address7)
                            else:
                                elements3 = None
                                self._offset = index7
                        else:
                            elements3 = None
                            self._offset = index7
                        if elements3 is None:
                            address0 = FAILURE
                        else:
                            address0 = TreeNode5(self._input[index7:self._offset], index7, elements3)
                            self._offset = self._offset
                        if address0 is FAILURE:
                            self._offset = index1
        self._cache['eos'][index0] = (address0, self._offset)
        return address0

    def _read__ws(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['_ws'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        remaining0, index1, elements0, address1 = 0, self._offset, [], True
        while address1 is not FAILURE:
            chunk0, max0 = None, self._offset + 1
            if max0 <= self._input_size:
                chunk0 = self._input[self._offset:max0]
            if chunk0 is not None and Grammar.REGEX_41.search(chunk0):
                address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                self._offset = self._offset + 1
            else:
                address1 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('[\\n\\r\\f \\t]')
            if address1 is not FAILURE:
                elements0.append(address1)
                remaining0 -= 1
        if remaining0 <= 0:
            address0 = self._actions.ignore(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        else:
            address0 = FAILURE
        self._cache['_ws'][index0] = (address0, self._offset)
        return address0

    def _read_line_joining(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['line_joining'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        chunk0, max0 = None, self._offset + 2
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == '%>':
            address1 = TreeNode(self._input[self._offset:self._offset + 2], self._offset, [])
            self._offset = self._offset + 2
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'%>\'')
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read__()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                remaining0, index2, elements1, address4 = 1, self._offset, [], True
                while address4 is not FAILURE:
                    chunk1, max1 = None, self._offset + 1
                    if max1 <= self._input_size:
                        chunk1 = self._input[self._offset:max1]
                    if chunk1 is not None and Grammar.REGEX_42.search(chunk1):
                        address4 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                        self._offset = self._offset + 1
                    else:
                        address4 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('[\\n\\r\\f]')
                    if address4 is not FAILURE:
                        elements1.append(address4)
                        remaining0 -= 1
                if remaining0 <= 0:
                    address3 = TreeNode(self._input[index2:self._offset], index2, elements1)
                    self._offset = self._offset
                else:
                    address3 = FAILURE
                if address3 is not FAILURE:
                    elements0.append(address3)
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.ignore(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['line_joining'][index0] = (address0, self._offset)
        return address0

    def _read_float(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['float'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        index2 = self._offset
        chunk0, max0 = None, self._offset + 1
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == '-':
            address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
            self._offset = self._offset + 1
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'-\'')
        if address1 is FAILURE:
            address1 = TreeNode(self._input[index2:index2], index2, [])
            self._offset = index2
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            remaining0, index3, elements1, address3 = 0, self._offset, [], True
            while address3 is not FAILURE:
                chunk1, max1 = None, self._offset + 1
                if max1 <= self._input_size:
                    chunk1 = self._input[self._offset:max1]
                if chunk1 is not None and Grammar.REGEX_43.search(chunk1):
                    address3 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                    self._offset = self._offset + 1
                else:
                    address3 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('[0-9]')
                if address3 is not FAILURE:
                    elements1.append(address3)
                    remaining0 -= 1
            if remaining0 <= 0:
                address2 = TreeNode(self._input[index3:self._offset], index3, elements1)
                self._offset = self._offset
            else:
                address2 = FAILURE
            if address2 is not FAILURE:
                elements0.append(address2)
                address4 = FAILURE
                chunk2, max2 = None, self._offset + 1
                if max2 <= self._input_size:
                    chunk2 = self._input[self._offset:max2]
                if chunk2 == '.':
                    address4 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                    self._offset = self._offset + 1
                else:
                    address4 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('\'.\'')
                if address4 is not FAILURE:
                    elements0.append(address4)
                    address5 = FAILURE
                    remaining1, index4, elements2, address6 = 1, self._offset, [], True
                    while address6 is not FAILURE:
                        chunk3, max3 = None, self._offset + 1
                        if max3 <= self._input_size:
                            chunk3 = self._input[self._offset:max3]
                        if chunk3 is not None and Grammar.REGEX_44.search(chunk3):
                            address6 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                            self._offset = self._offset + 1
                        else:
                            address6 = FAILURE
                            if self._offset > self._failure:
                                self._failure = self._offset
                                self._expected = []
                            if self._offset == self._failure:
                                self._expected.append('[0-9]')
                        if address6 is not FAILURE:
                            elements2.append(address6)
                            remaining1 -= 1
                    if remaining1 <= 0:
                        address5 = TreeNode(self._input[index4:self._offset], index4, elements2)
                        self._offset = self._offset
                    else:
                        address5 = FAILURE
                    if address5 is not FAILURE:
                        elements0.append(address5)
                    else:
                        elements0 = None
                        self._offset = index1
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.float_(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['float'][index0] = (address0, self._offset)
        return address0

    def _read_int(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['int'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        index2 = self._offset
        chunk0, max0 = None, self._offset + 1
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == '-':
            address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
            self._offset = self._offset + 1
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'-\'')
        if address1 is FAILURE:
            address1 = TreeNode(self._input[index2:index2], index2, [])
            self._offset = index2
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            remaining0, index3, elements1, address3 = 1, self._offset, [], True
            while address3 is not FAILURE:
                chunk1, max1 = None, self._offset + 1
                if max1 <= self._input_size:
                    chunk1 = self._input[self._offset:max1]
                if chunk1 is not None and Grammar.REGEX_45.search(chunk1):
                    address3 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                    self._offset = self._offset + 1
                else:
                    address3 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('[0-9]')
                if address3 is not FAILURE:
                    elements1.append(address3)
                    remaining0 -= 1
            if remaining0 <= 0:
                address2 = TreeNode(self._input[index3:self._offset], index3, elements1)
                self._offset = self._offset
            else:
                address2 = FAILURE
            if address2 is not FAILURE:
                elements0.append(address2)
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.int_(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['int'][index0] = (address0, self._offset)
        return address0

    def _read_number(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['number'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        address0 = self._read_float()
        if address0 is FAILURE:
            self._offset = index1
            address0 = self._read_int()
            if address0 is FAILURE:
                self._offset = index1
        self._cache['number'][index0] = (address0, self._offset)
        return address0

    def _read_string_escape(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['string_escape'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        chunk0, max0 = None, self._offset + 1
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == '\\':
            address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
            self._offset = self._offset + 1
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('"\\\\"')
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            chunk1, max1 = None, self._offset + 1
            if max1 <= self._input_size:
                chunk1 = self._input[self._offset:max1]
            if chunk1 is not None and Grammar.REGEX_46.search(chunk1):
                address2 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                self._offset = self._offset + 1
            else:
                address2 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('[\\\\runftvb\']')
            if address2 is not FAILURE:
                elements0.append(address2)
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        self._cache['string_escape'][index0] = (address0, self._offset)
        return address0

    def _read_string(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['string'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        chunk0, max0 = None, self._offset + 1
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == '\'':
            address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
            self._offset = self._offset + 1
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('"\'"')
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            remaining0, index2, elements1, address3 = 0, self._offset, [], True
            while address3 is not FAILURE:
                index3 = self._offset
                address3 = self._read_string_escape()
                if address3 is FAILURE:
                    self._offset = index3
                    chunk1, max1 = None, self._offset + 1
                    if max1 <= self._input_size:
                        chunk1 = self._input[self._offset:max1]
                    if chunk1 is not None and Grammar.REGEX_47.search(chunk1):
                        address3 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                        self._offset = self._offset + 1
                    else:
                        address3 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('[^\']')
                    if address3 is FAILURE:
                        self._offset = index3
                if address3 is not FAILURE:
                    elements1.append(address3)
                    remaining0 -= 1
            if remaining0 <= 0:
                address2 = TreeNode(self._input[index2:self._offset], index2, elements1)
                self._offset = self._offset
            else:
                address2 = FAILURE
            if address2 is not FAILURE:
                elements0.append(address2)
                address4 = FAILURE
                chunk2, max2 = None, self._offset + 1
                if max2 <= self._input_size:
                    chunk2 = self._input[self._offset:max2]
                if chunk2 == '\'':
                    address4 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                    self._offset = self._offset + 1
                else:
                    address4 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('"\'"')
                if address4 is not FAILURE:
                    elements0.append(address4)
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.string(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['string'][index0] = (address0, self._offset)
        return address0

    def _read_basic_name(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['basic_name'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        index2 = self._offset
        index3, elements1 = self._offset, []
        address2 = FAILURE
        address2 = self._read_keyword()
        if address2 is not FAILURE:
            elements1.append(address2)
            address3 = FAILURE
            index4 = self._offset
            address3 = self._read__()
            if address3 is FAILURE:
                self._offset = index4
                address3 = self._read_eos()
                if address3 is FAILURE:
                    self._offset = index4
            if address3 is not FAILURE:
                elements1.append(address3)
            else:
                elements1 = None
                self._offset = index3
        else:
            elements1 = None
            self._offset = index3
        if elements1 is None:
            address1 = FAILURE
        else:
            address1 = TreeNode7(self._input[index3:self._offset], index3, elements1)
            self._offset = self._offset
        self._offset = index2
        if address1 is FAILURE:
            address1 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
            self._offset = self._offset
        else:
            address1 = FAILURE
        if address1 is not FAILURE:
            elements0.append(address1)
            address4 = FAILURE
            chunk0, max0 = None, self._offset + 1
            if max0 <= self._input_size:
                chunk0 = self._input[self._offset:max0]
            if chunk0 is not None and Grammar.REGEX_48.search(chunk0):
                address4 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                self._offset = self._offset + 1
            else:
                address4 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('[a-zA-Z_]')
            if address4 is not FAILURE:
                elements0.append(address4)
                address5 = FAILURE
                remaining0, index5, elements2, address6 = 0, self._offset, [], True
                while address6 is not FAILURE:
                    chunk1, max1 = None, self._offset + 1
                    if max1 <= self._input_size:
                        chunk1 = self._input[self._offset:max1]
                    if chunk1 is not None and Grammar.REGEX_49.search(chunk1):
                        address6 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                        self._offset = self._offset + 1
                    else:
                        address6 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('[a-zA-Z_0-9]')
                    if address6 is not FAILURE:
                        elements2.append(address6)
                        remaining0 -= 1
                if remaining0 <= 0:
                    address5 = TreeNode(self._input[index5:self._offset], index5, elements2)
                    self._offset = self._offset
                else:
                    address5 = FAILURE
                if address5 is not FAILURE:
                    elements0.append(address5)
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.reference(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['basic_name'][index0] = (address0, self._offset)
        return address0

    def _read_name(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['name'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        chunk0, max0 = None, self._offset + 1
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == '$':
            address0 = self._actions.special_ref(self._input, self._offset, self._offset + 1, [])
            self._offset = self._offset + 1
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'$\'')
        if address0 is FAILURE:
            self._offset = index1
            chunk1, max1 = None, self._offset + 1
            if max1 <= self._input_size:
                chunk1 = self._input[self._offset:max1]
            if chunk1 == '?':
                address0 = self._actions.special_ref(self._input, self._offset, self._offset + 1, [])
                self._offset = self._offset + 1
            else:
                address0 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('\'?\'')
            if address0 is FAILURE:
                self._offset = index1
                chunk2, max2 = None, self._offset + 1
                if max2 <= self._input_size:
                    chunk2 = self._input[self._offset:max2]
                if chunk2 == '~':
                    address0 = self._actions.special_ref(self._input, self._offset, self._offset + 1, [])
                    self._offset = self._offset + 1
                else:
                    address0 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('\'~\'')
                if address0 is FAILURE:
                    self._offset = index1
                    chunk3, max3 = None, self._offset + 1
                    if max3 <= self._input_size:
                        chunk3 = self._input[self._offset:max3]
                    if chunk3 == '!':
                        address0 = self._actions.special_ref(self._input, self._offset, self._offset + 1, [])
                        self._offset = self._offset + 1
                    else:
                        address0 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('\'!\'')
                    if address0 is FAILURE:
                        self._offset = index1
                        chunk4, max4 = None, self._offset + 1
                        if max4 <= self._input_size:
                            chunk4 = self._input[self._offset:max4]
                        if chunk4 == '#':
                            address0 = self._actions.special_ref(self._input, self._offset, self._offset + 1, [])
                            self._offset = self._offset + 1
                        else:
                            address0 = FAILURE
                            if self._offset > self._failure:
                                self._failure = self._offset
                                self._expected = []
                            if self._offset == self._failure:
                                self._expected.append('\'#\'')
                        if address0 is FAILURE:
                            self._offset = index1
                            chunk5, max5 = None, self._offset + 1
                            if max5 <= self._input_size:
                                chunk5 = self._input[self._offset:max5]
                            if chunk5 == '@':
                                address0 = self._actions.special_ref(self._input, self._offset, self._offset + 1, [])
                                self._offset = self._offset + 1
                            else:
                                address0 = FAILURE
                                if self._offset > self._failure:
                                    self._failure = self._offset
                                    self._expected = []
                                if self._offset == self._failure:
                                    self._expected.append('\'@\'')
                            if address0 is FAILURE:
                                self._offset = index1
                                address0 = self._read_basic_name()
                                if address0 is FAILURE:
                                    self._offset = index1
        self._cache['name'][index0] = (address0, self._offset)
        return address0

    def _read_special_entry(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['special_entry'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        chunk0, max0 = None, self._offset + 1
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == '^':
            address0 = self._actions.special_entry(self._input, self._offset, self._offset + 1, [])
            self._offset = self._offset + 1
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'^\'')
        if address0 is FAILURE:
            self._offset = index1
            chunk1, max1 = None, self._offset + 1
            if max1 <= self._input_size:
                chunk1 = self._input[self._offset:max1]
            if chunk1 == '.':
                address0 = self._actions.special_entry(self._input, self._offset, self._offset + 1, [])
                self._offset = self._offset + 1
            else:
                address0 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('\'.\'')
            if address0 is FAILURE:
                self._offset = index1
                chunk2, max2 = None, self._offset + 1
                if max2 <= self._input_size:
                    chunk2 = self._input[self._offset:max2]
                if chunk2 == '=':
                    address0 = self._actions.special_entry(self._input, self._offset, self._offset + 1, [])
                    self._offset = self._offset + 1
                else:
                    address0 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('\'=\'')
                if address0 is FAILURE:
                    self._offset = index1
                    chunk3, max3 = None, self._offset + 5
                    if max3 <= self._input_size:
                        chunk3 = self._input[self._offset:max3]
                    if chunk3 == 'clear':
                        address0 = self._actions.special_entry(self._input, self._offset, self._offset + 5, [])
                        self._offset = self._offset + 5
                    else:
                        address0 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('\'clear\'')
                    if address0 is FAILURE:
                        self._offset = index1
                        chunk4, max4 = None, self._offset + 1
                        if max4 <= self._input_size:
                            chunk4 = self._input[self._offset:max4]
                        if chunk4 == ':':
                            address0 = self._actions.special_entry(self._input, self._offset, self._offset + 1, [])
                            self._offset = self._offset + 1
                        else:
                            address0 = FAILURE
                            if self._offset > self._failure:
                                self._failure = self._offset
                                self._expected = []
                            if self._offset == self._failure:
                                self._expected.append('\':\'')
                        if address0 is FAILURE:
                            self._offset = index1
                            chunk5, max5 = None, self._offset + 1
                            if max5 <= self._input_size:
                                chunk5 = self._input[self._offset:max5]
                            if chunk5 == '!':
                                address0 = self._actions.special_entry(self._input, self._offset, self._offset + 1, [])
                                self._offset = self._offset + 1
                            else:
                                address0 = FAILURE
                                if self._offset > self._failure:
                                    self._failure = self._offset
                                    self._expected = []
                                if self._offset == self._failure:
                                    self._expected.append('\'!\'')
                            if address0 is FAILURE:
                                self._offset = index1
        self._cache['special_entry'][index0] = (address0, self._offset)
        return address0

    def _read_new_bag(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['new_bag'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        index2, elements0 = self._offset, []
        address1 = FAILURE
        chunk0, max0 = None, self._offset + 2
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == '{:':
            address1 = TreeNode(self._input[self._offset:self._offset + 2], self._offset, [])
            self._offset = self._offset + 2
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'{:\'')
        if address1 is not FAILURE:
            address2 = FAILURE
            address2 = self._read__ws()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                remaining0, index3, elements1, address4 = 0, self._offset, [], True
                while address4 is not FAILURE:
                    index4, elements2 = self._offset, []
                    address5 = FAILURE
                    address5 = self._read__()
                    if address5 is not FAILURE:
                        elements2.append(address5)
                        address6 = FAILURE
                        address6 = self._read_statement()
                        if address6 is not FAILURE:
                            elements2.append(address6)
                            address7 = FAILURE
                            address7 = self._read__()
                            if address7 is not FAILURE:
                                elements2.append(address7)
                                address8 = FAILURE
                                index5 = self._offset
                                chunk1, max1 = None, self._offset + 2
                                if max1 <= self._input_size:
                                    chunk1 = self._input[self._offset:max1]
                                if chunk1 == ':}':
                                    address8 = TreeNode(self._input[self._offset:self._offset + 2], self._offset, [])
                                    self._offset = self._offset + 2
                                else:
                                    address8 = FAILURE
                                    if self._offset > self._failure:
                                        self._failure = self._offset
                                        self._expected = []
                                    if self._offset == self._failure:
                                        self._expected.append('\':}\'')
                                self._offset = index5
                                if address8 is FAILURE:
                                    address8 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                    self._offset = self._offset
                                else:
                                    address8 = FAILURE
                                if address8 is not FAILURE:
                                    elements2.append(address8)
                                else:
                                    elements2 = None
                                    self._offset = index4
                            else:
                                elements2 = None
                                self._offset = index4
                        else:
                            elements2 = None
                            self._offset = index4
                    else:
                        elements2 = None
                        self._offset = index4
                    if elements2 is None:
                        address4 = FAILURE
                    else:
                        address4 = TreeNode9(self._input[index4:self._offset], index4, elements2)
                        self._offset = self._offset
                    if address4 is not FAILURE:
                        elements1.append(address4)
                        remaining0 -= 1
                if remaining0 <= 0:
                    address3 = TreeNode(self._input[index3:self._offset], index3, elements1)
                    self._offset = self._offset
                else:
                    address3 = FAILURE
                if address3 is not FAILURE:
                    elements0.append(address3)
                    address9 = FAILURE
                    address9 = self._read__()
                    if address9 is not FAILURE:
                        elements0.append(address9)
                        address10 = FAILURE
                        address10 = self._read_statement()
                        if address10 is not FAILURE:
                            elements0.append(address10)
                            address11 = FAILURE
                            address11 = self._read__ws()
                            if address11 is not FAILURE:
                                elements0.append(address11)
                                address12 = FAILURE
                                chunk2, max2 = None, self._offset + 2
                                if max2 <= self._input_size:
                                    chunk2 = self._input[self._offset:max2]
                                if chunk2 == ':}':
                                    address12 = TreeNode(self._input[self._offset:self._offset + 2], self._offset, [])
                                    self._offset = self._offset + 2
                                else:
                                    address12 = FAILURE
                                    if self._offset > self._failure:
                                        self._failure = self._offset
                                        self._expected = []
                                    if self._offset == self._failure:
                                        self._expected.append('\':}\'')
                                if address12 is not FAILURE:
                                    address13 = FAILURE
                                    address13 = self._read__()
                                    if address13 is not FAILURE:
                                        elements0.append(address13)
                                    else:
                                        elements0 = None
                                        self._offset = index2
                                else:
                                    elements0 = None
                                    self._offset = index2
                            else:
                                elements0 = None
                                self._offset = index2
                        else:
                            elements0 = None
                            self._offset = index2
                    else:
                        elements0 = None
                        self._offset = index2
                else:
                    elements0 = None
                    self._offset = index2
            else:
                elements0 = None
                self._offset = index2
        else:
            elements0 = None
            self._offset = index2
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.new_bag(self._input, index2, self._offset, elements0)
            self._offset = self._offset
        if address0 is FAILURE:
            self._offset = index1
            index6, elements3 = self._offset, []
            address14 = FAILURE
            chunk3, max3 = None, self._offset + 1
            if max3 <= self._input_size:
                chunk3 = self._input[self._offset:max3]
            if chunk3 == '{':
                address14 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                self._offset = self._offset + 1
            else:
                address14 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('\'{\'')
            if address14 is not FAILURE:
                address15 = FAILURE
                address15 = self._read__()
                if address15 is not FAILURE:
                    elements3.append(address15)
                    address16 = FAILURE
                    chunk4, max4 = None, self._offset + 1
                    if max4 <= self._input_size:
                        chunk4 = self._input[self._offset:max4]
                    if chunk4 == ':':
                        address16 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                        self._offset = self._offset + 1
                    else:
                        address16 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('\':\'')
                    if address16 is not FAILURE:
                        address17 = FAILURE
                        address17 = self._read__()
                        if address17 is not FAILURE:
                            elements3.append(address17)
                            address18 = FAILURE
                            chunk5, max5 = None, self._offset + 1
                            if max5 <= self._input_size:
                                chunk5 = self._input[self._offset:max5]
                            if chunk5 == '}':
                                address18 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                self._offset = self._offset + 1
                            else:
                                address18 = FAILURE
                                if self._offset > self._failure:
                                    self._failure = self._offset
                                    self._expected = []
                                if self._offset == self._failure:
                                    self._expected.append('\'}\'')
                            if address18 is not FAILURE:
                                address19 = FAILURE
                                address19 = self._read__()
                                if address19 is not FAILURE:
                                    elements3.append(address19)
                                else:
                                    elements3 = None
                                    self._offset = index6
                            else:
                                elements3 = None
                                self._offset = index6
                        else:
                            elements3 = None
                            self._offset = index6
                    else:
                        elements3 = None
                        self._offset = index6
                else:
                    elements3 = None
                    self._offset = index6
            else:
                elements3 = None
                self._offset = index6
            if elements3 is None:
                address0 = FAILURE
            else:
                address0 = self._actions.new_bag(self._input, index6, self._offset, elements3)
                self._offset = self._offset
            if address0 is FAILURE:
                self._offset = index1
                index7, elements4 = self._offset, []
                address20 = FAILURE
                chunk6, max6 = None, self._offset + 2
                if max6 <= self._input_size:
                    chunk6 = self._input[self._offset:max6]
                if chunk6 == '{:':
                    address20 = TreeNode(self._input[self._offset:self._offset + 2], self._offset, [])
                    self._offset = self._offset + 2
                else:
                    address20 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('\'{:\'')
                if address20 is not FAILURE:
                    address21 = FAILURE
                    address21 = self._read__ws()
                    if address21 is not FAILURE:
                        elements4.append(address21)
                        address22 = FAILURE
                        chunk7, max7 = None, self._offset + 2
                        if max7 <= self._input_size:
                            chunk7 = self._input[self._offset:max7]
                        if chunk7 == ':}':
                            address22 = TreeNode(self._input[self._offset:self._offset + 2], self._offset, [])
                            self._offset = self._offset + 2
                        else:
                            address22 = FAILURE
                            if self._offset > self._failure:
                                self._failure = self._offset
                                self._expected = []
                            if self._offset == self._failure:
                                self._expected.append('\':}\'')
                        if address22 is not FAILURE:
                            address23 = FAILURE
                            address23 = self._read__()
                            if address23 is not FAILURE:
                                elements4.append(address23)
                            else:
                                elements4 = None
                                self._offset = index7
                        else:
                            elements4 = None
                            self._offset = index7
                    else:
                        elements4 = None
                        self._offset = index7
                else:
                    elements4 = None
                    self._offset = index7
                if elements4 is None:
                    address0 = FAILURE
                else:
                    address0 = self._actions.new_bag(self._input, index7, self._offset, elements4)
                    self._offset = self._offset
                if address0 is FAILURE:
                    self._offset = index1
        self._cache['new_bag'][index0] = (address0, self._offset)
        return address0

    def _read_roll_item(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['roll_item'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        index2, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_expression()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read__()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                chunk0, max0 = None, self._offset + 3
                if max0 <= self._input_size:
                    chunk0 = self._input[self._offset:max0]
                if chunk0 == '<->':
                    address3 = TreeNode(self._input[self._offset:self._offset + 3], self._offset, [])
                    self._offset = self._offset + 3
                else:
                    address3 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('\'<->\'')
                if address3 is not FAILURE:
                    address4 = FAILURE
                    address4 = self._read__()
                    if address4 is not FAILURE:
                        elements0.append(address4)
                        address5 = FAILURE
                        address5 = self._read_expression()
                        if address5 is not FAILURE:
                            elements0.append(address5)
                        else:
                            elements0 = None
                            self._offset = index2
                    else:
                        elements0 = None
                        self._offset = index2
                else:
                    elements0 = None
                    self._offset = index2
            else:
                elements0 = None
                self._offset = index2
        else:
            elements0 = None
            self._offset = index2
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.fill(self._input, index2, self._offset, elements0)
            self._offset = self._offset
        if address0 is FAILURE:
            self._offset = index1
            address0 = self._read_expression()
            if address0 is FAILURE:
                self._offset = index1
        self._cache['roll_item'][index0] = (address0, self._offset)
        return address0

    def _read_roll_def(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['roll_def'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        index2, elements0 = self._offset, []
        address1 = FAILURE
        chunk0, max0 = None, self._offset + 2
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == '[:':
            address1 = TreeNode(self._input[self._offset:self._offset + 2], self._offset, [])
            self._offset = self._offset + 2
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'[:\'')
        if address1 is not FAILURE:
            address2 = FAILURE
            address2 = self._read__ws()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                remaining0, index3, elements1, address4 = 0, self._offset, [], True
                while address4 is not FAILURE:
                    index4, elements2 = self._offset, []
                    address5 = FAILURE
                    address5 = self._read_roll_item()
                    if address5 is not FAILURE:
                        elements2.append(address5)
                        address6 = FAILURE
                        address6 = self._read__()
                        if address6 is not FAILURE:
                            elements2.append(address6)
                            address7 = FAILURE
                            chunk1, max1 = None, self._offset + 1
                            if max1 <= self._input_size:
                                chunk1 = self._input[self._offset:max1]
                            if chunk1 == ',':
                                address7 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                self._offset = self._offset + 1
                            else:
                                address7 = FAILURE
                                if self._offset > self._failure:
                                    self._failure = self._offset
                                    self._expected = []
                                if self._offset == self._failure:
                                    self._expected.append('\',\'')
                            if address7 is not FAILURE:
                                address8 = FAILURE
                                address8 = self._read__ws()
                                if address8 is not FAILURE:
                                    elements2.append(address8)
                                else:
                                    elements2 = None
                                    self._offset = index4
                            else:
                                elements2 = None
                                self._offset = index4
                        else:
                            elements2 = None
                            self._offset = index4
                    else:
                        elements2 = None
                        self._offset = index4
                    if elements2 is None:
                        address4 = FAILURE
                    else:
                        address4 = TreeNode14(self._input[index4:self._offset], index4, elements2)
                        self._offset = self._offset
                    if address4 is not FAILURE:
                        elements1.append(address4)
                        remaining0 -= 1
                if remaining0 <= 0:
                    address3 = TreeNode(self._input[index3:self._offset], index3, elements1)
                    self._offset = self._offset
                else:
                    address3 = FAILURE
                if address3 is not FAILURE:
                    elements0.append(address3)
                    address9 = FAILURE
                    index5 = self._offset
                    address9 = self._read_roll_item()
                    if address9 is FAILURE:
                        address9 = TreeNode(self._input[index5:index5], index5, [])
                        self._offset = index5
                    if address9 is not FAILURE:
                        elements0.append(address9)
                        address10 = FAILURE
                        address10 = self._read__ws()
                        if address10 is not FAILURE:
                            elements0.append(address10)
                            address11 = FAILURE
                            chunk2, max2 = None, self._offset + 2
                            if max2 <= self._input_size:
                                chunk2 = self._input[self._offset:max2]
                            if chunk2 == ':]':
                                address11 = TreeNode(self._input[self._offset:self._offset + 2], self._offset, [])
                                self._offset = self._offset + 2
                            else:
                                address11 = FAILURE
                                if self._offset > self._failure:
                                    self._failure = self._offset
                                    self._expected = []
                                if self._offset == self._failure:
                                    self._expected.append('\':]\'')
                            if address11 is not FAILURE:
                                address12 = FAILURE
                                address12 = self._read__()
                                if address12 is not FAILURE:
                                    elements0.append(address12)
                                else:
                                    elements0 = None
                                    self._offset = index2
                            else:
                                elements0 = None
                                self._offset = index2
                        else:
                            elements0 = None
                            self._offset = index2
                    else:
                        elements0 = None
                        self._offset = index2
                else:
                    elements0 = None
                    self._offset = index2
            else:
                elements0 = None
                self._offset = index2
        else:
            elements0 = None
            self._offset = index2
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.roll_def(self._input, index2, self._offset, elements0)
            self._offset = self._offset
        if address0 is FAILURE:
            self._offset = index1
            index6, elements3 = self._offset, []
            address13 = FAILURE
            chunk3, max3 = None, self._offset + 1
            if max3 <= self._input_size:
                chunk3 = self._input[self._offset:max3]
            if chunk3 == '[':
                address13 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                self._offset = self._offset + 1
            else:
                address13 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('\'[\'')
            if address13 is not FAILURE:
                elements3.append(address13)
                address14 = FAILURE
                address14 = self._read__()
                if address14 is not FAILURE:
                    elements3.append(address14)
                    address15 = FAILURE
                    chunk4, max4 = None, self._offset + 1
                    if max4 <= self._input_size:
                        chunk4 = self._input[self._offset:max4]
                    if chunk4 == ':':
                        address15 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                        self._offset = self._offset + 1
                    else:
                        address15 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('\':\'')
                    if address15 is not FAILURE:
                        elements3.append(address15)
                        address16 = FAILURE
                        address16 = self._read__()
                        if address16 is not FAILURE:
                            elements3.append(address16)
                            address17 = FAILURE
                            chunk5, max5 = None, self._offset + 1
                            if max5 <= self._input_size:
                                chunk5 = self._input[self._offset:max5]
                            if chunk5 == ']':
                                address17 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                self._offset = self._offset + 1
                            else:
                                address17 = FAILURE
                                if self._offset > self._failure:
                                    self._failure = self._offset
                                    self._expected = []
                                if self._offset == self._failure:
                                    self._expected.append('\']\'')
                            if address17 is not FAILURE:
                                elements3.append(address17)
                            else:
                                elements3 = None
                                self._offset = index6
                        else:
                            elements3 = None
                            self._offset = index6
                    else:
                        elements3 = None
                        self._offset = index6
                else:
                    elements3 = None
                    self._offset = index6
            else:
                elements3 = None
                self._offset = index6
            if elements3 is None:
                address0 = FAILURE
            else:
                address0 = self._actions.empty_roll(self._input, index6, self._offset, elements3)
                self._offset = self._offset
            if address0 is FAILURE:
                self._offset = index1
        self._cache['roll_def'][index0] = (address0, self._offset)
        return address0

    def _read_reduce(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['reduce'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        chunk0, max0 = None, self._offset + 1
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == '{':
            address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
            self._offset = self._offset + 1
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'{\'')
        if address1 is not FAILURE:
            address2 = FAILURE
            address2 = self._read__ws()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                index2 = self._offset
                index3 = self._offset
                chunk1, max1 = None, self._offset + 1
                if max1 <= self._input_size:
                    chunk1 = self._input[self._offset:max1]
                if chunk1 == ':':
                    address3 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                    self._offset = self._offset + 1
                else:
                    address3 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('\':\'')
                if address3 is FAILURE:
                    self._offset = index3
                    address3 = self._read_special_accessor()
                    if address3 is FAILURE:
                        self._offset = index3
                self._offset = index2
                if address3 is FAILURE:
                    address3 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                    self._offset = self._offset
                else:
                    address3 = FAILURE
                if address3 is not FAILURE:
                    elements0.append(address3)
                    address4 = FAILURE
                    address4 = self._read_expression()
                    if address4 is not FAILURE:
                        elements0.append(address4)
                        address5 = FAILURE
                        address5 = self._read__ws()
                        if address5 is not FAILURE:
                            elements0.append(address5)
                            address6 = FAILURE
                            chunk2, max2 = None, self._offset + 1
                            if max2 <= self._input_size:
                                chunk2 = self._input[self._offset:max2]
                            if chunk2 == '}':
                                address6 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                self._offset = self._offset + 1
                            else:
                                address6 = FAILURE
                                if self._offset > self._failure:
                                    self._failure = self._offset
                                    self._expected = []
                                if self._offset == self._failure:
                                    self._expected.append('\'}\'')
                            if address6 is not FAILURE:
                                address7 = FAILURE
                                address7 = self._read__()
                                if address7 is not FAILURE:
                                    elements0.append(address7)
                                else:
                                    elements0 = None
                                    self._offset = index1
                            else:
                                elements0 = None
                                self._offset = index1
                        else:
                            elements0 = None
                            self._offset = index1
                    else:
                        elements0 = None
                        self._offset = index1
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.reduce(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['reduce'][index0] = (address0, self._offset)
        return address0

    def _read_two_sided_op(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['two_sided_op'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        chunk0, max0 = None, self._offset + 1
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == '*':
            address0 = self._actions.two_sided_operator(self._input, self._offset, self._offset + 1, [])
            self._offset = self._offset + 1
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'*\'')
        if address0 is FAILURE:
            self._offset = index1
            chunk1, max1 = None, self._offset + 2
            if max1 <= self._input_size:
                chunk1 = self._input[self._offset:max1]
            if chunk1 == '%/':
                address0 = self._actions.two_sided_operator(self._input, self._offset, self._offset + 2, [])
                self._offset = self._offset + 2
            else:
                address0 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('\'%/\'')
            if address0 is FAILURE:
                self._offset = index1
                chunk2, max2 = None, self._offset + 1
                if max2 <= self._input_size:
                    chunk2 = self._input[self._offset:max2]
                if chunk2 == '/':
                    address0 = self._actions.two_sided_operator(self._input, self._offset, self._offset + 1, [])
                    self._offset = self._offset + 1
                else:
                    address0 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('\'/\'')
                if address0 is FAILURE:
                    self._offset = index1
                    chunk3, max3 = None, self._offset + 1
                    if max3 <= self._input_size:
                        chunk3 = self._input[self._offset:max3]
                    if chunk3 == '%':
                        address0 = self._actions.two_sided_operator(self._input, self._offset, self._offset + 1, [])
                        self._offset = self._offset + 1
                    else:
                        address0 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('\'%\'')
                    if address0 is FAILURE:
                        self._offset = index1
                        chunk4, max4 = None, self._offset + 1
                        if max4 <= self._input_size:
                            chunk4 = self._input[self._offset:max4]
                        if chunk4 == '+':
                            address0 = self._actions.two_sided_operator(self._input, self._offset, self._offset + 1, [])
                            self._offset = self._offset + 1
                        else:
                            address0 = FAILURE
                            if self._offset > self._failure:
                                self._failure = self._offset
                                self._expected = []
                            if self._offset == self._failure:
                                self._expected.append('\'+\'')
                        if address0 is FAILURE:
                            self._offset = index1
                            index2, elements0 = self._offset, []
                            address1 = FAILURE
                            chunk5, max5 = None, self._offset + 1
                            if max5 <= self._input_size:
                                chunk5 = self._input[self._offset:max5]
                            if chunk5 == '-':
                                address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                self._offset = self._offset + 1
                            else:
                                address1 = FAILURE
                                if self._offset > self._failure:
                                    self._failure = self._offset
                                    self._expected = []
                                if self._offset == self._failure:
                                    self._expected.append('\'-\'')
                            if address1 is not FAILURE:
                                elements0.append(address1)
                                address2 = FAILURE
                                index3 = self._offset
                                chunk6, max6 = None, self._offset + 1
                                if max6 <= self._input_size:
                                    chunk6 = self._input[self._offset:max6]
                                if chunk6 is not None and Grammar.REGEX_50.search(chunk6):
                                    address2 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                    self._offset = self._offset + 1
                                else:
                                    address2 = FAILURE
                                    if self._offset > self._failure:
                                        self._failure = self._offset
                                        self._expected = []
                                    if self._offset == self._failure:
                                        self._expected.append('[a-z_A-Z]')
                                self._offset = index3
                                if address2 is FAILURE:
                                    address2 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                    self._offset = self._offset
                                else:
                                    address2 = FAILURE
                                if address2 is not FAILURE:
                                    elements0.append(address2)
                                else:
                                    elements0 = None
                                    self._offset = index2
                            else:
                                elements0 = None
                                self._offset = index2
                            if elements0 is None:
                                address0 = FAILURE
                            else:
                                address0 = self._actions.two_sided_operator(self._input, index2, self._offset, elements0)
                                self._offset = self._offset
                            if address0 is FAILURE:
                                self._offset = index1
                                chunk7, max7 = None, self._offset + 2
                                if max7 <= self._input_size:
                                    chunk7 = self._input[self._offset:max7]
                                if chunk7 == 'or':
                                    address0 = self._actions.two_sided_operator(self._input, self._offset, self._offset + 2, [])
                                    self._offset = self._offset + 2
                                else:
                                    address0 = FAILURE
                                    if self._offset > self._failure:
                                        self._failure = self._offset
                                        self._expected = []
                                    if self._offset == self._failure:
                                        self._expected.append('\'or\'')
                                if address0 is FAILURE:
                                    self._offset = index1
                                    chunk8, max8 = None, self._offset + 3
                                    if max8 <= self._input_size:
                                        chunk8 = self._input[self._offset:max8]
                                    if chunk8 == 'and':
                                        address0 = self._actions.two_sided_operator(self._input, self._offset, self._offset + 3, [])
                                        self._offset = self._offset + 3
                                    else:
                                        address0 = FAILURE
                                        if self._offset > self._failure:
                                            self._failure = self._offset
                                            self._expected = []
                                        if self._offset == self._failure:
                                            self._expected.append('\'and\'')
                                    if address0 is FAILURE:
                                        self._offset = index1
                                        chunk9, max9 = None, self._offset + 3
                                        if max9 <= self._input_size:
                                            chunk9 = self._input[self._offset:max9]
                                        if chunk9 == 'isa':
                                            address0 = self._actions.two_sided_operator(self._input, self._offset, self._offset + 3, [])
                                            self._offset = self._offset + 3
                                        else:
                                            address0 = FAILURE
                                            if self._offset > self._failure:
                                                self._failure = self._offset
                                                self._expected = []
                                            if self._offset == self._failure:
                                                self._expected.append('\'isa\'')
                                        if address0 is FAILURE:
                                            self._offset = index1
                                            chunk10, max10 = None, self._offset + 1
                                            if max10 <= self._input_size:
                                                chunk10 = self._input[self._offset:max10]
                                            if chunk10 == '@':
                                                address0 = self._actions.two_sided_operator(self._input, self._offset, self._offset + 1, [])
                                                self._offset = self._offset + 1
                                            else:
                                                address0 = FAILURE
                                                if self._offset > self._failure:
                                                    self._failure = self._offset
                                                    self._expected = []
                                                if self._offset == self._failure:
                                                    self._expected.append('\'@\'')
                                            if address0 is FAILURE:
                                                self._offset = index1
                                                chunk11, max11 = None, self._offset + 2
                                                if max11 <= self._input_size:
                                                    chunk11 = self._input[self._offset:max11]
                                                if chunk11 == '==':
                                                    address0 = self._actions.two_sided_operator(self._input, self._offset, self._offset + 2, [])
                                                    self._offset = self._offset + 2
                                                else:
                                                    address0 = FAILURE
                                                    if self._offset > self._failure:
                                                        self._failure = self._offset
                                                        self._expected = []
                                                    if self._offset == self._failure:
                                                        self._expected.append('\'==\'')
                                                if address0 is FAILURE:
                                                    self._offset = index1
                                                    chunk12, max12 = None, self._offset + 2
                                                    if max12 <= self._input_size:
                                                        chunk12 = self._input[self._offset:max12]
                                                    if chunk12 == '!=':
                                                        address0 = self._actions.two_sided_operator(self._input, self._offset, self._offset + 2, [])
                                                        self._offset = self._offset + 2
                                                    else:
                                                        address0 = FAILURE
                                                        if self._offset > self._failure:
                                                            self._failure = self._offset
                                                            self._expected = []
                                                        if self._offset == self._failure:
                                                            self._expected.append('\'!=\'')
                                                    if address0 is FAILURE:
                                                        self._offset = index1
                                                        chunk13, max13 = None, self._offset + 2
                                                        if max13 <= self._input_size:
                                                            chunk13 = self._input[self._offset:max13]
                                                        if chunk13 == '<=':
                                                            address0 = self._actions.two_sided_operator(self._input, self._offset, self._offset + 2, [])
                                                            self._offset = self._offset + 2
                                                        else:
                                                            address0 = FAILURE
                                                            if self._offset > self._failure:
                                                                self._failure = self._offset
                                                                self._expected = []
                                                            if self._offset == self._failure:
                                                                self._expected.append('\'<=\'')
                                                        if address0 is FAILURE:
                                                            self._offset = index1
                                                            chunk14, max14 = None, self._offset + 2
                                                            if max14 <= self._input_size:
                                                                chunk14 = self._input[self._offset:max14]
                                                            if chunk14 == '>=':
                                                                address0 = self._actions.two_sided_operator(self._input, self._offset, self._offset + 2, [])
                                                                self._offset = self._offset + 2
                                                            else:
                                                                address0 = FAILURE
                                                                if self._offset > self._failure:
                                                                    self._failure = self._offset
                                                                    self._expected = []
                                                                if self._offset == self._failure:
                                                                    self._expected.append('\'>=\'')
                                                            if address0 is FAILURE:
                                                                self._offset = index1
                                                                chunk15, max15 = None, self._offset + 1
                                                                if max15 <= self._input_size:
                                                                    chunk15 = self._input[self._offset:max15]
                                                                if chunk15 == '<':
                                                                    address0 = self._actions.two_sided_operator(self._input, self._offset, self._offset + 1, [])
                                                                    self._offset = self._offset + 1
                                                                else:
                                                                    address0 = FAILURE
                                                                    if self._offset > self._failure:
                                                                        self._failure = self._offset
                                                                        self._expected = []
                                                                    if self._offset == self._failure:
                                                                        self._expected.append('\'<\'')
                                                                if address0 is FAILURE:
                                                                    self._offset = index1
                                                                    chunk16, max16 = None, self._offset + 1
                                                                    if max16 <= self._input_size:
                                                                        chunk16 = self._input[self._offset:max16]
                                                                    if chunk16 == '>':
                                                                        address0 = self._actions.two_sided_operator(self._input, self._offset, self._offset + 1, [])
                                                                        self._offset = self._offset + 1
                                                                    else:
                                                                        address0 = FAILURE
                                                                        if self._offset > self._failure:
                                                                            self._failure = self._offset
                                                                            self._expected = []
                                                                        if self._offset == self._failure:
                                                                            self._expected.append('\'>\'')
                                                                    if address0 is FAILURE:
                                                                        self._offset = index1
                                                                        chunk17, max17 = None, self._offset + 1
                                                                        if max17 <= self._input_size:
                                                                            chunk17 = self._input[self._offset:max17]
                                                                        if chunk17 == '&':
                                                                            address0 = self._actions.two_sided_operator(self._input, self._offset, self._offset + 1, [])
                                                                            self._offset = self._offset + 1
                                                                        else:
                                                                            address0 = FAILURE
                                                                            if self._offset > self._failure:
                                                                                self._failure = self._offset
                                                                                self._expected = []
                                                                            if self._offset == self._failure:
                                                                                self._expected.append('\'&\'')
                                                                        if address0 is FAILURE:
                                                                            self._offset = index1
        self._cache['two_sided_op'][index0] = (address0, self._offset)
        return address0

    def _read_one_sided_op(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['one_sided_op'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        chunk0, max0 = None, self._offset + 3
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == 'has':
            address0 = self._actions.one_sided_operator(self._input, self._offset, self._offset + 3, [])
            self._offset = self._offset + 3
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'has\'')
        if address0 is FAILURE:
            self._offset = index1
            chunk1, max1 = None, self._offset + 1
            if max1 <= self._input_size:
                chunk1 = self._input[self._offset:max1]
            if chunk1 == '#':
                address0 = self._actions.overload_only_operator(self._input, self._offset, self._offset + 1, [])
                self._offset = self._offset + 1
            else:
                address0 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('\'#\'')
            if address0 is FAILURE:
                self._offset = index1
                chunk2, max2 = None, self._offset + 1
                if max2 <= self._input_size:
                    chunk2 = self._input[self._offset:max2]
                if chunk2 == '0':
                    address0 = self._actions.overload_only_operator(self._input, self._offset, self._offset + 1, [])
                    self._offset = self._offset + 1
                else:
                    address0 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('\'0\'')
                if address0 is FAILURE:
                    self._offset = index1
                    index2, elements0 = self._offset, []
                    address1 = FAILURE
                    chunk3, max3 = None, self._offset + 1
                    if max3 <= self._input_size:
                        chunk3 = self._input[self._offset:max3]
                    if chunk3 == '{':
                        address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                        self._offset = self._offset + 1
                    else:
                        address1 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('\'{\'')
                    if address1 is not FAILURE:
                        elements0.append(address1)
                        address2 = FAILURE
                        address2 = self._read__()
                        if address2 is not FAILURE:
                            elements0.append(address2)
                            address3 = FAILURE
                            chunk4, max4 = None, self._offset + 1
                            if max4 <= self._input_size:
                                chunk4 = self._input[self._offset:max4]
                            if chunk4 == '}':
                                address3 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                self._offset = self._offset + 1
                            else:
                                address3 = FAILURE
                                if self._offset > self._failure:
                                    self._failure = self._offset
                                    self._expected = []
                                if self._offset == self._failure:
                                    self._expected.append('\'}\'')
                            if address3 is not FAILURE:
                                elements0.append(address3)
                            else:
                                elements0 = None
                                self._offset = index2
                        else:
                            elements0 = None
                            self._offset = index2
                    else:
                        elements0 = None
                        self._offset = index2
                    if elements0 is None:
                        address0 = FAILURE
                    else:
                        address0 = self._actions.overload_only_operator(self._input, index2, self._offset, elements0)
                        self._offset = self._offset
                    if address0 is FAILURE:
                        self._offset = index1
                        index3, elements1 = self._offset, []
                        address4 = FAILURE
                        chunk5, max5 = None, self._offset + 3
                        if max5 <= self._input_size:
                            chunk5 = self._input[self._offset:max5]
                        if chunk5 == 'for':
                            address4 = TreeNode(self._input[self._offset:self._offset + 3], self._offset, [])
                            self._offset = self._offset + 3
                        else:
                            address4 = FAILURE
                            if self._offset > self._failure:
                                self._failure = self._offset
                                self._expected = []
                            if self._offset == self._failure:
                                self._expected.append('\'for\'')
                        if address4 is not FAILURE:
                            elements1.append(address4)
                            address5 = FAILURE
                            address5 = self._read__()
                            if address5 is not FAILURE:
                                elements1.append(address5)
                                address6 = FAILURE
                                chunk6, max6 = None, self._offset + 5
                                if max6 <= self._input_size:
                                    chunk6 = self._input[self._offset:max6]
                                if chunk6 == 'every':
                                    address6 = TreeNode(self._input[self._offset:self._offset + 5], self._offset, [])
                                    self._offset = self._offset + 5
                                else:
                                    address6 = FAILURE
                                    if self._offset > self._failure:
                                        self._failure = self._offset
                                        self._expected = []
                                    if self._offset == self._failure:
                                        self._expected.append('\'every\'')
                                if address6 is not FAILURE:
                                    elements1.append(address6)
                                else:
                                    elements1 = None
                                    self._offset = index3
                            else:
                                elements1 = None
                                self._offset = index3
                        else:
                            elements1 = None
                            self._offset = index3
                        if elements1 is None:
                            address0 = FAILURE
                        else:
                            address0 = self._actions.overload_only_operator(self._input, index3, self._offset, elements1)
                            self._offset = self._offset
                        if address0 is FAILURE:
                            self._offset = index1
                            chunk7, max7 = None, self._offset + 1
                            if max7 <= self._input_size:
                                chunk7 = self._input[self._offset:max7]
                            if chunk7 == '?':
                                address0 = self._actions.overload_only_operator(self._input, self._offset, self._offset + 1, [])
                                self._offset = self._offset + 1
                            else:
                                address0 = FAILURE
                                if self._offset > self._failure:
                                    self._failure = self._offset
                                    self._expected = []
                                if self._offset == self._failure:
                                    self._expected.append('\'?\'')
                            if address0 is FAILURE:
                                self._offset = index1
        self._cache['one_sided_op'][index0] = (address0, self._offset)
        return address0

    def _read_overload_op(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['overload_op'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        index2, elements0 = self._offset, []
        address1 = FAILURE
        chunk0, max0 = None, self._offset + 2
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == '<[':
            address1 = TreeNode(self._input[self._offset:self._offset + 2], self._offset, [])
            self._offset = self._offset + 2
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'<[\'')
        if address1 is not FAILURE:
            address2 = FAILURE
            address2 = self._read__()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                address3 = self._read_two_sided_op()
                if address3 is not FAILURE:
                    elements0.append(address3)
                    address4 = FAILURE
                    address4 = self._read__()
                    if address4 is not FAILURE:
                        elements0.append(address4)
                        address5 = FAILURE
                        chunk1, max1 = None, self._offset + 1
                        if max1 <= self._input_size:
                            chunk1 = self._input[self._offset:max1]
                        if chunk1 == ']':
                            address5 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                            self._offset = self._offset + 1
                        else:
                            address5 = FAILURE
                            if self._offset > self._failure:
                                self._failure = self._offset
                                self._expected = []
                            if self._offset == self._failure:
                                self._expected.append('\']\'')
                        if address5 is not FAILURE:
                            address6 = FAILURE
                            address6 = self._read__()
                            if address6 is not FAILURE:
                                elements0.append(address6)
                            else:
                                elements0 = None
                                self._offset = index2
                        else:
                            elements0 = None
                            self._offset = index2
                    else:
                        elements0 = None
                        self._offset = index2
                else:
                    elements0 = None
                    self._offset = index2
            else:
                elements0 = None
                self._offset = index2
        else:
            elements0 = None
            self._offset = index2
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.left_op_overload(self._input, index2, self._offset, elements0)
            self._offset = self._offset
        if address0 is FAILURE:
            self._offset = index1
            index3, elements1 = self._offset, []
            address7 = FAILURE
            chunk2, max2 = None, self._offset + 1
            if max2 <= self._input_size:
                chunk2 = self._input[self._offset:max2]
            if chunk2 == '[':
                address7 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                self._offset = self._offset + 1
            else:
                address7 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('\'[\'')
            if address7 is not FAILURE:
                address8 = FAILURE
                address8 = self._read__()
                if address8 is not FAILURE:
                    elements1.append(address8)
                    address9 = FAILURE
                    address9 = self._read_two_sided_op()
                    if address9 is not FAILURE:
                        elements1.append(address9)
                        address10 = FAILURE
                        address10 = self._read__()
                        if address10 is not FAILURE:
                            elements1.append(address10)
                            address11 = FAILURE
                            chunk3, max3 = None, self._offset + 2
                            if max3 <= self._input_size:
                                chunk3 = self._input[self._offset:max3]
                            if chunk3 == ']>':
                                address11 = TreeNode(self._input[self._offset:self._offset + 2], self._offset, [])
                                self._offset = self._offset + 2
                            else:
                                address11 = FAILURE
                                if self._offset > self._failure:
                                    self._failure = self._offset
                                    self._expected = []
                                if self._offset == self._failure:
                                    self._expected.append('\']>\'')
                            if address11 is not FAILURE:
                                address12 = FAILURE
                                address12 = self._read__()
                                if address12 is not FAILURE:
                                    elements1.append(address12)
                                else:
                                    elements1 = None
                                    self._offset = index3
                            else:
                                elements1 = None
                                self._offset = index3
                        else:
                            elements1 = None
                            self._offset = index3
                    else:
                        elements1 = None
                        self._offset = index3
                else:
                    elements1 = None
                    self._offset = index3
            else:
                elements1 = None
                self._offset = index3
            if elements1 is None:
                address0 = FAILURE
            else:
                address0 = self._actions.right_op_overload(self._input, index3, self._offset, elements1)
                self._offset = self._offset
            if address0 is FAILURE:
                self._offset = index1
                index4, elements2 = self._offset, []
                address13 = FAILURE
                chunk4, max4 = None, self._offset + 1
                if max4 <= self._input_size:
                    chunk4 = self._input[self._offset:max4]
                if chunk4 == '[':
                    address13 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                    self._offset = self._offset + 1
                else:
                    address13 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('\'[\'')
                if address13 is not FAILURE:
                    address14 = FAILURE
                    address14 = self._read__()
                    if address14 is not FAILURE:
                        elements2.append(address14)
                        address15 = FAILURE
                        address15 = self._read_one_sided_op()
                        if address15 is not FAILURE:
                            elements2.append(address15)
                            address16 = FAILURE
                            address16 = self._read__()
                            if address16 is not FAILURE:
                                elements2.append(address16)
                                address17 = FAILURE
                                chunk5, max5 = None, self._offset + 1
                                if max5 <= self._input_size:
                                    chunk5 = self._input[self._offset:max5]
                                if chunk5 == ']':
                                    address17 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                    self._offset = self._offset + 1
                                else:
                                    address17 = FAILURE
                                    if self._offset > self._failure:
                                        self._failure = self._offset
                                        self._expected = []
                                    if self._offset == self._failure:
                                        self._expected.append('\']\'')
                                if address17 is not FAILURE:
                                    address18 = FAILURE
                                    address18 = self._read__()
                                    if address18 is not FAILURE:
                                        elements2.append(address18)
                                    else:
                                        elements2 = None
                                        self._offset = index4
                                else:
                                    elements2 = None
                                    self._offset = index4
                            else:
                                elements2 = None
                                self._offset = index4
                        else:
                            elements2 = None
                            self._offset = index4
                    else:
                        elements2 = None
                        self._offset = index4
                else:
                    elements2 = None
                    self._offset = index4
                if elements2 is None:
                    address0 = FAILURE
                else:
                    address0 = self._actions.one_sided_op_overload(self._input, index4, self._offset, elements2)
                    self._offset = self._offset
                if address0 is FAILURE:
                    self._offset = index1
        self._cache['overload_op'][index0] = (address0, self._offset)
        return address0

    def _read_special_accessor(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['special_accessor'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        chunk0, max0 = None, self._offset + 1
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == '#':
            address0 = self._actions.special_accessor(self._input, self._offset, self._offset + 1, [])
            self._offset = self._offset + 1
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'#\'')
        if address0 is FAILURE:
            self._offset = index1
            chunk1, max1 = None, self._offset + 1
            if max1 <= self._input_size:
                chunk1 = self._input[self._offset:max1]
            if chunk1 == '*':
                address0 = self._actions.special_accessor(self._input, self._offset, self._offset + 1, [])
                self._offset = self._offset + 1
            else:
                address0 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('\'*\'')
            if address0 is FAILURE:
                self._offset = index1
                chunk2, max2 = None, self._offset + 1
                if max2 <= self._input_size:
                    chunk2 = self._input[self._offset:max2]
                if chunk2 == '+':
                    address0 = self._actions.special_accessor(self._input, self._offset, self._offset + 1, [])
                    self._offset = self._offset + 1
                else:
                    address0 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('\'+\'')
                if address0 is FAILURE:
                    self._offset = index1
                    chunk3, max3 = None, self._offset + 1
                    if max3 <= self._input_size:
                        chunk3 = self._input[self._offset:max3]
                    if chunk3 == '=':
                        address0 = self._actions.special_accessor(self._input, self._offset, self._offset + 1, [])
                        self._offset = self._offset + 1
                    else:
                        address0 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('\'=\'')
                    if address0 is FAILURE:
                        self._offset = index1
                        chunk4, max4 = None, self._offset + 1
                        if max4 <= self._input_size:
                            chunk4 = self._input[self._offset:max4]
                        if chunk4 == '^':
                            address0 = self._actions.special_accessor(self._input, self._offset, self._offset + 1, [])
                            self._offset = self._offset + 1
                        else:
                            address0 = FAILURE
                            if self._offset > self._failure:
                                self._failure = self._offset
                                self._expected = []
                            if self._offset == self._failure:
                                self._expected.append('\'^\'')
                        if address0 is FAILURE:
                            self._offset = index1
        self._cache['special_accessor'][index0] = (address0, self._offset)
        return address0

    def _read_accessor(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['accessor'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        index2, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_basic_name()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read__()
            if address2 is not FAILURE:
                elements0.append(address2)
            else:
                elements0 = None
                self._offset = index2
        else:
            elements0 = None
            self._offset = index2
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode22(self._input[index2:self._offset], index2, elements0)
            self._offset = self._offset
        if address0 is FAILURE:
            self._offset = index1
            index3, elements1 = self._offset, []
            address3 = FAILURE
            chunk0, max0 = None, self._offset + 1
            if max0 <= self._input_size:
                chunk0 = self._input[self._offset:max0]
            if chunk0 == '{':
                address3 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                self._offset = self._offset + 1
            else:
                address3 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('\'{\'')
            if address3 is not FAILURE:
                address4 = FAILURE
                address4 = self._read__()
                if address4 is not FAILURE:
                    elements1.append(address4)
                    address5 = FAILURE
                    address5 = self._read_special_accessor()
                    if address5 is not FAILURE:
                        elements1.append(address5)
                        address6 = FAILURE
                        address6 = self._read__()
                        if address6 is not FAILURE:
                            elements1.append(address6)
                            address7 = FAILURE
                            chunk1, max1 = None, self._offset + 1
                            if max1 <= self._input_size:
                                chunk1 = self._input[self._offset:max1]
                            if chunk1 == '}':
                                address7 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                self._offset = self._offset + 1
                            else:
                                address7 = FAILURE
                                if self._offset > self._failure:
                                    self._failure = self._offset
                                    self._expected = []
                                if self._offset == self._failure:
                                    self._expected.append('\'}\'')
                            if address7 is not FAILURE:
                                address8 = FAILURE
                                address8 = self._read__()
                                if address8 is not FAILURE:
                                    elements1.append(address8)
                                else:
                                    elements1 = None
                                    self._offset = index3
                            else:
                                elements1 = None
                                self._offset = index3
                        else:
                            elements1 = None
                            self._offset = index3
                    else:
                        elements1 = None
                        self._offset = index3
                else:
                    elements1 = None
                    self._offset = index3
            else:
                elements1 = None
                self._offset = index3
            if elements1 is None:
                address0 = FAILURE
            else:
                address0 = TreeNode23(self._input[index3:self._offset], index3, elements1)
                self._offset = self._offset
            if address0 is FAILURE:
                self._offset = index1
                index4, elements2 = self._offset, []
                address9 = FAILURE
                chunk2, max2 = None, self._offset + 1
                if max2 <= self._input_size:
                    chunk2 = self._input[self._offset:max2]
                if chunk2 == '<':
                    address9 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                    self._offset = self._offset + 1
                else:
                    address9 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('\'<\'')
                if address9 is not FAILURE:
                    address10 = FAILURE
                    index5 = self._offset
                    chunk3, max3 = None, self._offset + 1
                    if max3 <= self._input_size:
                        chunk3 = self._input[self._offset:max3]
                    if chunk3 == '[':
                        address10 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                        self._offset = self._offset + 1
                    else:
                        address10 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('\'[\'')
                    self._offset = index5
                    if address10 is FAILURE:
                        address10 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                        self._offset = self._offset
                    else:
                        address10 = FAILURE
                    if address10 is not FAILURE:
                        elements2.append(address10)
                        address11 = FAILURE
                        address11 = self._read__()
                        if address11 is not FAILURE:
                            elements2.append(address11)
                            address12 = FAILURE
                            address12 = self._read_special_entry()
                            if address12 is not FAILURE:
                                elements2.append(address12)
                                address13 = FAILURE
                                address13 = self._read__()
                                if address13 is not FAILURE:
                                    elements2.append(address13)
                                    address14 = FAILURE
                                    chunk4, max4 = None, self._offset + 1
                                    if max4 <= self._input_size:
                                        chunk4 = self._input[self._offset:max4]
                                    if chunk4 == '>':
                                        address14 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                        self._offset = self._offset + 1
                                    else:
                                        address14 = FAILURE
                                        if self._offset > self._failure:
                                            self._failure = self._offset
                                            self._expected = []
                                        if self._offset == self._failure:
                                            self._expected.append('\'>\'')
                                    if address14 is not FAILURE:
                                        address15 = FAILURE
                                        address15 = self._read__()
                                        if address15 is not FAILURE:
                                            elements2.append(address15)
                                        else:
                                            elements2 = None
                                            self._offset = index4
                                    else:
                                        elements2 = None
                                        self._offset = index4
                                else:
                                    elements2 = None
                                    self._offset = index4
                            else:
                                elements2 = None
                                self._offset = index4
                        else:
                            elements2 = None
                            self._offset = index4
                    else:
                        elements2 = None
                        self._offset = index4
                else:
                    elements2 = None
                    self._offset = index4
                if elements2 is None:
                    address0 = FAILURE
                else:
                    address0 = TreeNode24(self._input[index4:self._offset], index4, elements2)
                    self._offset = self._offset
                if address0 is FAILURE:
                    self._offset = index1
                    index6, elements3 = self._offset, []
                    address16 = FAILURE
                    chunk5, max5 = None, self._offset + 1
                    if max5 <= self._input_size:
                        chunk5 = self._input[self._offset:max5]
                    if chunk5 == '<':
                        address16 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                        self._offset = self._offset + 1
                    else:
                        address16 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('\'<\'')
                    if address16 is not FAILURE:
                        address17 = FAILURE
                        index7 = self._offset
                        chunk6, max6 = None, self._offset + 1
                        if max6 <= self._input_size:
                            chunk6 = self._input[self._offset:max6]
                        if chunk6 == '[':
                            address17 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                            self._offset = self._offset + 1
                        else:
                            address17 = FAILURE
                            if self._offset > self._failure:
                                self._failure = self._offset
                                self._expected = []
                            if self._offset == self._failure:
                                self._expected.append('\'[\'')
                        self._offset = index7
                        if address17 is FAILURE:
                            address17 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                            self._offset = self._offset
                        else:
                            address17 = FAILURE
                        if address17 is not FAILURE:
                            elements3.append(address17)
                            address18 = FAILURE
                            address18 = self._read__()
                            if address18 is not FAILURE:
                                elements3.append(address18)
                                address19 = FAILURE
                                address19 = self._read_expression()
                                if address19 is not FAILURE:
                                    elements3.append(address19)
                                    address20 = FAILURE
                                    address20 = self._read__()
                                    if address20 is not FAILURE:
                                        elements3.append(address20)
                                        address21 = FAILURE
                                        chunk7, max7 = None, self._offset + 1
                                        if max7 <= self._input_size:
                                            chunk7 = self._input[self._offset:max7]
                                        if chunk7 == '>':
                                            address21 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                            self._offset = self._offset + 1
                                        else:
                                            address21 = FAILURE
                                            if self._offset > self._failure:
                                                self._failure = self._offset
                                                self._expected = []
                                            if self._offset == self._failure:
                                                self._expected.append('\'>\'')
                                        if address21 is not FAILURE:
                                            address22 = FAILURE
                                            address22 = self._read__()
                                            if address22 is not FAILURE:
                                                elements3.append(address22)
                                            else:
                                                elements3 = None
                                                self._offset = index6
                                        else:
                                            elements3 = None
                                            self._offset = index6
                                    else:
                                        elements3 = None
                                        self._offset = index6
                                else:
                                    elements3 = None
                                    self._offset = index6
                            else:
                                elements3 = None
                                self._offset = index6
                        else:
                            elements3 = None
                            self._offset = index6
                    else:
                        elements3 = None
                        self._offset = index6
                    if elements3 is None:
                        address0 = FAILURE
                    else:
                        address0 = self._actions.raw_accessor(self._input, index6, self._offset, elements3)
                        self._offset = self._offset
                    if address0 is FAILURE:
                        self._offset = index1
                        address0 = self._read_overload_op()
                        if address0 is FAILURE:
                            self._offset = index1
                            index8, elements4 = self._offset, []
                            address23 = FAILURE
                            address23 = self._read_reduce()
                            if address23 is not FAILURE:
                                elements4.append(address23)
                                address24 = FAILURE
                                address24 = self._read__()
                                if address24 is not FAILURE:
                                    elements4.append(address24)
                                else:
                                    elements4 = None
                                    self._offset = index8
                            else:
                                elements4 = None
                                self._offset = index8
                            if elements4 is None:
                                address0 = FAILURE
                            else:
                                address0 = TreeNode26(self._input[index8:self._offset], index8, elements4)
                                self._offset = self._offset
                            if address0 is FAILURE:
                                self._offset = index1
        self._cache['accessor'][index0] = (address0, self._offset)
        return address0

    def _read_accessing(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['accessing'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        address0 = self._read_reduce_expr()
        if address0 is FAILURE:
            self._offset = index1
            index2, elements0 = self._offset, []
            address1 = FAILURE
            chunk0, max0 = None, self._offset + 1
            if max0 <= self._input_size:
                chunk0 = self._input[self._offset:max0]
            if chunk0 == '<':
                address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                self._offset = self._offset + 1
            else:
                address1 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('\'<\'')
            if address1 is not FAILURE:
                address2 = FAILURE
                index3 = self._offset
                chunk1, max1 = None, self._offset + 1
                if max1 <= self._input_size:
                    chunk1 = self._input[self._offset:max1]
                if chunk1 == '[':
                    address2 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                    self._offset = self._offset + 1
                else:
                    address2 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('\'[\'')
                self._offset = index3
                if address2 is FAILURE:
                    address2 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                    self._offset = self._offset
                else:
                    address2 = FAILURE
                if address2 is not FAILURE:
                    elements0.append(address2)
                    address3 = FAILURE
                    address3 = self._read__()
                    if address3 is not FAILURE:
                        elements0.append(address3)
                        address4 = FAILURE
                        address4 = self._read_special_entry()
                        if address4 is not FAILURE:
                            elements0.append(address4)
                            address5 = FAILURE
                            address5 = self._read__()
                            if address5 is not FAILURE:
                                elements0.append(address5)
                                address6 = FAILURE
                                chunk2, max2 = None, self._offset + 1
                                if max2 <= self._input_size:
                                    chunk2 = self._input[self._offset:max2]
                                if chunk2 == '>':
                                    address6 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                    self._offset = self._offset + 1
                                else:
                                    address6 = FAILURE
                                    if self._offset > self._failure:
                                        self._failure = self._offset
                                        self._expected = []
                                    if self._offset == self._failure:
                                        self._expected.append('\'>\'')
                                if address6 is not FAILURE:
                                    address7 = FAILURE
                                    address7 = self._read__()
                                    if address7 is not FAILURE:
                                        elements0.append(address7)
                                    else:
                                        elements0 = None
                                        self._offset = index2
                                else:
                                    elements0 = None
                                    self._offset = index2
                            else:
                                elements0 = None
                                self._offset = index2
                        else:
                            elements0 = None
                            self._offset = index2
                    else:
                        elements0 = None
                        self._offset = index2
                else:
                    elements0 = None
                    self._offset = index2
            else:
                elements0 = None
                self._offset = index2
            if elements0 is None:
                address0 = FAILURE
            else:
                address0 = TreeNode27(self._input[index2:self._offset], index2, elements0)
                self._offset = self._offset
            if address0 is FAILURE:
                self._offset = index1
                address0 = self._read_overload_op()
                if address0 is FAILURE:
                    self._offset = index1
                    address0 = self._read_name()
                    if address0 is FAILURE:
                        self._offset = index1
        self._cache['accessing'][index0] = (address0, self._offset)
        return address0

    def _read_access(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['access'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        index2, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_accessing()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            remaining0, index3, elements1, address3 = 1, self._offset, [], True
            while address3 is not FAILURE:
                index4, elements2 = self._offset, []
                address4 = FAILURE
                address4 = self._read__ws()
                if address4 is not FAILURE:
                    elements2.append(address4)
                    address5 = FAILURE
                    chunk0, max0 = None, self._offset + 1
                    if max0 <= self._input_size:
                        chunk0 = self._input[self._offset:max0]
                    if chunk0 == '.':
                        address5 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                        self._offset = self._offset + 1
                    else:
                        address5 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('\'.\'')
                    if address5 is not FAILURE:
                        address6 = FAILURE
                        address6 = self._read_accessor()
                        if address6 is not FAILURE:
                            elements2.append(address6)
                        else:
                            elements2 = None
                            self._offset = index4
                    else:
                        elements2 = None
                        self._offset = index4
                else:
                    elements2 = None
                    self._offset = index4
                if elements2 is None:
                    address3 = FAILURE
                else:
                    address3 = TreeNode29(self._input[index4:self._offset], index4, elements2)
                    self._offset = self._offset
                if address3 is not FAILURE:
                    elements1.append(address3)
                    remaining0 -= 1
            if remaining0 <= 0:
                address2 = TreeNode(self._input[index3:self._offset], index3, elements1)
                self._offset = self._offset
            else:
                address2 = FAILURE
            if address2 is not FAILURE:
                elements0.append(address2)
            else:
                elements0 = None
                self._offset = index2
        else:
            elements0 = None
            self._offset = index2
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.access(self._input, index2, self._offset, elements0)
            self._offset = self._offset
        if address0 is FAILURE:
            self._offset = index1
            index5, elements3 = self._offset, []
            address7 = FAILURE
            chunk1, max1 = None, self._offset + 1
            if max1 <= self._input_size:
                chunk1 = self._input[self._offset:max1]
            if chunk1 == '<':
                address7 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                self._offset = self._offset + 1
            else:
                address7 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('\'<\'')
            if address7 is not FAILURE:
                address8 = FAILURE
                index6 = self._offset
                chunk2, max2 = None, self._offset + 1
                if max2 <= self._input_size:
                    chunk2 = self._input[self._offset:max2]
                if chunk2 == '[':
                    address8 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                    self._offset = self._offset + 1
                else:
                    address8 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('\'[\'')
                self._offset = index6
                if address8 is FAILURE:
                    address8 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                    self._offset = self._offset
                else:
                    address8 = FAILURE
                if address8 is not FAILURE:
                    elements3.append(address8)
                    address9 = FAILURE
                    address9 = self._read__()
                    if address9 is not FAILURE:
                        elements3.append(address9)
                        address10 = FAILURE
                        address10 = self._read_special_entry()
                        if address10 is not FAILURE:
                            elements3.append(address10)
                            address11 = FAILURE
                            address11 = self._read__()
                            if address11 is not FAILURE:
                                elements3.append(address11)
                                address12 = FAILURE
                                chunk3, max3 = None, self._offset + 1
                                if max3 <= self._input_size:
                                    chunk3 = self._input[self._offset:max3]
                                if chunk3 == '>':
                                    address12 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                    self._offset = self._offset + 1
                                else:
                                    address12 = FAILURE
                                    if self._offset > self._failure:
                                        self._failure = self._offset
                                        self._expected = []
                                    if self._offset == self._failure:
                                        self._expected.append('\'>\'')
                                if address12 is not FAILURE:
                                    address13 = FAILURE
                                    address13 = self._read__()
                                    if address13 is not FAILURE:
                                        elements3.append(address13)
                                    else:
                                        elements3 = None
                                        self._offset = index5
                                else:
                                    elements3 = None
                                    self._offset = index5
                            else:
                                elements3 = None
                                self._offset = index5
                        else:
                            elements3 = None
                            self._offset = index5
                    else:
                        elements3 = None
                        self._offset = index5
                else:
                    elements3 = None
                    self._offset = index5
            else:
                elements3 = None
                self._offset = index5
            if elements3 is None:
                address0 = FAILURE
            else:
                address0 = TreeNode30(self._input[index5:self._offset], index5, elements3)
                self._offset = self._offset
            if address0 is FAILURE:
                self._offset = index1
                address0 = self._read_name()
                if address0 is FAILURE:
                    self._offset = index1
        self._cache['access'][index0] = (address0, self._offset)
        return address0

    def _read_mult_op(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['mult_op'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        chunk0, max0 = None, self._offset + 1
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == '*':
            address0 = self._actions.two_sided_operator(self._input, self._offset, self._offset + 1, [])
            self._offset = self._offset + 1
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'*\'')
        if address0 is FAILURE:
            self._offset = index1
            chunk1, max1 = None, self._offset + 2
            if max1 <= self._input_size:
                chunk1 = self._input[self._offset:max1]
            if chunk1 == '%/':
                address0 = self._actions.two_sided_operator(self._input, self._offset, self._offset + 2, [])
                self._offset = self._offset + 2
            else:
                address0 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('\'%/\'')
            if address0 is FAILURE:
                self._offset = index1
                chunk2, max2 = None, self._offset + 1
                if max2 <= self._input_size:
                    chunk2 = self._input[self._offset:max2]
                if chunk2 == '/':
                    address0 = self._actions.two_sided_operator(self._input, self._offset, self._offset + 1, [])
                    self._offset = self._offset + 1
                else:
                    address0 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('\'/\'')
                if address0 is FAILURE:
                    self._offset = index1
                    index2, elements0 = self._offset, []
                    address1 = FAILURE
                    chunk3, max3 = None, self._offset + 1
                    if max3 <= self._input_size:
                        chunk3 = self._input[self._offset:max3]
                    if chunk3 == '%':
                        address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                        self._offset = self._offset + 1
                    else:
                        address1 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('\'%\'')
                    if address1 is not FAILURE:
                        elements0.append(address1)
                        address2 = FAILURE
                        index3 = self._offset
                        chunk4, max4 = None, self._offset + 1
                        if max4 <= self._input_size:
                            chunk4 = self._input[self._offset:max4]
                        if chunk4 == '>':
                            address2 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                            self._offset = self._offset + 1
                        else:
                            address2 = FAILURE
                            if self._offset > self._failure:
                                self._failure = self._offset
                                self._expected = []
                            if self._offset == self._failure:
                                self._expected.append('\'>\'')
                        self._offset = index3
                        if address2 is FAILURE:
                            address2 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                            self._offset = self._offset
                        else:
                            address2 = FAILURE
                        if address2 is not FAILURE:
                            elements0.append(address2)
                        else:
                            elements0 = None
                            self._offset = index2
                    else:
                        elements0 = None
                        self._offset = index2
                    if elements0 is None:
                        address0 = FAILURE
                    else:
                        address0 = self._actions.two_sided_operator(self._input, index2, self._offset, elements0)
                        self._offset = self._offset
                    if address0 is FAILURE:
                        self._offset = index1
        self._cache['mult_op'][index0] = (address0, self._offset)
        return address0

    def _read_add_op(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['add_op'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        chunk0, max0 = None, self._offset + 1
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == '+':
            address0 = self._actions.two_sided_operator(self._input, self._offset, self._offset + 1, [])
            self._offset = self._offset + 1
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'+\'')
        if address0 is FAILURE:
            self._offset = index1
            chunk1, max1 = None, self._offset + 1
            if max1 <= self._input_size:
                chunk1 = self._input[self._offset:max1]
            if chunk1 == '-':
                address0 = self._actions.two_sided_operator(self._input, self._offset, self._offset + 1, [])
                self._offset = self._offset + 1
            else:
                address0 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('\'-\'')
            if address0 is FAILURE:
                self._offset = index1
        self._cache['add_op'][index0] = (address0, self._offset)
        return address0

    def _read_anor_op(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['anor_op'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        chunk0, max0 = None, self._offset + 2
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == 'or':
            address0 = self._actions.two_sided_operator(self._input, self._offset, self._offset + 2, [])
            self._offset = self._offset + 2
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'or\'')
        if address0 is FAILURE:
            self._offset = index1
            index2, elements0 = self._offset, []
            address1 = FAILURE
            chunk1, max1 = None, self._offset + 3
            if max1 <= self._input_size:
                chunk1 = self._input[self._offset:max1]
            if chunk1 == 'and':
                address1 = TreeNode(self._input[self._offset:self._offset + 3], self._offset, [])
                self._offset = self._offset + 3
            else:
                address1 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('\'and\'')
            if address1 is not FAILURE:
                elements0.append(address1)
                address2 = FAILURE
                index3 = self._offset
                index4, elements1 = self._offset, []
                address3 = FAILURE
                address3 = self._read__()
                if address3 is not FAILURE:
                    elements1.append(address3)
                    address4 = FAILURE
                    chunk2, max2 = None, self._offset + 6
                    if max2 <= self._input_size:
                        chunk2 = self._input[self._offset:max2]
                    if chunk2 == 'always':
                        address4 = TreeNode(self._input[self._offset:self._offset + 6], self._offset, [])
                        self._offset = self._offset + 6
                    else:
                        address4 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('\'always\'')
                    if address4 is not FAILURE:
                        elements1.append(address4)
                    else:
                        elements1 = None
                        self._offset = index4
                else:
                    elements1 = None
                    self._offset = index4
                if elements1 is None:
                    address2 = FAILURE
                else:
                    address2 = TreeNode31(self._input[index4:self._offset], index4, elements1)
                    self._offset = self._offset
                self._offset = index3
                if address2 is FAILURE:
                    address2 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                    self._offset = self._offset
                else:
                    address2 = FAILURE
                if address2 is not FAILURE:
                    elements0.append(address2)
                else:
                    elements0 = None
                    self._offset = index2
            else:
                elements0 = None
                self._offset = index2
            if elements0 is None:
                address0 = FAILURE
            else:
                address0 = self._actions.two_sided_operator(self._input, index2, self._offset, elements0)
                self._offset = self._offset
            if address0 is FAILURE:
                self._offset = index1
        self._cache['anor_op'][index0] = (address0, self._offset)
        return address0

    def _read_comp_op(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['comp_op'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        chunk0, max0 = None, self._offset + 2
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == '==':
            address0 = self._actions.two_sided_operator(self._input, self._offset, self._offset + 2, [])
            self._offset = self._offset + 2
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'==\'')
        if address0 is FAILURE:
            self._offset = index1
            chunk1, max1 = None, self._offset + 2
            if max1 <= self._input_size:
                chunk1 = self._input[self._offset:max1]
            if chunk1 == '!=':
                address0 = self._actions.two_sided_operator(self._input, self._offset, self._offset + 2, [])
                self._offset = self._offset + 2
            else:
                address0 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('\'!=\'')
            if address0 is FAILURE:
                self._offset = index1
                chunk2, max2 = None, self._offset + 2
                if max2 <= self._input_size:
                    chunk2 = self._input[self._offset:max2]
                if chunk2 == '<=':
                    address0 = self._actions.two_sided_operator(self._input, self._offset, self._offset + 2, [])
                    self._offset = self._offset + 2
                else:
                    address0 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('\'<=\'')
                if address0 is FAILURE:
                    self._offset = index1
                    chunk3, max3 = None, self._offset + 2
                    if max3 <= self._input_size:
                        chunk3 = self._input[self._offset:max3]
                    if chunk3 == '>=':
                        address0 = self._actions.two_sided_operator(self._input, self._offset, self._offset + 2, [])
                        self._offset = self._offset + 2
                    else:
                        address0 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('\'>=\'')
                    if address0 is FAILURE:
                        self._offset = index1
                        chunk4, max4 = None, self._offset + 1
                        if max4 <= self._input_size:
                            chunk4 = self._input[self._offset:max4]
                        if chunk4 == '<':
                            address0 = self._actions.two_sided_operator(self._input, self._offset, self._offset + 1, [])
                            self._offset = self._offset + 1
                        else:
                            address0 = FAILURE
                            if self._offset > self._failure:
                                self._failure = self._offset
                                self._expected = []
                            if self._offset == self._failure:
                                self._expected.append('\'<\'')
                        if address0 is FAILURE:
                            self._offset = index1
                            chunk5, max5 = None, self._offset + 1
                            if max5 <= self._input_size:
                                chunk5 = self._input[self._offset:max5]
                            if chunk5 == '>':
                                address0 = self._actions.two_sided_operator(self._input, self._offset, self._offset + 1, [])
                                self._offset = self._offset + 1
                            else:
                                address0 = FAILURE
                                if self._offset > self._failure:
                                    self._failure = self._offset
                                    self._expected = []
                                if self._offset == self._failure:
                                    self._expected.append('\'>\'')
                            if address0 is FAILURE:
                                self._offset = index1
                                index2, elements0 = self._offset, []
                                address1 = FAILURE
                                chunk6, max6 = None, self._offset + 3
                                if max6 <= self._input_size:
                                    chunk6 = self._input[self._offset:max6]
                                if chunk6 == 'has':
                                    address1 = TreeNode(self._input[self._offset:self._offset + 3], self._offset, [])
                                    self._offset = self._offset + 3
                                else:
                                    address1 = FAILURE
                                    if self._offset > self._failure:
                                        self._failure = self._offset
                                        self._expected = []
                                    if self._offset == self._failure:
                                        self._expected.append('\'has\'')
                                if address1 is not FAILURE:
                                    elements0.append(address1)
                                    address2 = FAILURE
                                    index3 = self._offset
                                    index4, elements1 = self._offset, []
                                    address3 = FAILURE
                                    address3 = self._read__()
                                    if address3 is not FAILURE:
                                        elements1.append(address3)
                                        address4 = FAILURE
                                        chunk7, max7 = None, self._offset + 2
                                        if max7 <= self._input_size:
                                            chunk7 = self._input[self._offset:max7]
                                        if chunk7 == 'do':
                                            address4 = TreeNode(self._input[self._offset:self._offset + 2], self._offset, [])
                                            self._offset = self._offset + 2
                                        else:
                                            address4 = FAILURE
                                            if self._offset > self._failure:
                                                self._failure = self._offset
                                                self._expected = []
                                            if self._offset == self._failure:
                                                self._expected.append('\'do\'')
                                        if address4 is not FAILURE:
                                            elements1.append(address4)
                                        else:
                                            elements1 = None
                                            self._offset = index4
                                    else:
                                        elements1 = None
                                        self._offset = index4
                                    if elements1 is None:
                                        address2 = FAILURE
                                    else:
                                        address2 = TreeNode32(self._input[index4:self._offset], index4, elements1)
                                        self._offset = self._offset
                                    self._offset = index3
                                    if address2 is FAILURE:
                                        address2 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                        self._offset = self._offset
                                    else:
                                        address2 = FAILURE
                                    if address2 is not FAILURE:
                                        elements0.append(address2)
                                    else:
                                        elements0 = None
                                        self._offset = index2
                                else:
                                    elements0 = None
                                    self._offset = index2
                                if elements0 is None:
                                    address0 = FAILURE
                                else:
                                    address0 = self._actions.one_sided_operator(self._input, index2, self._offset, elements0)
                                    self._offset = self._offset
                                if address0 is FAILURE:
                                    self._offset = index1
                                    chunk8, max8 = None, self._offset + 3
                                    if max8 <= self._input_size:
                                        chunk8 = self._input[self._offset:max8]
                                    if chunk8 == 'isa':
                                        address0 = self._actions.two_sided_operator(self._input, self._offset, self._offset + 3, [])
                                        self._offset = self._offset + 3
                                    else:
                                        address0 = FAILURE
                                        if self._offset > self._failure:
                                            self._failure = self._offset
                                            self._expected = []
                                        if self._offset == self._failure:
                                            self._expected.append('\'isa\'')
                                    if address0 is FAILURE:
                                        self._offset = index1
        self._cache['comp_op'][index0] = (address0, self._offset)
        return address0

    def _read_assign_op(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['assign_op'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        chunk0, max0 = None, self._offset + 2
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == '+=':
            address0 = self._actions.text(self._input, self._offset, self._offset + 2, [])
            self._offset = self._offset + 2
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'+=\'')
        if address0 is FAILURE:
            self._offset = index1
            chunk1, max1 = None, self._offset + 2
            if max1 <= self._input_size:
                chunk1 = self._input[self._offset:max1]
            if chunk1 == '-=':
                address0 = self._actions.text(self._input, self._offset, self._offset + 2, [])
                self._offset = self._offset + 2
            else:
                address0 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('\'-=\'')
            if address0 is FAILURE:
                self._offset = index1
                chunk2, max2 = None, self._offset + 2
                if max2 <= self._input_size:
                    chunk2 = self._input[self._offset:max2]
                if chunk2 == '*=':
                    address0 = self._actions.text(self._input, self._offset, self._offset + 2, [])
                    self._offset = self._offset + 2
                else:
                    address0 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('\'*=\'')
                if address0 is FAILURE:
                    self._offset = index1
                    chunk3, max3 = None, self._offset + 2
                    if max3 <= self._input_size:
                        chunk3 = self._input[self._offset:max3]
                    if chunk3 == '/=':
                        address0 = self._actions.text(self._input, self._offset, self._offset + 2, [])
                        self._offset = self._offset + 2
                    else:
                        address0 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('\'/=\'')
                    if address0 is FAILURE:
                        self._offset = index1
                        chunk4, max4 = None, self._offset + 2
                        if max4 <= self._input_size:
                            chunk4 = self._input[self._offset:max4]
                        if chunk4 == '%=':
                            address0 = self._actions.text(self._input, self._offset, self._offset + 2, [])
                            self._offset = self._offset + 2
                        else:
                            address0 = FAILURE
                            if self._offset > self._failure:
                                self._failure = self._offset
                                self._expected = []
                            if self._offset == self._failure:
                                self._expected.append('\'%=\'')
                        if address0 is FAILURE:
                            self._offset = index1
                            chunk5, max5 = None, self._offset + 3
                            if max5 <= self._input_size:
                                chunk5 = self._input[self._offset:max5]
                            if chunk5 == '%/=':
                                address0 = self._actions.text(self._input, self._offset, self._offset + 3, [])
                                self._offset = self._offset + 3
                            else:
                                address0 = FAILURE
                                if self._offset > self._failure:
                                    self._failure = self._offset
                                    self._expected = []
                                if self._offset == self._failure:
                                    self._expected.append('\'%/=\'')
                            if address0 is FAILURE:
                                self._offset = index1
                                chunk6, max6 = None, self._offset + 2
                                if max6 <= self._input_size:
                                    chunk6 = self._input[self._offset:max6]
                                if chunk6 == '&=':
                                    address0 = self._actions.text(self._input, self._offset, self._offset + 2, [])
                                    self._offset = self._offset + 2
                                else:
                                    address0 = FAILURE
                                    if self._offset > self._failure:
                                        self._failure = self._offset
                                        self._expected = []
                                    if self._offset == self._failure:
                                        self._expected.append('\'&=\'')
                                if address0 is FAILURE:
                                    self._offset = index1
                                    index2, elements0 = self._offset, []
                                    address1 = FAILURE
                                    chunk7, max7 = None, self._offset + 1
                                    if max7 <= self._input_size:
                                        chunk7 = self._input[self._offset:max7]
                                    if chunk7 == '=':
                                        address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                        self._offset = self._offset + 1
                                    else:
                                        address1 = FAILURE
                                        if self._offset > self._failure:
                                            self._failure = self._offset
                                            self._expected = []
                                        if self._offset == self._failure:
                                            self._expected.append('\'=\'')
                                    if address1 is not FAILURE:
                                        elements0.append(address1)
                                        address2 = FAILURE
                                        index3 = self._offset
                                        chunk8, max8 = None, self._offset + 1
                                        if max8 <= self._input_size:
                                            chunk8 = self._input[self._offset:max8]
                                        if chunk8 == '>':
                                            address2 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                            self._offset = self._offset + 1
                                        else:
                                            address2 = FAILURE
                                            if self._offset > self._failure:
                                                self._failure = self._offset
                                                self._expected = []
                                            if self._offset == self._failure:
                                                self._expected.append('\'>\'')
                                        self._offset = index3
                                        if address2 is FAILURE:
                                            address2 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                            self._offset = self._offset
                                        else:
                                            address2 = FAILURE
                                        if address2 is not FAILURE:
                                            elements0.append(address2)
                                        else:
                                            elements0 = None
                                            self._offset = index2
                                    else:
                                        elements0 = None
                                        self._offset = index2
                                    if elements0 is None:
                                        address0 = FAILURE
                                    else:
                                        address0 = self._actions.text(self._input, index2, self._offset, elements0)
                                        self._offset = self._offset
                                    if address0 is FAILURE:
                                        self._offset = index1
        self._cache['assign_op'][index0] = (address0, self._offset)
        return address0

    def _read_expression(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['expression'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        address0 = self._read_use_if()
        self._cache['expression'][index0] = (address0, self._offset)
        return address0

    def _read_use_if(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['use_if'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        index2, elements0 = self._offset, []
        address1 = FAILURE
        chunk0, max0 = None, self._offset + 3
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == 'use':
            address1 = TreeNode(self._input[self._offset:self._offset + 3], self._offset, [])
            self._offset = self._offset + 3
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'use\'')
        if address1 is not FAILURE:
            address2 = FAILURE
            address2 = self._read__()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                address3 = self._read_expression()
                if address3 is not FAILURE:
                    elements0.append(address3)
                    address4 = FAILURE
                    address4 = self._read__()
                    if address4 is not FAILURE:
                        elements0.append(address4)
                        address5 = FAILURE
                        chunk1, max1 = None, self._offset + 2
                        if max1 <= self._input_size:
                            chunk1 = self._input[self._offset:max1]
                        if chunk1 == 'if':
                            address5 = TreeNode(self._input[self._offset:self._offset + 2], self._offset, [])
                            self._offset = self._offset + 2
                        else:
                            address5 = FAILURE
                            if self._offset > self._failure:
                                self._failure = self._offset
                                self._expected = []
                            if self._offset == self._failure:
                                self._expected.append('\'if\'')
                        if address5 is not FAILURE:
                            address6 = FAILURE
                            address6 = self._read__()
                            if address6 is not FAILURE:
                                elements0.append(address6)
                                address7 = FAILURE
                                address7 = self._read_anor()
                                if address7 is not FAILURE:
                                    elements0.append(address7)
                                    address8 = FAILURE
                                    address8 = self._read__()
                                    if address8 is not FAILURE:
                                        elements0.append(address8)
                                        address9 = FAILURE
                                        chunk2, max2 = None, self._offset + 9
                                        if max2 <= self._input_size:
                                            chunk2 = self._input[self._offset:max2]
                                        if chunk2 == 'otherwise':
                                            address9 = TreeNode(self._input[self._offset:self._offset + 9], self._offset, [])
                                            self._offset = self._offset + 9
                                        else:
                                            address9 = FAILURE
                                            if self._offset > self._failure:
                                                self._failure = self._offset
                                                self._expected = []
                                            if self._offset == self._failure:
                                                self._expected.append('\'otherwise\'')
                                        if address9 is not FAILURE:
                                            address10 = FAILURE
                                            address10 = self._read__()
                                            if address10 is not FAILURE:
                                                elements0.append(address10)
                                                address11 = FAILURE
                                                address11 = self._read_expression()
                                                if address11 is not FAILURE:
                                                    elements0.append(address11)
                                                else:
                                                    elements0 = None
                                                    self._offset = index2
                                            else:
                                                elements0 = None
                                                self._offset = index2
                                        else:
                                            elements0 = None
                                            self._offset = index2
                                    else:
                                        elements0 = None
                                        self._offset = index2
                                else:
                                    elements0 = None
                                    self._offset = index2
                            else:
                                elements0 = None
                                self._offset = index2
                        else:
                            elements0 = None
                            self._offset = index2
                    else:
                        elements0 = None
                        self._offset = index2
                else:
                    elements0 = None
                    self._offset = index2
            else:
                elements0 = None
                self._offset = index2
        else:
            elements0 = None
            self._offset = index2
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.use_if(self._input, index2, self._offset, elements0)
            self._offset = self._offset
        if address0 is FAILURE:
            self._offset = index1
            index3, elements1 = self._offset, []
            address12 = FAILURE
            chunk3, max3 = None, self._offset + 3
            if max3 <= self._input_size:
                chunk3 = self._input[self._offset:max3]
            if chunk3 == 'not':
                address12 = TreeNode(self._input[self._offset:self._offset + 3], self._offset, [])
                self._offset = self._offset + 3
            else:
                address12 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('\'not\'')
            if address12 is not FAILURE:
                address13 = FAILURE
                address13 = self._read__()
                if address13 is not FAILURE:
                    elements1.append(address13)
                    address14 = FAILURE
                    address14 = self._read_anor()
                    if address14 is not FAILURE:
                        elements1.append(address14)
                    else:
                        elements1 = None
                        self._offset = index3
                else:
                    elements1 = None
                    self._offset = index3
            else:
                elements1 = None
                self._offset = index3
            if elements1 is None:
                address0 = FAILURE
            else:
                address0 = self._actions.negate(self._input, index3, self._offset, elements1)
                self._offset = self._offset
            if address0 is FAILURE:
                self._offset = index1
                address0 = self._read_anor()
                if address0 is FAILURE:
                    self._offset = index1
        self._cache['use_if'][index0] = (address0, self._offset)
        return address0

    def _read_anor(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['anor'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        index2, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_comparison()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read__()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                address3 = self._read_anor_op()
                if address3 is not FAILURE:
                    elements0.append(address3)
                    address4 = FAILURE
                    address4 = self._read__()
                    if address4 is not FAILURE:
                        elements0.append(address4)
                        address5 = FAILURE
                        address5 = self._read_anor()
                        if address5 is not FAILURE:
                            elements0.append(address5)
                        else:
                            elements0 = None
                            self._offset = index2
                    else:
                        elements0 = None
                        self._offset = index2
                else:
                    elements0 = None
                    self._offset = index2
            else:
                elements0 = None
                self._offset = index2
        else:
            elements0 = None
            self._offset = index2
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.binary_op(self._input, index2, self._offset, elements0)
            self._offset = self._offset
        if address0 is FAILURE:
            self._offset = index1
            address0 = self._read_comparison()
            if address0 is FAILURE:
                self._offset = index1
        self._cache['anor'][index0] = (address0, self._offset)
        return address0

    def _read_comparison(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['comparison'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        index2, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_roll_math()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read__()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                address3 = self._read_comp_op()
                if address3 is not FAILURE:
                    elements0.append(address3)
                    address4 = FAILURE
                    address4 = self._read__()
                    if address4 is not FAILURE:
                        elements0.append(address4)
                        address5 = FAILURE
                        address5 = self._read_comparison()
                        if address5 is not FAILURE:
                            elements0.append(address5)
                        else:
                            elements0 = None
                            self._offset = index2
                    else:
                        elements0 = None
                        self._offset = index2
                else:
                    elements0 = None
                    self._offset = index2
            else:
                elements0 = None
                self._offset = index2
        else:
            elements0 = None
            self._offset = index2
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.binary_op(self._input, index2, self._offset, elements0)
            self._offset = self._offset
        if address0 is FAILURE:
            self._offset = index1
            address0 = self._read_roll_math()
            if address0 is FAILURE:
                self._offset = index1
        self._cache['comparison'][index0] = (address0, self._offset)
        return address0

    def _read_roll_math(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['roll_math'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        index2, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_add_math()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read__()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                chunk0, max0 = None, self._offset + 1
                if max0 <= self._input_size:
                    chunk0 = self._input[self._offset:max0]
                if chunk0 == '&':
                    address3 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                    self._offset = self._offset + 1
                else:
                    address3 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('\'&\'')
                if address3 is not FAILURE:
                    elements0.append(address3)
                    address4 = FAILURE
                    index3 = self._offset
                    chunk1, max1 = None, self._offset + 1
                    if max1 <= self._input_size:
                        chunk1 = self._input[self._offset:max1]
                    if chunk1 == '=':
                        address4 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                        self._offset = self._offset + 1
                    else:
                        address4 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('\'=\'')
                    self._offset = index3
                    if address4 is FAILURE:
                        address4 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                        self._offset = self._offset
                    else:
                        address4 = FAILURE
                    if address4 is not FAILURE:
                        elements0.append(address4)
                        address5 = FAILURE
                        address5 = self._read__()
                        if address5 is not FAILURE:
                            elements0.append(address5)
                            address6 = FAILURE
                            address6 = self._read_roll_math()
                            if address6 is not FAILURE:
                                elements0.append(address6)
                            else:
                                elements0 = None
                                self._offset = index2
                        else:
                            elements0 = None
                            self._offset = index2
                    else:
                        elements0 = None
                        self._offset = index2
                else:
                    elements0 = None
                    self._offset = index2
            else:
                elements0 = None
                self._offset = index2
        else:
            elements0 = None
            self._offset = index2
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.binary_op(self._input, index2, self._offset, elements0)
            self._offset = self._offset
        if address0 is FAILURE:
            self._offset = index1
            address0 = self._read_add_math()
            if address0 is FAILURE:
                self._offset = index1
        self._cache['roll_math'][index0] = (address0, self._offset)
        return address0

    def _read_add_math(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['add_math'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        index2, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_mult_math()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read__()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                address3 = self._read_add_op()
                if address3 is not FAILURE:
                    elements0.append(address3)
                    address4 = FAILURE
                    index3 = self._offset
                    chunk0, max0 = None, self._offset + 1
                    if max0 <= self._input_size:
                        chunk0 = self._input[self._offset:max0]
                    if chunk0 == '=':
                        address4 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                        self._offset = self._offset + 1
                    else:
                        address4 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('\'=\'')
                    self._offset = index3
                    if address4 is FAILURE:
                        address4 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                        self._offset = self._offset
                    else:
                        address4 = FAILURE
                    if address4 is not FAILURE:
                        elements0.append(address4)
                        address5 = FAILURE
                        address5 = self._read__()
                        if address5 is not FAILURE:
                            elements0.append(address5)
                            address6 = FAILURE
                            address6 = self._read_add_math()
                            if address6 is not FAILURE:
                                elements0.append(address6)
                            else:
                                elements0 = None
                                self._offset = index2
                        else:
                            elements0 = None
                            self._offset = index2
                    else:
                        elements0 = None
                        self._offset = index2
                else:
                    elements0 = None
                    self._offset = index2
            else:
                elements0 = None
                self._offset = index2
        else:
            elements0 = None
            self._offset = index2
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.binary_op(self._input, index2, self._offset, elements0)
            self._offset = self._offset
        if address0 is FAILURE:
            self._offset = index1
            address0 = self._read_mult_math()
            if address0 is FAILURE:
                self._offset = index1
        self._cache['add_math'][index0] = (address0, self._offset)
        return address0

    def _read_mult_math(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['mult_math'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        index2, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_lambda_expr()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read__()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                address3 = self._read_mult_op()
                if address3 is not FAILURE:
                    elements0.append(address3)
                    address4 = FAILURE
                    index3 = self._offset
                    chunk0, max0 = None, self._offset + 1
                    if max0 <= self._input_size:
                        chunk0 = self._input[self._offset:max0]
                    if chunk0 == '=':
                        address4 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                        self._offset = self._offset + 1
                    else:
                        address4 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('\'=\'')
                    self._offset = index3
                    if address4 is FAILURE:
                        address4 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                        self._offset = self._offset
                    else:
                        address4 = FAILURE
                    if address4 is not FAILURE:
                        elements0.append(address4)
                        address5 = FAILURE
                        address5 = self._read__()
                        if address5 is not FAILURE:
                            elements0.append(address5)
                            address6 = FAILURE
                            address6 = self._read_mult_math()
                            if address6 is not FAILURE:
                                elements0.append(address6)
                            else:
                                elements0 = None
                                self._offset = index2
                        else:
                            elements0 = None
                            self._offset = index2
                    else:
                        elements0 = None
                        self._offset = index2
                else:
                    elements0 = None
                    self._offset = index2
            else:
                elements0 = None
                self._offset = index2
        else:
            elements0 = None
            self._offset = index2
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.binary_op(self._input, index2, self._offset, elements0)
            self._offset = self._offset
        if address0 is FAILURE:
            self._offset = index1
            address0 = self._read_lambda_expr()
            if address0 is FAILURE:
                self._offset = index1
        self._cache['mult_math'][index0] = (address0, self._offset)
        return address0

    def _read_lambda_expr(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['lambda_expr'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        address0 = self._read_lambda_def()
        if address0 is FAILURE:
            self._offset = index1
            address0 = self._read_modify()
            if address0 is FAILURE:
                self._offset = index1
        self._cache['lambda_expr'][index0] = (address0, self._offset)
        return address0

    def _read_modify(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['modify'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        index2, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_first_modifier_call()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            remaining0, index3, elements1, address3 = 0, self._offset, [], True
            while address3 is not FAILURE:
                address3 = self._read_modifier_call()
                if address3 is not FAILURE:
                    elements1.append(address3)
                    remaining0 -= 1
            if remaining0 <= 0:
                address2 = TreeNode(self._input[index3:self._offset], index3, elements1)
                self._offset = self._offset
            else:
                address2 = FAILURE
            if address2 is not FAILURE:
                elements0.append(address2)
            else:
                elements0 = None
                self._offset = index2
        else:
            elements0 = None
            self._offset = index2
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.modify(self._input, index2, self._offset, elements0)
            self._offset = self._offset
        if address0 is FAILURE:
            self._offset = index1
            address0 = self._read_dice()
            if address0 is FAILURE:
                self._offset = index1
        self._cache['modify'][index0] = (address0, self._offset)
        return address0

    def _read_dice(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['dice'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        index2, elements0 = self._offset, []
        address1 = FAILURE
        index3 = self._offset
        index4 = self._offset
        address1 = self._read_name()
        if address1 is FAILURE:
            self._offset = index4
            address1 = self._read_string()
            if address1 is FAILURE:
                self._offset = index4
        self._offset = index3
        if address1 is FAILURE:
            address1 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
            self._offset = self._offset
        else:
            address1 = FAILURE
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read_reduce_expr()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                address3 = self._read__()
                if address3 is not FAILURE:
                    elements0.append(address3)
                    address4 = FAILURE
                    chunk0, max0 = None, self._offset + 1
                    if max0 <= self._input_size:
                        chunk0 = self._input[self._offset:max0]
                    if chunk0 is not None and chunk0.lower() == 'd'.lower():
                        address4 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                        self._offset = self._offset + 1
                    else:
                        address4 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('`d`')
                    if address4 is not FAILURE:
                        address5 = FAILURE
                        address5 = self._read__()
                        if address5 is not FAILURE:
                            elements0.append(address5)
                            address6 = FAILURE
                            index5 = self._offset
                            index6 = self._offset
                            address6 = self._read_name()
                            if address6 is FAILURE:
                                self._offset = index6
                                address6 = self._read_string()
                                if address6 is FAILURE:
                                    self._offset = index6
                            self._offset = index5
                            if address6 is FAILURE:
                                address6 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                self._offset = self._offset
                            else:
                                address6 = FAILURE
                            if address6 is not FAILURE:
                                elements0.append(address6)
                                address7 = FAILURE
                                address7 = self._read_reduce_expr()
                                if address7 is not FAILURE:
                                    elements0.append(address7)
                                else:
                                    elements0 = None
                                    self._offset = index2
                            else:
                                elements0 = None
                                self._offset = index2
                        else:
                            elements0 = None
                            self._offset = index2
                    else:
                        elements0 = None
                        self._offset = index2
                else:
                    elements0 = None
                    self._offset = index2
            else:
                elements0 = None
                self._offset = index2
        else:
            elements0 = None
            self._offset = index2
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.dice(self._input, index2, self._offset, elements0)
            self._offset = self._offset
        if address0 is FAILURE:
            self._offset = index1
            address0 = self._read_access()
            if address0 is FAILURE:
                self._offset = index1
                address0 = self._read_reduce_expr()
                if address0 is FAILURE:
                    self._offset = index1
        self._cache['dice'][index0] = (address0, self._offset)
        return address0

    def _read_reduce_expr(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['reduce_expr'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        address0 = self._read_roll_def()
        if address0 is FAILURE:
            self._offset = index1
            address0 = self._read_new_bag()
            if address0 is FAILURE:
                self._offset = index1
                address0 = self._read_reduce()
                if address0 is FAILURE:
                    self._offset = index1
                    index2, elements0 = self._offset, []
                    address1 = FAILURE
                    chunk0, max0 = None, self._offset + 1
                    if max0 <= self._input_size:
                        chunk0 = self._input[self._offset:max0]
                    if chunk0 == '(':
                        address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                        self._offset = self._offset + 1
                    else:
                        address1 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('\'(\'')
                    if address1 is not FAILURE:
                        address2 = FAILURE
                        address2 = self._read__ws()
                        if address2 is not FAILURE:
                            elements0.append(address2)
                            address3 = FAILURE
                            address3 = self._read_expression()
                            if address3 is not FAILURE:
                                elements0.append(address3)
                                address4 = FAILURE
                                address4 = self._read__ws()
                                if address4 is not FAILURE:
                                    elements0.append(address4)
                                    address5 = FAILURE
                                    chunk1, max1 = None, self._offset + 1
                                    if max1 <= self._input_size:
                                        chunk1 = self._input[self._offset:max1]
                                    if chunk1 == ')':
                                        address5 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                        self._offset = self._offset + 1
                                    else:
                                        address5 = FAILURE
                                        if self._offset > self._failure:
                                            self._failure = self._offset
                                            self._expected = []
                                        if self._offset == self._failure:
                                            self._expected.append('\')\'')
                                    if address5 is not FAILURE:
                                        address6 = FAILURE
                                        address6 = self._read__()
                                        if address6 is not FAILURE:
                                            elements0.append(address6)
                                        else:
                                            elements0 = None
                                            self._offset = index2
                                    else:
                                        elements0 = None
                                        self._offset = index2
                                else:
                                    elements0 = None
                                    self._offset = index2
                            else:
                                elements0 = None
                                self._offset = index2
                        else:
                            elements0 = None
                            self._offset = index2
                    else:
                        elements0 = None
                        self._offset = index2
                    if elements0 is None:
                        address0 = FAILURE
                    else:
                        address0 = TreeNode42(self._input[index2:self._offset], index2, elements0)
                        self._offset = self._offset
                    if address0 is FAILURE:
                        self._offset = index1
                        address0 = self._read_atom()
                        if address0 is FAILURE:
                            self._offset = index1
        self._cache['reduce_expr'][index0] = (address0, self._offset)
        return address0

    def _read_atom(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['atom'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        address0 = self._read_number()
        if address0 is FAILURE:
            self._offset = index1
            address0 = self._read_name()
            if address0 is FAILURE:
                self._offset = index1
                address0 = self._read_string()
                if address0 is FAILURE:
                    self._offset = index1
        self._cache['atom'][index0] = (address0, self._offset)
        return address0

    def _read_modifier_tail(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['modifier_tail'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_access()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read__()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                index2 = self._offset
                address3 = self._read_modifier_args()
                if address3 is FAILURE:
                    address3 = TreeNode(self._input[index2:index2], index2, [])
                    self._offset = index2
                if address3 is not FAILURE:
                    elements0.append(address3)
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.modifier_call(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['modifier_tail'][index0] = (address0, self._offset)
        return address0

    def _read_first_modifier_call(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['first_modifier_call'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_dice()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read__()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                index2 = self._offset
                chunk0, max0 = None, self._offset + 1
                if max0 <= self._input_size:
                    chunk0 = self._input[self._offset:max0]
                if chunk0 == '-':
                    address3 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                    self._offset = self._offset + 1
                else:
                    address3 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('\'-\'')
                if address3 is FAILURE:
                    self._offset = index2
                    chunk1, max1 = None, self._offset + 1
                    if max1 <= self._input_size:
                        chunk1 = self._input[self._offset:max1]
                    if chunk1 == ':':
                        address3 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                        self._offset = self._offset + 1
                    else:
                        address3 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('\':\'')
                    if address3 is FAILURE:
                        self._offset = index2
                if address3 is not FAILURE:
                    elements0.append(address3)
                    address4 = FAILURE
                    chunk2, max2 = None, self._offset + 1
                    if max2 <= self._input_size:
                        chunk2 = self._input[self._offset:max2]
                    if chunk2 == '>':
                        address4 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                        self._offset = self._offset + 1
                    else:
                        address4 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('\'>\'')
                    if address4 is not FAILURE:
                        address5 = FAILURE
                        address5 = self._read__()
                        if address5 is not FAILURE:
                            elements0.append(address5)
                            address6 = FAILURE
                            address6 = self._read_modifier_tail()
                            if address6 is not FAILURE:
                                elements0.append(address6)
                            else:
                                elements0 = None
                                self._offset = index1
                        else:
                            elements0 = None
                            self._offset = index1
                    else:
                        elements0 = None
                        self._offset = index1
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.first_modifier_call(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['first_modifier_call'][index0] = (address0, self._offset)
        return address0

    def _read_modifier_call(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['modifier_call'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read__ws()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            chunk0, max0 = None, self._offset + 2
            if max0 <= self._input_size:
                chunk0 = self._input[self._offset:max0]
            if chunk0 == '->':
                address2 = TreeNode(self._input[self._offset:self._offset + 2], self._offset, [])
                self._offset = self._offset + 2
            else:
                address2 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('\'->\'')
            if address2 is not FAILURE:
                address3 = FAILURE
                address3 = self._read__()
                if address3 is not FAILURE:
                    elements0.append(address3)
                    address4 = FAILURE
                    address4 = self._read_modifier_tail()
                    if address4 is not FAILURE:
                        elements0.append(address4)
                    else:
                        elements0 = None
                        self._offset = index1
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode45(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        self._cache['modifier_call'][index0] = (address0, self._offset)
        return address0

    def _read_modifier_args(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['modifier_args'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        chunk0, max0 = None, self._offset + 1
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == '(':
            address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
            self._offset = self._offset + 1
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'(\'')
        if address1 is not FAILURE:
            address2 = FAILURE
            address2 = self._read__ws()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                remaining0, index2, elements1, address4 = 0, self._offset, [], True
                while address4 is not FAILURE:
                    index3, elements2 = self._offset, []
                    address5 = FAILURE
                    address5 = self._read_expression()
                    if address5 is not FAILURE:
                        elements2.append(address5)
                        address6 = FAILURE
                        address6 = self._read__()
                        if address6 is not FAILURE:
                            elements2.append(address6)
                            address7 = FAILURE
                            chunk1, max1 = None, self._offset + 1
                            if max1 <= self._input_size:
                                chunk1 = self._input[self._offset:max1]
                            if chunk1 == ',':
                                address7 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                self._offset = self._offset + 1
                            else:
                                address7 = FAILURE
                                if self._offset > self._failure:
                                    self._failure = self._offset
                                    self._expected = []
                                if self._offset == self._failure:
                                    self._expected.append('\',\'')
                            if address7 is not FAILURE:
                                address8 = FAILURE
                                address8 = self._read__ws()
                                if address8 is not FAILURE:
                                    elements2.append(address8)
                                else:
                                    elements2 = None
                                    self._offset = index3
                            else:
                                elements2 = None
                                self._offset = index3
                        else:
                            elements2 = None
                            self._offset = index3
                    else:
                        elements2 = None
                        self._offset = index3
                    if elements2 is None:
                        address4 = FAILURE
                    else:
                        address4 = TreeNode47(self._input[index3:self._offset], index3, elements2)
                        self._offset = self._offset
                    if address4 is not FAILURE:
                        elements1.append(address4)
                        remaining0 -= 1
                if remaining0 <= 0:
                    address3 = TreeNode(self._input[index2:self._offset], index2, elements1)
                    self._offset = self._offset
                else:
                    address3 = FAILURE
                if address3 is not FAILURE:
                    elements0.append(address3)
                    address9 = FAILURE
                    index4 = self._offset
                    address9 = self._read_expression()
                    if address9 is FAILURE:
                        address9 = TreeNode(self._input[index4:index4], index4, [])
                        self._offset = index4
                    if address9 is not FAILURE:
                        elements0.append(address9)
                        address10 = FAILURE
                        address10 = self._read__()
                        if address10 is not FAILURE:
                            elements0.append(address10)
                            address11 = FAILURE
                            chunk2, max2 = None, self._offset + 1
                            if max2 <= self._input_size:
                                chunk2 = self._input[self._offset:max2]
                            if chunk2 == ')':
                                address11 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                self._offset = self._offset + 1
                            else:
                                address11 = FAILURE
                                if self._offset > self._failure:
                                    self._failure = self._offset
                                    self._expected = []
                                if self._offset == self._failure:
                                    self._expected.append('\')\'')
                            if address11 is not FAILURE:
                                address12 = FAILURE
                                address12 = self._read__()
                                if address12 is not FAILURE:
                                    elements0.append(address12)
                                else:
                                    elements0 = None
                                    self._offset = index1
                            else:
                                elements0 = None
                                self._offset = index1
                        else:
                            elements0 = None
                            self._offset = index1
                    else:
                        elements0 = None
                        self._offset = index1
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.arg_list(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['modifier_args'][index0] = (address0, self._offset)
        return address0

    def _read_modifier_params(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['modifier_params'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        remaining0, index2, elements1, address2 = 0, self._offset, [], True
        while address2 is not FAILURE:
            index3, elements2 = self._offset, []
            address3 = FAILURE
            address3 = self._read_basic_name()
            if address3 is not FAILURE:
                elements2.append(address3)
                address4 = FAILURE
                address4 = self._read__()
                if address4 is not FAILURE:
                    elements2.append(address4)
                    address5 = FAILURE
                    chunk0, max0 = None, self._offset + 1
                    if max0 <= self._input_size:
                        chunk0 = self._input[self._offset:max0]
                    if chunk0 == ',':
                        address5 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                        self._offset = self._offset + 1
                    else:
                        address5 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('\',\'')
                    if address5 is not FAILURE:
                        address6 = FAILURE
                        address6 = self._read__ws()
                        if address6 is not FAILURE:
                            elements2.append(address6)
                        else:
                            elements2 = None
                            self._offset = index3
                    else:
                        elements2 = None
                        self._offset = index3
                else:
                    elements2 = None
                    self._offset = index3
            else:
                elements2 = None
                self._offset = index3
            if elements2 is None:
                address2 = FAILURE
            else:
                address2 = TreeNode48(self._input[index3:self._offset], index3, elements2)
                self._offset = self._offset
            if address2 is not FAILURE:
                elements1.append(address2)
                remaining0 -= 1
        if remaining0 <= 0:
            address1 = TreeNode(self._input[index2:self._offset], index2, elements1)
            self._offset = self._offset
        else:
            address1 = FAILURE
        if address1 is not FAILURE:
            elements0.append(address1)
            address7 = FAILURE
            index4 = self._offset
            address7 = self._read_basic_name()
            if address7 is FAILURE:
                address7 = TreeNode(self._input[index4:index4], index4, [])
                self._offset = index4
            if address7 is not FAILURE:
                elements0.append(address7)
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.param_list(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['modifier_params'][index0] = (address0, self._offset)
        return address0

    def _read_small_modifier_body(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['small_modifier_body'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_modifier_params()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read__()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                chunk0, max0 = None, self._offset + 1
                if max0 <= self._input_size:
                    chunk0 = self._input[self._offset:max0]
                if chunk0 == ':':
                    address3 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                    self._offset = self._offset + 1
                else:
                    address3 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('\':\'')
                if address3 is not FAILURE:
                    address4 = FAILURE
                    address4 = self._read__()
                    if address4 is not FAILURE:
                        elements0.append(address4)
                        address5 = FAILURE
                        index2 = self._offset
                        chunk1, max1 = None, self._offset + 1
                        if max1 <= self._input_size:
                            chunk1 = self._input[self._offset:max1]
                        if chunk1 == '[':
                            address5 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                            self._offset = self._offset + 1
                        else:
                            address5 = FAILURE
                            if self._offset > self._failure:
                                self._failure = self._offset
                                self._expected = []
                            if self._offset == self._failure:
                                self._expected.append('\'[\'')
                        self._offset = index2
                        if address5 is FAILURE:
                            address5 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                            self._offset = self._offset
                        else:
                            address5 = FAILURE
                        if address5 is not FAILURE:
                            elements0.append(address5)
                            address6 = FAILURE
                            address6 = self._read__()
                            if address6 is not FAILURE:
                                elements0.append(address6)
                                address7 = FAILURE
                                address7 = self._read_expression()
                                if address7 is not FAILURE:
                                    elements0.append(address7)
                                else:
                                    elements0 = None
                                    self._offset = index1
                            else:
                                elements0 = None
                                self._offset = index1
                        else:
                            elements0 = None
                            self._offset = index1
                    else:
                        elements0 = None
                        self._offset = index1
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.small_modifier_body(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['small_modifier_body'][index0] = (address0, self._offset)
        return address0

    def _read_normal_modifier_body(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['normal_modifier_body'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_modifier_params()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read__()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                index2 = self._offset
                chunk0, max0 = None, self._offset + 1
                if max0 <= self._input_size:
                    chunk0 = self._input[self._offset:max0]
                if chunk0 == ':':
                    address3 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                    self._offset = self._offset + 1
                else:
                    address3 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('\':\'')
                if address3 is FAILURE:
                    address3 = TreeNode(self._input[index2:index2], index2, [])
                    self._offset = index2
                if address3 is not FAILURE:
                    address4 = FAILURE
                    address4 = self._read__ws()
                    if address4 is not FAILURE:
                        elements0.append(address4)
                        address5 = FAILURE
                        chunk1, max1 = None, self._offset + 1
                        if max1 <= self._input_size:
                            chunk1 = self._input[self._offset:max1]
                        if chunk1 == '[':
                            address5 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                            self._offset = self._offset + 1
                        else:
                            address5 = FAILURE
                            if self._offset > self._failure:
                                self._failure = self._offset
                                self._expected = []
                            if self._offset == self._failure:
                                self._expected.append('\'[\'')
                        if address5 is not FAILURE:
                            address6 = FAILURE
                            address6 = self._read__()
                            if address6 is not FAILURE:
                                elements0.append(address6)
                                address7 = FAILURE
                                index3 = self._offset
                                address7 = self._read_block_body()
                                if address7 is FAILURE:
                                    address7 = TreeNode(self._input[index3:index3], index3, [])
                                    self._offset = index3
                                if address7 is not FAILURE:
                                    elements0.append(address7)
                                    address8 = FAILURE
                                    address8 = self._read__()
                                    if address8 is not FAILURE:
                                        elements0.append(address8)
                                        address9 = FAILURE
                                        chunk2, max2 = None, self._offset + 1
                                        if max2 <= self._input_size:
                                            chunk2 = self._input[self._offset:max2]
                                        if chunk2 == ']':
                                            address9 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                            self._offset = self._offset + 1
                                        else:
                                            address9 = FAILURE
                                            if self._offset > self._failure:
                                                self._failure = self._offset
                                                self._expected = []
                                            if self._offset == self._failure:
                                                self._expected.append('\']\'')
                                        if address9 is not FAILURE:
                                            address10 = FAILURE
                                            address10 = self._read__()
                                            if address10 is not FAILURE:
                                                elements0.append(address10)
                                            else:
                                                elements0 = None
                                                self._offset = index1
                                        else:
                                            elements0 = None
                                            self._offset = index1
                                    else:
                                        elements0 = None
                                        self._offset = index1
                                else:
                                    elements0 = None
                                    self._offset = index1
                            else:
                                elements0 = None
                                self._offset = index1
                        else:
                            elements0 = None
                            self._offset = index1
                    else:
                        elements0 = None
                        self._offset = index1
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.normal_modifier_body(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['normal_modifier_body'][index0] = (address0, self._offset)
        return address0

    def _read_modifier_def_target(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['modifier_def_target'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        address0 = self._read_access()
        if address0 is FAILURE:
            self._offset = index1
            index2, elements0 = self._offset, []
            address1 = FAILURE
            chunk0, max0 = None, self._offset + 1
            if max0 <= self._input_size:
                chunk0 = self._input[self._offset:max0]
            if chunk0 == '<':
                address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                self._offset = self._offset + 1
            else:
                address1 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('\'<\'')
            if address1 is not FAILURE:
                address2 = FAILURE
                address2 = self._read__()
                if address2 is not FAILURE:
                    elements0.append(address2)
                    address3 = FAILURE
                    address3 = self._read_special_entry()
                    if address3 is not FAILURE:
                        elements0.append(address3)
                        address4 = FAILURE
                        address4 = self._read__()
                        if address4 is not FAILURE:
                            elements0.append(address4)
                            address5 = FAILURE
                            chunk1, max1 = None, self._offset + 1
                            if max1 <= self._input_size:
                                chunk1 = self._input[self._offset:max1]
                            if chunk1 == '>':
                                address5 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                self._offset = self._offset + 1
                            else:
                                address5 = FAILURE
                                if self._offset > self._failure:
                                    self._failure = self._offset
                                    self._expected = []
                                if self._offset == self._failure:
                                    self._expected.append('\'>\'')
                            if address5 is not FAILURE:
                                address6 = FAILURE
                                address6 = self._read__()
                                if address6 is not FAILURE:
                                    elements0.append(address6)
                                else:
                                    elements0 = None
                                    self._offset = index2
                            else:
                                elements0 = None
                                self._offset = index2
                        else:
                            elements0 = None
                            self._offset = index2
                    else:
                        elements0 = None
                        self._offset = index2
                else:
                    elements0 = None
                    self._offset = index2
            else:
                elements0 = None
                self._offset = index2
            if elements0 is None:
                address0 = FAILURE
            else:
                address0 = TreeNode51(self._input[index2:self._offset], index2, elements0)
                self._offset = self._offset
            if address0 is FAILURE:
                self._offset = index1
                chunk2, max2 = None, self._offset + 1
                if max2 <= self._input_size:
                    chunk2 = self._input[self._offset:max2]
                if chunk2 == '?':
                    address0 = self._actions.special_ref(self._input, self._offset, self._offset + 1, [])
                    self._offset = self._offset + 1
                else:
                    address0 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('\'?\'')
                if address0 is FAILURE:
                    self._offset = index1
        self._cache['modifier_def_target'][index0] = (address0, self._offset)
        return address0

    def _read_modifier_def(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['modifier_def'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_modifier_def_target()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read__()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                chunk0, max0 = None, self._offset + 2
                if max0 <= self._input_size:
                    chunk0 = self._input[self._offset:max0]
                if chunk0 == '<-':
                    address3 = TreeNode(self._input[self._offset:self._offset + 2], self._offset, [])
                    self._offset = self._offset + 2
                else:
                    address3 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('\'<-\'')
                if address3 is not FAILURE:
                    address4 = FAILURE
                    index2 = self._offset
                    chunk1, max1 = None, self._offset + 1
                    if max1 <= self._input_size:
                        chunk1 = self._input[self._offset:max1]
                    if chunk1 == '>':
                        address4 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                        self._offset = self._offset + 1
                    else:
                        address4 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('\'>\'')
                    self._offset = index2
                    if address4 is FAILURE:
                        address4 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                        self._offset = self._offset
                    else:
                        address4 = FAILURE
                    if address4 is not FAILURE:
                        elements0.append(address4)
                        address5 = FAILURE
                        address5 = self._read__ws()
                        if address5 is not FAILURE:
                            elements0.append(address5)
                            address6 = FAILURE
                            index3 = self._offset
                            address6 = self._read_small_modifier_body()
                            if address6 is FAILURE:
                                self._offset = index3
                                address6 = self._read_normal_modifier_body()
                                if address6 is FAILURE:
                                    self._offset = index3
                            if address6 is not FAILURE:
                                elements0.append(address6)
                            else:
                                elements0 = None
                                self._offset = index1
                        else:
                            elements0 = None
                            self._offset = index1
                    else:
                        elements0 = None
                        self._offset = index1
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.modifier_def(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['modifier_def'][index0] = (address0, self._offset)
        return address0

    def _read_lambda_def(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['lambda_def'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        chunk0, max0 = None, self._offset + 1
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == '!':
            address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
            self._offset = self._offset + 1
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'!\'')
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read__()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                chunk1, max1 = None, self._offset + 2
                if max1 <= self._input_size:
                    chunk1 = self._input[self._offset:max1]
                if chunk1 == '<-':
                    address3 = TreeNode(self._input[self._offset:self._offset + 2], self._offset, [])
                    self._offset = self._offset + 2
                else:
                    address3 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('\'<-\'')
                if address3 is not FAILURE:
                    address4 = FAILURE
                    index2 = self._offset
                    chunk2, max2 = None, self._offset + 1
                    if max2 <= self._input_size:
                        chunk2 = self._input[self._offset:max2]
                    if chunk2 == '>':
                        address4 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                        self._offset = self._offset + 1
                    else:
                        address4 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('\'>\'')
                    self._offset = index2
                    if address4 is FAILURE:
                        address4 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                        self._offset = self._offset
                    else:
                        address4 = FAILURE
                    if address4 is not FAILURE:
                        elements0.append(address4)
                        address5 = FAILURE
                        address5 = self._read__ws()
                        if address5 is not FAILURE:
                            elements0.append(address5)
                            address6 = FAILURE
                            index3 = self._offset
                            address6 = self._read_small_modifier_body()
                            if address6 is FAILURE:
                                self._offset = index3
                                address6 = self._read_normal_modifier_body()
                                if address6 is FAILURE:
                                    self._offset = index3
                            if address6 is not FAILURE:
                                elements0.append(address6)
                            else:
                                elements0 = None
                                self._offset = index1
                        else:
                            elements0 = None
                            self._offset = index1
                    else:
                        elements0 = None
                        self._offset = index1
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.modifier_def(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['lambda_def'][index0] = (address0, self._offset)
        return address0

    def _read_then(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['then'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        chunk0, max0 = None, self._offset + 4
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == 'then':
            address1 = TreeNode(self._input[self._offset:self._offset + 4], self._offset, [])
            self._offset = self._offset + 4
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'then\'')
        if address1 is not FAILURE:
            address2 = FAILURE
            address2 = self._read__ws()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                address3 = self._read_stmt_or_expr()
                if address3 is not FAILURE:
                    elements0.append(address3)
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode54(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        self._cache['then'][index0] = (address0, self._offset)
        return address0

    def _read_if_then(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['if_then'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        chunk0, max0 = None, self._offset + 2
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == 'if':
            address1 = TreeNode(self._input[self._offset:self._offset + 2], self._offset, [])
            self._offset = self._offset + 2
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'if\'')
        if address1 is not FAILURE:
            address2 = FAILURE
            address2 = self._read__()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                address3 = self._read_expression()
                if address3 is not FAILURE:
                    elements0.append(address3)
                    address4 = FAILURE
                    address4 = self._read__()
                    if address4 is not FAILURE:
                        elements0.append(address4)
                        address5 = FAILURE
                        address5 = self._read_then()
                        if address5 is not FAILURE:
                            elements0.append(address5)
                        else:
                            elements0 = None
                            self._offset = index1
                    else:
                        elements0 = None
                        self._offset = index1
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.if_(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['if_then'][index0] = (address0, self._offset)
        return address0

    def _read_unless(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['unless'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        chunk0, max0 = None, self._offset + 6
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == 'unless':
            address1 = TreeNode(self._input[self._offset:self._offset + 6], self._offset, [])
            self._offset = self._offset + 6
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'unless\'')
        if address1 is not FAILURE:
            address2 = FAILURE
            address2 = self._read__()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                address3 = self._read_expression()
                if address3 is not FAILURE:
                    elements0.append(address3)
                    address4 = FAILURE
                    address4 = self._read__()
                    if address4 is not FAILURE:
                        elements0.append(address4)
                        address5 = FAILURE
                        address5 = self._read_then()
                        if address5 is not FAILURE:
                            elements0.append(address5)
                        else:
                            elements0 = None
                            self._offset = index1
                    else:
                        elements0 = None
                        self._offset = index1
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.unless(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['unless'][index0] = (address0, self._offset)
        return address0

    def _read_otherwise(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['otherwise'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        chunk0, max0 = None, self._offset + 9
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == 'otherwise':
            address1 = TreeNode(self._input[self._offset:self._offset + 9], self._offset, [])
            self._offset = self._offset + 9
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'otherwise\'')
        if address1 is not FAILURE:
            address2 = FAILURE
            address2 = self._read__ws()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                address3 = self._read_stmt_or_expr()
                if address3 is not FAILURE:
                    elements0.append(address3)
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.otherwise(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['otherwise'][index0] = (address0, self._offset)
        return address0

    def _read_basic_load_list(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['basic_load_list'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        remaining0, index2, elements1, address2 = 0, self._offset, [], True
        while address2 is not FAILURE:
            index3, elements2 = self._offset, []
            address3 = FAILURE
            address3 = self._read_basic_name()
            if address3 is not FAILURE:
                elements2.append(address3)
                address4 = FAILURE
                address4 = self._read__()
                if address4 is not FAILURE:
                    elements2.append(address4)
                    address5 = FAILURE
                    chunk0, max0 = None, self._offset + 1
                    if max0 <= self._input_size:
                        chunk0 = self._input[self._offset:max0]
                    if chunk0 == ',':
                        address5 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                        self._offset = self._offset + 1
                    else:
                        address5 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('\',\'')
                    if address5 is not FAILURE:
                        address6 = FAILURE
                        address6 = self._read__ws()
                        if address6 is not FAILURE:
                            elements2.append(address6)
                        else:
                            elements2 = None
                            self._offset = index3
                    else:
                        elements2 = None
                        self._offset = index3
                else:
                    elements2 = None
                    self._offset = index3
            else:
                elements2 = None
                self._offset = index3
            if elements2 is None:
                address2 = FAILURE
            else:
                address2 = TreeNode58(self._input[index3:self._offset], index3, elements2)
                self._offset = self._offset
            if address2 is not FAILURE:
                elements1.append(address2)
                remaining0 -= 1
        if remaining0 <= 0:
            address1 = TreeNode(self._input[index2:self._offset], index2, elements1)
            self._offset = self._offset
        else:
            address1 = FAILURE
        if address1 is not FAILURE:
            elements0.append(address1)
            address7 = FAILURE
            index4 = self._offset
            address7 = self._read_basic_name()
            if address7 is FAILURE:
                address7 = TreeNode(self._input[index4:index4], index4, [])
                self._offset = index4
            if address7 is not FAILURE:
                elements0.append(address7)
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        self._cache['basic_load_list'][index0] = (address0, self._offset)
        return address0

    def _read_access_load_list(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['access_load_list'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        remaining0, index2, elements1, address2 = 0, self._offset, [], True
        while address2 is not FAILURE:
            index3, elements2 = self._offset, []
            address3 = FAILURE
            address3 = self._read_access()
            if address3 is not FAILURE:
                elements2.append(address3)
                address4 = FAILURE
                address4 = self._read__()
                if address4 is not FAILURE:
                    elements2.append(address4)
                    address5 = FAILURE
                    chunk0, max0 = None, self._offset + 1
                    if max0 <= self._input_size:
                        chunk0 = self._input[self._offset:max0]
                    if chunk0 == ',':
                        address5 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                        self._offset = self._offset + 1
                    else:
                        address5 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('\',\'')
                    if address5 is not FAILURE:
                        address6 = FAILURE
                        address6 = self._read__ws()
                        if address6 is not FAILURE:
                            elements2.append(address6)
                        else:
                            elements2 = None
                            self._offset = index3
                    else:
                        elements2 = None
                        self._offset = index3
                else:
                    elements2 = None
                    self._offset = index3
            else:
                elements2 = None
                self._offset = index3
            if elements2 is None:
                address2 = FAILURE
            else:
                address2 = TreeNode59(self._input[index3:self._offset], index3, elements2)
                self._offset = self._offset
            if address2 is not FAILURE:
                elements1.append(address2)
                remaining0 -= 1
        if remaining0 <= 0:
            address1 = TreeNode(self._input[index2:self._offset], index2, elements1)
            self._offset = self._offset
        else:
            address1 = FAILURE
        if address1 is not FAILURE:
            elements0.append(address1)
            address7 = FAILURE
            index4 = self._offset
            address7 = self._read_access()
            if address7 is FAILURE:
                address7 = TreeNode(self._input[index4:index4], index4, [])
                self._offset = index4
            if address7 is not FAILURE:
                elements0.append(address7)
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        self._cache['access_load_list'][index0] = (address0, self._offset)
        return address0

    def _read_loadable(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['loadable'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        address0 = self._read_new_bag()
        if address0 is FAILURE:
            self._offset = index1
            address0 = self._read_access_load_list()
            if address0 is FAILURE:
                self._offset = index1
        self._cache['loadable'][index0] = (address0, self._offset)
        return address0

    def _read_load_into(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['load_into'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        chunk0, max0 = None, self._offset + 4
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == 'into':
            address1 = TreeNode(self._input[self._offset:self._offset + 4], self._offset, [])
            self._offset = self._offset + 4
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'into\'')
        if address1 is not FAILURE:
            address2 = FAILURE
            address2 = self._read__()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                address3 = self._read_access()
                if address3 is not FAILURE:
                    elements0.append(address3)
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode60(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        self._cache['load_into'][index0] = (address0, self._offset)
        return address0

    def _read_load_from(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['load_from'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        chunk0, max0 = None, self._offset + 4
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == 'from':
            address1 = TreeNode(self._input[self._offset:self._offset + 4], self._offset, [])
            self._offset = self._offset + 4
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'from\'')
        if address1 is not FAILURE:
            address2 = FAILURE
            address2 = self._read__()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                address3 = self._read_loadable()
                if address3 is not FAILURE:
                    elements0.append(address3)
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode61(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        self._cache['load_from'][index0] = (address0, self._offset)
        return address0

    def _read_load(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['load'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        index2, elements0 = self._offset, []
        address1 = FAILURE
        chunk0, max0 = None, self._offset + 4
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == 'load':
            address1 = TreeNode(self._input[self._offset:self._offset + 4], self._offset, [])
            self._offset = self._offset + 4
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'load\'')
        if address1 is not FAILURE:
            address2 = FAILURE
            address2 = self._read__()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                chunk1, max1 = None, self._offset + 1
                if max1 <= self._input_size:
                    chunk1 = self._input[self._offset:max1]
                if chunk1 == '*':
                    address3 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                    self._offset = self._offset + 1
                else:
                    address3 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('\'*\'')
                if address3 is not FAILURE:
                    elements0.append(address3)
                    address4 = FAILURE
                    address4 = self._read__()
                    if address4 is not FAILURE:
                        elements0.append(address4)
                        address5 = FAILURE
                        address5 = self._read_load_from()
                        if address5 is not FAILURE:
                            elements0.append(address5)
                            address6 = FAILURE
                            address6 = self._read__()
                            if address6 is not FAILURE:
                                elements0.append(address6)
                                address7 = FAILURE
                                index3 = self._offset
                                address7 = self._read_load_into()
                                if address7 is FAILURE:
                                    address7 = TreeNode(self._input[index3:index3], index3, [])
                                    self._offset = index3
                                if address7 is not FAILURE:
                                    elements0.append(address7)
                                else:
                                    elements0 = None
                                    self._offset = index2
                            else:
                                elements0 = None
                                self._offset = index2
                        else:
                            elements0 = None
                            self._offset = index2
                    else:
                        elements0 = None
                        self._offset = index2
                else:
                    elements0 = None
                    self._offset = index2
            else:
                elements0 = None
                self._offset = index2
        else:
            elements0 = None
            self._offset = index2
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.load_from_into(self._input, index2, self._offset, elements0)
            self._offset = self._offset
        if address0 is FAILURE:
            self._offset = index1
            index4, elements1 = self._offset, []
            address8 = FAILURE
            chunk2, max2 = None, self._offset + 4
            if max2 <= self._input_size:
                chunk2 = self._input[self._offset:max2]
            if chunk2 == 'load':
                address8 = TreeNode(self._input[self._offset:self._offset + 4], self._offset, [])
                self._offset = self._offset + 4
            else:
                address8 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('\'load\'')
            if address8 is not FAILURE:
                address9 = FAILURE
                address9 = self._read__()
                if address9 is not FAILURE:
                    elements1.append(address9)
                    address10 = FAILURE
                    address10 = self._read_loadable()
                    if address10 is not FAILURE:
                        elements1.append(address10)
                        address11 = FAILURE
                        address11 = self._read__()
                        if address11 is not FAILURE:
                            elements1.append(address11)
                            address12 = FAILURE
                            address12 = self._read_load_from()
                            if address12 is not FAILURE:
                                elements1.append(address12)
                                address13 = FAILURE
                                address13 = self._read__()
                                if address13 is not FAILURE:
                                    elements1.append(address13)
                                    address14 = FAILURE
                                    address14 = self._read_load_into()
                                    if address14 is not FAILURE:
                                        elements1.append(address14)
                                    else:
                                        elements1 = None
                                        self._offset = index4
                                else:
                                    elements1 = None
                                    self._offset = index4
                            else:
                                elements1 = None
                                self._offset = index4
                        else:
                            elements1 = None
                            self._offset = index4
                    else:
                        elements1 = None
                        self._offset = index4
                else:
                    elements1 = None
                    self._offset = index4
            else:
                elements1 = None
                self._offset = index4
            if elements1 is None:
                address0 = FAILURE
            else:
                address0 = self._actions.load_from_into(self._input, index4, self._offset, elements1)
                self._offset = self._offset
            if address0 is FAILURE:
                self._offset = index1
                index5, elements2 = self._offset, []
                address15 = FAILURE
                chunk3, max3 = None, self._offset + 4
                if max3 <= self._input_size:
                    chunk3 = self._input[self._offset:max3]
                if chunk3 == 'load':
                    address15 = TreeNode(self._input[self._offset:self._offset + 4], self._offset, [])
                    self._offset = self._offset + 4
                else:
                    address15 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('\'load\'')
                if address15 is not FAILURE:
                    address16 = FAILURE
                    address16 = self._read__()
                    if address16 is not FAILURE:
                        elements2.append(address16)
                        address17 = FAILURE
                        address17 = self._read_loadable()
                        if address17 is not FAILURE:
                            elements2.append(address17)
                            address18 = FAILURE
                            address18 = self._read__()
                            if address18 is not FAILURE:
                                elements2.append(address18)
                                address19 = FAILURE
                                address19 = self._read_load_from()
                                if address19 is not FAILURE:
                                    elements2.append(address19)
                                else:
                                    elements2 = None
                                    self._offset = index5
                            else:
                                elements2 = None
                                self._offset = index5
                        else:
                            elements2 = None
                            self._offset = index5
                    else:
                        elements2 = None
                        self._offset = index5
                else:
                    elements2 = None
                    self._offset = index5
                if elements2 is None:
                    address0 = FAILURE
                else:
                    address0 = self._actions.load_from(self._input, index5, self._offset, elements2)
                    self._offset = self._offset
                if address0 is FAILURE:
                    self._offset = index1
                    index6, elements3 = self._offset, []
                    address20 = FAILURE
                    chunk4, max4 = None, self._offset + 4
                    if max4 <= self._input_size:
                        chunk4 = self._input[self._offset:max4]
                    if chunk4 == 'load':
                        address20 = TreeNode(self._input[self._offset:self._offset + 4], self._offset, [])
                        self._offset = self._offset + 4
                    else:
                        address20 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('\'load\'')
                    if address20 is not FAILURE:
                        address21 = FAILURE
                        address21 = self._read__()
                        if address21 is not FAILURE:
                            elements3.append(address21)
                            address22 = FAILURE
                            address22 = self._read_loadable()
                            if address22 is not FAILURE:
                                elements3.append(address22)
                                address23 = FAILURE
                                address23 = self._read__()
                                if address23 is not FAILURE:
                                    elements3.append(address23)
                                    address24 = FAILURE
                                    address24 = self._read_load_into()
                                    if address24 is not FAILURE:
                                        elements3.append(address24)
                                    else:
                                        elements3 = None
                                        self._offset = index6
                                else:
                                    elements3 = None
                                    self._offset = index6
                            else:
                                elements3 = None
                                self._offset = index6
                        else:
                            elements3 = None
                            self._offset = index6
                    else:
                        elements3 = None
                        self._offset = index6
                    if elements3 is None:
                        address0 = FAILURE
                    else:
                        address0 = self._actions.load_into(self._input, index6, self._offset, elements3)
                        self._offset = self._offset
                    if address0 is FAILURE:
                        self._offset = index1
                        index7, elements4 = self._offset, []
                        address25 = FAILURE
                        chunk5, max5 = None, self._offset + 4
                        if max5 <= self._input_size:
                            chunk5 = self._input[self._offset:max5]
                        if chunk5 == 'load':
                            address25 = TreeNode(self._input[self._offset:self._offset + 4], self._offset, [])
                            self._offset = self._offset + 4
                        else:
                            address25 = FAILURE
                            if self._offset > self._failure:
                                self._failure = self._offset
                                self._expected = []
                            if self._offset == self._failure:
                                self._expected.append('\'load\'')
                        if address25 is not FAILURE:
                            address26 = FAILURE
                            address26 = self._read__()
                            if address26 is not FAILURE:
                                elements4.append(address26)
                                address27 = FAILURE
                                address27 = self._read_loadable()
                                if address27 is not FAILURE:
                                    elements4.append(address27)
                                else:
                                    elements4 = None
                                    self._offset = index7
                            else:
                                elements4 = None
                                self._offset = index7
                        else:
                            elements4 = None
                            self._offset = index7
                        if elements4 is None:
                            address0 = FAILURE
                        else:
                            address0 = self._actions.load(self._input, index7, self._offset, elements4)
                            self._offset = self._offset
                        if address0 is FAILURE:
                            self._offset = index1
        self._cache['load'][index0] = (address0, self._offset)
        return address0

    def _read_except_when(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['except_when'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        chunk0, max0 = None, self._offset + 6
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == 'except':
            address1 = TreeNode(self._input[self._offset:self._offset + 6], self._offset, [])
            self._offset = self._offset + 6
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'except\'')
        if address1 is not FAILURE:
            address2 = FAILURE
            address2 = self._read__()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                chunk1, max1 = None, self._offset + 4
                if max1 <= self._input_size:
                    chunk1 = self._input[self._offset:max1]
                if chunk1 == 'when':
                    address3 = TreeNode(self._input[self._offset:self._offset + 4], self._offset, [])
                    self._offset = self._offset + 4
                else:
                    address3 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('\'when\'')
                if address3 is not FAILURE:
                    address4 = FAILURE
                    address4 = self._read__()
                    if address4 is not FAILURE:
                        elements0.append(address4)
                        address5 = FAILURE
                        address5 = self._read_expression()
                        if address5 is not FAILURE:
                            elements0.append(address5)
                            address6 = FAILURE
                            address6 = self._read__()
                            if address6 is not FAILURE:
                                elements0.append(address6)
                                address7 = FAILURE
                                address7 = self._read_then()
                                if address7 is not FAILURE:
                                    elements0.append(address7)
                                else:
                                    elements0 = None
                                    self._offset = index1
                            else:
                                elements0 = None
                                self._offset = index1
                        else:
                            elements0 = None
                            self._offset = index1
                    else:
                        elements0 = None
                        self._offset = index1
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.predicated_statement(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['except_when'][index0] = (address0, self._offset)
        return address0

    def _read_restart_pos(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['restart_pos'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        index2, elements0 = self._offset, []
        address1 = FAILURE
        chunk0, max0 = None, self._offset + 6
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == 'before':
            address1 = TreeNode(self._input[self._offset:self._offset + 6], self._offset, [])
            self._offset = self._offset + 6
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'before\'')
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read__()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                index3 = self._offset
                address3 = self._read_name()
                if address3 is FAILURE:
                    address3 = TreeNode(self._input[index3:index3], index3, [])
                    self._offset = index3
                if address3 is not FAILURE:
                    elements0.append(address3)
                else:
                    elements0 = None
                    self._offset = index2
            else:
                elements0 = None
                self._offset = index2
        else:
            elements0 = None
            self._offset = index2
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.restart(self._input, index2, self._offset, elements0)
            self._offset = self._offset
        if address0 is FAILURE:
            self._offset = index1
            index4, elements1 = self._offset, []
            address4 = FAILURE
            chunk1, max1 = None, self._offset + 2
            if max1 <= self._input_size:
                chunk1 = self._input[self._offset:max1]
            if chunk1 == 'at':
                address4 = TreeNode(self._input[self._offset:self._offset + 2], self._offset, [])
                self._offset = self._offset + 2
            else:
                address4 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('\'at\'')
            if address4 is not FAILURE:
                elements1.append(address4)
                address5 = FAILURE
                address5 = self._read__()
                if address5 is not FAILURE:
                    elements1.append(address5)
                    address6 = FAILURE
                    index5 = self._offset
                    address6 = self._read_name()
                    if address6 is FAILURE:
                        address6 = TreeNode(self._input[index5:index5], index5, [])
                        self._offset = index5
                    if address6 is not FAILURE:
                        elements1.append(address6)
                    else:
                        elements1 = None
                        self._offset = index4
                else:
                    elements1 = None
                    self._offset = index4
            else:
                elements1 = None
                self._offset = index4
            if elements1 is None:
                address0 = FAILURE
            else:
                address0 = self._actions.restart(self._input, index4, self._offset, elements1)
                self._offset = self._offset
            if address0 is FAILURE:
                self._offset = index1
                index6, elements2 = self._offset, []
                address7 = FAILURE
                chunk2, max2 = None, self._offset + 5
                if max2 <= self._input_size:
                    chunk2 = self._input[self._offset:max2]
                if chunk2 == 'after':
                    address7 = TreeNode(self._input[self._offset:self._offset + 5], self._offset, [])
                    self._offset = self._offset + 5
                else:
                    address7 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('\'after\'')
                if address7 is not FAILURE:
                    elements2.append(address7)
                    address8 = FAILURE
                    address8 = self._read__()
                    if address8 is not FAILURE:
                        elements2.append(address8)
                        address9 = FAILURE
                        index7 = self._offset
                        address9 = self._read_name()
                        if address9 is FAILURE:
                            address9 = TreeNode(self._input[index7:index7], index7, [])
                            self._offset = index7
                        if address9 is not FAILURE:
                            elements2.append(address9)
                        else:
                            elements2 = None
                            self._offset = index6
                    else:
                        elements2 = None
                        self._offset = index6
                else:
                    elements2 = None
                    self._offset = index6
                if elements2 is None:
                    address0 = FAILURE
                else:
                    address0 = self._actions.restart(self._input, index6, self._offset, elements2)
                    self._offset = self._offset
                if address0 is FAILURE:
                    self._offset = index1
        self._cache['restart_pos'][index0] = (address0, self._offset)
        return address0

    def _read_stmt_or_expr(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['stmt_or_expr'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        address0 = self._read_statement()
        if address0 is FAILURE:
            self._offset = index1
            address0 = self._read_expression()
            if address0 is FAILURE:
                self._offset = index1
        self._cache['stmt_or_expr'][index0] = (address0, self._offset)
        return address0

    def _read_block_body(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['block_body'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        remaining0, index2, elements1, address2 = 0, self._offset, [], True
        while address2 is not FAILURE:
            index3, elements2 = self._offset, []
            address3 = FAILURE
            address3 = self._read_statement()
            if address3 is not FAILURE:
                elements2.append(address3)
                address4 = FAILURE
                address4 = self._read__()
                if address4 is not FAILURE:
                    elements2.append(address4)
                    address5 = FAILURE
                    index4 = self._offset
                    chunk0, max0 = None, self._offset + 1
                    if max0 <= self._input_size:
                        chunk0 = self._input[self._offset:max0]
                    if chunk0 == ']':
                        address5 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                        self._offset = self._offset + 1
                    else:
                        address5 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('\']\'')
                    self._offset = index4
                    if address5 is FAILURE:
                        address5 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                        self._offset = self._offset
                    else:
                        address5 = FAILURE
                    if address5 is not FAILURE:
                        elements2.append(address5)
                    else:
                        elements2 = None
                        self._offset = index3
                else:
                    elements2 = None
                    self._offset = index3
            else:
                elements2 = None
                self._offset = index3
            if elements2 is None:
                address2 = FAILURE
            else:
                address2 = TreeNode72(self._input[index3:self._offset], index3, elements2)
                self._offset = self._offset
            if address2 is not FAILURE:
                elements1.append(address2)
                remaining0 -= 1
        if remaining0 <= 0:
            address1 = TreeNode(self._input[index2:self._offset], index2, elements1)
            self._offset = self._offset
        else:
            address1 = FAILURE
        if address1 is not FAILURE:
            elements0.append(address1)
            address6 = FAILURE
            address6 = self._read__()
            if address6 is not FAILURE:
                elements0.append(address6)
                address7 = FAILURE
                address7 = self._read_statement()
                if address7 is not FAILURE:
                    elements0.append(address7)
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode71(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        self._cache['block_body'][index0] = (address0, self._offset)
        return address0

    def _read_loop_name(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['loop_name'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        chunk0, max0 = None, self._offset + 1
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == '@':
            address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
            self._offset = self._offset + 1
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'@\'')
        if address1 is not FAILURE:
            address2 = FAILURE
            address2 = self._read__()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                address3 = self._read_basic_name()
                if address3 is not FAILURE:
                    elements0.append(address3)
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.loop_name(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['loop_name'][index0] = (address0, self._offset)
        return address0

    def _read_loop_body(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['loop_body'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        chunk0, max0 = None, self._offset + 2
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == 'do':
            address1 = TreeNode(self._input[self._offset:self._offset + 2], self._offset, [])
            self._offset = self._offset + 2
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'do\'')
        if address1 is not FAILURE:
            address2 = FAILURE
            address2 = self._read__ws()
            if address2 is not FAILURE:
                address3 = FAILURE
                address3 = self._read_stmt_or_expr()
                if address3 is not FAILURE:
                    elements0.append(address3)
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.loop_body(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['loop_body'][index0] = (address0, self._offset)
        return address0

    def _read_but_if_stmt(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['but_if_stmt'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        index2, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_expression()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read__()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                index3 = self._offset
                chunk0, max0 = None, self._offset + 3
                if max0 <= self._input_size:
                    chunk0 = self._input[self._offset:max0]
                if chunk0 == 'but':
                    address3 = TreeNode(self._input[self._offset:self._offset + 3], self._offset, [])
                    self._offset = self._offset + 3
                else:
                    address3 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('\'but\'')
                self._offset = index3
                if address3 is not FAILURE:
                    address3 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                    self._offset = self._offset
                else:
                    address3 = FAILURE
                if address3 is not FAILURE:
                    elements0.append(address3)
                else:
                    elements0 = None
                    self._offset = index2
            else:
                elements0 = None
                self._offset = index2
        else:
            elements0 = None
            self._offset = index2
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode75(self._input[index2:self._offset], index2, elements0)
            self._offset = self._offset
        if address0 is FAILURE:
            self._offset = index1
            address0 = self._read_stmt_or_expr()
            if address0 is FAILURE:
                self._offset = index1
        self._cache['but_if_stmt'][index0] = (address0, self._offset)
        return address0

    def _read_but_if(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['but_if'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        chunk0, max0 = None, self._offset + 3
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == 'but':
            address1 = TreeNode(self._input[self._offset:self._offset + 3], self._offset, [])
            self._offset = self._offset + 3
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'but\'')
        if address1 is not FAILURE:
            address2 = FAILURE
            index2 = self._offset
            chunk1, max1 = None, self._offset + 6
            if max1 <= self._input_size:
                chunk1 = self._input[self._offset:max1]
            if chunk1 == 'always':
                address2 = TreeNode(self._input[self._offset:self._offset + 6], self._offset, [])
                self._offset = self._offset + 6
            else:
                address2 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('\'always\'')
            self._offset = index2
            if address2 is FAILURE:
                address2 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                self._offset = self._offset
            else:
                address2 = FAILURE
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                address3 = self._read__()
                if address3 is not FAILURE:
                    elements0.append(address3)
                    address4 = FAILURE
                    chunk2, max2 = None, self._offset + 2
                    if max2 <= self._input_size:
                        chunk2 = self._input[self._offset:max2]
                    if chunk2 == 'if':
                        address4 = TreeNode(self._input[self._offset:self._offset + 2], self._offset, [])
                        self._offset = self._offset + 2
                    else:
                        address4 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('\'if\'')
                    if address4 is not FAILURE:
                        address5 = FAILURE
                        address5 = self._read__()
                        if address5 is not FAILURE:
                            elements0.append(address5)
                            address6 = FAILURE
                            index3 = self._offset
                            address6 = self._read_expression()
                            if address6 is FAILURE:
                                self._offset = index3
                                chunk3, max3 = None, self._offset + 1
                                if max3 <= self._input_size:
                                    chunk3 = self._input[self._offset:max3]
                                if chunk3 == '*':
                                    address6 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                    self._offset = self._offset + 1
                                else:
                                    address6 = FAILURE
                                    if self._offset > self._failure:
                                        self._failure = self._offset
                                        self._expected = []
                                    if self._offset == self._failure:
                                        self._expected.append('\'*\'')
                                if address6 is FAILURE:
                                    self._offset = index3
                            if address6 is not FAILURE:
                                elements0.append(address6)
                                address7 = FAILURE
                                address7 = self._read__()
                                if address7 is not FAILURE:
                                    elements0.append(address7)
                                    address8 = FAILURE
                                    chunk4, max4 = None, self._offset + 6
                                    if max4 <= self._input_size:
                                        chunk4 = self._input[self._offset:max4]
                                    if chunk4 == 'occurs':
                                        address8 = TreeNode(self._input[self._offset:self._offset + 6], self._offset, [])
                                        self._offset = self._offset + 6
                                    else:
                                        address8 = FAILURE
                                        if self._offset > self._failure:
                                            self._failure = self._offset
                                            self._expected = []
                                        if self._offset == self._failure:
                                            self._expected.append('\'occurs\'')
                                    if address8 is not FAILURE:
                                        address9 = FAILURE
                                        address9 = self._read__()
                                        if address9 is not FAILURE:
                                            elements0.append(address9)
                                            address10 = FAILURE
                                            address10 = self._read_then()
                                            if address10 is not FAILURE:
                                                elements0.append(address10)
                                            else:
                                                elements0 = None
                                                self._offset = index1
                                        else:
                                            elements0 = None
                                            self._offset = index1
                                    else:
                                        elements0 = None
                                        self._offset = index1
                                else:
                                    elements0 = None
                                    self._offset = index1
                            else:
                                elements0 = None
                                self._offset = index1
                        else:
                            elements0 = None
                            self._offset = index1
                    else:
                        elements0 = None
                        self._offset = index1
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.but_if(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['but_if'][index0] = (address0, self._offset)
        return address0

    def _read_always(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['always'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        chunk0, max0 = None, self._offset + 3
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == 'but':
            address1 = TreeNode(self._input[self._offset:self._offset + 3], self._offset, [])
            self._offset = self._offset + 3
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'but\'')
        if address1 is not FAILURE:
            address2 = FAILURE
            address2 = self._read__()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                chunk1, max1 = None, self._offset + 6
                if max1 <= self._input_size:
                    chunk1 = self._input[self._offset:max1]
                if chunk1 == 'always':
                    address3 = TreeNode(self._input[self._offset:self._offset + 6], self._offset, [])
                    self._offset = self._offset + 6
                else:
                    address3 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('\'always\'')
                if address3 is not FAILURE:
                    address4 = FAILURE
                    address4 = self._read__ws()
                    if address4 is not FAILURE:
                        elements0.append(address4)
                        address5 = FAILURE
                        address5 = self._read_stmt_or_expr()
                        if address5 is not FAILURE:
                            elements0.append(address5)
                        else:
                            elements0 = None
                            self._offset = index1
                    else:
                        elements0 = None
                        self._offset = index1
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.always(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['always'][index0] = (address0, self._offset)
        return address0

    def _read_attempt(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['attempt'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        index2, elements0 = self._offset, []
        address1 = FAILURE
        chunk0, max0 = None, self._offset + 7
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == 'attempt':
            address1 = TreeNode(self._input[self._offset:self._offset + 7], self._offset, [])
            self._offset = self._offset + 7
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'attempt\'')
        if address1 is not FAILURE:
            address2 = FAILURE
            address2 = self._read__ws()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                address3 = self._read_but_if_stmt()
                if address3 is not FAILURE:
                    elements0.append(address3)
                    address4 = FAILURE
                    address4 = self._read__ws()
                    if address4 is not FAILURE:
                        elements0.append(address4)
                        address5 = FAILURE
                        address5 = self._read_always()
                        if address5 is not FAILURE:
                            elements0.append(address5)
                        else:
                            elements0 = None
                            self._offset = index2
                    else:
                        elements0 = None
                        self._offset = index2
                else:
                    elements0 = None
                    self._offset = index2
            else:
                elements0 = None
                self._offset = index2
        else:
            elements0 = None
            self._offset = index2
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.attempt(self._input, index2, self._offset, elements0)
            self._offset = self._offset
        if address0 is FAILURE:
            self._offset = index1
            index3, elements1 = self._offset, []
            address6 = FAILURE
            chunk1, max1 = None, self._offset + 7
            if max1 <= self._input_size:
                chunk1 = self._input[self._offset:max1]
            if chunk1 == 'attempt':
                address6 = TreeNode(self._input[self._offset:self._offset + 7], self._offset, [])
                self._offset = self._offset + 7
            else:
                address6 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('\'attempt\'')
            if address6 is not FAILURE:
                address7 = FAILURE
                address7 = self._read__ws()
                if address7 is not FAILURE:
                    elements1.append(address7)
                    address8 = FAILURE
                    address8 = self._read_but_if_stmt()
                    if address8 is not FAILURE:
                        elements1.append(address8)
                        address9 = FAILURE
                        address9 = self._read__ws()
                        if address9 is not FAILURE:
                            elements1.append(address9)
                            address10 = FAILURE
                            remaining0, index4, elements2, address11 = 1, self._offset, [], True
                            while address11 is not FAILURE:
                                address11 = self._read_but_if()
                                if address11 is not FAILURE:
                                    elements2.append(address11)
                                    remaining0 -= 1
                            if remaining0 <= 0:
                                address10 = TreeNode(self._input[index4:self._offset], index4, elements2)
                                self._offset = self._offset
                            else:
                                address10 = FAILURE
                            if address10 is not FAILURE:
                                elements1.append(address10)
                                address12 = FAILURE
                                index5 = self._offset
                                index6, elements3 = self._offset, []
                                address13 = FAILURE
                                address13 = self._read__ws()
                                if address13 is not FAILURE:
                                    elements3.append(address13)
                                    address14 = FAILURE
                                    address14 = self._read_always()
                                    if address14 is not FAILURE:
                                        elements3.append(address14)
                                    else:
                                        elements3 = None
                                        self._offset = index6
                                else:
                                    elements3 = None
                                    self._offset = index6
                                if elements3 is None:
                                    address12 = FAILURE
                                else:
                                    address12 = TreeNode80(self._input[index6:self._offset], index6, elements3)
                                    self._offset = self._offset
                                if address12 is FAILURE:
                                    address12 = TreeNode(self._input[index5:index5], index5, [])
                                    self._offset = index5
                                if address12 is not FAILURE:
                                    elements1.append(address12)
                                else:
                                    elements1 = None
                                    self._offset = index3
                            else:
                                elements1 = None
                                self._offset = index3
                        else:
                            elements1 = None
                            self._offset = index3
                    else:
                        elements1 = None
                        self._offset = index3
                else:
                    elements1 = None
                    self._offset = index3
            else:
                elements1 = None
                self._offset = index3
            if elements1 is None:
                address0 = FAILURE
            else:
                address0 = self._actions.attempt(self._input, index3, self._offset, elements1)
                self._offset = self._offset
            if address0 is FAILURE:
                self._offset = index1
                index7, elements4 = self._offset, []
                address15 = FAILURE
                chunk2, max2 = None, self._offset + 7
                if max2 <= self._input_size:
                    chunk2 = self._input[self._offset:max2]
                if chunk2 == 'attempt':
                    address15 = TreeNode(self._input[self._offset:self._offset + 7], self._offset, [])
                    self._offset = self._offset + 7
                else:
                    address15 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('\'attempt\'')
                if address15 is not FAILURE:
                    address16 = FAILURE
                    address16 = self._read__ws()
                    if address16 is not FAILURE:
                        elements4.append(address16)
                        address17 = FAILURE
                        address17 = self._read_but_if_stmt()
                        if address17 is not FAILURE:
                            elements4.append(address17)
                        else:
                            elements4 = None
                            self._offset = index7
                    else:
                        elements4 = None
                        self._offset = index7
                else:
                    elements4 = None
                    self._offset = index7
                if elements4 is None:
                    address0 = FAILURE
                else:
                    address0 = self._actions.attempt(self._input, index7, self._offset, elements4)
                    self._offset = self._offset
                if address0 is FAILURE:
                    self._offset = index1
        self._cache['attempt'][index0] = (address0, self._offset)
        return address0

    def _read_statement(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['statement'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        address0 = self._read_eos()
        if address0 is FAILURE:
            self._offset = index1
            chunk0, max0 = None, self._offset + 5
            if max0 <= self._input_size:
                chunk0 = self._input[self._offset:max0]
            if chunk0 == 'leave':
                address0 = self._actions.leave(self._input, self._offset, self._offset + 5, [])
                self._offset = self._offset + 5
            else:
                address0 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('\'leave\'')
            if address0 is FAILURE:
                self._offset = index1
                address0 = self._read_attempt()
                if address0 is FAILURE:
                    self._offset = index1
                    index2, elements0 = self._offset, []
                    address1 = FAILURE
                    chunk1, max1 = None, self._offset + 4
                    if max1 <= self._input_size:
                        chunk1 = self._input[self._offset:max1]
                    if chunk1 == 'oops':
                        address1 = TreeNode(self._input[self._offset:self._offset + 4], self._offset, [])
                        self._offset = self._offset + 4
                    else:
                        address1 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('\'oops\'')
                    if address1 is not FAILURE:
                        address2 = FAILURE
                        address2 = self._read__()
                        if address2 is not FAILURE:
                            elements0.append(address2)
                            address3 = FAILURE
                            address3 = self._read_expression()
                            if address3 is not FAILURE:
                                elements0.append(address3)
                            else:
                                elements0 = None
                                self._offset = index2
                        else:
                            elements0 = None
                            self._offset = index2
                    else:
                        elements0 = None
                        self._offset = index2
                    if elements0 is None:
                        address0 = FAILURE
                    else:
                        address0 = self._actions.oops(self._input, index2, self._offset, elements0)
                        self._offset = self._offset
                    if address0 is FAILURE:
                        self._offset = index1
                        index3, elements1 = self._offset, []
                        address4 = FAILURE
                        chunk2, max2 = None, self._offset + 5
                        if max2 <= self._input_size:
                            chunk2 = self._input[self._offset:max2]
                        if chunk2 == 'clear':
                            address4 = TreeNode(self._input[self._offset:self._offset + 5], self._offset, [])
                            self._offset = self._offset + 5
                        else:
                            address4 = FAILURE
                            if self._offset > self._failure:
                                self._failure = self._offset
                                self._expected = []
                            if self._offset == self._failure:
                                self._expected.append('\'clear\'')
                        if address4 is not FAILURE:
                            address5 = FAILURE
                            address5 = self._read__()
                            if address5 is not FAILURE:
                                elements1.append(address5)
                                address6 = FAILURE
                                address6 = self._read_access()
                                if address6 is not FAILURE:
                                    elements1.append(address6)
                                else:
                                    elements1 = None
                                    self._offset = index3
                            else:
                                elements1 = None
                                self._offset = index3
                        else:
                            elements1 = None
                            self._offset = index3
                        if elements1 is None:
                            address0 = FAILURE
                        else:
                            address0 = self._actions.clear(self._input, index3, self._offset, elements1)
                            self._offset = self._offset
                        if address0 is FAILURE:
                            self._offset = index1
                            index4, elements2 = self._offset, []
                            address7 = FAILURE
                            chunk3, max3 = None, self._offset + 7
                            if max3 <= self._input_size:
                                chunk3 = self._input[self._offset:max3]
                            if chunk3 == 'restart':
                                address7 = TreeNode(self._input[self._offset:self._offset + 7], self._offset, [])
                                self._offset = self._offset + 7
                            else:
                                address7 = FAILURE
                                if self._offset > self._failure:
                                    self._failure = self._offset
                                    self._expected = []
                                if self._offset == self._failure:
                                    self._expected.append('\'restart\'')
                            if address7 is not FAILURE:
                                address8 = FAILURE
                                address8 = self._read__()
                                if address8 is not FAILURE:
                                    elements2.append(address8)
                                    address9 = FAILURE
                                    address9 = self._read_restart_pos()
                                    if address9 is not FAILURE:
                                        elements2.append(address9)
                                    else:
                                        elements2 = None
                                        self._offset = index4
                                else:
                                    elements2 = None
                                    self._offset = index4
                            else:
                                elements2 = None
                                self._offset = index4
                            if elements2 is None:
                                address0 = FAILURE
                            else:
                                address0 = TreeNode84(self._input[index4:self._offset], index4, elements2)
                                self._offset = self._offset
                            if address0 is FAILURE:
                                self._offset = index1
                                index5, elements3 = self._offset, []
                                address10 = FAILURE
                                chunk4, max4 = None, self._offset + 1
                                if max4 <= self._input_size:
                                    chunk4 = self._input[self._offset:max4]
                                if chunk4 == '[':
                                    address10 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                    self._offset = self._offset + 1
                                else:
                                    address10 = FAILURE
                                    if self._offset > self._failure:
                                        self._failure = self._offset
                                        self._expected = []
                                    if self._offset == self._failure:
                                        self._expected.append('\'[\'')
                                if address10 is not FAILURE:
                                    address11 = FAILURE
                                    index6 = self._offset
                                    chunk5, max5 = None, self._offset + 1
                                    if max5 <= self._input_size:
                                        chunk5 = self._input[self._offset:max5]
                                    if chunk5 == ':':
                                        address11 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                        self._offset = self._offset + 1
                                    else:
                                        address11 = FAILURE
                                        if self._offset > self._failure:
                                            self._failure = self._offset
                                            self._expected = []
                                        if self._offset == self._failure:
                                            self._expected.append('\':\'')
                                    self._offset = index6
                                    if address11 is FAILURE:
                                        address11 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                        self._offset = self._offset
                                    else:
                                        address11 = FAILURE
                                    if address11 is not FAILURE:
                                        elements3.append(address11)
                                        address12 = FAILURE
                                        address12 = self._read__ws()
                                        if address12 is not FAILURE:
                                            elements3.append(address12)
                                            address13 = FAILURE
                                            address13 = self._read_block_body()
                                            if address13 is not FAILURE:
                                                elements3.append(address13)
                                                address14 = FAILURE
                                                address14 = self._read__ws()
                                                if address14 is not FAILURE:
                                                    elements3.append(address14)
                                                    address15 = FAILURE
                                                    chunk6, max6 = None, self._offset + 1
                                                    if max6 <= self._input_size:
                                                        chunk6 = self._input[self._offset:max6]
                                                    if chunk6 == ']':
                                                        address15 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                                        self._offset = self._offset + 1
                                                    else:
                                                        address15 = FAILURE
                                                        if self._offset > self._failure:
                                                            self._failure = self._offset
                                                            self._expected = []
                                                        if self._offset == self._failure:
                                                            self._expected.append('\']\'')
                                                    if address15 is not FAILURE:
                                                        address16 = FAILURE
                                                        address16 = self._read__()
                                                        if address16 is not FAILURE:
                                                            elements3.append(address16)
                                                        else:
                                                            elements3 = None
                                                            self._offset = index5
                                                    else:
                                                        elements3 = None
                                                        self._offset = index5
                                                else:
                                                    elements3 = None
                                                    self._offset = index5
                                            else:
                                                elements3 = None
                                                self._offset = index5
                                        else:
                                            elements3 = None
                                            self._offset = index5
                                    else:
                                        elements3 = None
                                        self._offset = index5
                                else:
                                    elements3 = None
                                    self._offset = index5
                                if elements3 is None:
                                    address0 = FAILURE
                                else:
                                    address0 = self._actions.block(self._input, index5, self._offset, elements3)
                                    self._offset = self._offset
                                if address0 is FAILURE:
                                    self._offset = index1
                                    index7, elements4 = self._offset, []
                                    address17 = FAILURE
                                    chunk7, max7 = None, self._offset + 1
                                    if max7 <= self._input_size:
                                        chunk7 = self._input[self._offset:max7]
                                    if chunk7 == '[':
                                        address17 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                        self._offset = self._offset + 1
                                    else:
                                        address17 = FAILURE
                                        if self._offset > self._failure:
                                            self._failure = self._offset
                                            self._expected = []
                                        if self._offset == self._failure:
                                            self._expected.append('\'[\'')
                                    if address17 is not FAILURE:
                                        address18 = FAILURE
                                        index8 = self._offset
                                        chunk8, max8 = None, self._offset + 1
                                        if max8 <= self._input_size:
                                            chunk8 = self._input[self._offset:max8]
                                        if chunk8 == ':':
                                            address18 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                            self._offset = self._offset + 1
                                        else:
                                            address18 = FAILURE
                                            if self._offset > self._failure:
                                                self._failure = self._offset
                                                self._expected = []
                                            if self._offset == self._failure:
                                                self._expected.append('\':\'')
                                        self._offset = index8
                                        if address18 is FAILURE:
                                            address18 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                            self._offset = self._offset
                                        else:
                                            address18 = FAILURE
                                        if address18 is not FAILURE:
                                            elements4.append(address18)
                                            address19 = FAILURE
                                            address19 = self._read__ws()
                                            if address19 is not FAILURE:
                                                elements4.append(address19)
                                                address20 = FAILURE
                                                chunk9, max9 = None, self._offset + 1
                                                if max9 <= self._input_size:
                                                    chunk9 = self._input[self._offset:max9]
                                                if chunk9 == ']':
                                                    address20 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                                    self._offset = self._offset + 1
                                                else:
                                                    address20 = FAILURE
                                                    if self._offset > self._failure:
                                                        self._failure = self._offset
                                                        self._expected = []
                                                    if self._offset == self._failure:
                                                        self._expected.append('\']\'')
                                                if address20 is not FAILURE:
                                                    address21 = FAILURE
                                                    address21 = self._read__()
                                                    if address21 is not FAILURE:
                                                        elements4.append(address21)
                                                    else:
                                                        elements4 = None
                                                        self._offset = index7
                                                else:
                                                    elements4 = None
                                                    self._offset = index7
                                            else:
                                                elements4 = None
                                                self._offset = index7
                                        else:
                                            elements4 = None
                                            self._offset = index7
                                    else:
                                        elements4 = None
                                        self._offset = index7
                                    if elements4 is None:
                                        address0 = FAILURE
                                    else:
                                        address0 = self._actions.block(self._input, index7, self._offset, elements4)
                                        self._offset = self._offset
                                    if address0 is FAILURE:
                                        self._offset = index1
                                        index9, elements5 = self._offset, []
                                        address22 = FAILURE
                                        chunk10, max10 = None, self._offset + 2
                                        if max10 <= self._input_size:
                                            chunk10 = self._input[self._offset:max10]
                                        if chunk10 == '={':
                                            address22 = TreeNode(self._input[self._offset:self._offset + 2], self._offset, [])
                                            self._offset = self._offset + 2
                                        else:
                                            address22 = FAILURE
                                            if self._offset > self._failure:
                                                self._failure = self._offset
                                                self._expected = []
                                            if self._offset == self._failure:
                                                self._expected.append('\'={\'')
                                        if address22 is not FAILURE:
                                            address23 = FAILURE
                                            index10 = self._offset
                                            chunk11, max11 = None, self._offset + 1
                                            if max11 <= self._input_size:
                                                chunk11 = self._input[self._offset:max11]
                                            if chunk11 == ':':
                                                address23 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                                self._offset = self._offset + 1
                                            else:
                                                address23 = FAILURE
                                                if self._offset > self._failure:
                                                    self._failure = self._offset
                                                    self._expected = []
                                                if self._offset == self._failure:
                                                    self._expected.append('\':\'')
                                            self._offset = index10
                                            if address23 is FAILURE:
                                                address23 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                                self._offset = self._offset
                                            else:
                                                address23 = FAILURE
                                            if address23 is not FAILURE:
                                                elements5.append(address23)
                                                address24 = FAILURE
                                                address24 = self._read__()
                                                if address24 is not FAILURE:
                                                    elements5.append(address24)
                                                    address25 = FAILURE
                                                    address25 = self._read_access()
                                                    if address25 is not FAILURE:
                                                        elements5.append(address25)
                                                        address26 = FAILURE
                                                        address26 = self._read__()
                                                        if address26 is not FAILURE:
                                                            elements5.append(address26)
                                                            address27 = FAILURE
                                                            chunk12, max12 = None, self._offset + 1
                                                            if max12 <= self._input_size:
                                                                chunk12 = self._input[self._offset:max12]
                                                            if chunk12 == '}':
                                                                address27 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                                                self._offset = self._offset + 1
                                                            else:
                                                                address27 = FAILURE
                                                                if self._offset > self._failure:
                                                                    self._failure = self._offset
                                                                    self._expected = []
                                                                if self._offset == self._failure:
                                                                    self._expected.append('\'}\'')
                                                            if address27 is not FAILURE:
                                                                address28 = FAILURE
                                                                address28 = self._read__()
                                                                if address28 is not FAILURE:
                                                                    elements5.append(address28)
                                                                else:
                                                                    elements5 = None
                                                                    self._offset = index9
                                                            else:
                                                                elements5 = None
                                                                self._offset = index9
                                                        else:
                                                            elements5 = None
                                                            self._offset = index9
                                                    else:
                                                        elements5 = None
                                                        self._offset = index9
                                                else:
                                                    elements5 = None
                                                    self._offset = index9
                                            else:
                                                elements5 = None
                                                self._offset = index9
                                        else:
                                            elements5 = None
                                            self._offset = index9
                                        if elements5 is None:
                                            address0 = FAILURE
                                        else:
                                            address0 = self._actions.reduce_and_assign(self._input, index9, self._offset, elements5)
                                            self._offset = self._offset
                                        if address0 is FAILURE:
                                            self._offset = index1
                                            address0 = self._read_load()
                                            if address0 is FAILURE:
                                                self._offset = index1
                                                address0 = self._read_modifier_def()
                                                if address0 is FAILURE:
                                                    self._offset = index1
                                                    index11, elements6 = self._offset, []
                                                    address29 = FAILURE
                                                    address29 = self._read_if_then()
                                                    if address29 is not FAILURE:
                                                        elements6.append(address29)
                                                        address30 = FAILURE
                                                        remaining0, index12, elements7, address31 = 0, self._offset, [], True
                                                        while address31 is not FAILURE:
                                                            index13, elements8 = self._offset, []
                                                            address32 = FAILURE
                                                            address32 = self._read__ws()
                                                            if address32 is not FAILURE:
                                                                elements8.append(address32)
                                                                address33 = FAILURE
                                                                address33 = self._read_unless()
                                                                if address33 is not FAILURE:
                                                                    elements8.append(address33)
                                                                else:
                                                                    elements8 = None
                                                                    self._offset = index13
                                                            else:
                                                                elements8 = None
                                                                self._offset = index13
                                                            if elements8 is None:
                                                                address31 = FAILURE
                                                            else:
                                                                address31 = TreeNode89(self._input[index13:self._offset], index13, elements8)
                                                                self._offset = self._offset
                                                            if address31 is not FAILURE:
                                                                elements7.append(address31)
                                                                remaining0 -= 1
                                                        if remaining0 <= 0:
                                                            address30 = TreeNode(self._input[index12:self._offset], index12, elements7)
                                                            self._offset = self._offset
                                                        else:
                                                            address30 = FAILURE
                                                        if address30 is not FAILURE:
                                                            elements6.append(address30)
                                                            address34 = FAILURE
                                                            index14 = self._offset
                                                            index15, elements9 = self._offset, []
                                                            address35 = FAILURE
                                                            address35 = self._read__ws()
                                                            if address35 is not FAILURE:
                                                                elements9.append(address35)
                                                                address36 = FAILURE
                                                                address36 = self._read_otherwise()
                                                                if address36 is not FAILURE:
                                                                    elements9.append(address36)
                                                                else:
                                                                    elements9 = None
                                                                    self._offset = index15
                                                            else:
                                                                elements9 = None
                                                                self._offset = index15
                                                            if elements9 is None:
                                                                address34 = FAILURE
                                                            else:
                                                                address34 = TreeNode90(self._input[index15:self._offset], index15, elements9)
                                                                self._offset = self._offset
                                                            if address34 is FAILURE:
                                                                address34 = TreeNode(self._input[index14:index14], index14, [])
                                                                self._offset = index14
                                                            if address34 is not FAILURE:
                                                                elements6.append(address34)
                                                            else:
                                                                elements6 = None
                                                                self._offset = index11
                                                        else:
                                                            elements6 = None
                                                            self._offset = index11
                                                    else:
                                                        elements6 = None
                                                        self._offset = index11
                                                    if elements6 is None:
                                                        address0 = FAILURE
                                                    else:
                                                        address0 = self._actions.if_stmt(self._input, index11, self._offset, elements6)
                                                        self._offset = self._offset
                                                    if address0 is FAILURE:
                                                        self._offset = index1
                                                        index16, elements10 = self._offset, []
                                                        address37 = FAILURE
                                                        chunk13, max13 = None, self._offset + 3
                                                        if max13 <= self._input_size:
                                                            chunk13 = self._input[self._offset:max13]
                                                        if chunk13 == 'for':
                                                            address37 = TreeNode(self._input[self._offset:self._offset + 3], self._offset, [])
                                                            self._offset = self._offset + 3
                                                        else:
                                                            address37 = FAILURE
                                                            if self._offset > self._failure:
                                                                self._failure = self._offset
                                                                self._expected = []
                                                            if self._offset == self._failure:
                                                                self._expected.append('\'for\'')
                                                        if address37 is not FAILURE:
                                                            address38 = FAILURE
                                                            address38 = self._read__()
                                                            if address38 is not FAILURE:
                                                                elements10.append(address38)
                                                                address39 = FAILURE
                                                                chunk14, max14 = None, self._offset + 5
                                                                if max14 <= self._input_size:
                                                                    chunk14 = self._input[self._offset:max14]
                                                                if chunk14 == 'every':
                                                                    address39 = TreeNode(self._input[self._offset:self._offset + 5], self._offset, [])
                                                                    self._offset = self._offset + 5
                                                                else:
                                                                    address39 = FAILURE
                                                                    if self._offset > self._failure:
                                                                        self._failure = self._offset
                                                                        self._expected = []
                                                                    if self._offset == self._failure:
                                                                        self._expected.append('\'every\'')
                                                                if address39 is not FAILURE:
                                                                    address40 = FAILURE
                                                                    address40 = self._read__()
                                                                    if address40 is not FAILURE:
                                                                        elements10.append(address40)
                                                                        address41 = FAILURE
                                                                        index17 = self._offset
                                                                        address41 = self._read_loop_name()
                                                                        if address41 is FAILURE:
                                                                            address41 = TreeNode(self._input[index17:index17], index17, [])
                                                                            self._offset = index17
                                                                        if address41 is not FAILURE:
                                                                            elements10.append(address41)
                                                                            address42 = FAILURE
                                                                            address42 = self._read__()
                                                                            if address42 is not FAILURE:
                                                                                elements10.append(address42)
                                                                                address43 = FAILURE
                                                                                address43 = self._read_basic_name()
                                                                                if address43 is not FAILURE:
                                                                                    elements10.append(address43)
                                                                                    address44 = FAILURE
                                                                                    address44 = self._read__()
                                                                                    if address44 is not FAILURE:
                                                                                        elements10.append(address44)
                                                                                        address45 = FAILURE
                                                                                        chunk15, max15 = None, self._offset + 4
                                                                                        if max15 <= self._input_size:
                                                                                            chunk15 = self._input[self._offset:max15]
                                                                                        if chunk15 == 'that':
                                                                                            address45 = TreeNode(self._input[self._offset:self._offset + 4], self._offset, [])
                                                                                            self._offset = self._offset + 4
                                                                                        else:
                                                                                            address45 = FAILURE
                                                                                            if self._offset > self._failure:
                                                                                                self._failure = self._offset
                                                                                                self._expected = []
                                                                                            if self._offset == self._failure:
                                                                                                self._expected.append('\'that\'')
                                                                                        if address45 is not FAILURE:
                                                                                            address46 = FAILURE
                                                                                            address46 = self._read__()
                                                                                            if address46 is not FAILURE:
                                                                                                elements10.append(address46)
                                                                                                address47 = FAILURE
                                                                                                address47 = self._read_expression()
                                                                                                if address47 is not FAILURE:
                                                                                                    elements10.append(address47)
                                                                                                    address48 = FAILURE
                                                                                                    address48 = self._read__()
                                                                                                    if address48 is not FAILURE:
                                                                                                        elements10.append(address48)
                                                                                                        address49 = FAILURE
                                                                                                        chunk16, max16 = None, self._offset + 3
                                                                                                        if max16 <= self._input_size:
                                                                                                            chunk16 = self._input[self._offset:max16]
                                                                                                        if chunk16 == 'has':
                                                                                                            address49 = TreeNode(self._input[self._offset:self._offset + 3], self._offset, [])
                                                                                                            self._offset = self._offset + 3
                                                                                                        else:
                                                                                                            address49 = FAILURE
                                                                                                            if self._offset > self._failure:
                                                                                                                self._failure = self._offset
                                                                                                                self._expected = []
                                                                                                            if self._offset == self._failure:
                                                                                                                self._expected.append('\'has\'')
                                                                                                        if address49 is not FAILURE:
                                                                                                            address50 = FAILURE
                                                                                                            address50 = self._read__()
                                                                                                            if address50 is not FAILURE:
                                                                                                                elements10.append(address50)
                                                                                                                address51 = FAILURE
                                                                                                                address51 = self._read_loop_body()
                                                                                                                if address51 is not FAILURE:
                                                                                                                    elements10.append(address51)
                                                                                                                else:
                                                                                                                    elements10 = None
                                                                                                                    self._offset = index16
                                                                                                            else:
                                                                                                                elements10 = None
                                                                                                                self._offset = index16
                                                                                                        else:
                                                                                                            elements10 = None
                                                                                                            self._offset = index16
                                                                                                    else:
                                                                                                        elements10 = None
                                                                                                        self._offset = index16
                                                                                                else:
                                                                                                    elements10 = None
                                                                                                    self._offset = index16
                                                                                            else:
                                                                                                elements10 = None
                                                                                                self._offset = index16
                                                                                        else:
                                                                                            elements10 = None
                                                                                            self._offset = index16
                                                                                    else:
                                                                                        elements10 = None
                                                                                        self._offset = index16
                                                                                else:
                                                                                    elements10 = None
                                                                                    self._offset = index16
                                                                            else:
                                                                                elements10 = None
                                                                                self._offset = index16
                                                                        else:
                                                                            elements10 = None
                                                                            self._offset = index16
                                                                    else:
                                                                        elements10 = None
                                                                        self._offset = index16
                                                                else:
                                                                    elements10 = None
                                                                    self._offset = index16
                                                            else:
                                                                elements10 = None
                                                                self._offset = index16
                                                        else:
                                                            elements10 = None
                                                            self._offset = index16
                                                        if elements10 is None:
                                                            address0 = FAILURE
                                                        else:
                                                            address0 = self._actions.for_every(self._input, index16, self._offset, elements10)
                                                            self._offset = self._offset
                                                        if address0 is FAILURE:
                                                            self._offset = index1
                                                            index18, elements11 = self._offset, []
                                                            address52 = FAILURE
                                                            chunk17, max17 = None, self._offset + 5
                                                            if max17 <= self._input_size:
                                                                chunk17 = self._input[self._offset:max17]
                                                            if chunk17 == 'until':
                                                                address52 = TreeNode(self._input[self._offset:self._offset + 5], self._offset, [])
                                                                self._offset = self._offset + 5
                                                            else:
                                                                address52 = FAILURE
                                                                if self._offset > self._failure:
                                                                    self._failure = self._offset
                                                                    self._expected = []
                                                                if self._offset == self._failure:
                                                                    self._expected.append('\'until\'')
                                                            if address52 is not FAILURE:
                                                                address53 = FAILURE
                                                                address53 = self._read__()
                                                                if address53 is not FAILURE:
                                                                    elements11.append(address53)
                                                                    address54 = FAILURE
                                                                    index19 = self._offset
                                                                    address54 = self._read_loop_name()
                                                                    if address54 is FAILURE:
                                                                        address54 = TreeNode(self._input[index19:index19], index19, [])
                                                                        self._offset = index19
                                                                    if address54 is not FAILURE:
                                                                        elements11.append(address54)
                                                                        address55 = FAILURE
                                                                        address55 = self._read__()
                                                                        if address55 is not FAILURE:
                                                                            elements11.append(address55)
                                                                            address56 = FAILURE
                                                                            address56 = self._read_expression()
                                                                            if address56 is not FAILURE:
                                                                                elements11.append(address56)
                                                                                address57 = FAILURE
                                                                                address57 = self._read__()
                                                                                if address57 is not FAILURE:
                                                                                    elements11.append(address57)
                                                                                    address58 = FAILURE
                                                                                    address58 = self._read_loop_body()
                                                                                    if address58 is not FAILURE:
                                                                                        elements11.append(address58)
                                                                                        address59 = FAILURE
                                                                                        address59 = self._read__ws()
                                                                                        if address59 is not FAILURE:
                                                                                            elements11.append(address59)
                                                                                            address60 = FAILURE
                                                                                            remaining1, index20, elements12, address61 = 0, self._offset, [], True
                                                                                            while address61 is not FAILURE:
                                                                                                index21, elements13 = self._offset, []
                                                                                                address62 = FAILURE
                                                                                                address62 = self._read_except_when()
                                                                                                if address62 is not FAILURE:
                                                                                                    elements13.append(address62)
                                                                                                    address63 = FAILURE
                                                                                                    address63 = self._read__ws()
                                                                                                    if address63 is not FAILURE:
                                                                                                        elements13.append(address63)
                                                                                                    else:
                                                                                                        elements13 = None
                                                                                                        self._offset = index21
                                                                                                else:
                                                                                                    elements13 = None
                                                                                                    self._offset = index21
                                                                                                if elements13 is None:
                                                                                                    address61 = FAILURE
                                                                                                else:
                                                                                                    address61 = TreeNode93(self._input[index21:self._offset], index21, elements13)
                                                                                                    self._offset = self._offset
                                                                                                if address61 is not FAILURE:
                                                                                                    elements12.append(address61)
                                                                                                    remaining1 -= 1
                                                                                            if remaining1 <= 0:
                                                                                                address60 = TreeNode(self._input[index20:self._offset], index20, elements12)
                                                                                                self._offset = self._offset
                                                                                            else:
                                                                                                address60 = FAILURE
                                                                                            if address60 is not FAILURE:
                                                                                                elements11.append(address60)
                                                                                                address64 = FAILURE
                                                                                                index22 = self._offset
                                                                                                address64 = self._read_otherwise()
                                                                                                if address64 is FAILURE:
                                                                                                    address64 = TreeNode(self._input[index22:index22], index22, [])
                                                                                                    self._offset = index22
                                                                                                if address64 is not FAILURE:
                                                                                                    elements11.append(address64)
                                                                                                else:
                                                                                                    elements11 = None
                                                                                                    self._offset = index18
                                                                                            else:
                                                                                                elements11 = None
                                                                                                self._offset = index18
                                                                                        else:
                                                                                            elements11 = None
                                                                                            self._offset = index18
                                                                                    else:
                                                                                        elements11 = None
                                                                                        self._offset = index18
                                                                                else:
                                                                                    elements11 = None
                                                                                    self._offset = index18
                                                                            else:
                                                                                elements11 = None
                                                                                self._offset = index18
                                                                        else:
                                                                            elements11 = None
                                                                            self._offset = index18
                                                                    else:
                                                                        elements11 = None
                                                                        self._offset = index18
                                                                else:
                                                                    elements11 = None
                                                                    self._offset = index18
                                                            else:
                                                                elements11 = None
                                                                self._offset = index18
                                                            if elements11 is None:
                                                                address0 = FAILURE
                                                            else:
                                                                address0 = self._actions.until_do(self._input, index18, self._offset, elements11)
                                                                self._offset = self._offset
                                                            if address0 is FAILURE:
                                                                self._offset = index1
                                                                index23, elements14 = self._offset, []
                                                                address65 = FAILURE
                                                                address65 = self._read_access()
                                                                if address65 is not FAILURE:
                                                                    elements14.append(address65)
                                                                    address66 = FAILURE
                                                                    address66 = self._read__()
                                                                    if address66 is not FAILURE:
                                                                        elements14.append(address66)
                                                                        address67 = FAILURE
                                                                        chunk18, max18 = None, self._offset + 2
                                                                        if max18 <= self._input_size:
                                                                            chunk18 = self._input[self._offset:max18]
                                                                        if chunk18 == '=>':
                                                                            address67 = TreeNode(self._input[self._offset:self._offset + 2], self._offset, [])
                                                                            self._offset = self._offset + 2
                                                                        else:
                                                                            address67 = FAILURE
                                                                            if self._offset > self._failure:
                                                                                self._failure = self._offset
                                                                                self._expected = []
                                                                            if self._offset == self._failure:
                                                                                self._expected.append('\'=>\'')
                                                                        if address67 is not FAILURE:
                                                                            address68 = FAILURE
                                                                            address68 = self._read__()
                                                                            if address68 is not FAILURE:
                                                                                elements14.append(address68)
                                                                                address69 = FAILURE
                                                                                address69 = self._read_modifier_tail()
                                                                                if address69 is not FAILURE:
                                                                                    elements14.append(address69)
                                                                                    address70 = FAILURE
                                                                                    remaining2, index24, elements15, address71 = 0, self._offset, [], True
                                                                                    while address71 is not FAILURE:
                                                                                        address71 = self._read_modifier_call()
                                                                                        if address71 is not FAILURE:
                                                                                            elements15.append(address71)
                                                                                            remaining2 -= 1
                                                                                    if remaining2 <= 0:
                                                                                        address70 = TreeNode(self._input[index24:self._offset], index24, elements15)
                                                                                        self._offset = self._offset
                                                                                    else:
                                                                                        address70 = FAILURE
                                                                                    if address70 is not FAILURE:
                                                                                        elements14.append(address70)
                                                                                    else:
                                                                                        elements14 = None
                                                                                        self._offset = index23
                                                                                else:
                                                                                    elements14 = None
                                                                                    self._offset = index23
                                                                            else:
                                                                                elements14 = None
                                                                                self._offset = index23
                                                                        else:
                                                                            elements14 = None
                                                                            self._offset = index23
                                                                    else:
                                                                        elements14 = None
                                                                        self._offset = index23
                                                                else:
                                                                    elements14 = None
                                                                    self._offset = index23
                                                                if elements14 is None:
                                                                    address0 = FAILURE
                                                                else:
                                                                    address0 = self._actions.modify_and_assign(self._input, index23, self._offset, elements14)
                                                                    self._offset = self._offset
                                                                if address0 is FAILURE:
                                                                    self._offset = index1
                                                                    index25, elements16 = self._offset, []
                                                                    address72 = FAILURE
                                                                    address72 = self._read_access()
                                                                    if address72 is not FAILURE:
                                                                        elements16.append(address72)
                                                                        address73 = FAILURE
                                                                        address73 = self._read__()
                                                                        if address73 is not FAILURE:
                                                                            elements16.append(address73)
                                                                            address74 = FAILURE
                                                                            address74 = self._read_assign_op()
                                                                            if address74 is not FAILURE:
                                                                                elements16.append(address74)
                                                                                address75 = FAILURE
                                                                                address75 = self._read__ws()
                                                                                if address75 is not FAILURE:
                                                                                    elements16.append(address75)
                                                                                    address76 = FAILURE
                                                                                    address76 = self._read_expression()
                                                                                    if address76 is not FAILURE:
                                                                                        elements16.append(address76)
                                                                                    else:
                                                                                        elements16 = None
                                                                                        self._offset = index25
                                                                                else:
                                                                                    elements16 = None
                                                                                    self._offset = index25
                                                                            else:
                                                                                elements16 = None
                                                                                self._offset = index25
                                                                        else:
                                                                            elements16 = None
                                                                            self._offset = index25
                                                                    else:
                                                                        elements16 = None
                                                                        self._offset = index25
                                                                    if elements16 is None:
                                                                        address0 = FAILURE
                                                                    else:
                                                                        address0 = self._actions.assignment(self._input, index25, self._offset, elements16)
                                                                        self._offset = self._offset
                                                                    if address0 is FAILURE:
                                                                        self._offset = index1
                                                                        index26, elements17 = self._offset, []
                                                                        address77 = FAILURE
                                                                        address77 = self._read_expression()
                                                                        if address77 is not FAILURE:
                                                                            elements17.append(address77)
                                                                            address78 = FAILURE
                                                                            address78 = self._read__()
                                                                            if address78 is not FAILURE:
                                                                                elements17.append(address78)
                                                                                address79 = FAILURE
                                                                                address79 = self._read_eos()
                                                                                if address79 is not FAILURE:
                                                                                    elements17.append(address79)
                                                                                else:
                                                                                    elements17 = None
                                                                                    self._offset = index26
                                                                            else:
                                                                                elements17 = None
                                                                                self._offset = index26
                                                                        else:
                                                                            elements17 = None
                                                                            self._offset = index26
                                                                        if elements17 is None:
                                                                            address0 = FAILURE
                                                                        else:
                                                                            address0 = TreeNode96(self._input[index26:self._offset], index26, elements17)
                                                                            self._offset = self._offset
                                                                        if address0 is FAILURE:
                                                                            self._offset = index1
        self._cache['statement'][index0] = (address0, self._offset)
        return address0


class Parser(Grammar):
    def __init__(self, input, actions, types):
        self._input = input
        self._input_size = len(input)
        self._actions = actions
        self._types = types
        self._offset = 0
        self._cache = defaultdict(dict)
        self._failure = 0
        self._expected = []

    def parse(self):
        tree = self._read_start()
        if tree is not FAILURE and self._offset == self._input_size:
            return tree
        if not self._expected:
            self._failure = self._offset
            self._expected.append('<EOF>')
        raise ParseError(format_error(self._input, self._failure, self._expected))


def format_error(input, offset, expected):
    lines, line_no, position = input.split('\n'), 0, 0
    while position <= offset:
        position += len(lines[line_no]) + 1
        line_no += 1
    message, line = 'Line ' + str(line_no) + ': expected ' + ', '.join(expected) + '\n', lines[line_no - 1]
    message += line + '\n'
    position -= len(line) + 1
    message += ' ' * (offset - position)
    return message + '^'

def parse(input, actions=None, types=None):
    parser = Parser(input, actions, types)
    return parser.parse()
