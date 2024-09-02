# This is Codility test for data cleaning using pandas

import pandas as pd

def process_data():
    """
    Load the biopics data, clean it, and save the cleaned version to a new CSV file.

    Returns:
        A pandas DataFrame with the cleaned data.
    """
    # Load the biopics data
    biopics = pd.read_csv("biopics.csv", encoding='latin-1')

    # Remove duplicate rows
    biopics.drop_duplicates(subset='title', inplace=True)

    # Rename columns
    # Clean up the biopics data
    # Find and count duplicate rows
    biopics.drop_duplicates(subset='title',inplace=True)
    biopics.rename(columns={'box_office': 'earnings'}, inplace=True)

    # Drop rows with missing earnings
    biopics.dropna(subset=['earnings'], inplace=True)

    # Drop rows with year_release before 1990
    biopics = biopics[biopics['year_release'] >= 1990]

    # Convert categorical columns
    biopics['type_of_subject'] = biopics['type_of_subject'].astype('category')
    biopics['country'] = biopics['country'].astype('category')

    # Convert earnings to millions
    biopics['earnings'] = biopics['earnings'] / 1000000

    # Select the desired columns and sort by earnings
    biopics = biopics[['title', 'year_release', 'earnings', 'country', 'type_of_subject', 'lead_actor_actress', 'lead_actor_actress_known']]
    biopics.sort_values(by='earnings', ascending=False, inplace=True)

    # Save the cleaned data to a new CSV file
    biopics.to_csv("biopics_clean.csv", index=False)
    return biopics.reset_index(drop=True)

process_data()