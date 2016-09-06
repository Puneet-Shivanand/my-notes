from Bio import Entrez
from Bio import Medline
Entrez.email='puneet.as@leucinerichbio.com'

handle= Entrez.esearch(db='gene', retmax=10, term='kinetochore')
record = Entrez.read(handle)
ids=record['IdList']


def retrieve_annotation(id_list):

    """Annotates Entrez Gene IDs using Bio.Entrez, in particular epost (to
    submit the data to NCBI) and esummary to retrieve the information.
    Returns a list of dictionaries with the annotations."""

    request = Entrez.epost("gene",id=",".join(id_list))
    try:
        result = Entrez.read(request)
    except RuntimeError as e:
        #FIXME: How generate NAs instead of causing an error with invalid IDs?
        print "An error occurred while retrieving the annotations."
        print "The error returned was %s" % e
        sys.exit(-1)

    webEnv = result["WebEnv"]
    queryKey = result["QueryKey"]
    data = Entrez.esummary(db="gene", webenv=webEnv, query_key =
            queryKey)
    annotations = Entrez.read(data)

    print "Retrieved %d annotations for %d genes" % (len(annotations),
            len(id_list))

    return annotations

def print_data(annotation):
    for gene_data in annotation:
        gene_id = gene_data["Id"]
        gene_symbol = gene_data["NomenclatureSymbol"]
        gene_name = gene_data["Description"]
        print "ID: %s - Gene Symbol: %s - Gene Name: %s" % (gene_id, gene_symbol, gene_name)




