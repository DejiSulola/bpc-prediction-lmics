from util.helpers import create_file_path
from util.excel import recast_excel_file
from util.excel import merge_excel_files
from util.excel import recast_and_merge_excel_files
from util.latex import excel_to_latex_table

# Merge excel file - Regional
merge_excel_files('results/region/east_asia_and_pacific', 'results/region/east_asia_and_pacific_models.xlsx')
merge_excel_files('results/region/europe_and_central_asia', 'results/region/europe_and_central_asia_models.xlsx')
merge_excel_files('results/region/latin_america_and_caribbean', 'results/region/latin_america_and_caribbean_models.xlsx')
merge_excel_files('results/region/middle_east_and_north_africa', 'results/region/middle_east_and_north_africa_models.xlsx')
merge_excel_files('results/region/south_asia', 'results/region/south_asia_models.xlsx')
merge_excel_files('results/region/sub_saharan_africa', 'results/region/sub_saharan_africa_models.xlsx')

# Merge excel file - Country
merge_excel_files('results/countries/afghanistan', 'results/countries/afghanistan_models.xlsx')
merge_excel_files('results/countries/algeria', 'results/countries/algeria_models.xlsx')
# merge_excel_files('results/countries/american_samoa', 'results/countries/american_samoa_models.xlsx')
merge_excel_files('results/countries/armenia', 'results/countries/armenia_models.xlsx')
merge_excel_files('results/countries/azerbaijan', 'results/countries/azerbaijan_models.xlsx')
merge_excel_files('results/countries/bahamas', 'results/countries/bahamas_models.xlsx')
merge_excel_files('results/countries/bangladesh', 'results/countries/bangladesh_models.xlsx')
merge_excel_files('results/countries/barbados', 'results/countries/barbados_models.xlsx')
merge_excel_files('results/countries/belarus', 'results/countries/belarus_models.xlsx')
merge_excel_files('results/countries/benin', 'results/countries/benin_models.xlsx')
merge_excel_files('results/countries/bhutan', 'results/countries/bhutan_models.xlsx')
merge_excel_files('results/countries/botswana', 'results/countries/botswana_models.xlsx')
# merge_excel_files('results/countries/british_virgin_islands', 'results/countries/british_virgin_islands_models.xlsx')
# merge_excel_files('results/countries/cayman_islands', 'results/countries/cayman_islands_models.xlsx')
# merge_excel_files('results/countries/central_african_republic', 'results/countries/central_african_republic_models.xlsx')
merge_excel_files('results/countries/chad', 'results/countries/chad_models.xlsx')
merge_excel_files('results/countries/comoros', 'results/countries/comoros_models.xlsx')
# merge_excel_files('results/countries/cook_islands', 'results/countries/cook_islands_models.xlsx')
# merge_excel_files('results/countries/cote_divoire', 'results/countries/cote_divoire_models.xlsx')
# merge_excel_files('results/countries/democratic_republic_of_the_congo', 'results/countries/democratic_republic_of_the_congo_models.xlsx')
merge_excel_files('results/countries/ecuador', 'results/countries/ecuador_models.xlsx')
merge_excel_files('results/countries/eritrea', 'results/countries/eritrea_models.xlsx')
merge_excel_files('results/countries/eswatini', 'results/countries/eswatini_models.xlsx')
merge_excel_files('results/countries/ethiopia', 'results/countries/ethiopia_models.xlsx')
merge_excel_files('results/countries/fiji', 'results/countries/fiji_models.xlsx')
# merge_excel_files('results/countries/french_polynesia', 'results/countries/french_polynesia_models.xlsx')
merge_excel_files('results/countries/gabon', 'results/countries/gabon_models.xlsx')
merge_excel_files('results/countries/gambia', 'results/countries/gambia_models.xlsx')
merge_excel_files('results/countries/georgia', 'results/countries/georgia_models.xlsx')
merge_excel_files('results/countries/ghana', 'results/countries/ghana_models.xlsx')
merge_excel_files('results/countries/grenada', 'results/countries/grenada_models.xlsx')
merge_excel_files('results/countries/guinea', 'results/countries/guinea_models.xlsx')
merge_excel_files('results/countries/guyana', 'results/countries/guyana_models.xlsx')
merge_excel_files('results/countries/kiribati', 'results/countries/kiribati_models.xlsx')
merge_excel_files('results/countries/kyrgyzstan', 'results/countries/kyrgyzstan_models.xlsx')
# merge_excel_files('results/countries/lao_people_democratic_republic', 'results/countries/lao_people_democratic_republic_models.xlsx')
merge_excel_files('results/countries/lesotho', 'results/countries/lesotho_models.xlsx')
merge_excel_files('results/countries/liberia', 'results/countries/liberia_models.xlsx')
merge_excel_files('results/countries/libya', 'results/countries/libya_models.xlsx')
merge_excel_files('results/countries/madagascar', 'results/countries/madagascar_models.xlsx')
merge_excel_files('results/countries/malawi', 'results/countries/malawi_models.xlsx')
merge_excel_files('results/countries/maldives', 'results/countries/maldives_models.xlsx')
merge_excel_files('results/countries/mali', 'results/countries/mali_models.xlsx')
# merge_excel_files('results/countries/mauritania', 'results/countries/mauritania_models.xlsx')
merge_excel_files('results/countries/micronesia', 'results/countries/micronesia_models.xlsx')
merge_excel_files('results/countries/moldova', 'results/countries/moldova_models.xlsx')
merge_excel_files('results/countries/mongolia', 'results/countries/mongolia_models.xlsx')
merge_excel_files('results/countries/mozambique', 'results/countries/mozambique_models.xlsx')
merge_excel_files('results/countries/myanmar', 'results/countries/myanmar_models.xlsx')
merge_excel_files('results/countries/namibia', 'results/countries/namibia_models.xlsx')
merge_excel_files('results/countries/nauru', 'results/countries/nauru_models.xlsx')
merge_excel_files('results/countries/nepal', 'results/countries/nepal_models.xlsx')
merge_excel_files('results/countries/niger', 'results/countries/niger_models.xlsx')
merge_excel_files('results/countries/niue', 'results/countries/niue_models.xlsx')
merge_excel_files('results/countries/palau', 'results/countries/palau_models.xlsx')
merge_excel_files('results/countries/palestine', 'results/countries/palestine_models.xlsx')
merge_excel_files('results/countries/qatar', 'results/countries/qatar_models.xlsx')
merge_excel_files('results/countries/rwanda', 'results/countries/rwanda_models.xlsx')
merge_excel_files('results/countries/samoa', 'results/countries/samoa_models.xlsx')
# merge_excel_files('results/countries/sierra_leone', 'results/countries/sierra_leone_models.xlsx')
# merge_excel_files('results/countries/solomon_islands', 'results/countries/solomon_islands_models.xlsx')
# merge_excel_files('results/countries/sri_lanka', 'results/countries/sri_lanka_models.xlsx')
merge_excel_files('results/countries/tanzania', 'results/countries/tanzania_models.xlsx')
# merge_excel_files('results/countries/timor-leste', 'results/countries/timor-leste_models.xlsx')
merge_excel_files('results/countries/togo', 'results/countries/togo_models.xlsx')
merge_excel_files('results/countries/tokelau', 'results/countries/tokelau_models.xlsx')
merge_excel_files('results/countries/tonga', 'results/countries/tonga_models.xlsx')
merge_excel_files('results/countries/tuvalu', 'results/countries/tuvalu_models.xlsx')
merge_excel_files('results/countries/uganda', 'results/countries/uganda_models.xlsx')
merge_excel_files('results/countries/vanuatu', 'results/countries/vanuatu_models.xlsx')
merge_excel_files('results/countries/zambia', 'results/countries/zambia_models.xlsx')

# Check folders
create_file_path('results/latex')

# Recast global model
recast_excel_file('results/global/global_models.xlsx', 'results/latex/global_models.xlsx')

# Recast regional model
recast_and_merge_excel_files('results/region/', 'results/latex/region_models.xlsx')

# Recast country model
recast_and_merge_excel_files('results/countries/', 'results/latex/country_models.xlsx', is_country=True)

# Convert excel table to Latex
excel_to_latex_table('results/latex/global_models.xlsx',
                     'Global Model Results.', 'tbl:global_model', 'results/latex/global_models.tex', is_global=True)
excel_to_latex_table('results/latex/region_models.xlsx',
                     'Region Model Results.', 'tbl:region_model', 'results/latex/region_models.tex')
excel_to_latex_table('results/latex/country_models.xlsx',
                     'Country Model Results.', 'tbl:country_model', 'results/latex/country_models.tex')
