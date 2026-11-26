# Annual Report RAG Evaluation Dataset

**Sources** - S&P Global -- Annual Report 2025
(`annual-report-2025.pdf`) - Amazon -- Annual Report 2025
(`Amazon-2025-Annual-Report.pdf`)

**Total:** 30 questions --- 15 from each report.

> Page numbers below refer to PDF page positions, as listed in the
> evaluation set.

## 1. Easy questions (10)

  ---------------------------------------------------------------------------------------
            \# Source    Question      Correct answer     PDF page Difficulty   Type
  ------------ --------- ------------- -------------- ------------ ------------ ---------
             1 S&P       What was the  Revenue:                  2 Easy         Single
               Global    company's     **\$15,336**                             figure
                         revenue in    (in millions).                           
                         2025?                                                  

             2 S&P       What were the **\$17.83**               2 Easy         Single
               Global    adjusted                                               figure
                         diluted                                                
                         earnings per                                           
                         common share                                           
                         in 2025?                                               

             3 S&P       What was the  **\$13,088**              2 Easy         Single
               Global    company's     (in millions).                           figure
                         total debt at                                          
                         the end of                                             
                         2025?                                                  

             4 S&P       How much      **\$3.84**                2 Easy         Single
               Global    dividend was                                           figure
                         paid per                                               
                         common share                                           
                         in 2025?                                               

             5 S&P       On what date  **April 29,              12 Easy         Single
               Global    did the       2025**                                   figure
                         company                                                
                         announce its                                           
                         decision to                                            
                         separate its                                           
                         Mobility                                               
                         segment?                                               

             6 Amazon    What was      **\$717                   8 Easy         Single
                         Amazon's      billion**                                figure
                         total revenue                                          
                         in 2025?                                               

             7 Amazon    How many      **over one                3 Easy         Single
                         robots were   million                                  figure
                         operating in  robots**                                 
                         Amazon's                                               
                         fulfillment                                            
                         centers?                                               

             8 Amazon    How much has  **over \$4                3 Easy         Single
                         Amazon        billion**                                figure
                         committed to                                           
                         expanding its                                          
                         rural                                                  
                         delivery                                               
                         network?                                               

             9 Amazon    How many      **more than               3 Easy         Single
                         satellites    200                                      figure
                         had Amazon    satellites**                             
                         put into                                               
                         space for its                                          
                         low Earth                                              
                         orbit                                                  
                         network?                                               

            10 Amazon    How much new  **3.9                     5 Easy         Single
                         power         gigawatts                                figure
                         capacity did  ("GW")**                                 
                         AWS add in                                             
                         2025?                                                  
  ---------------------------------------------------------------------------------------

