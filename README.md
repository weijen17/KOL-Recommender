# KOL Recommender

- Recommend KOL based on celebrity attributes.

## Prerequisites

- Python 3.12+
- Docker and Docker Compose (for containerized deployment)
- Full KOL listing with designated attributes (excel)

## Setup

### Local Setup

1. Clone the repository:
```bash
git clone 
cd KOL-Recommender
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env and add your API keys
```

5. Run the application with celebrity attributes:
```bash
python main.py --性别 "男" --年龄 "00后" --国籍 "中国" --职业 "网红" --形象 "多才多艺" --粉丝性别 "女" --粉丝年龄 "25-29" --粉丝城市级别 "一线城市" --粉丝区域 "华东、华中" --粉丝省份 "北京市、上海市"
```

### Docker Setup

1. Set up environment variables:
```bash
cp .env.example .env
# Edit .env and add your API keys
`````

2. Build and run with Docker Compose:
```bash
docker-compose run --rm kol-recommender

or

docker-compose up --build
```

## Main Application Usage

1. Place your input KOL_Listing file (excel file) in **input/raw_data** directory. 
2. Amend env file accordingly, especially the INPUT_FILENAME which refers to the filename of KOL raw data.
3. Exexute main.py with **celebrity attributes**. 
```bash
python main.py --性别 "男" --年龄 "00后" --国籍 "中国" --职业 "网红" --形象 "多才多艺" --粉丝性别 "女" --粉丝年龄 "25-29" --粉丝城市级别 "一线城市" --粉丝区域 "华东、华中" --粉丝省份 "北京市、上海市"
```
4. After executing main.py, the **KOL Recommendation** result will be in **artifact/result** directory.

## Caveat

1. (Jaccard) Similarity score is calculated based on categorical features. Numerical(Continuous) feature is yet to be considered.
2. For your input KOL_Listing file reference, please refer to "KOL_Listing_Template.xlsx" in misc directory. The fields name must remain exactly the same as the template file, but the field value can be changed accordingly.

## Workflow

```
┌─────────────┐
│   Input     │──► KOL raw data that contain features in excel
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Sim Score   │──► KOL Jaccard Similarity score is calculated based on provided celebrity attribute.
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Result    │──► Output KOL recommendation result in excel
└─────────────┘
```


# File System Structure
```
project/
├── artifact/       # Generated outputs and intermediate artifacts (result)
│   ├── result/     # **KOL recommendation result**
├── input/          # Input data files
│   ├── raw_data/   # **KOL raw data*
├── logs/           # Logs
├── misc/           # Miscellaneous files, e.g., input template file
├── src/            # Source code
│   ├── recommender/     # Primary Recommender source code
│   ├── configs/    # Configuration files and environmental variables
└── tests/          # Test suites ongoing (boilerplate code, ignore)
```
