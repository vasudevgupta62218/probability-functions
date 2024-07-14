from multiapp import Multiapp
from apps import Poisson_dist,Normal_dist

app=Multiapp()
app.add_app("Poisson Distribution",Poisson_dist)
app.add_app("Normal Distribution",Normal_dist)

app.run()