## 2. Medium questions (10)

  ------------------------------------------------------------------------------------------------------
            \# Source    Question            Correct answer          PDF page Difficulty   Type
  ------------ --------- ------------------- ------------------- ------------ ------------ -------------
            11 S&P       Compare the         Revenue: 2025                 13 Medium       Table lookup
               Global    company's revenue,  **\$15,336**, 2024                            
                         operating profit    **\$14,208**, 2023                            
                         and diluted         **\$12,497**.                                 
                         earnings per share  Operating profit:                             
                         for 2023, 2024 and  2025 **\$6,478**,                             
                         2025.               2024 **\$5,580**,                             
                                             2023 **\$4,020**.                             
                                             Diluted earnings                              
                                             per share: 2025                               
                                             **\$14.66**, 2024                             
                                             **\$12.35**, 2023                             
                                             **\$8.23**.                                   

            12 S&P       How was 2025        Subscription                  15 Medium       Table lookup
               Global    revenue distributed revenue: **\$7,865                            
                         across the          (51%)**;                                      
                         different revenue   Non-subscription /                            
                         categories, and     transaction                                   
                         what percentage did revenue: **\$3,144                            
                         each category       (21%)**;                                      
                         contribute?         Non-transaction                               
                                             revenue: **\$2,054                            
                                             (13%)**;                                      
                                             Asset-linked fees:                            
                                             **\$1,206 (8%)**;                             
                                             Sales usage-based                             
                                             royalties: **\$444                            
                                             (3%)**; Recurring                             
                                             variable: **\$623                             
                                             (4%)**.                                       

            13 S&P       Compare U.S. and    U.S. revenue: 2025            15 Medium       Table lookup
               Global    international       **\$9,322**, 2024                             
                         revenue in 2025 and **\$8,640**;                                  
                         2024, including     International                                 
                         their percentage of revenue: 2025                                 
                         total revenue.      **\$6,014**, 2024                             
                                             **\$5,568**. U.S.                             
                                             revenue represented                           
                                             **61%** of total                              
                                             revenue in both                               
                                             years, while                                  
                                             international                                 
                                             revenue represented                           
                                             **39%** in both                               
                                             years.                                        

            14 S&P       How did             Market                        17 Medium       Table lookup
               Global    operating-related   Intelligence:                                 
                         expenses and        operating-related                             
                         selling and general **\$2,082 /                                   
                         expenses change     \$2,016**, selling                            
                         across the five     and general                                   
                         business segments   **\$1,215 /                                   
                         between 2024 and    \$1,186**. Ratings:                           
                         2025?               **\$1,072 /                                   
                                             \$1,033**, **\$607                            
                                             / \$593**. Energy:                            
                                             **\$735 / \$701**,                            
                                             **\$483 / \$459**.                            
                                             Mobility: **\$530 /                           
                                             \$487**, **\$519 /                            
                                             \$493**. Indices:                             
                                             **\$271 / \$245**,                            
                                             **\$265 / \$237**.                            
                                             Values are 2025 /                             
                                             2024, in millions.                            

            15 S&P       Compare reported    Reported: Net                  9 Medium       Table lookup
               Global    net income          income attributable                           
                         attributable to S&P to SPGI                                       
                         Global and diluted  **\$4,471**,                                  
                         EPS with their      diluted EPS                                   
                         adjusted values in  **\$14.66**.                                  
                         2025.               Adjusted: Net                                 
                                             income attributable                           
                                             to SPGI                                       
                                             **\$5,441**,                                  
                                             diluted EPS                                   
                                             **\$17.83**.                                  

            16 Amazon    Compare the         North America: 2024           26 Medium       Table lookup
                         operating income of **\$24,967**, 2025                            
                         North America,      **\$29,619**.                                 
                         International and   International: 2024                           
                         AWS in 2024 and     **\$3,792**, 2025                             
                         2025. Which segment **\$4,750**. AWS:                             
                         had the highest     2024 **\$39,834**,                            
                         operating income in 2025 **\$45,606**.                            
                         2025?               Consolidated: 2024                            
                                             **\$68,593**, 2025                            
                                             **\$79,975**. AWS                             
                                             had the highest                               
                                             operating income.                             
                                             (In millions.)                                

            17 Amazon    Compare the total   North America:                67 Medium       Table lookup
                         assets of the three **\$196,029 to                                
                         operating segments  \$235,652**;                                  
                         between 2023 and    International:                                
                         2025. Which segment **\$69,718 to                                 
                         experienced the     \$81,984**; AWS:                              
                         largest increase?   **\$108,533 to                                
                                             \$252,588**. AWS                              
                                             experienced the                               
                                             largest increase.                             
                                             (In millions.)                                

            18 Amazon    What were the total 2026: **\$51,666**;           59 Medium       Table lookup
                         contractual         2027: **\$46,259**;                           
                         commitments for     2028: **\$36,084**;                           
                         each year from 2026 2029: **\$32,019**;                           
                         through 2030, and   2030: **\$32,153**;                           
                         thereafter?         Thereafter:                                   
                                             **\$241,480**.                                
                                             Total commitments:                            
                                             **\$439,661**. (In                            
                                             millions.)                                    

            19 Amazon    How much did        2025: **\$79,975**;           26 Medium       Calculation
                         consolidated        2024: **\$68,593**.                           
                         operating income    Calculation:                                  
                         increase between    \$79,975 − \$68,593                           
                         2024 and 2025, in   = **\$11,382                                  
                         millions?           million**.                                    

            20 Amazon    How much did total  2025:                         67 Medium       Calculation
                         net additions to    **\$142,352**;                                
                         property and        2024: **\$85,752**.                           
                         equipment increase  Calculation:                                  
                         between 2024 and    \$142,352 −                                   
                         2025, in millions?  \$85,752 =                                    
                                             **\$56,600                                    
                                             million**.                                    
  ------------------------------------------------------------------------------------------------------

