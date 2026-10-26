import unittest
from app import *
class DomainTests(unittest.TestCase):
    def test_interaction_shape(self):self.assertEqual(features(np.ones((3,4)),np.ones((3,2))).shape,(3,14))
    def test_context_split(self):
        _,_,_,g=generate();tr,te=group_split(g,[6,7]);self.assertFalse(set(g[tr])&set(g[te]))
    def test_multioutput_fit(self):
        x=np.arange(60.).reshape(-1,1);y=np.column_stack([x[:,0],2*x[:,0]]);self.assertLess(rmse(y,ridge_predict(ridge(x,y,.001),x)),.001)
