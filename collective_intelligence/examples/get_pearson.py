import sys
import recommendations
from recommendations import critics
#recommendations.sim_pearson(recommendations.critics, 'Lisa Rose', 'Gene Seymour')
for key in recommendations.critics:
    print key, '=>', recommendations.sim_pearson(recommendations.critics,sys.argv[1],key)
