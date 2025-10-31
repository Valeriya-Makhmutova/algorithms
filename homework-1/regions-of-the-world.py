import csv
        
with open('input.txt') as f:
    reader = csv.DictReader(f, delimiter=';')
    
    data_dict = {}
    for row in reader:

        country = row['Country']
        region = row['Region']
        literacy = row['Literacy']
          
        if region not in data_dict:
          data_dict[region] = {'contries': 0, 'high_literacy_countries': 0}
        
        data_dict[region]['contries'] += 1
        if int(float(row['Literacy'])) >= 90:
           data_dict[region]['high_literacy_countries'] += 1
    
    max_rate = 0
    
    for key in data_dict:
       rate = data_dict[key]['high_literacy_countries'] / data_dict[key]['contries']
       data_dict[key]['rate'] = rate
       if max_rate < rate:
          max_rate = rate
    
    sorted_list_of_regions = sorted(data_dict.items())
    sorted_dict = dict(sorted_list_of_regions)

    fo = open('output.txt', 'w')
    matching_regions = []
    for region in sorted_dict:
       if max_rate == data_dict[region]['rate']:
          matching_regions.append(region)

    if matching_regions:
        fo.write('\n'.join(matching_regions))
