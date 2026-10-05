import numpy as np

ran=np.random.default_rng(seed=42)
x=ran.integers(low=0,high=15,size=(10,1))
m=2
c=3
noise=np.random.uniform(size=(10,1))
y=m*x+c+noise
m_pred=0
c_pred=0


y_pred=m_pred*x + c_pred 



for i in range(1,50000):
    msd=np.mean((y-y_pred)**2)
    dmsdm=(2/10)*np.sum((y_pred-y)*x)
    dmsdc=(2/10)*np.sum(y_pred-y)

    lr=0.0001

    m_pred=m_pred-lr*dmsdm
    c_pred=c_pred-lr*dmsdc
    y_pred=m_pred*x + c_pred 
    print(m_pred)
    print(c_pred)