## 3. Hard questions (10)

  ------------------------------------------------------------------------------------------------
            \# Source    Question        Correct answer         PDF page Difficulty   Type
  ------------ --------- --------------- ------------------ ------------ ------------ ------------
            21 S&P       How did the     The report states:       13, 15 Hard         Vague
               Global    company do this **"Revenue                                   
                         year?           increased 8%                                 
                                         driven by                                    
                                         increases at all                             
                                         of our reportable                            
                                         segments."** It                              
                                         also reports that                            
                                         operating profit                             
                                         increased **16%**,                           
                                         net income                                   
                                         increased **16%**,                           
                                         and diluted                                  
                                         earnings per share                           
                                         increased **19%**                            
                                         compared with                                
                                         2024.                                        

            22 S&P       What were the   Revenue growth was       13--14 Hard         Narrative
               Global    main factors    driven by                                    
                         behind the      increases across                             
                         company's       all reportable                               
                         revenue growth  segments. Ratings                            
                         during the      benefited from                               
                         year?           growth in                                    
                                         transaction and                              
                                         non-transaction                              
                                         revenue. Market                              
                                         Intelligence                                 
                                         benefited from                               
                                         subscription                                 
                                         revenue growth and                           
                                         acquisitions.                                
                                         Energy benefited                             
                                         from continued                               
                                         demand for market                            
                                         data and market                              
                                         insights. Mobility                           
                                         benefited from                               
                                         Dealer and                                   
                                         Financial business                           
                                         growth. Indices                              
                                         benefited from                               
                                         higher                                       
                                         asset-linked fees,                           
                                         exchange-traded                              
                                         derivative revenue                           
                                         and data                                     
                                         subscription                                 
                                         revenue.                                     

            23 S&P       What changes is The company               14, 7 Hard         Multi-part
               Global    the company     describes three                              
                         making to       strategic                                    
                         improve its     objectives:                                  
                         operations and  **Advance market                             
                         prepare for     leadership**,                                
                         future growth?  **Expand                                     
                                         high-growth                                  
                                         adjacencies**, and                           
                                         **Amplify                                    
                                         Enterprise                                   
                                         Capabilities and                             
                                         AI**. It also                                
                                         describes an                                 
                                         integrated                                   
                                         operating model                              
                                         designed to remove                           
                                         silos, investments                           
                                         in AI, strategic                             
                                         collaborations,                              
                                         expansion of                                 
                                         differentiated                               
                                         data sets, and                               
                                         improvements in                              
                                         productivity and                             
                                         risk management.                             

            24 S&P       What could      The report states:           14 Hard         Narrative
               Global    prevent the     **"There can be no                           
                         company from    assurance that we                            
                         achieving its   will achieve                                 
                         strategic       success in                                   
                         objectives?     implementing any                             
                                         one or more of                               
                                         these strategies                             
                                         as a variety of                              
                                         factors could                                
                                         unfavorably impact                           
                                         operating results,                           
                                         including                                    
                                         prolonged                                    
                                         difficulties in                              
                                         the global credit                            
                                         markets and a                                
                                         change in the                                
                                         regulatory                                   
                                         environment                                  
                                         affecting our                                
                                         businesses."**                               

            25 S&P       What major      On April 29, 2025,           12 Hard         Multi-part
               Global    business        the Board decided                            
                         restructuring   to pursue a full                             
                         is planned, and separation of the                            
                         what is the     Mobility segment,                            
                         expected        creating a new                               
                         timeline?       publicly traded                              
                                         company. The                                 
                                         transaction is                               
                                         expected to be                               
                                         implemented                                  
                                         through a spin-off                           
                                         of shares to S&P                             
                                         Global                                       
                                         shareholders and                             
                                         is expected to be                            
                                         completed                                    
                                         **mid-2026**,                                
                                         subject to                                   
                                         customary legal                              
                                         and regulatory                               
                                         requirements and                             
                                         approvals.                                   

            26 Amazon    How did the     Amazon's revenue              8 Hard         Vague
                         company do this grew **12%                                   
                         year?           year-over-year                               
                                         ("YoY") from \$638                           
                                         billion to \$717                             
                                         billion**.                                   
                                         Operating income                             
                                         improved **17%                               
                                         YoY, from \$69                               
                                         billion ... to                               
                                         \$80 billion**.                              
                                         Free Cash Flow                               
                                         decreased **from                             
                                         \$38 billion to                              
                                         \$11 billion**,                              
                                         primarily driven                             
                                         by increased                                 
                                         purchases of                                 
                                         property and                                 
                                         equipment.                                   

            27 Amazon    Why is the      **"Free Cash Flow             8 Hard         Vague
                         company         decreased from                               
                         generating less \$38 billion to                              
                         free cash flow  \$11 billion,                                
                         despite its     driven primarily                             
                         improved        by a                                         
                         operating       year-over-year                               
                         income?         increase of \$50.7                           
                                         billion in                                   
                                         purchases of                                 
                                         property and                                 
                                         equipment, net of                            
                                         proceeds from                                
                                         sales and                                    
                                         incentives. This                             
                                         FCF change                                   
                                         primarily reflects                           
                                         capex investments                            
                                         in artificial                                
                                         intelligence."**                             

            28 Amazon    What major      The company                3--6 Hard         Multi-part
                         investments is  describes                                    
                         the company     investments in                               
                         making to       robotics to                                  
                         support its     improve delivery                             
                         future growth,  speed, reduce                                
                         and what        costs and automate                           
                         customer        fulfillment                                  
                         problems are    activities; rural                            
                         these           delivery expansion                           
                         investments     to serve remote                              
                         intended to     communities;                                 
                         solve?          Amazon Leo to                                
                                         improve broadband                            
                                         connectivity; and                            
                                         AI infrastructure                            
                                         through AWS. It                              
                                         also describes                               
                                         investments in                               
                                         custom chips, data                           
                                         centers and                                  
                                         networking                                   
                                         infrastructure to                            
                                         support AI demand.                           

            29 Amazon    What factors    The report                   31 Hard         Narrative
                         could           identifies risks                             
                         negatively      including                                    
                         affect the      fluctuations in                              
                         company's       foreign exchange                             
                         future          rates and energy                             
                         performance?    prices, changes in                           
                                         global economic                              
                                         conditions, tariff                           
                                         and trade                                    
                                         policies, resource                           
                                         and supply                                   
                                         volatility,                                  
                                         customer demand                              
                                         and spending,                                
                                         inflation,                                   
                                         interest rates,                              
                                         labor constraints,                           
                                         world events,                                
                                         competition,                                 
                                         litigation,                                  
                                         government                                   
                                         investigations,                              
                                         inventory                                    
                                         management,                                  
                                         fulfillment                                  
                                         productivity and                             
                                         geopolitical                                 
                                         conditions.                                  

            30 Amazon    What is the     The report          3--4, 6, 31 Hard         Vague
                         company doing   describes efforts                            
                         to make its     to lower prices,                             
                         services more   improve                                      
                         useful and      availability,                                
                         convenient for  offer faster                                 
                         customers?      delivery, increase                           
                                         selection, improve                           
                                         reliability and                              
                                         earn customer                                
                                         trust. It also                               
                                         discusses Same-Day                           
                                         Delivery, Prime                              
                                         Air, Amazon Now,                             
                                         Amazon Leo,                                  
                                         robotics and                                 
                                         AI-enabled                                   
                                         customer                                     
                                         experiences.                                 
  ------------------------------------------------------------------------------------------------

## Evaluation notes

-   Questions 21, 26 and 27 are useful for testing retrieval across
    multiple sections.
-   Questions 22, 28 and 29 test narrative retrieval and synthesis.
-   Questions 12--18 test multi-column table retrieval.
-   Questions 21, 26, 27, 30 and other broad prompts test vague
    natural-language queries.
-   Calculation answers are derived from figures stated in the PDFs;
    they are not necessarily quoted as pre-calculated values in the
    reports.

**Important:** Before using this as a scored benchmark, independently
verify each answer and page reference against the source PDFs. In
particular, distinguish printed report page numbers from PDF viewer page
positions.
