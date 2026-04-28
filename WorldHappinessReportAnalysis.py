import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

yearselect=[2015, 2016, 2017, 2018, 2019,2020,2021,2022,2023,2024,2025]
regionselect=["All", "Sub-Saharan Africa", "Middle East and Northern Africa", "Central and Eastern Europe", "Western Europe", "Eastern Asia", "Southeastern Asia", "Southern Asia", "Australia and New Zealand", "North America", "Latin America and Caribbean"]
st.set_page_config(layout="wide")

st.title("World Happiness Report Analysis")
st.write("_This analysis explores the World Happiness Report data from 2015 to 2025, providing insights into global happiness trends, regional differences, the factors that contribute to happiness levels across countries, and predict future scores._")
 
tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Factor Analysis", "Country Trends", "Forecasting"])
with tab1:
    col1, col2 = st.columns(2)
    with col1:
        year = st.selectbox("Select Year", yearselect, key="year1")
    with col2:
        region = st.selectbox("Select Region", regionselect, key="region1")

    file_name = f"{year}.csv"
    df = pd.read_csv(file_name)
    if region != "All":
        df = df[df["Region"] == region]
    st.subheader(f"World Happiness Index {year}")
    with st.expander("See Detailed Overview"):
        st.dataframe(df)
    if region == "All":
        st.write(f"_The total number of countries included in the analysis for the year {year} is **{len(df)}**._")
    if region != "All":
        st.write(f"_The total number of countries included in the analysis for the region of **{region}** in the year {year} is **{len(df)}**._")
    
    col5,col6,col7=st.columns(3)
    with col5:
        st.markdown("---")
        top_country = df.loc[df["Happiness Score"].idxmax(), "Country"]
        if region == "All" or (region != "All" and len(df) >= 20):
            st.header("Top 10 Happiest Countries")
            top10 = df.sort_values("Happiness Score", ascending=False).head(10)
            plt.figure(figsize=(6,4))
            plt.barh(top10["Country"], top10["Happiness Score"])
            plt.gca().invert_yaxis()
            plt.title(f"Top 10 Happiest Countries ({year})")
            plt.xlabel("Happiness Score")
            plt.ylabel("Country")
            st.pyplot(plt)
        if region == "All":
            st.write(f"_The happiest country in the world for the year {year} was **{top_country}**._")
        if region != "All":
            st.write(f"_The happiest country in the region of **{region}** for the year {year} was **{top_country}** with a happiness score of **{df['Happiness Score'].max():.2f}**._")
        if region == "All" or region == "Western Europe":
            def ordinal(n):
                if 10 <= n % 100 <= 20:
                    suffix = "th"
                else:
                    suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
                return str(n) + suffix
            years = [2015, 2016, 2017, 2018, 2019,2020,2021,2022,2023,2024,2025]
            happiest = {}
            for y in years:
                temp_df = pd.read_csv(f"{y}.csv")
                top = temp_df.loc[temp_df["Happiness Score"].idxmax(), "Country"]
                happiest[y] = top
            streak = {}
            prev_country = None
            count = 0
            for y in sorted(happiest.keys()):
                country = happiest[y]
                if country == prev_country:
                    count += 1
                else:
                    count = 1
                streak[y] = count
                prev_country = country
            year_selected = int(year)
            country = happiest[year_selected]
            n = streak[year_selected]
            if n > 1:
                st.write(f"_**{country}** has been ranked as the happiest for the {ordinal(n)} consecutive year._")
        st.markdown("---")
        lowest_country = df.loc[df["Happiness Score"].idxmin(), "Country"]
        if region == "All" or (region != "All" and len(df) >= 20):
            st.header("10 Least Happiest Countries")
            bottom10 = df.sort_values("Happiness Score", ascending=False).tail(10)
            plt.figure(figsize=(6,4))
            plt.barh(bottom10["Country"], bottom10["Happiness Score"])
            plt.gca().invert_yaxis()
            plt.title(f"10 Least Happiest Countries ({year})")
            plt.xlabel("Happiness Score")
            plt.ylabel("Country")
            st.pyplot(plt)
        if region == "All":
            st.write(f"_The least happy country in the world for the year {year} was **{lowest_country}**._")
        if region != "All":
            st.write(f"_The least happy country in the region of **{region}** for the year {year} was **{lowest_country}** with a happiness score of **{df['Happiness Score'].min():.2f}**._")
        if region == "All" or region == "Southern Asia":
            def ordinal(n):
                if 10 <= n % 100 <= 20:
                    suffix = "th"
                else:
                    suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
                return str(n) + suffix
            years = [2015, 2016, 2017, 2018, 2019,2020,2021,2022,2023,2024,2025]
            leasthappiest = {}
            for y in years:
                temp_df2 = pd.read_csv(f"{y}.csv")
                bottom = temp_df2.loc[temp_df2["Happiness Score"].idxmin(), "Country"]
                leasthappiest[y] = bottom
            streak = {}
            prev_country = None
            count = 0
            for y in sorted(leasthappiest.keys()):
                country = leasthappiest[y]
                if country == prev_country:
                    count += 1
                else:
                    count = 1
                streak[y] = count
                prev_country = country
            year_selected = int(year)
            country = leasthappiest[year_selected]
            n = streak[year_selected]
            if n > 1:
                st.write(f"_**{country}** has been ranked as the least happiest for the {ordinal(n)} consecutive year._")
    with col6:
        st.markdown("---")
        import matplotlib.ticker as mtick
        st.header("Average Happiness by Region")
        region_avg = df.groupby("Region")["Happiness Score"].mean()
        region_avg= region_avg.sort_values(ascending=False)
        if region == "All":
            plt.figure(figsize=(6,4))
            plt.barh(region_avg.index, region_avg.values)
            plt.gca().invert_yaxis()
            plt.title(f"Average Happiness by Region ({year})")
            plt.xlabel("Score")
            plt.ylabel("Region")
            st.pyplot(plt)
        if region != "All":
            plt.figure(figsize=(3,1))
            plt.barh(region_avg.index, region_avg.values)
            plt.gca().invert_yaxis()
            plt.title(f"Average Happiness by Region ({year})")
            plt.xlabel("Score")
            plt.ylabel("Region")
            st.pyplot(plt)
        q1 = df["Happiness Score"].quantile(0.25)
        q3 = df["Happiness Score"].quantile(0.75)
        if region != "All" and region_avg.values[0] > q3:
            st.write(f"_The average happiness score for the region **{region}** in the year {year} was **{region_avg.values[0]:.2f}**, which is one of the highest in the world._")
        elif region != "All" and region_avg.values[0] < q1:
            st.write(f"_The average happiness score for the region **{region}** in the year {year} was **{region_avg.values[0]:.2f}**, which is one of the lowest in the world._")
        elif region != "All" and region_avg.values[0] > q1 and region_avg.values[0] < q3:
            st.write(f"_The average happiness score for the region **{region}** in the year {year} was **{region_avg.values[0]:.2f}**, which is around the global average._")
        if region== "All":
            top_region =region_avg.idxmax()
            second_region = region_avg.index[1]
            third_region = region_avg.index[2]
            bottom_region =region_avg.idxmin()
            low_second_region = region_avg.index[8]
            low_third_region = region_avg.index[7]
            middle_first_region = region_avg.index[3]
            middle_second_region = region_avg.index[4]
            middle_third_region =region_avg.index[5]
            middle_fourth_region = region_avg.index[6]
        if region == "All" or region == "Sub-Saharan Africa":
            africa_df = df[df["Region"] == "Sub-Saharan Africa"]
            top_africa_country = africa_df.loc[
                africa_df["Happiness Score"].idxmax(), "Country"]
        if region == "All" or region == "Southern Asia":
            sa_df = df[df["Region"] == "Southern Asia"]
            top_south_asia = sa_df.loc[
            sa_df["Happiness Score"].idxmax(), "Country"]
        if region == "All" or region == "Southeastern Asia":
            se_asia_df = df[df["Region"] == "Southeastern Asia"]
            top_se_asia = se_asia_df.loc[
                se_asia_df["Happiness Score"].idxmax(), "Country"]
            lowest_se_asia = se_asia_df.loc[
                se_asia_df["Happiness Score"].idxmin(), "Country"]
        if region == "All" or region == "Middle East and Northern Africa":
            mena_df = df[df["Region"] == "Middle East and Northern Africa"]
            top_mena = mena_df.loc[
                mena_df["Happiness Score"].idxmax(), "Country"]
            bottom_mena = mena_df.loc[
            mena_df["Happiness Score"].idxmin(), "Country"]
        if region == "All" or region == "Central and Eastern Europe":   
            ce_europe_df = df[df["Region"] == "Central and Eastern Europe"]
            top_ce_europe = ce_europe_df.loc[
                ce_europe_df["Happiness Score"].idxmax(), "Country"]
        if region == "All" or region == "Western Europe":
            EU_df= df[df["Region"] == "Western Europe"]
            top_EU = EU_df.loc[
                EU_df["Happiness Score"].idxmax(), "Country"]
        if region == "All" or region == "Australia and New Zealand":
            ANZ_df= df[df["Region"] == "Australia and New Zealand"]             
            top_ANZ = ANZ_df.loc[
                ANZ_df["Happiness Score"].idxmax(), "Country"]
        if region == "All" or region == "North America":
            NA_df= df[df["Region"] == "North America"]  
            top_NA = NA_df.loc[
                NA_df["Happiness Score"].idxmax(), "Country"]
        if region == "All":
            with st.expander("See Insights"):
                st.write(f"_The region with the highest average happiness score in the world for the year {year} was **{top_region}** followed by **{second_region}** and **{third_region}**. The region includes countries such as **{top_NA}**, **{top_EU}**, and **{top_ANZ}**, which were among the top ranked countries in the world this year._")
                st.write(f"_The region with the lowest average happiness score in the world for the year {year} was **{bottom_region}** followed by **{low_second_region}** and **{low_third_region}**._")
                st.write(f"_The regions with average happiness scores in the middle include **{middle_first_region}**, **{middle_second_region}**, **{middle_third_region}**, and **{middle_fourth_region}**. These regions have a mix of countries with varying levels of happiness, with some countries performing well and others facing challenges that impact their happiness scores._")

        st.markdown("---")
        st.header("Variation in Happiness by Region")
        region_var = df.groupby("Region")["Happiness Score"].var()
        region_var=region_var.sort_values(ascending=False)
        if region == "All":
            plt.figure(figsize=(6,4))
            plt.barh(region_var.index, region_var.values)
            plt.gca().invert_yaxis()
            plt.title(f"Variation in Happiness by Region ({year})")
            plt.xlabel("Score")
            plt.ylabel("Region")
            st.pyplot(plt)
        if region != "All":
            plt.figure(figsize=(3,1))
            plt.barh(region_var.index, region_var.values)
            plt.gca().xaxis.set_major_formatter(mtick.FormatStrFormatter('%.2f'))
            plt.gca().invert_yaxis()
            plt.title(f"Variation in Happiness by Region ({year})")
            plt.xlabel("Score")
            plt.ylabel("Region")
            st.pyplot(plt)
        if region == "All":
            with st.expander("See Insights"):
                st.write(f"_The region with the highest variation in happiness scores in the world for the year {year} was **{region_var.idxmax()}** followed by **{region_var.index[1]}** and **{region_var.index[2]}**. This indicates a wide range of happiness levels within these regions, with some countries performing very well and others facing significant challenges that impact their happiness scores._")
                st.write(f"_The region with the lowest variation in happiness scores in the world for the year {year} was **{region_var.idxmin()}** followed by **{region_var.index[-2]}** and **{region_var.index[-3]}**. This suggests relatively less disparity in happiness levels among countries within these regions, with most countries having similar happiness scores._") 
                st.write(f"_The regions with moderate variation in happiness scores include **{region_var.index[3]}**, **{region_var.index[4]}**, **{region_var.index[5]}**, and **{region_var.index[6]}**._")
        full_df = pd.read_csv(file_name)
        if region != "All":
            df = full_df[full_df["Region"] == region]
        else:
            df = full_df
        full_region_var = full_df.groupby("Region")["Happiness Score"].var()
        q1_var = full_region_var.quantile(0.25)
        q3_var = full_region_var.quantile(0.75)
        if region != "All" and full_region_var.loc[region] > q3_var:
            st.write(f"_The variation in happiness scores in {region} is very high with a variance of  **{full_region_var.loc[region]:.2f}**._")    
        elif region != "All" and full_region_var.loc[region] < q1_var:
            st.write(f"_The variation of happiness scores in {region} is very low with a variance of  **{full_region_var.loc[region]:.2f}**._")
        elif region != "All" and full_region_var.loc[region] > q1_var and full_region_var.loc[region] < q3_var:
            st.write(f"_The variation of happiness scores in {region} is moderate with a variance of **{full_region_var.loc[region]:.2f}**._")
    with col7:
        st.markdown("---")
        import seaborn as sns
        st.header("Distribution of Happiness Scores")
        plt.figure(figsize=(5, 3))
        sns.histplot(
            df["Happiness Score"],
            kde=True,         
            bins=20
        )
        plt.xlabel("Happiness Score")
        plt.ylabel("Frequency")
        plt.title(f"Distribution of Happiness Scores ({year})")
        plt.tight_layout()
        st.pyplot(plt)
        if region == "All":
            mean = df["Happiness Score"].mean()
            median = df["Happiness Score"].median()
            std = df["Happiness Score"].std()
            if mean > median:
                shape = "right-skewed (more lower scores, few very high scores)"
            elif mean < median:
                shape = "left-skewed (more higher scores, few very low scores)"
            else:
                shape = "approximately symmetric"
            if std > 0.7:
                spread = "high variation"
            elif std > 0.4:
                spread = "moderate variation"
            else:
                spread = "low variation"
            with st.expander("See Insights"):
                    st.write(
                        f"_The distribution of happiness scores in {year} is **{shape}** with **{spread}**. "
                        f"The average score is **{mean:.2f}**, while the median is **{median:.2f}**, and the standard deviation is **{std:.2f}**, indicating how scores are spread across countries._")
        if region != "All":
            mean = df["Happiness Score"].mean()
            median = df["Happiness Score"].median()
            std = df["Happiness Score"].std()
            if mean > median:
                shape = "right-skewed (more lower scores, few very high scores)"
            elif mean < median:
                shape = "left-skewed (more higher scores, few very low scores)"
            else:
                shape = "approximately symmetric"
            if std > 0.7:
                spread = "high variation"
            elif std > 0.4:
                spread = "moderate variation"
            else:
                spread = "low variation"
            with st.expander("See Insights"):
                    st.write(f"_The distribution of happiness scores in the {region} for the year {year} is **{shape}** with **{spread}**. "
                f"The average score is **{mean:.2f}**, while the median is **{median:.2f}**, and the standard deviation is **{std:.2f}**, indicating how scores are spread across countries in the {region}._"
            )

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Top Country", top_country)
    c2.metric("Lowest Country", lowest_country)
    c3.metric("Average Score", round(df["Happiness Score"].mean(), 2))
    c4.metric("Countries", len(df))

