"""
The Problem

We would like you to change the below function to return which land parcels the given company owns (** directly and indirectly **).

When you are ready, please open any text-editor/IDE you wish, paste the code below, and share your screen so we can collaborate on the solution.

** Don't forget you can ask as many questions as you want. **

"""

companies = [
    {"id": "c1", "name": "Big Corp A", "parentId": None},
    {"id": "c2", "name": "Big Corp B", "parentId": None},
    {"id": "c3", "name": "Medium Corp A", "parentId": "c1"},
    {"id": "c4", "name": "Medium Corp B", "parentId": "c2"},
    {"id": "c5", "name": "Small Corp A", "parentId": "c3"},
    {"id": "c6", "name": "Small Corp B", "parentId": "c3"},
]

land_parcels = [
    {"id": "l1", "companyId": "c1"},
    {"id": "l2", "companyId": "c2"},
    {"id": "l3", "companyId": "c3"},
    {"id": "l4", "companyId": "c5"},
    {"id": "l5", "companyId": "c5"},
]

land_parcels_dict = {}

for land_parcel in land_parcels:

    if not land_parcels_dict.get(land_parcel['companyId']):
        land_parcels_dict[land_parcel['companyId']] = []

    land_parcels_dict[land_parcel['companyId']].append(land_parcel)

# print(land_parcels_dict)

companies_inverted_relation = {}

for company in companies:
    companies_inverted_relation[company['id']] = company

for company_inverted_relation_key in companies_inverted_relation:
    company_inverted_relation = companies_inverted_relation.get(company_inverted_relation_key)
    if company_inverted_relation.get("parentId"):
        if not companies_inverted_relation[company_inverted_relation["parentId"]].get("children"):
            companies_inverted_relation[company_inverted_relation["parentId"]]['children'] = []

        companies_inverted_relation[company_inverted_relation["parentId"]]["children"].append(
            company_inverted_relation["id"])


# print(companies_inverted_relation)


# Implement the following function
#  E.g. get_land_parcels_for_company("c1") => ["l1","l3","l4","l5"]
def get_land_parcels_for_company(company_id):
    # print(land_parcels_dict.get(company_id))

    company_ids = get_correlated_company_ids(company_id)

    parcels = []
    for company_id in company_ids:
        if land_parcels_dict.get(company_id):
            parcels.extend([lp['id'] for lp in land_parcels_dict[company_id]])

    return set(parcels)


def get_correlated_company_ids(company_id):
    company_ids = [company_id]
    if companies_inverted_relation.get(company_id).get('children'):
        children_company_ids = companies_inverted_relation[company_id]['children']
        company_ids.extend(children_company_ids)
        for c in children_company_ids:
            company_ids.extend(get_correlated_company_ids(c))

    return set(company_ids)


if __name__ == '__main__':
    get_land_parcels_for_company("c1")
