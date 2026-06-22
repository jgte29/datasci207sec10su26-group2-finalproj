
data_schema = {
    "conditionaltype": {
        "type": "Char",
        "length": "3",
        "description": "Conditional Type. This flag provides information about the condition of a security's trading. The most common value by far is RW (Regular Way), but additional codes exist to identify unusual circumstances that might require special processing.",
        "mappings": {
            "N/A": "Not Applicable ",
            "NT": "Not Tracked ",
            "NW": "Non-Leading When Issued ",
            "RW": "Regular Way ",
            "WI": "When Issued "
        }
    },
    "cusip": {
        "type": "Char",
        "length": "8",
        "description": "CUSIP"
    },
    "cusip9": {
        "type": "Char",
        "length": "9",
        "description": "CUSIP9"
    },
    "delactiontype": {
        "type": "Char",
        "length": "5",
        "description": "Delisting Corporate Action Type. This flag provides additional information about a distribution and has about sixty values for easy identification of specific types of events. For many uses, the Action Component Type in the DisType column is sufficient.",
        "mappings": {
            "GDR": "Dropped ",
            "GEX": "Exchange ",
            "GLI": "Liquidation ",
            "LOS": "Lost Source ",
            "MER": "Merger ",
            "N/A": "Not Applicable "
        }
    },
    "delpaymenttype": {
        "type": "Char",
        "length": "4",
        "description": "Delisting Payment Summary Type. This flag provides information on what the share holder received as part of the delisting. There are about two dozens different values. The most common are: PRCF (Price Final), CASH, and STK (Stock).",
        "mappings": {
            "CASH": "Cash ",
            "CNC": "Common and Non-Common ",
            "COP": "Cash and Other Property ",
            "CSHN": "Cash and Non-Common ",
            "CST": "Cash and Stock ",
            "CUS": "Cash and Untracked Stock ",
            "DW": "Declared Worthless ",
            "MAF": "Merger Attempt Failed ",
            "MMI": "Missing Information ",
            "MUT": "Mutual Funds ",
            "N/A": "Not Applicable ",
            "NCOM": "Non-Common ",
            "NCOP": "Non-Common and Other Property ",
            "OP": "Other Property ",
            "PRCF": "Price Final ",
            "SNC": "Stock and Non-Common ",
            "SOP": "Stock and Other Property ",
            "STK": "Stock ",
            "UMAP": "Unmapped ",
            "UNAV": "Unavailable ",
            "USNC": "Untracked Stock and Non-Common ",
            "USOP": "Untracked Stock and Other Property ",
            "USTK": "Untracked Stock "
        }
    },
    "delreasontype": {
        "type": "Char",
        "length": "5",
        "description": "Delisting Reason Type. This flag provides additional information, if available, on why a security delisted. There are about three dozen values, but the majority of the time, an additional reason is UNAV.",
        "mappings": {
            "BKPY": "Bankruptcy ",
            "CORQ": "Company Request ",
            "DEEX": "Denied Exception ",
            "DELQ": "Delinquent ",
            "DERE": "Deregistration ",
            "EQRQ": "Equity Requirements ",
            "FARG": "Failure to Register ",
            "FDCV": "Fund Conversion ",
            "FING": "Financial Guidelines ",
            "INSC": "Insufficient Capital ",
            "INSF": "Insufficient Float ",
            "LP": "Low Price ",
            "MTMK": "Market Makers ",
            "MVB": "Moved to Boston ",
            "MVCHI": "Moved to Chicago ",
            "MVMF": "Moved to Mutual Fund ",
            "MVMO": "Moved to Montreal ",
            "MVNM": "Moved to NYSE MKT ",
            "MVOT": "Moved to OTC ",
            "MVPAC": "Moved to Pacific ",
            "MVPH": "Moved to Philadelphia ",
            "MVTO": "Moved to Toronto ",
            "N/A": "Not Applicable ",
            "NACT": "Not Applicable - Active ",
            "OFFRE": "Offer Rescinded ",
            "PUBI": "Public Interest ",
            "SERQ": "SEC Required ",
            "SHLD": "Shareholders ",
            "UNAV": "Unavailable ",
            "UNL": "Unlisted ",
            "VIO": "Violation "
        }
    },
    "delstatustype": {
        "type": "Char",
        "length": "4",
        "description": "Delisting Completion Status Type. This flag provides information about the status of the delisting information. The vast majority of delistings are either FPAY (Final Payment) and VCL (Valued, Closed), but some additional values exist to identify unusual circumstances.",
        "mappings": {
            "FPAY": "Final Payment ",
            "N/A": "Not Applicable ",
            "NDC": "No Distributions, Closed ",
            "NDP": "No Distributions, Pending ",
            "NFC": "No Final, Closed ",
            "NFP": "No Final, Pending ",
            "NVP": "No Value, Pending ",
            "UNAV": "Unavailable ",
            "VCL": "Valued, Closed "
        }
    },
    "disamountsourcetype": {
        "type": "Char",
        "length": "3",
        "description": "Distribution Amount Source Type. This flag provides information about the source of the distribution amount.",
        "mappings": {
            "CF": "Non-Transferable - Calculated ",
            "CV": "Calculated but Transferable ",
            "FM": "Fair Market Value ",
            "MK": "Market Value ",
            "MP": "Market Value - Price Provided ",
            "N/A": "Not Applicable ",
            "NF": "Non-Transferable - Fair Market ",
            "UN": "Unknown ",
            "UT": "Unknown Transferable ",
            "UV": "Non-Transferable - Unknown "
        }
    },
    "disdeclaredt": {
        "type": "Date",
        "description": "Declaration Date"
    },
    "disdetailtype": {
        "type": "Char",
        "length": "8",
        "description": "Distribution Detail Type. This flag provides additional granularity for the component type of a distribution. For many uses, component type is sufficient, but for those needing additional detail, there over 70 values for this code.",
        "mappings": {
            "CAPG": "Capital Gains ",
            "CDIV": "Cash Dividend ",
            "CDM": "Cash Dividend - Missing Terms ",
            "CDPSR": "Cash Dividend - Proceeds from Sale of Rights ",
            "CPBLST": "Cash Payment - Buyback - Limited Self Tender ",
            "CPEX": "Cash Payment - Exchange ",
            "CPEXCSH": "Cash Payment - Exchange - Cash ",
            "CPFL": "Cash Payment - Final Liquidation ",
            "CPM": "Cash Payment - Merger ",
            "CPPL": "Cash Payment - Partial Liquidation ",
            "CPRCSH": "Cash Payment - Reorganization - Cash ",
            "CPSCM": "Cash Payment - Shares Changed Merger ",
            "CPSCMO": "Cash Payment - Shares Changed Merger Other ",
            "CPSIL": "Cash Payment - Step in Liquidation ",
            "CPSOA": "Cash Payment - Sale of Assets ",
            "ICLA": "Issuer Change - Liquidation Announcement ",
            "ICSAA": "Issuer Change - Sale of Assets Announcement ",
            "ROC": "Return of Capital ",
            "RPSR": "ROC - Proceeds from Sale of Rights ",
            "SDIV": "Special Dividends ",
            "SDROC": "Special Dividends - ROC ",
            "SECBLST": "Security Payment - Buyback -< "
        }
    },
    "disdivamt": {
        "type": "Decimal",
        "length": "11.4",
        "description": "Dividend Amount"
    },
    "disexdt": {
        "type": "Date",
        "description": "Ex-Distribution Date"
    },
    "disfacpr": {
        "type": "Decimal",
        "length": "10.6",
        "description": "Factor To Adjust Price"
    },
    "disfacshr": {
        "type": "Decimal",
        "length": "10.6",
        "description": "Factor To Adjust Shares"
    },
    "disfreqtype": {
        "type": "Char",
        "length": "3",
        "description": "Distribution Frequency Type. This flag indicates the frequency of the distribution. The most common values are Q (Quarterly), M (Monthly) and U (Unspecified).",
        "mappings": {
            "A": "Annual ",
            "E": "Extra or Special ",
            "I": "Interim ",
            "M": "Monthly ",
            "N": "Non-Recurring ",
            "N/A": "Not Applicable ",
            "Q": "Quarterly ",
            "S": "Semi-Annual ",
            "U": "Unspecified ",
            "X": "Unknown ",
            "Y": "Year-End "
        }
    },
    "disordinaryflg": {
        "type": "Char",
        "length": "1",
        "description": "Distribution Ordinary Dividend Flag",
        "mappings": {
            "N": "No",
            "Y": "Yes"
        }
    },
    "disorigcurtype": {
        "type": "Char",
        "length": "3",
        "description": "Distribution Original Currency Type. This flag provides information on what currency a distribution was paid. Almost all cash payments in the CRSP files are USD (US Dollar), but some are NUS (Non-US).",
        "mappings": {
            "N/A": "Not Applicable ",
            "NUS": "Non-US ",
            "USD": "United States dollar "
        }
    },
    "dispaydt": {
        "type": "Date",
        "description": "Payment Date"
    },
    "dispaymenttype": {
        "type": "Char",
        "length": "4",
        "description": "Distribution Payment Method Type. Indicates what payment type the share holders received. Over 90% of the values are USD (US Dollars). The next most common is SS (Same Security - usual splits).",
        "mappings": {
            "FX": "Foreign Currency ",
            "N/A": "Not Applicable ",
            "OP": "Other Property ",
            "OS": "Other Security ",
            "SS": "Same Security ",
            "UN": "Unspecified ",
            "UNIT": "Units Including Same Issue of Common Stock ",
            "USD": "USD ",
            "X": "Unknown "
        }
    },
    "dispermco": {
        "type": "Int32",
        "description": "PERMCO of the Issuer Providing Payment"
    },
    "dispermno": {
        "type": "Int32",
        "description": "PERMNO of the Security Received"
    },
    "disrecorddt": {
        "type": "Date",
        "description": "Record Date"
    },
    "disseqnbr": {
        "type": "Int16",
        "description": "Distribution Sequence Number"
    },
    "distaxtype": {
        "type": "Char",
        "length": "3",
        "description": "Distribution Tax Status Type. Indicates the tax status of payment that the share holders received. About 80% of the values are D (taxable as a dividend) followed by N (non-taxable).",
        "mappings": {
            "C": "Capital Gains ",
            "D": "Dividend ",
            "F": "Full ",
            "G": "Gain/Loss ",
            "N": "Non-Taxable ",
            "N/A": "Not Applicable ",
            "P": "Plan ",
            "R": "Return of Capital ",
            "T": "Tax Receipt ",
            "U": "Unspecified ",
            "X": "Unknown "
        }
    },
    "distype": {
        "type": "Char",
        "length": "4",
        "description": "Distribution Type. Provides a high level descriptions of the distribution type. The most common value is CD (Cash Dividend about 90%) followed by FRS (Forward or Reverse Split about 4%).",
        "mappings": {
            "CD": "Cash Dividend ",
            "CG": "Capital Gains ",
            "CP": "Cash Payment ",
            "FRS": "Forward or Reverse Split ",
            "IN": "Issuer Notification ",
            "N/A": "Not Applicable ",
            "ROC": "Return of Capital ",
            "SD": "Special Dividends ",
            "SP": "Security Payment ",
            "TSOO": "Total Shares Outstanding Observation "
        }
    },
    "dlyask": {
        "type": "Decimal",
        "length": "11.4",
        "description": "Daily Ask",
        "siz_alias": "ask"
    },
    "dlybid": {
        "type": "Decimal",
        "length": "11.4",
        "description": "Daily Bid",
        "siz_alias": "bid"
    },
    "dlycaldt": {
        "type": "Date",
        "description": "Daily Calendar Date",
        "siz_alias": "date"
    },
    "dlycap": {
        "type": "Decimal",
        "length": "13.2",
        "description": "Daily Capitalization"
    },
    "dlycapflg": {
        "type": "Char",
        "length": "2",
        "description": "Daily Capitalization Flag. Provides information as to why a capitalization is missing or if it is based an ADR and excluded from certain CRSP Index calculations.",
        "mappings": {
            "AD": "ADR ",
            "BP": "Basis Price Capitalization ",
            "DE": "Delisted ",
            "MP": "Missing Price ",
            "MS": "Missing Shares ",
            "NA": "Not Applicable ",
            "NT": "Not Tracked ",
            "PB": "Prior Basis Price Capitalization "
        }
    },
    "dlyclose": {
        "type": "Decimal",
        "length": "11.4",
        "description": "Daily Close"
    },
    "dlycumfacpr": {
        "type": "Decimal",
        "length": "13.6",
        "description": "Daily Cumulative Factor to Adjust Price",
        "siz_alias": "cfacpr"
    },
    "dlycumfacshr": {
        "type": "Decimal",
        "length": "13.6",
        "description": "Daily Cumulative Factor to Adjust Shares/Volume",
        "siz_alias": "cfacshr"
    },
    "dlydelflg": {
        "type": "Char",
        "length": "1",
        "description": "Daily Delisting Flag",
        "mappings": {
            "N": "No",
            "Y": "Yes"
        }
    },
    "dlydistretflg": {
        "type": "Char",
        "length": "2",
        "description": "Daily Distribution Return Impact Flag. Summarizes how many and what types distributions impact a security return.",
        "mappings": {
            "C1": "One Ordinary Cash Dividend ",
            "C2": "Two Ordinary Cash Dividends ",
            "CS": "One Cash Dividend & One Stock Split ",
            "D1": "One Delisting Action ",
            "D2": "Two Delisting Actions ",
            "F1": "One Share Factor - Non-Split ",
            "M2": "Two Corporate Actions ",
            "MU": "Multiple Corporate Actions ",
            "N1": "One Non-Ordinary ",
            "NA": "Not Applicable ",
            "NO": "No Corporate Actions ",
            "O1": "One 'Other' Action ",
            "P1": "One Price Factor - Non-Split ",
            "S1": "One Stock Split/Dividend ",
            "S2": "Two Stock Splits/Dividends ",
            "T1": "One (Tender) Offer Action "
        }
    },
    "dlyfacprc": {
        "type": "Decimal",
        "length": "10.6",
        "description": "Daily Factor To Adjust Price"
    },
    "dlyhigh": {
        "type": "Decimal",
        "length": "11.4",
        "description": "Daily High",
        "siz_alias": "askhi"
    },
    "dlylow": {
        "type": "Decimal",
        "length": "11.4",
        "description": "Daily Low",
        "siz_alias": "bidlo"
    },
    "dlymmcnt": {
        "type": "Int16",
        "description": "Daily Market Maker Count"
    },
    "dlynonorddivamt": {
        "type": "Decimal",
        "length": "11.4",
        "description": "Daily Non-Ordinary Dividend Amount"
    },
    "dlynumtrd": {
        "type": "Int32",
        "description": "Daily Number Of Trades",
        "siz_alias": "numtrd"
    },
    "dlyopen": {
        "type": "Decimal",
        "length": "11.4",
        "description": "Daily Open",
        "siz_alias": "openprc"
    },
    "dlyorddivamt": {
        "type": "Decimal",
        "length": "11.4",
        "description": "Daily Ordinary Dividend Amount"
    },
    "dlyprc": {
        "type": "Decimal",
        "length": "11.4",
        "description": "Daily Price",
        "siz_alias": "prc"
    },
    "dlyprcflg": {
        "type": "Char",
        "length": "2",
        "description": "Daily Price Flag. Most values are BA (Bid/Ask Average) or TR (Closing Trade).",
        "mappings": {
            "BA": "Bid Ask Average ",
            "DA": "Delisting Amount (no Delisting Price) ",
            "DM": "Delisting Price/Amount Missing ",
            "DP": "Delisting Price ",
            "GP": "Gap - more than 10 periods ",
            "MI": "Missing - Prior to BegDt ",
            "MP": "Missing Price ",
            "NA": "Not Applicable ",
            "NS": "New Security ",
            "NT": "Not Tracked ",
            "TR": "Closing Trade Price "
        }
    },
    "dlyprcvol": {
        "type": "Decimal",
        "length": "14.1",
        "description": "Daily Price Volume"
    },
    "dlyprevcap": {
        "type": "Decimal",
        "length": "13.2",
        "description": "Daily Previous Capitalization"
    },
    "dlyprevcapflg": {
        "type": "Char",
        "length": "2",
        "description": "Daily Previous Capitalization Flag. Provides information as to why a capitalization is missing or if it is based an ADR.",
        "mappings": {
            "AD": "ADR ",
            "BP": "Basis Price Capitalization ",
            "DE": "Delisted ",
            "MP": "Missing Price ",
            "MS": "Missing Shares ",
            "NA": "Not Applicable ",
            "NT": "Not Tracked ",
            "PB": "Prior Basis Price Capitalization "
        }
    },
    "dlyprevdt": {
        "type": "Date",
        "description": "Daily Previous Price Date"
    },
    "dlyprevprc": {
        "type": "Decimal",
        "length": "11.4",
        "description": "Daily Previous Price"
    },
    "dlyprevprcflg": {
        "type": "Char",
        "length": "2",
        "description": "Daily Previous Price Flag. Most values are BA (Bid/Ask Average) or TR (Closing Trade).",
        "mappings": {
            "BA": "Bid Ask Average ",
            "DA": "Delisting Amount (no Delisting Price) ",
            "DM": "Delisting Price/Amount Missing ",
            "DP": "Delisting Price ",
            "GP": "Gap - more than 10 periods ",
            "MI": "Missing - Prior to BegDt ",
            "MP": "Missing Price ",
            "NA": "Not Applicable ",
            "NS": "New Security ",
            "NT": "Not Tracked ",
            "TR": "Closing Trade Price "
        }
    },
    "dlyret": {
        "type": "Decimal",
        "length": "10.6",
        "description": "Daily Total Return",
        "siz_alias": "ret"
    },
    "dlyretdurflg": {
        "type": "Char",
        "length": "2",
        "description": "Daily Return Duration Flag. Provides additional information to describe the duration of a security return.",
        "mappings": {
            "D1": "1 Trading Day and 1 Calendar Day ",
            "D2": "1 Trading Day and 2 Calendar Days ",
            "D3": "1 Trading Day and 3 Calendar Days ",
            "D4": "1 Trading Day and 4 Calendar Days ",
            "DD": "Other Daily Delisting Return Duration ",
            "DU": "1 Trading Day & 5 or more Calendar Days ",
            "MR": "Missing Return ",
            "P1": "Multi-period 2 Trading Days or Months ",
            "P2": "Multi-period 3 Trading Days or Months ",
            "P3": "Multi-period 4 Trading Days or Months ",
            "P4": "Multi-period 5 Trading Days or Months ",
            "P5": "Multi-period 6 Trading Days or Months ",
            "P6": "Multi-period 7 Trading Days or Months ",
            "P7": "Multi-period 8 Trading Days or Months ",
            "P8": "Multi-period 9 Trading Days or Months ",
            "P9": "Multi-period 10 Trading Days or Months "
        }
    },
    "dlyreti": {
        "type": "Decimal",
        "length": "10.6",
        "description": "Daily Income Return"
    },
    "dlyretmissflg": {
        "type": "Char",
        "length": "2",
        "description": "Daily Return Missing Flag. Provides information about why a security return is missing. The most common value is NA, but common missing values are MP and NT.",
        "mappings": {
            "DG": "Delisting Price GT 10 periods from delisting date ",
            "DM": "Delisting Price/Amount Missing ",
            "DP": "Delisting Pending ",
            "GP": "Gap Between Prices Too Large ",
            "MP": "Missing Price ",
            "MV": "Missing Corporate Action Value ",
            "NA": "Not Applicable ",
            "NS": "New Security ",
            "NT": "Not Tracked ",
            "RA": "Return after Not Tracked period "
        }
    },
    "dlyretx": {
        "type": "Decimal",
        "length": "10.6",
        "description": "Daily Price Return",
        "siz_alias": "retx"
    },
    "dlyvol": {
        "type": "Decimal",
        "length": "14",
        "description": "Daily Volume",
        "siz_alias": "vol"
    },
    "ewretd": {
        "type": "Decimal",
        "length": "10.6",
        "description": "Equal-weighted return including dividends"
    },
    "ewretx": {
        "type": "Decimal",
        "length": "10.6",
        "description": "Equal-weighted return excluding dividends"
    },
    "exchangetier": {
        "type": "Char",
        "length": "3",
        "description": "Exchange Tier. Used to differentiate among the NASDAQ exchange tiers.",
        "mappings": {
            "G": "Global Market - formerly NMS - after 20060701 ",
            "N/A": "Not Applicable ",
            "NMS": "The NASDAQ National Market ",
            "Q": "Capital Market - formerly SmallCap-after 20060701 ",
            "S": "Global Select Market - new subset - after 20060701 ",
            "SC": "NASDAQ Small Cap Market on or after 19920615 ",
            "SC1": "The NASDAQ Small Cap Market before June 15, 1992 "
        }
    },
    "hdrcusip": {
        "type": "Char",
        "length": "8",
        "description": "Header CUSIP -8 Characters"
    },
    "hdrcusip9": {
        "type": "Char",
        "length": "9",
        "description": "Header CUSIP -9 Characters"
    },
    "icbindustry": {
        "type": "Char",
        "length": "7",
        "description": "ICB Industry Code. Mnemonic Code for the Industry Level of the ICB.",
        "mappings": {
            "BASMAT": "Basic Materials ",
            "CONDIS": "Consumer Discretionary ",
            "CONSTAP": "Consumer Staples ",
            "ENERGY": "Energy ",
            "FINL": "Financials ",
            "HEALTH": "Health Care ",
            "INDL": "Industrials ",
            "NOAVAIL": "Not Available ",
            "REIT": "Real Estate Investment Trusts ",
            "TECH": "Technology ",
            "TELECOM": "Telecommunications ",
            "UTIL": "Utilities "
        }
    },
    "issuernm": {
        "type": "Char",
        "length": "50",
        "description": "Issuer Name"
    },
    "issuertype": {
        "type": "Char",
        "length": "4",
        "description": "Issuer Type. Provides information about an issuer corporate type.",
        "mappings": {
            "ACOR": "Assumed Corporation ",
            "CORP": "Corporation ",
            "REIT": "REIT "
        }
    },
    "naics": {
        "type": "Char",
        "length": "6",
        "description": "NAICS Code"
    },
    "nasdcompno": {
        "type": "Int32",
        "description": "Nasdaq Company Number"
    },
    "nasdissuno": {
        "type": "Int32",
        "description": "Nasdaq Issue Number"
    },
    "permco": {
        "type": "Int32",
        "description": "PERMCO",
        "siz_alias": "permco"
    },
    "permno": {
        "type": "Int32",
        "description": "PERMNO",
        "siz_alias": "permno"
    },
    "primaryexch": {
        "type": "Char",
        "length": "1",
        "description": "Primary Exchange",
        "mappings": {
            "A": "NYSE American",
            "B": "BATS",
            "I": "IEX",
            "N": "NYSE",
            "Q": "NASDAQ",
            "R": "NYSE ARCA",
            "X": "Unknown"
        }
    },
    "secinfoenddt": {
        "type": "Date",
        "description": "Security Information End Date"
    },
    "secinfostartdt": {
        "type": "Date",
        "description": "Security Information Start Date"
    },
    "securityactiveflg": {
        "type": "Char",
        "length": "1",
        "description": "Security Active Flag",
        "mappings": {
            "N": "No",
            "Y": "Yes"
        }
    },
    "securitybegdt": {
        "type": "Date",
        "description": "Begin Date of Stock Data"
    },
    "securityenddt": {
        "type": "Date",
        "description": "End Date of Stock Data"
    },
    "securityhdrflg": {
        "type": "Char",
        "length": "1",
        "description": "Security Header Flag",
        "mappings": {
            "N": "No",
            "Y": "Yes "
        }
    },
    "securitynm": {
        "type": "Char",
        "length": "60",
        "description": "Security Name"
    },
    "securitysubtype": {
        "type": "Char",
        "length": "3",
        "description": "Security Sub-Type. Provides addition granularity to the security type code. Most securities are COM (Common), but ETF, CEF (Closed-End Fund) and others exist.",
        "mappings": {
            "ATR": "Americus Trust ",
            "CEF": "Closed End Fund ",
            "COM": "Common ",
            "ETF": "Exchange Traded Fund ",
            "ETV": "Exchange Traded Vehicle ",
            "UNK": "Unknown or Unspecified "
        }
    },
    "securitytype": {
        "type": "Char",
        "length": "4",
        "description": "Security Type. Provides a high level security type. This grain is sufficient for many uses, but more granularity is available in the security sub-type.",
        "mappings": {
            "DERV": "Derivative ",
            "EQTY": "Equity ",
            "FUND": "Fund ",
            "N/A": "Not Applicable "
        }
    },
    "shareclass": {
        "type": "Char",
        "length": "1",
        "description": "Share Class. Most securities are NONE.",
        "mappings": {
            "1": "Class 1 ",
            "A": "Class A ",
            "B": "Class B ",
            "C": "Class C ",
            "D": "Class D ",
            "E": "Class E ",
            "G": "Class G ",
            "H": "Class H ",
            "L": "Class L ",
            "N": "Class N ",
            "NCS": "No Class Specified ",
            "P": "Class P ",
            "S": "Class S ",
            "T": "Class T ",
            "U": "Class U ",
            "V": "Class V ",
            "Z": "Class Z "
        }
    },
    "sharetype": {
        "type": "Char",
        "length": "3",
        "description": "Share Type. Provides information about the security share type that can be used to select, exclude, or group securities.",
        "mappings": {
            "AD": "American Depositary Receipt ",
            "CE": "Certificate ",
            "N/A": "Not Applicable ",
            "NS": "No special share type specified ",
            "SB": "Shares of Beneficial Interest ",
            "UG": "Units General "
        }
    },
    "shradrflg": {
        "type": "Char",
        "length": "1",
        "description": "Share Adr Flag",
        "mappings": {
            "N": "No",
            "Y": "Yes"
        }
    },
    "shrenddt": {
        "type": "Date",
        "description": "Share Information End Date"
    },
    "shrfactype": {
        "type": "Char",
        "length": "2",
        "description": "Share Factor Type. Summarizes how many and what types distributions impact a security return.",
        "mappings": {
            "C1": "One Ordinary Cash Dividend ",
            "C2": "Two Ordinary Cash Dividends ",
            "CS": "One Cash Dividend & One Stock Split ",
            "D1": "One Delisting Action ",
            "D2": "Two Delisting Actions ",
            "F1": "One Share Factor - Non-Split ",
            "M2": "Two Corporate Actions ",
            "MU": "Multiple Corporate Actions ",
            "N1": "One Non-Ordinary ",
            "NA": "Not Applicable ",
            "NO": "No Corporate Actions ",
            "O1": "One 'Other' Action ",
            "P1": "One Price Factor - Non-Split ",
            "S1": "One Stock Split/Dividend ",
            "S2": "Two Stock Splits/Dividends ",
            "T1": "One (Tender) Offer Action "
        }
    },
    "shrout": {
        "type": "Int32",
        "description": "Shares Outstanding",
        "siz_alias": "shrout"
    },
    "shrsource": {
        "type": "Char",
        "length": "3",
        "description": "Share Change Source Type. Provides transparency into the source of the row in StkShares. These values are seldom used in calculations, but can be useful for summaries.",
        "mappings": {
            "EVS": "Split/Dividend Event ",
            "NC": "Name Change ",
            "OBS": "Observation From Source "
        }
    },
    "shrstartdt": {
        "type": "Date",
        "description": "Share Information Start Date"
    },
    "siccd": {
        "type": "Int32",
        "description": "Sic Code"
    },
    "sprtrn": {
        "type": "Decimal",
        "length": "10.6",
        "description": "Return on the S&P 500 Index"
    },
    "ticker": {
        "type": "Char",
        "length": "5",
        "description": "Ticker"
    },
    "tradingstatusflg": {
        "type": "Char",
        "length": "1",
        "description": "Trading Status Flag. Provides a user with the ability to select, exclude, and group by the trading status.",
        "mappings": {
            "A": "Active ",
            "D": "Delisted ",
            "H": "Halted ",
            "S": "Suspended ",
            "X": "Unknown or Unavailable "
        }
    },
    "tradingsymbol": {
        "type": "Char",
        "length": "7",
        "description": "Trading Symbol"
    },
    "uesindustry": {
        "type": "Char",
        "length": "10",
        "description": "Mnemonic Code for the Industry Level of the UES. Provides a mnemonic character value for the highest level (first two digits) of ICE's Industry Classification Benchmark.",
        "mappings": {
            "CONDIS": "Consumer Discretionary ",
            "CONSTAP": "Consumer Staples ",
            "ENERGY": "Energy ",
            "FINL": "Financials ",
            "HEALTH": "Healthcare ",
            "INDL": "Industrials ",
            "MATL": "Materials ",
            "MEDCOMM": "Media & Communications ",
            "NOAVAIL": "Not Available ",
            "QUASGOV": "Quasi Government ",
            "REIT": "Real Estate & REITS ",
            "SOVRN": "Sovereign ",
            "TECH": "Technology ",
            "TRUST": "Trust ",
            "UTIL": "Utilities "
        }
    },
    "usincflg": {
        "type": "Char",
        "length": "1",
        "description": "US Incorporation Flag",
        "mappings": {
            "N": "No ",
            "X": "Unavailable ",
            "Y": "Yes "
        }
    },
    "vwretd": {
        "type": "Decimal",
        "length": "10.6",
        "description": "Value-weighted return including dividends"
    },
    "vwretx": {
        "type": "Decimal",
        "length": "10.6",
        "description": "Value-weighted return excluding dividends"
    },
    "yyyymmdd": {
        "type": "Int32",
        "description": "YYYYMMDD - Daily Calendar Period Key"
    }
}
