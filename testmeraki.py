import meraki

apikey = 'fd6dd87d96915f21bc0e0b3d96a866ff0e53e381'

dashboard = meraki.DashboardAPI(apikey)

my_orgs = dashboard.organizations.getOrganizations()

for organ in my_orgs:
    if "DevNet" in organ['name']:
        print (organ)
        print ('*' * 20)
