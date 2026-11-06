import pandas as pd
#okay so with the ingestion this is what i am gonna do, like how functions work in mathematics, i am going to map some set of undefined values in x to y so f(x) = y, so the function is applied on the values of x

#now, i will define a dictionary
NAMES_MAPPING = {
   "sam":"Samuel",
   "sammy":"Samuel",
   "big sam":"Samuel",
   "sammy tuga":"Samuel",

   "danny":"Daniel", 
   "dan":"Daniel",
   "dani":"Daniel"
}

def standardize_names(short_names):
    if pd.isna(short_names):
        return "missing/ unmapped"

    clean_names = str(short_names).strip().lower()

    return NAMES_MAPPING.get(short_names, "not an actual name")

def run_ingestion_pipeline(input_file, output_file):
    print(f"ETL STEP1: extraction of data")
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Notice: {input_file} not found. Generating mockup sample")

    sample_data = {
        "shipment_id": [101, 102, 103, 104, 105],
        "raw_region": ["sam", "big sam", "sammy tuga", "danny", "dani"],
        "weight_kg": [12.5, 4.0, 8.2, 15.0, 3.1]    
    }
    df = pd.DataFrame(sample_data)