with tab2:
    col3, col4 = st.columns(2)
    with col3:
        year2 = st.selectbox("Select Year", yearselect, key="year2")
    with col4:
        region2 = st.selectbox("Select Region", regionselect, key="region2")

    file_name = f"{year2}.csv"
    df = pd.read_csv(file_name)
    if region2 != "All":
        df = df[df["Region"] == region2]
    st.subheader(f"World Happiness Index {year2}")
    with st.expander("See Detailed Overview"):
        st.dataframe(df)
    if region2 == "All":
        st.write(f"_The total number of countries included in the analysis for the year {year2} is **{len(df)}**._")
    if region2 != "All":
        st.write(f"_The total number of countries included in the analysis for the region of **{region2}** in the year {year2} is **{len(df)}**._")

    col8, col9= st.columns(2)
    with col8:
        st.markdown("---")
        plt.figure(figsize=(6,4))
        st.header("Correlation Heatmap")
        sns.heatmap(df[['Happiness Score', 'Economy (GDP per Capita)','Freedom','Social Support','Generosity','Trust (Government Corruption)'
                        ,'Health (Life Expectancy)']].corr(),annot=True)
        plt.title(f"Happiness Scores {year2} Correlation Heatmap    ({region2})")
        st.pyplot(plt)
        with st.expander("See Insights"):
            st.write(f"_The correlation heatmap shows the relationships between the happiness score and various factors such as economy, freedom, social support, generosity, trust in government, and health that contribute to the overall happiness of a country._")
            corr = df[['Happiness Score', 'Economy (GDP per Capita)',
                    'Freedom','Social Support','Generosity',
                    'Trust (Government Corruption)',
                    'Health (Life Expectancy)']].corr()
            factors = {
                "Economy (GDP per Capita)": "GDP Per Capita",
                "Freedom": "Freedom",
                "Social Support": "Social support",
                "Generosity": "Generosity",
                "Trust (Government Corruption)": "Trust in government",
                "Health (Life Expectancy)": "Health (life expectancy)"
            }
            def classify(c):
                if c > 0.7:
                    return "strong positive"
                elif c > 0.3:
                    return "moderate positive"
                elif c > -0.3 and c < 0.3:
                    return "no"
                elif c < -0.7:
                    return "strong negative"
                elif c < -0.3:
                    return "moderate negative"

            for col, name in factors.items():
                c = corr.loc["Happiness Score", col]
                relation = classify(c)
                
                if region2 == "All":
                    st.write(f"_**{name}** has **{relation}** correlation with the Happiness Score._")
                else:
                    st.write(f"_**{name}** in the {region2} has **{relation}** correlation with the Happiness Score._")           

        st.markdown("---")
        import numpy as np
        st.header("Happiness Relation to Each Factor")
        plt.figure(figsize=(15, 10))
        x = df["Economy (GDP per Capita)"]
        y = df["Happiness Score"]
        m, b = np.polyfit(x, y, 1)
        plt.subplot(2,3,1)
        plt.scatter(x, y)
        plt.plot(x, m*x + b)
        plt.title(f"GDP per Capita vs Happiness Score in {year2}")
        plt.xlabel("GDP per Capita")
        plt.ylabel("Happiness Score")

        x = df["Freedom"]
        y = df["Happiness Score"]
        m, b = np.polyfit(x, y, 1)
        plt.subplot(2,3,2)
        plt.scatter(x, y)
        plt.plot(x, m*x + b)
        plt.title(f"Freedom vs Happiness Score in {year2}")
        plt.xlabel("Freedom")
        plt.ylabel("Happiness Score")

        x = df["Generosity"]
        y = df["Happiness Score"]
        m, b = np.polyfit(x, y, 1)
        plt.subplot(2,3,3)
        plt.scatter(x, y)
        plt.plot(x, m*x + b)
        plt.title(f"Generosity vs Happiness Score in {year2}")
        plt.xlabel("Generosity")
        plt.ylabel("Happiness Score")

        x = df["Health (Life Expectancy)"]
        y = df["Happiness Score"]
        m, b = np.polyfit(x, y, 1)
        plt.subplot(2,3,4)
        plt.scatter(x, y)
        plt.plot(x, m*x + b)
        plt.title(f"Life Expectancy vs Happiness Score in {year2}")
        plt.xlabel("Life Expectancy")
        plt.ylabel("Happiness Score")

        x = df["Social Support"]
        y = df["Happiness Score"]
        m, b = np.polyfit(x, y, 1)
        plt.subplot(2,3,5)
        plt.scatter(x, y)
        plt.plot(x, m*x + b)
        plt.title(f"Social Support vs Happiness Score in {year2}")
        plt.xlabel("Social Support")
        plt.ylabel("Happiness Score")

        x = df["Trust (Government Corruption)"]
        y = df["Happiness Score"]
        m, b = np.polyfit(x, y, 1)
        plt.subplot(2,3,6)
        plt.scatter(x, y)
        plt.plot(x, m*x + b)
        plt.title(f"Corruption Perception vs Happiness Score in {year2}")
        plt.xlabel("Corruption Perception")
        plt.ylabel("Happiness Score")
        st.pyplot(plt)
        with st.expander("See Insights"):
            st.write(f"_The scatter plots with trend lines show the relationships between happiness scores and various factors such as GDP per capita, freedom, generosity, health (life expectancy), social support, and trust in government. The strength and direction of these relationships can be observed from the plots._")
            def describe_relationship(x, y):
                corr = x.corr(y)
                if corr > 0.7:
                    strength_direction = "strong positive"
                elif corr > 0.3:
                    strength_direction = "moderate positive"
                elif corr > -0.3 and corr < 0.3:
                    strength_direction = "no clear"
                elif corr < -0.3:
                    strength_direction = "moderate negative"
                elif corr < -0.7:
                    strength_direction = "strong negative"
                return f"{strength_direction} relationship"
            factors = [
                "Economy (GDP per Capita)",
                "Freedom",
                "Generosity",
                "Health (Life Expectancy)",
                "Social Support",
                "Trust (Government Corruption)"
            ]
            for factor in factors:
                relation = describe_relationship(df[factor], df["Happiness Score"])
                if region2 == "All":
                    st.write(f"_**{factor}** shows a **{relation}** with the Happiness Score._")
                else:
                    st.write(f"_**{factor}** in the {region2} shows a **{relation}** with the Happiness Score._")
    with col9:
        st.markdown("---")
        st.header("Average Dystopia Residual by Region")
        if region2 == "All":
            plt.figure(figsize=(6,4))
            dystopia_region_avg= df.groupby("Region")["Dystopia Residual"].mean()
            dystopia_region_avg = dystopia_region_avg.sort_values(ascending=False)
            plt.barh(dystopia_region_avg.index, dystopia_region_avg.values)
            plt.gca().invert_yaxis()
            plt.title(f"Average Dystopia Residual by Region ({year2})")
            plt.xlabel("Dystopia Residual")
            plt.ylabel("Region")
            st.pyplot(plt)
            with st.expander("See Insights"):
                st.write(f"_The Dystopia Residual represents the portion of the happiness score that cannot be explained by the six factors. It can be interpreted as the baseline level of happiness that would exist in a hypothetical dystopian world where all other factors are at their minimum levels. A higher Dystopia Residual indicates that there are additional factors contributing to happiness that are not captured by the six variables, while a lower Dystopia Residual suggests that the six main factors explain most of the variation in happiness scores._")
                st.write(f"_The region with the highest average Dystopia Residual in the world for the year {year2} was **{dystopia_region_avg.idxmax()}** followed by **{dystopia_region_avg.index[1]}** and **{dystopia_region_avg.index[2]}**._")
                st.write(f"_The region with the lowest average Dystopia Residual in the world for the year {year2} was **{dystopia_region_avg.idxmin()}** followed by **{dystopia_region_avg.index[-2]}** and **{dystopia_region_avg.index[-3]}**._")                
        if region2 != "All":
            plt.figure(figsize=(3,1))
            dystopia_region_avg= df.groupby("Region")["Dystopia Residual"].mean()
            dystopia_region_avg = dystopia_region_avg.sort_values(ascending=False)
            plt.barh(dystopia_region_avg.index, dystopia_region_avg.values)
            plt.gca().invert_yaxis()
            plt.title(f"Average Dystopia Residual by Region ({year2})")
            plt.xlabel("Dystopia Residual")
            plt.ylabel("Region")
            st.pyplot(plt)
            with st.expander("See Insights"):
                st.write(f"_The Dystopia Residual represents the portion of the happiness score that cannot be explained by the six factors. It can be interpreted as the baseline level of happiness that would exist in a hypothetical dystopian world where all other factors are at their minimum levels. A higher Dystopia Residual indicates that there are additional factors contributing to happiness that are not captured by the six variables, while a lower Dystopia Residual suggests that the six main factors explain most of the variation in happiness scores._")
                st.write(f"_The average Dystopia Residual for the region of **{region2}** in the year {year2} was **{dystopia_region_avg.values[0]:.2f}**._")
        st.markdown("---")
        st.header("Average Contribution of Factors to Happiness Score")
        factors = [
            "Economy (GDP per Capita)",
            "Social Support",
            "Health (Life Expectancy)",
            "Freedom",
            "Trust (Government Corruption)",
            "Generosity",
        ]
        avg_values = df[factors].mean()
        plt.figure(figsize=(10, 6))
        plt.bar(avg_values.index, avg_values.values)
        plt.ylabel("Average Contribution")
        plt.xticks(rotation=45, ha='right')
        plt.title(f"Average Contribution of Factors to Happiness Score ({year2})")
        plt.tight_layout()
        st.pyplot(plt)
        descriptions = {
            factors[0]: "indicating that the economy is the very important factor influencing happiness levels",
            factors[1]: "suggesting that social support plays a crucial role in determining happiness levels",
            factors[2]: "highlighting the importance of health and life expectancy in influencing happiness levels",
            factors[3]: "emphasizing the significance of freedom in shaping happiness levels",
            factors[4]: "indicating that trust in government and low corruption are key factors influencing happiness levels",
            factors[5]: "suggesting that generosity and kindness play a significant role in determining happiness levels"
        }
        max_factor = avg_values.idxmax()
        min_factor = avg_values.idxmin()
        region_text = "across all countries" if region2 == "All" else f"in the {region2}"
        with st.expander("See Insights"):
            st.write(f"_The factor that contributes the most to happiness **{region_text}** is **{max_factor}** with an average of **{avg_values.max():.2f}**._")
            st.write(f"_The **{max_factor}** has the highest contribution, {descriptions[max_factor]}._")
            st.write(f"_The factor that contributes the least to happiness **{region_text}** is **{min_factor}** with an average of **{avg_values.min():.2f}**._")
            st.write(f"_The **{min_factor}** has the lowest contribution, meaning it has relatively less impact on happiness levels._")
        st.markdown("---")
        st.header("Dystopia Residual vs Six Factors Combined")
        df["Combined Factors"] = (
            df["Economy (GDP per Capita)"] +
            df["Freedom"] +
            df["Generosity"] +
            df["Health (Life Expectancy)"] +
            df["Social Support"] +
            df["Trust (Government Corruption)"]
        )
        avg_combined = df["Combined Factors"].mean()
        avg_dystopia = df["Dystopia Residual"].mean()
        labels = ["Combined Factors", "Dystopia Residual"]
        values = [avg_combined, avg_dystopia]
        plt.figure(figsize=(6,4))
        plt.bar(labels, values)
        plt.title(f"Average Contribution Dystopia Residual vs Six Factors Combined ({year2})")
        plt.ylabel("Average Value")
        st.pyplot(plt)
        if region2 == "All":
            if avg_combined-avg_dystopia >2:
                st.write(f"_The average contribution of the six factors combined is significantly higher than the average Dystopia Residual._")
            elif avg_combined-avg_dystopia >1:
                st.write(f"_The average contribution of the six factors combined is higher than the average Dystopia Residual._")
            elif avg_combined-avg_dystopia >0:
                st.write(f"_The average contribution of the six factors combined is slightly higher than the average Dystopia Residual._")
            else:
                st.write(f"_The average contribution of the six factors combined is lower than the average Dystopia Residual._")
        if region2 != "All":
            if avg_combined-avg_dystopia >2:
                st.write(f"_The average contribution of the six factors combined in the {region2} is significantly higher than the average Dystopia Residual._")
            elif avg_combined-avg_dystopia >1:
                st.write(f"_The average contribution of the six factors combined in the {region2} is moderately higher than the average Dystopia Residual._")
            elif avg_combined-avg_dystopia >0:
                st.write(f"_The average contribution of the six factors combined in the {region2} is slightly higher than the average Dystopia Residual._")
            else:
                st.write(f"_The average contribution of the six factors combined in the {region2} is lower than the average Dystopia Residual._")

    c5, c6,c7= st.columns(3)
    c5.metric("Average Dystopia Residual", round(df["Dystopia Residual"].mean(), 2))
    c6.metric("Average Score for Combined Factors", round(df["Combined Factors"].mean(), 2))
    c7.metric("Countries", len(df))

