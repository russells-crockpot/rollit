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
        self._ = elements[1]


class TreeNode4(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode4, self).__init__(text, offset, elements)
        self._ws = elements[6]
        self._ = elements[7]


class TreeNode5(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode5, self).__init__(text, offset, elements)
        self._ws = elements[2]
        self._ = elements[3]


class TreeNode6(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode6, self).__init__(text, offset, elements)
        self._ = elements[2]
        self.access = elements[1]


class TreeNode7(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode7, self).__init__(text, offset, elements)
        self._ws = elements[0]
        self._ = elements[4]


class TreeNode8(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode8, self).__init__(text, offset, elements)
        self.expression = elements[0]
        self._ = elements[1]
        self._ws = elements[3]


class TreeNode9(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode9, self).__init__(text, offset, elements)
        self._ws = elements[0]
        self._ = elements[3]
        self.basic_name = elements[2]


class TreeNode10(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode10, self).__init__(text, offset, elements)
        self.reduce = elements[0]
        self._ = elements[1]


class TreeNode11(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode11, self).__init__(text, offset, elements)
        self._ws = elements[0]


class TreeNode12(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode12, self).__init__(text, offset, elements)
        self.reduce_expr = elements[0]


class TreeNode13(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode13, self).__init__(text, offset, elements)
        self._ = elements[0]


class TreeNode14(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode14, self).__init__(text, offset, elements)
        self._ = elements[6]
        self.expression = elements[7]
        self.comparison = elements[4]


class TreeNode15(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode15, self).__init__(text, offset, elements)
        self._ = elements[0]
        self.comparison = elements[1]


class TreeNode16(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode16, self).__init__(text, offset, elements)
        self.roll_math = elements[0]
        self._ = elements[3]
        self.comp_op = elements[2]
        self.comparison = elements[4]


class TreeNode17(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode17, self).__init__(text, offset, elements)
        self.add_math = elements[0]
        self._ = elements[4]
        self.roll_op = elements[2]
        self.roll_math = elements[5]


class TreeNode18(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode18, self).__init__(text, offset, elements)
        self.mult_math = elements[0]
        self._ = elements[4]
        self.add_op = elements[2]
        self.add_math = elements[5]


class TreeNode19(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode19, self).__init__(text, offset, elements)
        self.modify = elements[0]
        self._ = elements[4]
        self.mult_op = elements[2]
        self.mult_math = elements[5]


class TreeNode20(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode20, self).__init__(text, offset, elements)
        self._ = elements[0]
        self.modify = elements[1]


class TreeNode21(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode21, self).__init__(text, offset, elements)
        self.dice = elements[0]
        self._ = elements[1]


class TreeNode22(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode22, self).__init__(text, offset, elements)
        self.reduce_expr = elements[5]
        self._ = elements[3]


class TreeNode23(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode23, self).__init__(text, offset, elements)
        self._ws = elements[3]
        self.expression = elements[2]


class TreeNode24(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode24, self).__init__(text, offset, elements)
        self.basic_name = elements[0]
        self._ = elements[1]
        self._ws = elements[2]


class TreeNode25(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode25, self).__init__(text, offset, elements)
        self._ = elements[5]
        self.expression = elements[1]
        self._ws = elements[3]
        self.statement = elements[4]


class TreeNode26(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode26, self).__init__(text, offset, elements)
        self._ = elements[5]
        self.expression = elements[1]
        self._ws = elements[3]
        self.statement = elements[4]


class TreeNode27(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode27, self).__init__(text, offset, elements)
        self._ws = elements[0]
        self.stmt_or_expr = elements[1]


class TreeNode28(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode28, self).__init__(text, offset, elements)
        self.basic_name = elements[0]
        self._ = elements[1]
        self._ws = elements[3]


class TreeNode29(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode29, self).__init__(text, offset, elements)
        self.access = elements[0]
        self._ = elements[1]
        self._ws = elements[3]


class TreeNode30(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode30, self).__init__(text, offset, elements)
        self._ = elements[0]
        self.access = elements[1]


class TreeNode31(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode31, self).__init__(text, offset, elements)
        self._ = elements[0]
        self.basic_load_list = elements[1]


class TreeNode32(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode32, self).__init__(text, offset, elements)
        self._ = elements[4]
        self.load_from = elements[3]


class TreeNode33(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode33, self).__init__(text, offset, elements)
        self._ = elements[2]
        self.access_load_list = elements[3]


class TreeNode34(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode34, self).__init__(text, offset, elements)
        self._ = elements[4]
        self.basic_load_list = elements[1]
        self.load_from = elements[3]
        self.load_into = elements[5]


class TreeNode35(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode35, self).__init__(text, offset, elements)
        self._ = elements[2]
        self.basic_load_list = elements[1]
        self.load_from = elements[3]


class TreeNode36(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode36, self).__init__(text, offset, elements)
        self._ = elements[2]
        self.basic_load_list = elements[1]
        self.load_into = elements[3]


class TreeNode37(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode37, self).__init__(text, offset, elements)
        self._ = elements[0]
        self.basic_load_list = elements[1]


class TreeNode38(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode38, self).__init__(text, offset, elements)
        self._ = elements[1]


class TreeNode39(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode39, self).__init__(text, offset, elements)
        self._ = elements[1]


class TreeNode40(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode40, self).__init__(text, offset, elements)
        self._ = elements[1]


class TreeNode41(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode41, self).__init__(text, offset, elements)
        self._ = elements[3]
        self.expression = elements[2]
        self._ws = elements[4]
        self.stmt_or_expr = elements[5]


class TreeNode42(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode42, self).__init__(text, offset, elements)
        self._ = elements[0]
        self.basic_name = elements[1]


class TreeNode43(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode43, self).__init__(text, offset, elements)
        self.stmt_or_expr = elements[0]


class TreeNode44(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode44, self).__init__(text, offset, elements)
        self._ = elements[1]


class TreeNode45(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode45, self).__init__(text, offset, elements)
        self.statement = elements[0]
        self._ = elements[1]


class TreeNode46(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode46, self).__init__(text, offset, elements)
        self.expression = elements[0]
        self._ = elements[1]


class TreeNode47(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode47, self).__init__(text, offset, elements)
        self._ = elements[0]
        self.restart_pos = elements[1]


class TreeNode48(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode48, self).__init__(text, offset, elements)
        self._ws = elements[2]
        self.block_stmt = elements[1]
        self._ = elements[3]


class TreeNode49(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode49, self).__init__(text, offset, elements)
        self._ws = elements[0]
        self._ = elements[1]


class TreeNode50(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode50, self).__init__(text, offset, elements)
        self.if_then = elements[0]


class TreeNode51(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode51, self).__init__(text, offset, elements)
        self._ws = elements[0]
        self.unless = elements[1]


class TreeNode52(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode52, self).__init__(text, offset, elements)
        self._ws = elements[0]
        self.otherwise = elements[1]


class TreeNode53(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode53, self).__init__(text, offset, elements)
        self._ = elements[9]
        self.basic_name = elements[4]
        self.expression = elements[7]
        self.loop_body = elements[10]


class TreeNode54(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode54, self).__init__(text, offset, elements)
        self._ = elements[4]
        self.expression = elements[3]
        self.loop_body = elements[5]
        self._ws = elements[6]


class TreeNode55(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode55, self).__init__(text, offset, elements)
        self.except_when = elements[0]
        self._ws = elements[1]


