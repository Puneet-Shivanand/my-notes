import sys
import recommendations
from recommendations import critics
for key in recommendations.critics:
    print key, '=>', recommendations.sim_distance(recommendations.critics,sys.argv[1],key)