with tab3:
    years = [2015, 2016, 2017, 2018, 2019,2020,2021,2022,2023,2024,2025]
    st.header(f"Happiness Score Trends Over Time from {years[0]} to {years[-1]}")
    df1 = []

    for year in years:
        df = pd.read_csv(f"{year}.csv")
        df["Year"] = year
        df1.append(df)
    combined_df = pd.concat(df1, ignore_index=True)
    col12,col13= st.columns(2)
    with col12:
        country = st.selectbox("Select Country", combined_df["Country"].unique())
    country_data = combined_df[combined_df["Country"] == country]
    country_data = country_data.sort_values("Year")
    import plotly.express as px
    fig = px.line(
        country_data,
        x="Year",
        y="Happiness Score",
        markers=True,
        title=f"Happiness Trend for {country}"
    )
    st.plotly_chart(fig)
    country_data = combined_df[combined_df["Country"] == country]
    country_data = country_data.sort_values("Year")
    peak_year = country_data.loc[country_data["Happiness Score"].idxmax(), "Year"]
    peak_score = country_data["Happiness Score"].max()
    lowest_year = country_data.loc[country_data["Happiness Score"].idxmin(), "Year"]
    lowest_score = country_data["Happiness Score"].min()
    st.markdown("---")
    with st.expander("See Insights"):
        st.write(
            f"_The highest happiness score for **{country}** was recorded in **{peak_year}** "
            f"with a score of **{peak_score:.2f}**._"
        )
        st.write(
            f"_The lowest happiness score for **{country}** was recorded in **{lowest_year}** "
            f"with a score of **{lowest_score:.2f}**._"
        )