class TreeNode56(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode56, self).__init__(text, offset, elements)
        self.access = elements[0]
        self._ = elements[1]
        self.assign_op = elements[2]
        self._ws = elements[3]
        self.expression = elements[4]


class TreeNode57(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode57, self).__init__(text, offset, elements)
        self.access = elements[0]
        self._ = elements[5]
        self.modifier_params = elements[3]
        self._ws = elements[4]
        self.stmt_or_expr = elements[6]


class TreeNode58(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode58, self).__init__(text, offset, elements)
        self.expression = elements[0]
        self._ = elements[1]
        self.eos = elements[2]


class ParseError(SyntaxError):
    pass


FAILURE = object()


class Grammar(object):
    REGEX_1 = re.compile('^[^\\n\\r\\f]')
    REGEX_2 = re.compile('^[ \\t]')
    REGEX_3 = re.compile('^[\\n\\r\\f]')
    REGEX_4 = re.compile('^[\\n\\r\\f \\t]')
    REGEX_5 = re.compile('^[\\n\\r\\f]')
    REGEX_6 = re.compile('^[0-9]')
    REGEX_7 = re.compile('^[0-9]')
    REGEX_8 = re.compile('^[0-9]')
    REGEX_9 = re.compile('^[\\\\runftvb\']')
    REGEX_10 = re.compile('^[^\']')
    REGEX_11 = re.compile('^[a-zA-Z_]')
    REGEX_12 = re.compile('^[a-zA-Z_0-9]')

    def _read_start(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['start'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        remaining0, index2, elements1, address2 = 0, self._offset, [], True
        while address2 is not FAILURE:
            index3, elements2 = self._offset, []
            address3 = FAILURE
            address3 = self._read__()
            if address3 is not FAILURE:
                elements2.append(address3)
                address4 = FAILURE
                address4 = self._read_statement()
                if address4 is not FAILURE:
                    elements2.append(address4)
                    address5 = FAILURE
                    address5 = self._read__()
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
                address2 = TreeNode2(self._input[index3:self._offset], index3, elements2)
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
            index4 = self._offset
            address6 = self._read_stmt_or_expr()
            if address6 is FAILURE:
                address6 = TreeNode(self._input[index4:index4], index4, [])
                self._offset = index4
            if address6 is not FAILURE:
                elements0.append(address6)
                address7 = FAILURE
                address7 = self._read__ws()
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
            address0 = self._actions.statements(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['start'][index0] = (address0, self._offset)
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
            remaining0, index2, elements1, address3 = 1, self._offset, [], True
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
            if chunk0 is not None and Grammar.REGEX_2.search(chunk0):
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
                if chunk0 is not None and Grammar.REGEX_3.search(chunk0):
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
            if chunk0 is not None and Grammar.REGEX_4.search(chunk0):
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
                    if chunk1 is not None and Grammar.REGEX_5.search(chunk1):
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
                if chunk1 is not None and Grammar.REGEX_6.search(chunk1):
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
                        if chunk3 is not None and Grammar.REGEX_7.search(chunk3):
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
                if chunk1 is not None and Grammar.REGEX_8.search(chunk1):
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
            if chunk1 is not None and Grammar.REGEX_9.search(chunk1):
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
                    if chunk1 is not None and Grammar.REGEX_10.search(chunk1):
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
        chunk0, max0 = None, self._offset + 1
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 is not None and Grammar.REGEX_11.search(chunk0):
            address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
            self._offset = self._offset + 1
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('[a-zA-Z_]')
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            remaining0, index2, elements1, address3 = 0, self._offset, [], True
            while address3 is not FAILURE:
                chunk1, max1 = None, self._offset + 1
                if max1 <= self._input_size:
                    chunk1 = self._input[self._offset:max1]
                if chunk1 is not None and Grammar.REGEX_12.search(chunk1):
                    address3 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                    self._offset = self._offset + 1
                else:
                    address3 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('[a-zA-Z_0-9]')
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
            address0 = self._actions.text(self._input, index1, self._offset, elements0)
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
                        address0 = self._read_basic_name()
                        if address0 is FAILURE:
                            self._offset = index1
        self._cache['name'][index0] = (address0, self._offset)
        return address0

    def _read_enlarge(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['enlarge'].get(index0)
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
                address3 = self._read_expression()
                if address3 is FAILURE:
                    address3 = TreeNode(self._input[index2:index2], index2, [])
                    self._offset = index2
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
                        if chunk1 == '@':
                            address5 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                            self._offset = self._offset + 1
                        else:
                            address5 = FAILURE
                            if self._offset > self._failure:
                                self._failure = self._offset
                                self._expected = []
                            if self._offset == self._failure:
                                self._expected.append('\'@\'')
                        if address5 is not FAILURE:
                            elements0.append(address5)
                            address6 = FAILURE
                            address6 = self._read__ws()
                            if address6 is not FAILURE:
                                elements0.append(address6)
                                address7 = FAILURE
                                index3 = self._offset
                                address7 = self._read_expression()
                                if address7 is FAILURE:
                                    address7 = TreeNode(self._input[index3:index3], index3, [])
                                    self._offset = index3
                                if address7 is not FAILURE:
                                    elements0.append(address7)
                                    address8 = FAILURE
                                    address8 = self._read__ws()
                                    if address8 is not FAILURE:
                                        elements0.append(address8)
                                        address9 = FAILURE
                                        chunk2, max2 = None, self._offset + 1
                                        if max2 <= self._input_size:
                                            chunk2 = self._input[self._offset:max2]
                                        if chunk2 == '}':
                                            address9 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                            self._offset = self._offset + 1
                                        else:
                                            address9 = FAILURE
                                            if self._offset > self._failure:
                                                self._failure = self._offset
                                                self._expected = []
                                            if self._offset == self._failure:
                                                self._expected.append('\'}\'')
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
            address0 = self._actions.enlarge(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['enlarge'][index0] = (address0, self._offset)
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
                address3 = self._read_expression()
                if address3 is FAILURE:
                    self._offset = index2
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
                    if address3 is FAILURE:
                        self._offset = index2
                if address3 is not FAILURE:
                    elements0.append(address3)
                    address4 = FAILURE
                    address4 = self._read__ws()
                    if address4 is not FAILURE:
                        elements0.append(address4)
                        address5 = FAILURE
                        chunk2, max2 = None, self._offset + 1
                        if max2 <= self._input_size:
                            chunk2 = self._input[self._offset:max2]
                        if chunk2 == '}':
                            address5 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                            self._offset = self._offset + 1
                        else:
                            address5 = FAILURE
                            if self._offset > self._failure:
                                self._failure = self._offset
                                self._expected = []
                            if self._offset == self._failure:
                                self._expected.append('\'}\'')
                        if address5 is not FAILURE:
                            address6 = FAILURE
                            address6 = self._read__()
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
            address0 = self._actions.reduce(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['reduce'][index0] = (address0, self._offset)
        return address0

    def _read_modifier_call(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['modifier_call'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        chunk0, max0 = None, self._offset + 2
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == '->':
            address1 = TreeNode(self._input[self._offset:self._offset + 2], self._offset, [])
            self._offset = self._offset + 2
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'->\'')
        if address1 is not FAILURE:
            address2 = FAILURE
            address2 = self._read__()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                address3 = self._read_access()
                if address3 is not FAILURE:
                    elements0.append(address3)
                    address4 = FAILURE
                    address4 = self._read__()
                    if address4 is not FAILURE:
                        elements0.append(address4)
                        address5 = FAILURE
                        index2 = self._offset
                        address5 = self._read_modifier_args()
                        if address5 is FAILURE:
                            address5 = TreeNode(self._input[index2:index2], index2, [])
                            self._offset = index2
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
            address0 = self._actions.modifier_call(self._input, index1, self._offset, elements0)
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
                                elements2.append(address7)
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
                        address4 = TreeNode8(self._input[index3:self._offset], index3, elements2)
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

    def _read_accessor(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['accessor'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        index2, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read__ws()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            chunk0, max0 = None, self._offset + 1
            if max0 <= self._input_size:
                chunk0 = self._input[self._offset:max0]
            if chunk0 == '.':
                address2 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                self._offset = self._offset + 1
            else:
                address2 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('\'.\'')
            if address2 is not FAILURE:
                address3 = FAILURE
                address3 = self._read__()
                if address3 is not FAILURE:
                    elements0.append(address3)
                    address4 = FAILURE
                    address4 = self._read_basic_name()
                    if address4 is not FAILURE:
                        elements0.append(address4)
                        address5 = FAILURE
                        address5 = self._read__()
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
            address0 = TreeNode9(self._input[index2:self._offset], index2, elements0)
            self._offset = self._offset
        if address0 is FAILURE:
            self._offset = index1
            index3, elements1 = self._offset, []
            address6 = FAILURE
            index4 = self._offset
            index5, elements2 = self._offset, []
            address7 = FAILURE
            address7 = self._read__ws()
            if address7 is not FAILURE:
                elements2.append(address7)
                address8 = FAILURE
                chunk1, max1 = None, self._offset + 1
                if max1 <= self._input_size:
                    chunk1 = self._input[self._offset:max1]
                if chunk1 == '.':
                    address8 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                    self._offset = self._offset + 1
                else:
                    address8 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('\'.\'')
                if address8 is not FAILURE:
                    elements2.append(address8)
                else:
                    elements2 = None
                    self._offset = index5
            else:
                elements2 = None
                self._offset = index5
            if elements2 is None:
                address6 = FAILURE
            else:
                address6 = TreeNode11(self._input[index5:self._offset], index5, elements2)
                self._offset = self._offset
            if address6 is FAILURE:
                self._offset = index4
                address6 = self._read__()
                if address6 is FAILURE:
                    self._offset = index4
            if address6 is not FAILURE:
                address9 = FAILURE
                address9 = self._read_reduce()
                if address9 is not FAILURE:
                    elements1.append(address9)
                    address10 = FAILURE
                    address10 = self._read__()
                    if address10 is not FAILURE:
                        elements1.append(address10)
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
                address0 = TreeNode10(self._input[index3:self._offset], index3, elements1)
                self._offset = self._offset
            if address0 is FAILURE:
                self._offset = index1
        self._cache['accessor'][index0] = (address0, self._offset)
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
        address1 = self._read_reduce_expr()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            remaining0, index3, elements1, address3 = 1, self._offset, [], True
            while address3 is not FAILURE:
                address3 = self._read_accessor()
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
            address0 = self._actions.text(self._input, self._offset, self._offset + 1, [])
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
                address0 = self._actions.text(self._input, self._offset, self._offset + 2, [])
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
                    address0 = self._actions.text(self._input, self._offset, self._offset + 1, [])
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
                        address0 = self._actions.text(self._input, index2, self._offset, elements0)
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
            address0 = self._actions.text(self._input, self._offset, self._offset + 1, [])
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
                address0 = self._actions.text(self._input, self._offset, self._offset + 1, [])
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
            address0 = self._actions.text(self._input, self._offset, self._offset + 2, [])
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
                address0 = self._actions.text(self._input, self._offset, self._offset + 2, [])
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
                    address0 = self._actions.text(self._input, self._offset, self._offset + 2, [])
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
                        address0 = self._actions.text(self._input, self._offset, self._offset + 2, [])
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
                            address0 = self._actions.text(self._input, self._offset, self._offset + 1, [])
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
                                address0 = self._actions.text(self._input, self._offset, self._offset + 1, [])
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
                                        address2 = TreeNode13(self._input[index4:self._offset], index4, elements1)
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
                                    address0 = self._actions.text(self._input, index2, self._offset, elements0)
                                    self._offset = self._offset
                                if address0 is FAILURE:
                                    self._offset = index1
                                    chunk8, max8 = None, self._offset + 3
                                    if max8 <= self._input_size:
                                        chunk8 = self._input[self._offset:max8]
                                    if chunk8 == 'and':
                                        address0 = self._actions.text(self._input, self._offset, self._offset + 3, [])
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
                                        chunk9, max9 = None, self._offset + 2
                                        if max9 <= self._input_size:
                                            chunk9 = self._input[self._offset:max9]
                                        if chunk9 == 'or':
                                            address0 = self._actions.text(self._input, self._offset, self._offset + 2, [])
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
        self._cache['comp_op'][index0] = (address0, self._offset)
        return address0

    def _read_roll_op(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['roll_op'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        chunk0, max0 = None, self._offset + 1
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == '&':
            address0 = self._actions.text(self._input, self._offset, self._offset + 1, [])
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
            chunk1, max1 = None, self._offset + 1
            if max1 <= self._input_size:
                chunk1 = self._input[self._offset:max1]
            if chunk1 == '^':
                address0 = self._actions.text(self._input, self._offset, self._offset + 1, [])
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
        self._cache['roll_op'][index0] = (address0, self._offset)
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
                                if chunk6 == '^=':
                                    address0 = self._actions.text(self._input, self._offset, self._offset + 2, [])
                                    self._offset = self._offset + 2
                                else:
                                    address0 = FAILURE
                                    if self._offset > self._failure:
                                        self._failure = self._offset
                                        self._expected = []
                                    if self._offset == self._failure:
                                        self._expected.append('\'^=\'')
                                if address0 is FAILURE:
                                    self._offset = index1
                                    chunk7, max7 = None, self._offset + 2
                                    if max7 <= self._input_size:
                                        chunk7 = self._input[self._offset:max7]
                                    if chunk7 == '&=':
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
                                        chunk8, max8 = None, self._offset + 1
                                        if max8 <= self._input_size:
                                            chunk8 = self._input[self._offset:max8]
                                        if chunk8 == '=':
                                            address0 = self._actions.text(self._input, self._offset, self._offset + 1, [])
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
                                address7 = self._read_comparison()
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
                    address14 = self._read_comparison()
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
                address0 = self._read_comparison()
                if address0 is FAILURE:
                    self._offset = index1
        self._cache['use_if'][index0] = (address0, self._offset)
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
                address3 = self._read_roll_op()
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
        address1 = self._read_modify()
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
            index4, elements1 = self._offset, []
            address7 = FAILURE
            chunk1, max1 = None, self._offset + 1
            if max1 <= self._input_size:
                chunk1 = self._input[self._offset:max1]
            if chunk1 == '#':
                address7 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                self._offset = self._offset + 1
            else:
                address7 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('\'#\'')
            if address7 is not FAILURE:
                address8 = FAILURE
                address8 = self._read__()
                if address8 is not FAILURE:
                    elements1.append(address8)
                    address9 = FAILURE
                    address9 = self._read_modify()
                    if address9 is not FAILURE:
                        elements1.append(address9)
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
                address0 = self._actions.length(self._input, index4, self._offset, elements1)
                self._offset = self._offset
            if address0 is FAILURE:
                self._offset = index1
                address0 = self._read_modify()
                if address0 is FAILURE:
                    self._offset = index1
        self._cache['mult_math'][index0] = (address0, self._offset)
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
        address1 = self._read_dice()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read__()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                remaining0, index3, elements1, address4 = 1, self._offset, [], True
                while address4 is not FAILURE:
                    address4 = self._read_modifier_call()
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
        address0 = self._read_enlarge()
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
                    elements0.append(address1)
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
                    address0 = TreeNode23(self._input[index2:self._offset], index2, elements0)
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
                address2 = TreeNode24(self._input[index3:self._offset], index3, elements2)
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
        self._cache['modifier_params'][index0] = (address0, self._offset)
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
                        chunk1, max1 = None, self._offset + 4
                        if max1 <= self._input_size:
                            chunk1 = self._input[self._offset:max1]
                        if chunk1 == 'then':
                            address5 = TreeNode(self._input[self._offset:self._offset + 4], self._offset, [])
                            self._offset = self._offset + 4
                        else:
                            address5 = FAILURE
                            if self._offset > self._failure:
                                self._failure = self._offset
                                self._expected = []
                            if self._offset == self._failure:
                                self._expected.append('\'then\'')
                        if address5 is not FAILURE:
                            address6 = FAILURE
                            address6 = self._read__ws()
                            if address6 is not FAILURE:
                                elements0.append(address6)
                                address7 = FAILURE
                                address7 = self._read_statement()
                                if address7 is not FAILURE:
                                    elements0.append(address7)
                                    address8 = FAILURE
                                    address8 = self._read__()
                                    if address8 is not FAILURE:
                                        elements0.append(address8)
                                        address9 = FAILURE
                                        remaining0, index2, elements1, address10 = 0, self._offset, [], True
                                        while address10 is not FAILURE:
                                            address10 = self._read_eos()
                                            if address10 is not FAILURE:
                                                elements1.append(address10)
                                                remaining0 -= 1
                                        if remaining0 <= 0:
                                            address9 = TreeNode(self._input[index2:self._offset], index2, elements1)
                                            self._offset = self._offset
                                        else:
                                            address9 = FAILURE
                                        if address9 is not FAILURE:
                                            elements0.append(address9)
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
            address0 = self._actions.predicated_statement(self._input, index1, self._offset, elements0)
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
                        chunk1, max1 = None, self._offset + 4
                        if max1 <= self._input_size:
                            chunk1 = self._input[self._offset:max1]
                        if chunk1 == 'then':
                            address5 = TreeNode(self._input[self._offset:self._offset + 4], self._offset, [])
                            self._offset = self._offset + 4
                        else:
                            address5 = FAILURE
                            if self._offset > self._failure:
                                self._failure = self._offset
                                self._expected = []
                            if self._offset == self._failure:
                                self._expected.append('\'then\'')
                        if address5 is not FAILURE:
                            address6 = FAILURE
                            address6 = self._read__ws()
                            if address6 is not FAILURE:
                                elements0.append(address6)
                                address7 = FAILURE
                                address7 = self._read_statement()
                                if address7 is not FAILURE:
                                    elements0.append(address7)
                                    address8 = FAILURE
                                    address8 = self._read__()
                                    if address8 is not FAILURE:
                                        elements0.append(address8)
                                        address9 = FAILURE
                                        remaining0, index2, elements1, address10 = 0, self._offset, [], True
                                        while address10 is not FAILURE:
                                            address10 = self._read_eos()
                                            if address10 is not FAILURE:
                                                elements1.append(address10)
                                                remaining0 -= 1
                                        if remaining0 <= 0:
                                            address9 = TreeNode(self._input[index2:self._offset], index2, elements1)
                                            self._offset = self._offset
                                        else:
                                            address9 = FAILURE
                                        if address9 is not FAILURE:
                                            elements0.append(address9)
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
            address0 = self._actions.predicated_statement(self._input, index1, self._offset, elements0)
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
                        elements2.append(address5)
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
                address2 = TreeNode28(self._input[index3:self._offset], index3, elements2)
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
                        elements2.append(address5)
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
                address2 = TreeNode29(self._input[index3:self._offset], index3, elements2)
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
            address0 = TreeNode30(self._input[index1:self._offset], index1, elements0)
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
                address3 = self._read_basic_load_list()
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
            address0 = TreeNode31(self._input[index1:self._offset], index1, elements0)
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
                    chunk3, max3 = None, self._offset + 1
                    if max3 <= self._input_size:
                        chunk3 = self._input[self._offset:max3]
                    if chunk3 == '!':
                        address10 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                        self._offset = self._offset + 1
                    else:
                        address10 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('\'!\'')
                    if address10 is not FAILURE:
                        address11 = FAILURE
                        address11 = self._read__()
                        if address11 is not FAILURE:
                            elements1.append(address11)
                            address12 = FAILURE
                            chunk4, max4 = None, self._offset + 4
                            if max4 <= self._input_size:
                                chunk4 = self._input[self._offset:max4]
                            if chunk4 == 'into':
                                address12 = TreeNode(self._input[self._offset:self._offset + 4], self._offset, [])
                                self._offset = self._offset + 4
                            else:
                                address12 = FAILURE
                                if self._offset > self._failure:
                                    self._failure = self._offset
                                    self._expected = []
                                if self._offset == self._failure:
                                    self._expected.append('\'into\'')
                            if address12 is not FAILURE:
                                address13 = FAILURE
                                address13 = self._read__()
                                if address13 is not FAILURE:
                                    elements1.append(address13)
                                    address14 = FAILURE
                                    address14 = self._read_access_load_list()
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
                address0 = self._actions.create_bag(self._input, index4, self._offset, elements1)
                self._offset = self._offset
            if address0 is FAILURE:
                self._offset = index1
                index5, elements2 = self._offset, []
                address15 = FAILURE
                chunk5, max5 = None, self._offset + 4
                if max5 <= self._input_size:
                    chunk5 = self._input[self._offset:max5]
                if chunk5 == 'load':
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
                        address17 = self._read_basic_load_list()
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
                                    address20 = FAILURE
                                    address20 = self._read__()
                                    if address20 is not FAILURE:
                                        elements2.append(address20)
                                        address21 = FAILURE
                                        address21 = self._read_load_into()
                                        if address21 is not FAILURE:
                                            elements2.append(address21)
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
                    else:
                        elements2 = None
                        self._offset = index5
                else:
                    elements2 = None
                    self._offset = index5
                if elements2 is None:
                    address0 = FAILURE
                else:
                    address0 = self._actions.load_from_into(self._input, index5, self._offset, elements2)
                    self._offset = self._offset
                if address0 is FAILURE:
                    self._offset = index1
                    index6, elements3 = self._offset, []
                    address22 = FAILURE
                    chunk6, max6 = None, self._offset + 4
                    if max6 <= self._input_size:
                        chunk6 = self._input[self._offset:max6]
                    if chunk6 == 'load':
                        address22 = TreeNode(self._input[self._offset:self._offset + 4], self._offset, [])
                        self._offset = self._offset + 4
                    else:
                        address22 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('\'load\'')
                    if address22 is not FAILURE:
                        address23 = FAILURE
                        address23 = self._read__()
                        if address23 is not FAILURE:
                            elements3.append(address23)
                            address24 = FAILURE
                            address24 = self._read_basic_load_list()
                            if address24 is not FAILURE:
                                elements3.append(address24)
                                address25 = FAILURE
                                address25 = self._read__()
                                if address25 is not FAILURE:
                                    elements3.append(address25)
                                    address26 = FAILURE
                                    address26 = self._read_load_from()
                                    if address26 is not FAILURE:
                                        elements3.append(address26)
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
                        address0 = self._actions.load_from(self._input, index6, self._offset, elements3)
                        self._offset = self._offset
                    if address0 is FAILURE:
                        self._offset = index1
                        index7, elements4 = self._offset, []
                        address27 = FAILURE
                        chunk7, max7 = None, self._offset + 4
                        if max7 <= self._input_size:
                            chunk7 = self._input[self._offset:max7]
                        if chunk7 == 'load':
                            address27 = TreeNode(self._input[self._offset:self._offset + 4], self._offset, [])
                            self._offset = self._offset + 4
                        else:
                            address27 = FAILURE
                            if self._offset > self._failure:
                                self._failure = self._offset
                                self._expected = []
                            if self._offset == self._failure:
                                self._expected.append('\'load\'')
                        if address27 is not FAILURE:
                            address28 = FAILURE
                            address28 = self._read__()
                            if address28 is not FAILURE:
                                elements4.append(address28)
                                address29 = FAILURE
                                address29 = self._read_basic_load_list()
                                if address29 is not FAILURE:
                                    elements4.append(address29)
                                    address30 = FAILURE
                                    address30 = self._read__()
                                    if address30 is not FAILURE:
                                        elements4.append(address30)
                                        address31 = FAILURE
                                        address31 = self._read_load_into()
                                        if address31 is not FAILURE:
                                            elements4.append(address31)
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
                            address0 = self._actions.load_into(self._input, index7, self._offset, elements4)
                            self._offset = self._offset
                        if address0 is FAILURE:
                            self._offset = index1
                            index8, elements5 = self._offset, []
                            address32 = FAILURE
                            chunk8, max8 = None, self._offset + 4
                            if max8 <= self._input_size:
                                chunk8 = self._input[self._offset:max8]
                            if chunk8 == 'load':
                                address32 = TreeNode(self._input[self._offset:self._offset + 4], self._offset, [])
                                self._offset = self._offset + 4
                            else:
                                address32 = FAILURE
                                if self._offset > self._failure:
                                    self._failure = self._offset
                                    self._expected = []
                                if self._offset == self._failure:
                                    self._expected.append('\'load\'')
                            if address32 is not FAILURE:
                                address33 = FAILURE
                                address33 = self._read__()
                                if address33 is not FAILURE:
                                    elements5.append(address33)
                                    address34 = FAILURE
                                    address34 = self._read_basic_load_list()
                                    if address34 is not FAILURE:
                                        elements5.append(address34)
                                    else:
                                        elements5 = None
                                        self._offset = index8
                                else:
                                    elements5 = None
                                    self._offset = index8
                            else:
                                elements5 = None
                                self._offset = index8
                            if elements5 is None:
                                address0 = FAILURE
                            else:
                                address0 = self._actions.load(self._input, index8, self._offset, elements5)
                                self._offset = self._offset
                            if address0 is FAILURE:
                                self._offset = index1
        self._cache['load'][index0] = (address0, self._offset)
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
                                chunk2, max2 = None, self._offset + 4
                                if max2 <= self._input_size:
                                    chunk2 = self._input[self._offset:max2]
                                if chunk2 == 'then':
                                    address7 = TreeNode(self._input[self._offset:self._offset + 4], self._offset, [])
                                    self._offset = self._offset + 4
                                else:
                                    address7 = FAILURE
                                    if self._offset > self._failure:
                                        self._failure = self._offset
                                        self._expected = []
                                    if self._offset == self._failure:
                                        self._expected.append('\'then\'')
                                if address7 is not FAILURE:
                                    address8 = FAILURE
                                    address8 = self._read__ws()
                                    if address8 is not FAILURE:
                                        elements0.append(address8)
                                        address9 = FAILURE
                                        address9 = self._read_stmt_or_expr()
                                        if address9 is not FAILURE:
                                            elements0.append(address9)
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
            address0 = self._actions.predicated_statement(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['except_when'][index0] = (address0, self._offset)
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

    def _read_block_stmt(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['block_stmt'].get(index0)
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
                address2 = TreeNode45(self._input[index3:self._offset], index3, elements2)
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
                index5 = self._offset
                index6, elements3 = self._offset, []
                address8 = FAILURE
                address8 = self._read_expression()
                if address8 is not FAILURE:
                    elements3.append(address8)
                    address9 = FAILURE
                    address9 = self._read__()
                    if address9 is not FAILURE:
                        elements3.append(address9)
                        address10 = FAILURE
                        index7 = self._offset
                        chunk1, max1 = None, self._offset + 1
                        if max1 <= self._input_size:
                            chunk1 = self._input[self._offset:max1]
                        if chunk1 == ']':
                            address10 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                            self._offset = self._offset + 1
                        else:
                            address10 = FAILURE
                            if self._offset > self._failure:
                                self._failure = self._offset
                                self._expected = []
                            if self._offset == self._failure:
                                self._expected.append('\']\'')
                        self._offset = index7
                        if address10 is not FAILURE:
                            address10 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                            self._offset = self._offset
                        else:
                            address10 = FAILURE
                        if address10 is not FAILURE:
                            elements3.append(address10)
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
                    address7 = FAILURE
                else:
                    address7 = TreeNode46(self._input[index6:self._offset], index6, elements3)
                    self._offset = self._offset
                if address7 is FAILURE:
                    self._offset = index5
                    address7 = self._read_statement()
                    if address7 is FAILURE:
                        self._offset = index5
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
            address0 = TreeNode44(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        self._cache['block_stmt'][index0] = (address0, self._offset)
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
                index2, elements0 = self._offset, []
                address1 = FAILURE
                chunk1, max1 = None, self._offset + 7
                if max1 <= self._input_size:
                    chunk1 = self._input[self._offset:max1]
                if chunk1 == 'restart':
                    address1 = TreeNode(self._input[self._offset:self._offset + 7], self._offset, [])
                    self._offset = self._offset + 7
                else:
                    address1 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('\'restart\'')
                if address1 is not FAILURE:
                    address2 = FAILURE
                    address2 = self._read__()
                    if address2 is not FAILURE:
                        elements0.append(address2)
                        address3 = FAILURE
                        address3 = self._read_restart_pos()
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
                    address0 = TreeNode47(self._input[index2:self._offset], index2, elements0)
                    self._offset = self._offset
                if address0 is FAILURE:
                    self._offset = index1
                    index3, elements1 = self._offset, []
                    address4 = FAILURE
                    chunk2, max2 = None, self._offset + 1
                    if max2 <= self._input_size:
                        chunk2 = self._input[self._offset:max2]
                    if chunk2 == '[':
                        address4 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                        self._offset = self._offset + 1
                    else:
                        address4 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('\'[\'')
                    if address4 is not FAILURE:
                        address5 = FAILURE
                        address5 = self._read__ws()
                        if address5 is not FAILURE:
                            elements1.append(address5)
                            address6 = FAILURE
                            address6 = self._read_block_stmt()
                            if address6 is not FAILURE:
                                elements1.append(address6)
                                address7 = FAILURE
                                address7 = self._read__ws()
                                if address7 is not FAILURE:
                                    elements1.append(address7)
                                    address8 = FAILURE
                                    chunk3, max3 = None, self._offset + 1
                                    if max3 <= self._input_size:
                                        chunk3 = self._input[self._offset:max3]
                                    if chunk3 == ']':
                                        address8 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                        self._offset = self._offset + 1
                                    else:
                                        address8 = FAILURE
                                        if self._offset > self._failure:
                                            self._failure = self._offset
                                            self._expected = []
                                        if self._offset == self._failure:
                                            self._expected.append('\']\'')
                                    if address8 is not FAILURE:
                                        address9 = FAILURE
                                        address9 = self._read__()
                                        if address9 is not FAILURE:
                                            elements1.append(address9)
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
                        address0 = self._actions.block(self._input, index3, self._offset, elements1)
                        self._offset = self._offset
                    if address0 is FAILURE:
                        self._offset = index1
                        index4, elements2 = self._offset, []
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
                            address11 = self._read__ws()
                            if address11 is not FAILURE:
                                elements2.append(address11)
                                address12 = FAILURE
                                chunk5, max5 = None, self._offset + 1
                                if max5 <= self._input_size:
                                    chunk5 = self._input[self._offset:max5]
                                if chunk5 == ']':
                                    address12 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                    self._offset = self._offset + 1
                                else:
                                    address12 = FAILURE
                                    if self._offset > self._failure:
                                        self._failure = self._offset
                                        self._expected = []
                                    if self._offset == self._failure:
                                        self._expected.append('\']\'')
                                if address12 is not FAILURE:
                                    address13 = FAILURE
                                    address13 = self._read__()
                                    if address13 is not FAILURE:
                                        elements2.append(address13)
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
                            address0 = self._actions.empty_block(self._input, index4, self._offset, elements2)
                            self._offset = self._offset
                        if address0 is FAILURE:
                            self._offset = index1
                            address0 = self._read_load()
                            if address0 is FAILURE:
                                self._offset = index1
                                index5, elements3 = self._offset, []
                                address14 = FAILURE
                                address14 = self._read_if_then()
                                if address14 is not FAILURE:
                                    elements3.append(address14)
                                    address15 = FAILURE
                                    remaining0, index6, elements4, address16 = 0, self._offset, [], True
                                    while address16 is not FAILURE:
                                        index7, elements5 = self._offset, []
                                        address17 = FAILURE
                                        address17 = self._read__ws()
                                        if address17 is not FAILURE:
                                            elements5.append(address17)
                                            address18 = FAILURE
                                            address18 = self._read_unless()
                                            if address18 is not FAILURE:
                                                elements5.append(address18)
                                            else:
                                                elements5 = None
                                                self._offset = index7
                                        else:
                                            elements5 = None
                                            self._offset = index7
                                        if elements5 is None:
                                            address16 = FAILURE
                                        else:
                                            address16 = TreeNode51(self._input[index7:self._offset], index7, elements5)
                                            self._offset = self._offset
                                        if address16 is not FAILURE:
                                            elements4.append(address16)
                                            remaining0 -= 1
                                    if remaining0 <= 0:
                                        address15 = TreeNode(self._input[index6:self._offset], index6, elements4)
                                        self._offset = self._offset
                                    else:
                                        address15 = FAILURE
                                    if address15 is not FAILURE:
                                        elements3.append(address15)
                                        address19 = FAILURE
                                        index8 = self._offset
                                        index9, elements6 = self._offset, []
                                        address20 = FAILURE
                                        address20 = self._read__ws()
                                        if address20 is not FAILURE:
                                            elements6.append(address20)
                                            address21 = FAILURE
                                            address21 = self._read_otherwise()
                                            if address21 is not FAILURE:
                                                elements6.append(address21)
                                            else:
                                                elements6 = None
                                                self._offset = index9
                                        else:
                                            elements6 = None
                                            self._offset = index9
                                        if elements6 is None:
                                            address19 = FAILURE
                                        else:
                                            address19 = TreeNode52(self._input[index9:self._offset], index9, elements6)
                                            self._offset = self._offset
                                        if address19 is FAILURE:
                                            address19 = TreeNode(self._input[index8:index8], index8, [])
                                            self._offset = index8
                                        if address19 is not FAILURE:
                                            elements3.append(address19)
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
                                    address0 = self._actions.if_stmt(self._input, index5, self._offset, elements3)
                                    self._offset = self._offset
                                if address0 is FAILURE:
                                    self._offset = index1
                                    index10, elements7 = self._offset, []
                                    address22 = FAILURE
                                    chunk6, max6 = None, self._offset + 3
                                    if max6 <= self._input_size:
                                        chunk6 = self._input[self._offset:max6]
                                    if chunk6 == 'for':
                                        address22 = TreeNode(self._input[self._offset:self._offset + 3], self._offset, [])
                                        self._offset = self._offset + 3
                                    else:
                                        address22 = FAILURE
                                        if self._offset > self._failure:
                                            self._failure = self._offset
                                            self._expected = []
                                        if self._offset == self._failure:
                                            self._expected.append('\'for\'')
                                    if address22 is not FAILURE:
                                        address23 = FAILURE
                                        address23 = self._read__()
                                        if address23 is not FAILURE:
                                            elements7.append(address23)
                                            address24 = FAILURE
                                            chunk7, max7 = None, self._offset + 5
                                            if max7 <= self._input_size:
                                                chunk7 = self._input[self._offset:max7]
                                            if chunk7 == 'every':
                                                address24 = TreeNode(self._input[self._offset:self._offset + 5], self._offset, [])
                                                self._offset = self._offset + 5
                                            else:
                                                address24 = FAILURE
                                                if self._offset > self._failure:
                                                    self._failure = self._offset
                                                    self._expected = []
                                                if self._offset == self._failure:
                                                    self._expected.append('\'every\'')
                                            if address24 is not FAILURE:
                                                address25 = FAILURE
                                                address25 = self._read__()
                                                if address25 is not FAILURE:
                                                    elements7.append(address25)
                                                    address26 = FAILURE
                                                    index11 = self._offset
                                                    address26 = self._read_loop_name()
                                                    if address26 is FAILURE:
                                                        address26 = TreeNode(self._input[index11:index11], index11, [])
                                                        self._offset = index11
                                                    if address26 is not FAILURE:
                                                        elements7.append(address26)
                                                        address27 = FAILURE
                                                        address27 = self._read__()
                                                        if address27 is not FAILURE:
                                                            elements7.append(address27)
                                                            address28 = FAILURE
                                                            address28 = self._read_basic_name()
                                                            if address28 is not FAILURE:
                                                                elements7.append(address28)
                                                                address29 = FAILURE
                                                                address29 = self._read__()
                                                                if address29 is not FAILURE:
                                                                    elements7.append(address29)
                                                                    address30 = FAILURE
                                                                    chunk8, max8 = None, self._offset + 4
                                                                    if max8 <= self._input_size:
                                                                        chunk8 = self._input[self._offset:max8]
                                                                    if chunk8 == 'that':
                                                                        address30 = TreeNode(self._input[self._offset:self._offset + 4], self._offset, [])
                                                                        self._offset = self._offset + 4
                                                                    else:
                                                                        address30 = FAILURE
                                                                        if self._offset > self._failure:
                                                                            self._failure = self._offset
                                                                            self._expected = []
                                                                        if self._offset == self._failure:
                                                                            self._expected.append('\'that\'')
                                                                    if address30 is not FAILURE:
                                                                        address31 = FAILURE
                                                                        address31 = self._read__()
                                                                        if address31 is not FAILURE:
                                                                            elements7.append(address31)
                                                                            address32 = FAILURE
                                                                            address32 = self._read_expression()
                                                                            if address32 is not FAILURE:
                                                                                elements7.append(address32)
                                                                                address33 = FAILURE
                                                                                address33 = self._read__()
                                                                                if address33 is not FAILURE:
                                                                                    elements7.append(address33)
                                                                                    address34 = FAILURE
                                                                                    chunk9, max9 = None, self._offset + 3
                                                                                    if max9 <= self._input_size:
                                                                                        chunk9 = self._input[self._offset:max9]
                                                                                    if chunk9 == 'has':
                                                                                        address34 = TreeNode(self._input[self._offset:self._offset + 3], self._offset, [])
                                                                                        self._offset = self._offset + 3
                                                                                    else:
                                                                                        address34 = FAILURE
                                                                                        if self._offset > self._failure:
                                                                                            self._failure = self._offset
                                                                                            self._expected = []
                                                                                        if self._offset == self._failure:
                                                                                            self._expected.append('\'has\'')
                                                                                    if address34 is not FAILURE:
                                                                                        address35 = FAILURE
                                                                                        address35 = self._read__()
                                                                                        if address35 is not FAILURE:
                                                                                            elements7.append(address35)
                                                                                            address36 = FAILURE
                                                                                            address36 = self._read_loop_body()
                                                                                            if address36 is not FAILURE:
                                                                                                elements7.append(address36)
                                                                                            else:
                                                                                                elements7 = None
                                                                                                self._offset = index10
                                                                                        else:
                                                                                            elements7 = None
                                                                                            self._offset = index10
                                                                                    else:
                                                                                        elements7 = None
                                                                                        self._offset = index10
                                                                                else:
                                                                                    elements7 = None
                                                                                    self._offset = index10
                                                                            else:
                                                                                elements7 = None
                                                                                self._offset = index10
                                                                        else:
                                                                            elements7 = None
                                                                            self._offset = index10
                                                                    else:
                                                                        elements7 = None
                                                                        self._offset = index10
                                                                else:
                                                                    elements7 = None
                                                                    self._offset = index10
                                                            else:
                                                                elements7 = None
                                                                self._offset = index10
                                                        else:
                                                            elements7 = None
                                                            self._offset = index10
                                                    else:
                                                        elements7 = None
                                                        self._offset = index10
                                                else:
                                                    elements7 = None
                                                    self._offset = index10
                                            else:
                                                elements7 = None
                                                self._offset = index10
                                        else:
                                            elements7 = None
                                            self._offset = index10
                                    else:
                                        elements7 = None
                                        self._offset = index10
                                    if elements7 is None:
                                        address0 = FAILURE
                                    else:
                                        address0 = self._actions.for_every(self._input, index10, self._offset, elements7)
                                        self._offset = self._offset
                                    if address0 is FAILURE:
                                        self._offset = index1
                                        index12, elements8 = self._offset, []
                                        address37 = FAILURE
                                        chunk10, max10 = None, self._offset + 5
                                        if max10 <= self._input_size:
                                            chunk10 = self._input[self._offset:max10]
                                        if chunk10 == 'until':
                                            address37 = TreeNode(self._input[self._offset:self._offset + 5], self._offset, [])
                                            self._offset = self._offset + 5
                                        else:
                                            address37 = FAILURE
                                            if self._offset > self._failure:
                                                self._failure = self._offset
                                                self._expected = []
                                            if self._offset == self._failure:
                                                self._expected.append('\'until\'')
                                        if address37 is not FAILURE:
                                            address38 = FAILURE
                                            address38 = self._read__()
                                            if address38 is not FAILURE:
                                                elements8.append(address38)
                                                address39 = FAILURE
                                                index13 = self._offset
                                                address39 = self._read_loop_name()
                                                if address39 is FAILURE:
                                                    address39 = TreeNode(self._input[index13:index13], index13, [])
                                                    self._offset = index13
                                                if address39 is not FAILURE:
                                                    elements8.append(address39)
                                                    address40 = FAILURE
                                                    address40 = self._read__()
                                                    if address40 is not FAILURE:
                                                        elements8.append(address40)
                                                        address41 = FAILURE
                                                        address41 = self._read_expression()
                                                        if address41 is not FAILURE:
                                                            elements8.append(address41)
                                                            address42 = FAILURE
                                                            address42 = self._read__()
                                                            if address42 is not FAILURE:
                                                                elements8.append(address42)
                                                                address43 = FAILURE
                                                                address43 = self._read_loop_body()
                                                                if address43 is not FAILURE:
                                                                    elements8.append(address43)
                                                                    address44 = FAILURE
                                                                    address44 = self._read__ws()
                                                                    if address44 is not FAILURE:
                                                                        elements8.append(address44)
                                                                        address45 = FAILURE
                                                                        remaining1, index14, elements9, address46 = 0, self._offset, [], True
                                                                        while address46 is not FAILURE:
                                                                            index15, elements10 = self._offset, []
                                                                            address47 = FAILURE
                                                                            address47 = self._read_except_when()
                                                                            if address47 is not FAILURE:
                                                                                elements10.append(address47)
                                                                                address48 = FAILURE
                                                                                address48 = self._read__ws()
                                                                                if address48 is not FAILURE:
                                                                                    elements10.append(address48)
                                                                                else:
                                                                                    elements10 = None
                                                                                    self._offset = index15
                                                                            else:
                                                                                elements10 = None
                                                                                self._offset = index15
                                                                            if elements10 is None:
                                                                                address46 = FAILURE
                                                                            else:
                                                                                address46 = TreeNode55(self._input[index15:self._offset], index15, elements10)
                                                                                self._offset = self._offset
                                                                            if address46 is not FAILURE:
                                                                                elements9.append(address46)
                                                                                remaining1 -= 1
                                                                        if remaining1 <= 0:
                                                                            address45 = TreeNode(self._input[index14:self._offset], index14, elements9)
                                                                            self._offset = self._offset
                                                                        else:
                                                                            address45 = FAILURE
                                                                        if address45 is not FAILURE:
                                                                            elements8.append(address45)
                                                                            address49 = FAILURE
                                                                            index16 = self._offset
                                                                            address49 = self._read_otherwise()
                                                                            if address49 is FAILURE:
                                                                                address49 = TreeNode(self._input[index16:index16], index16, [])
                                                                                self._offset = index16
                                                                            if address49 is not FAILURE:
                                                                                elements8.append(address49)
                                                                            else:
                                                                                elements8 = None
                                                                                self._offset = index12
                                                                        else:
                                                                            elements8 = None
                                                                            self._offset = index12
                                                                    else:
                                                                        elements8 = None
                                                                        self._offset = index12
                                                                else:
                                                                    elements8 = None
                                                                    self._offset = index12
                                                            else:
                                                                elements8 = None
                                                                self._offset = index12
                                                        else:
                                                            elements8 = None
                                                            self._offset = index12
                                                    else:
                                                        elements8 = None
                                                        self._offset = index12
                                                else:
                                                    elements8 = None
                                                    self._offset = index12
                                            else:
                                                elements8 = None
                                                self._offset = index12
                                        else:
                                            elements8 = None
                                            self._offset = index12
                                        if elements8 is None:
                                            address0 = FAILURE
                                        else:
                                            address0 = self._actions.until_do(self._input, index12, self._offset, elements8)
                                            self._offset = self._offset
                                        if address0 is FAILURE:
                                            self._offset = index1
                                            index17, elements11 = self._offset, []
                                            address50 = FAILURE
                                            address50 = self._read_access()
                                            if address50 is not FAILURE:
                                                elements11.append(address50)
                                                address51 = FAILURE
                                                address51 = self._read__()
                                                if address51 is not FAILURE:
                                                    elements11.append(address51)
                                                    address52 = FAILURE
                                                    address52 = self._read_assign_op()
                                                    if address52 is not FAILURE:
                                                        elements11.append(address52)
                                                        address53 = FAILURE
                                                        address53 = self._read__ws()
                                                        if address53 is not FAILURE:
                                                            elements11.append(address53)
                                                            address54 = FAILURE
                                                            address54 = self._read_expression()
                                                            if address54 is not FAILURE:
                                                                elements11.append(address54)
                                                            else:
                                                                elements11 = None
                                                                self._offset = index17
                                                        else:
                                                            elements11 = None
                                                            self._offset = index17
                                                    else:
                                                        elements11 = None
                                                        self._offset = index17
                                                else:
                                                    elements11 = None
                                                    self._offset = index17
                                            else:
                                                elements11 = None
                                                self._offset = index17
                                            if elements11 is None:
                                                address0 = FAILURE
                                            else:
                                                address0 = self._actions.assignment(self._input, index17, self._offset, elements11)
                                                self._offset = self._offset
                                            if address0 is FAILURE:
                                                self._offset = index1
                                                index18, elements12 = self._offset, []
                                                address55 = FAILURE
                                                address55 = self._read_access()
                                                if address55 is not FAILURE:
                                                    elements12.append(address55)
                                                    address56 = FAILURE
                                                    address56 = self._read__()
                                                    if address56 is not FAILURE:
                                                        elements12.append(address56)
                                                        address57 = FAILURE
                                                        chunk11, max11 = None, self._offset + 2
                                                        if max11 <= self._input_size:
                                                            chunk11 = self._input[self._offset:max11]
                                                        if chunk11 == '<-':
                                                            address57 = TreeNode(self._input[self._offset:self._offset + 2], self._offset, [])
                                                            self._offset = self._offset + 2
                                                        else:
                                                            address57 = FAILURE
                                                            if self._offset > self._failure:
                                                                self._failure = self._offset
                                                                self._expected = []
                                                            if self._offset == self._failure:
                                                                self._expected.append('\'<-\'')
                                                        if address57 is not FAILURE:
                                                            address58 = FAILURE
                                                            address58 = self._read__()
                                                            if address58 is not FAILURE:
                                                                elements12.append(address58)
                                                                address59 = FAILURE
                                                                address59 = self._read_modifier_params()
                                                                if address59 is not FAILURE:
                                                                    elements12.append(address59)
                                                                    address60 = FAILURE
                                                                    address60 = self._read__ws()
                                                                    if address60 is not FAILURE:
                                                                        elements12.append(address60)
                                                                        address61 = FAILURE
                                                                        index19 = self._offset
                                                                        chunk12, max12 = None, self._offset + 1
                                                                        if max12 <= self._input_size:
                                                                            chunk12 = self._input[self._offset:max12]
                                                                        if chunk12 == ':':
                                                                            address61 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                                                            self._offset = self._offset + 1
                                                                        else:
                                                                            address61 = FAILURE
                                                                            if self._offset > self._failure:
                                                                                self._failure = self._offset
                                                                                self._expected = []
                                                                            if self._offset == self._failure:
                                                                                self._expected.append('\':\'')
                                                                        if address61 is FAILURE:
                                                                            self._offset = index19
                                                                            index20, elements13 = self._offset, []
                                                                            address62 = FAILURE
                                                                            index21 = self._offset
                                                                            chunk13, max13 = None, self._offset + 1
                                                                            if max13 <= self._input_size:
                                                                                chunk13 = self._input[self._offset:max13]
                                                                            if chunk13 == ':':
                                                                                address62 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                                                                self._offset = self._offset + 1
                                                                            else:
                                                                                address62 = FAILURE
                                                                                if self._offset > self._failure:
                                                                                    self._failure = self._offset
                                                                                    self._expected = []
                                                                                if self._offset == self._failure:
                                                                                    self._expected.append('\':\'')
                                                                            if address62 is FAILURE:
                                                                                address62 = TreeNode(self._input[index21:index21], index21, [])
                                                                                self._offset = index21
                                                                            if address62 is not FAILURE:
                                                                                elements13.append(address62)
                                                                                address63 = FAILURE
                                                                                index22 = self._offset
                                                                                chunk14, max14 = None, self._offset + 1
                                                                                if max14 <= self._input_size:
                                                                                    chunk14 = self._input[self._offset:max14]
                                                                                if chunk14 == '[':
                                                                                    address63 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                                                                    self._offset = self._offset + 1
                                                                                else:
                                                                                    address63 = FAILURE
                                                                                    if self._offset > self._failure:
                                                                                        self._failure = self._offset
                                                                                        self._expected = []
                                                                                    if self._offset == self._failure:
                                                                                        self._expected.append('\'[\'')
                                                                                self._offset = index22
                                                                                if address63 is not FAILURE:
                                                                                    address63 = TreeNode(self._input[self._offset:self._offset], self._offset, [])
                                                                                    self._offset = self._offset
                                                                                else:
                                                                                    address63 = FAILURE
                                                                                if address63 is not FAILURE:
                                                                                    elements13.append(address63)
                                                                                else:
                                                                                    elements13 = None
                                                                                    self._offset = index20
                                                                            else:
                                                                                elements13 = None
                                                                                self._offset = index20
                                                                            if elements13 is None:
                                                                                address61 = FAILURE
                                                                            else:
                                                                                address61 = TreeNode(self._input[index20:self._offset], index20, elements13)
                                                                                self._offset = self._offset
                                                                            if address61 is FAILURE:
                                                                                self._offset = index19
                                                                        if address61 is not FAILURE:
                                                                            address64 = FAILURE
                                                                            address64 = self._read__()
                                                                            if address64 is not FAILURE:
                                                                                elements12.append(address64)
                                                                                address65 = FAILURE
                                                                                address65 = self._read_stmt_or_expr()
                                                                                if address65 is not FAILURE:
                                                                                    elements12.append(address65)
                                                                                else:
                                                                                    elements12 = None
                                                                                    self._offset = index18
                                                                            else:
                                                                                elements12 = None
                                                                                self._offset = index18
                                                                        else:
                                                                            elements12 = None
                                                                            self._offset = index18
                                                                    else:
                                                                        elements12 = None
                                                                        self._offset = index18
                                                                else:
                                                                    elements12 = None
                                                                    self._offset = index18
                                                            else:
                                                                elements12 = None
                                                                self._offset = index18
                                                        else:
                                                            elements12 = None
                                                            self._offset = index18
                                                    else:
                                                        elements12 = None
                                                        self._offset = index18
                                                else:
                                                    elements12 = None
                                                    self._offset = index18
                                                if elements12 is None:
                                                    address0 = FAILURE
                                                else:
                                                    address0 = self._actions.modifier_def(self._input, index18, self._offset, elements12)
                                                    self._offset = self._offset
                                                if address0 is FAILURE:
                                                    self._offset = index1
                                                    index23, elements14 = self._offset, []
                                                    address66 = FAILURE
                                                    address66 = self._read_expression()
                                                    if address66 is not FAILURE:
                                                        elements14.append(address66)
                                                        address67 = FAILURE
                                                        address67 = self._read__()
                                                        if address67 is not FAILURE:
                                                            elements14.append(address67)
                                                            address68 = FAILURE
                                                            address68 = self._read_eos()
                                                            if address68 is not FAILURE:
                                                                elements14.append(address68)
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
                                                        address0 = TreeNode58(self._input[index23:self._offset], index23, elements14)
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
