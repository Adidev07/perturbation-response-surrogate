"""Predict synthetic expression changes from fictional intervention descriptors and cellular contexts."""
from kit import *
TITLE='Context-Held-Out Perturbation Response'
LIVE=False

def features(desc,context,interaction=True):
    return np.column_stack([desc,context,(desc[:,:,None]*context[:,None,:]).reshape(len(desc),-1)]) if interaction else desc
def generate(seed=42):
    rng=np.random.default_rng(seed);contexts=np.repeat(np.arange(8),80);c=rng.normal(size=(8,2))[contexts];desc=rng.normal(size=(len(c),4));x=features(desc,c);y=x@rng.normal(0,.4,(x.shape[1],20))+rng.normal(0,.2,(len(c),20));return desc,c,y,contexts
def run(d,a):
    desc,c,y,groups=generate(a.seed);tr,te=group_split(groups,[6,7]);x=features(desc,c);w=ridge(x[tr],y[tr],2);simple=ridge(desc[tr],y[tr],2)
    return dict(test_rmse=rmse(y[te],ridge_predict(w,x[te])),descriptor_only_rmse=rmse(y[te],ridge_predict(simple,desc[te])),mean_baseline_rmse=rmse(y[te],np.tile(y[tr].mean(axis=0),(len(te),1))),heldout_contexts=[6,7],scope='Fictional intervention descriptors, not actionable genetic designs.'),dict(weights=w,descriptors=desc,context=c,response=y,groups=groups)

if __name__=="__main__":main(run)
