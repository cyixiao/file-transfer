from flagdata.cleaner.text_cleaner import DataCleaner

if __name__ == "__main__":
    cleaner = DataCleaner("HOME/FlagData/config/cleaner_config.yaml")
    cleaner.clean()
