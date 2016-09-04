# coding: utf-8

#Read in Excel file, break up advertiser url string, drop unnecessary cols
def read_clean(file_name):
    import pandas as pd
    wb = pd.read_excel(file_name)
    cols = ["Url", "Advertisers", "Similar Web Global Rank"]
    wb = wb[cols]
    split_ad = []
    for i in wb["Advertisers"]:
        split_ad.append(str(i).split(','))
    wb["Split Adv"] = split_ad
    return(wb)

#Count advertiser occurence
def adv_count(prospect, comp1, comp2, wb):
    prospect_count = 0
    comp1_count = 0
    comp2_count = 0
    for i in wb["Split Adv"]:
        if prospect in i:
            prospect_count += 1
        if comp1 in i:
            comp1_count += 1
        if comp2 in i:
            comp2_count += 1
    answer_string = "Publishers linking to: \n" + prospect + ": " + str(prospect_count) + "\n" + comp1 + ": " + str(comp1_count)  + "\n" + comp2 + ": " + str(comp2_count)
    return(answer_string)

#Remove shitty sites, remove publishers linking to prospect, sort by Similar Web Rank, return top 30 publishers
def top_pubs(wb, prospect):
    clean_wb = wb[~wb["Url"].str.contains('blogspot.com$|weebly.com$|tumblr.com$|inbox.com$|typepad.com$')]

    #Workaround to remove rows where the prospect is present. I am almost positive there is a better way to do this.
    present_list = []
    for i in clean_wb["Split Adv"]:
        present_list.append(prospect not in i)
    clean_wb = clean_wb[present_list]

    sorted_wb = clean_wb.sort_values(by="Similar Web Global Rank")
    top_pubs = list(sorted_wb["Url"].head(30))
    top_pubs2 = ""
    for i in top_pubs:
        top_pubs2 = top_pubs2 + i + "\n"
    return(top_pubs2)

# Run the above, write to a new txt file

def run_prt(wb, prospect, comp1, comp2):
    import os
    import sys
    new_name = prospect + ".txt"
    new_file = open(new_name, 'w')
    wb = read_clean(wb)
    top_publishers = top_pubs(wb, prospect)
    adv_count_string = adv_count(prospect, comp1, comp2, wb)
    print(top_publishers)
    print(adv_count_string)
    new_file.write(adv_count_string  + "\n \n Top 30 Publishers Linking to Competitors: \n" + top_publishers)
    new_file.close()
    os.system("vim "+new_name)