with tab4:
    col10, col11= st.columns(2)
    with col10:
        st.header("Happiness Score Prediction (2026-2029)")
        from sklearn.linear_model import LinearRegression
        from sklearn.model_selection import train_test_split
        from sklearn.metrics import mean_squared_error, r2_score
        year1 = [2015, 2016, 2017, 2018, 2019,2020,2021,2022,2023,2024,2025]
        df2 = {}
        def load_data():
            for years in year1:
                df = pd.read_csv(f"{years}.csv")
                df = df[['Country', 'Happiness Score']]
                df.columns = ['Country', f'Score_{years}']
                df2[years] = df
            return df2
        df2 = load_data()
        df_merged = df2[2015]
        for years in year1[1:]:
            df_merged = df_merged.merge(df2[years], on='Country')
        st.subheader("Happiness Scores from 2015 to 2025")
        with st.expander("See Scores"):
            st.dataframe(df_merged.head(160))
        data=[]
        for _, row in df_merged.iterrows():
            scores = [row[f'Score_{years}'] for years in year1]
            for i in range(len(scores) - 3):
                X = scores[i:i+3]      
                y = scores[i+3]        
                data.append(X + [y])
        df_model = pd.DataFrame(data, columns=['t1', 't2', 't3', 'target'])
        X = df_model[['t1', 't2', 't3']]
        y = df_model['target']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42 )
        model = LinearRegression()
        model.fit(X_train, y_train)
        predictions = []
        for _, row in df_merged.iterrows():
            s1 = row['Score_2023']
            s2 = row['Score_2024']
            s3 = row['Score_2025']
            pred_2026 = model.predict([[s1, s2, s3]])[0]
            pred_2027 = model.predict([[s2, s3, pred_2026]])[0]
            pred_2028 = model.predict([[s3, pred_2026, pred_2027]])[0]
            pred_2029 = model.predict([[pred_2026, pred_2027, pred_2028]])[0]
            predictions.append({
                'Country': row['Country'],
                '2026': pred_2026,
                '2027': pred_2027,
                '2028': pred_2028,
                '2029': pred_2029
            })
        df_predictions = pd.DataFrame(predictions)
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        st.markdown("---")
        st.subheader("Model Performance")
        with st.expander("See Model Performance"):
                st.write(f"**Mean Squared Error:** {mse:.3f}")
                st.write(f"**R² Score:** {r2:.3f}")
        with st.expander("See Model Explanation"):
                st.write("""
                The model uses Linear Regression to predict future happiness scores 
                based on the previous three years.

                A train-test split is used to evaluate performance:
                - R² score shows how well the model explains the data
                - MSE shows prediction error

                Higher R² and lower MSE indicate better performance.
                """)
    with col11:
        st.markdown("---")
        st.subheader("Predicted Happiness Score for 2026-2029")
        with st.expander("See Scores"):
            st.dataframe(df_predictions.head(160))
        years_pred = ["2026", "2027", "2028", "2029"]
        for y in years_pred:
            top_country = df_predictions.loc[df_predictions[y].idxmax(), "Country"]
            bottom_country = df_predictions.loc[df_predictions[y].idxmin(), "Country"]
            st.write(f"**{y}:** The happiest country might become **{top_country}**, while the least happy country might become **{bottom_country}**.")
        st.markdown("---")
        country = st.selectbox("Select Country", df_predictions['Country'])
        selected = df_predictions[df_predictions['Country'] == country]
        st.write("Prediction for selected country:")
        st.dataframe(selected)