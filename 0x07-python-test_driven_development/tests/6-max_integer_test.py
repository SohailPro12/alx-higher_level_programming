#!/usr/bin/python3
"""Unittest for the method of  max_integer([..])
"""
import unittest
m_i = __import__('6-max_integer').max_integer


class Test_Max_Integer(unittest.TestCase):
    """max_integer([..]) tests are here"""
    
    def test_no_arg(self):
        """No argumnts tests"""
        self.assertEqual(max_integer(), None)

    def test_empty_list(self):
        """empty aregument test"""
        self.assertEqual(max_integer([]), None)

    def test_one(self):
        """one arg max"""
        self.assertEqual(max_integer([98]), 98)

    def test_identical(self):
        """Identical args"""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_max_start(self):
        """diffrent args"""
        self.assertEqual(max_integer([5, 4, 3, 2]), 5)

    def test_ordered(self):
        """Ordered args"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_ordered_larger(self):
        """ordered plus 2"""
        self.assertEqual(max_integer([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]), 20)

    def test_unordered(self):
        """unordered args"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_unordered_larger(self):
        """Unordered plus 2"""
        self.assertEqual(max_integer([23, 58, 91, 24, 1024, 89, 98,
                                     108, 256, 512]), 1024)

    def test_positives_and_negatives(self):
        """positve and negativs"""
        self.assertEqual(
            max_integer([-23, 58, 91, 24, -1024, 89, 98, 108, -256, -512]),
            108)

    def test_positives_and_negatives_large(self):
        """positive and negative plus"""
        self.assertEqual(
            max_integer(
                [-6351, 9735, -8649, 4405, 6261, -1907, -9443, -6308,
                    7474, -2513, 5721, 2319, 74, 7946, -5544, 7693, -7013,
                    29, 3596, 1108, 6702, 4873, -9452, -5949, -9640, -2156,
                    -4104, 5772, 5121, -2186, -4870, -4116, 6443, -9381,
                    -9388, 8552, 3582, 3500, 7924, 211, -2976, 6346, -5405,
                    899, -3432, -2550, -3353, 6944, 96230]), 96230)

    def test_negatives(self):
        """just negatives"""
        self.assertEqual(
            max_integer(
                [-6105619, -854849, -562553, -3088955, -6711290, -4817844,
                    -1907189, -8110534, -6601769, -5837524, -4726702,
                    -8433749, -7251403, -5117635, -2979207, -1335257,
                    -6129976, -5791439, -3481890, -7828832, -6954726,
                    -5272933, -4952516, -6115545, -8333464, -7271456,
                    -7202853, -6891036, -4379807, -7955196, -1536591,
                    -2839083, -2586661, -9941097, -1]), -1)

    def test_ints_and_floats(self):
        """ints and floats type args"""
        self.assertEqual(
            max_integer(
                [10, 99.8, -100, -0.1, 1000, 9999, -100000, 9998.9]), 9999)

    def test_ints_and_floats_large(self):
        """ints and floats type args plus"""
        self.assertEqual(
            max_integer(
                [199872.7619047619, 115249.8813559322, 37972.944444444445,
                    120549.90322580645, 30889.777777777777, 986136.4,
                    393382.5416666667, 15441.826086956522, 2503567,
                    176118.87179487178, 372359.4, 142747.61538461538,
                    383318.8181818182, 297732.2727272727, 104980.52702702703,
                    98409.27272727272, 617459.875, 56556.62162162162, 61958.8,
                    88923.34444444445, 114726.20731707317, 143303.55,
                    38233.83516483517, 94065.72857142857, 42789.892857142855,
                    44182.47169811321, 41313.101265822785, 67705.18965517242,
                    1222423.5, 44966.55405405405, 37153.6, 82085.08,
                    559793.2857142857, 30031.58823529412, 126947.4262295082,
                    309222.3125, 125132.82089552238, 37276.27397260274,
                    99726.62903225806, 4270.788235294118, 490468.4375,
                    54086.642857142855, 73068.5, 108526.5081967213, 52943.875,
                    128534.875, 61069.433333333334, 37142.71951219512,
                    51481.13114754098, 571618.5,999999999, 35977.166666666664,
                    142333.11764705883, 199123.75]), 999999999)

    def test_floats(self):
        """just floats args"""
        self.assertEqual(
            max_integer(
                [.00123, .457568, .02345, .23423434, .45675674, .678678,
                    .867090, .74653, .5745375]), 0.86709)

    def test_floats_large(self):
        """large float args"""
        self.assertEqual(
            max_integer(
                [0.36701449486981136, 0.22932193120425423, 17.269673745943177,
                    0.6021998063297004, 7.040663644666581, 0.318418153098476,
                    0.14782568486828354, 1.694150096609713, 0.523292479047324,
                    6.577278388003499, 0.03165696316739835,
                    0.9723205356754642, 1.0167973840532782,
                    0.17994528432150622, 0.34268959203149724,
                    0.8237893847200373, 6.564703466354198, 0.650943204479027,
                    1.8902940005294793, 7.691604865311827, 8.897302744173896,
                    1.0780411284398352, 1.6564018996809176,
                    0.7495378363397325, 0.6460418901123863,
                    0.29656944388569284, 1.2020859950744733,
                    2.695758513783994, 0.37293339285604976,
                    0.8540047898304736, 0.16021193325291794,
                    0.027891891117170508, 0.8464685760135892,
                    4.506719557284897, 2.0258041087808, 4.525163681550944,
                    1.3277284362225874, 3.042753010712081, 2.4201460936424986,
                    0.6254206993310946, 3.6037820704785766,
                    0.5843942753272469, 2.994055932449279, 0.5168645505697169,
                    0.014982685631661026, 0.02477737364433171,
                    0.47120480947220955, 2.5056796257122915,
                    1.3349487122618868, 0.08451917751917885,
                    1.0157082402123356, 29.496355326217376,
                    10.171800729369348, 1.1263544935158727,
                    0.47572929035550277, 3.712323073375754,
                    0.5742929278531704, 0.43940976988732966,
                    0.09537099783126887, 1.4936141049902174,
                    5.764320019082692, 4.322880498170903, 2.004237813008687,
                    0.42770576125452897, 1.7136005979522013,100.99
                    8.877571036363525, 0.6825287480571863, 2.6834294650218338,
                    0.7504024417975861, 0.2762206358275793,
                    0.20607476376994402, 0.9497689034126077,
                    2.1498649449691807]), 100.99)

    def test_numeric_string(self):
        """string number"""
        self.assertEqual(max_integer("192834754"), "9")

    def test_string(self):
        """just string"""
        self.assertEqual(max_integer("Holberton"), "t")

    def test_lists(self):
        """list args"""
        self.assertEqual(max_integer([[], [2], [4], [2, 9]]), [4])

    def test_str_list(self):
        """sstring list arg"""
        self.assertEqual(
            max_integer([["foo"], ["boo"], ["abc"], ["sic"], ["ric"]]),
            ["sic"])

    def test_inf(self):
        """float list"""
        self.assertEqual(max_integer([99, float('inf'), float('-inf')]),
                         float('inf'))

    def test_nan(self):
        """nana nana"""
        self.assertEqual(max_integer([99, float('nan'), 100]), 100)

    def test_mixed_list(self):
        """strings and num"""
        with self.assertRaises(TypeError):
            max_integer([[], [2], [4], [2, 9], 99, "foo"])

    def test_mixed_list_int_str(self):
        """raises"""
        with self.assertRaises(TypeError):
            max_integer([99, "foo"])

    def test_none(self):
        """raises"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_dict(self):
        """raises"""
        with self.assertRaises(TypeError):
            max_integer([{20: 23, 14: 45}, {"a": "b"}])

    def test_int(self):
        """raises"""
        with self.assertRaises(TypeError):
            max_integer(98)

    def test_float(self):
        """raises"""
        with self.assertRaises(TypeError):
            max_integer(9.8)

if __name__ == '__main__':
    unittest.main()
