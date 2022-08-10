# Task 
Buying a house in the UK incurs a tax which varies according to the price of the house and circumstances of the purchaser e.g. a higher rate is paid if you are buying a second home. In Scotland this is called Land and Buildings Transaction Tax (LBTT), but you may know it as Stamp Duty (The equivalent tax in England). 
 
We need you to write a piece of code which given the price of a house will calculate the LBBT due to be paid. A key part of any technical project is gaining understanding in unfamiliar business domains, for this reason we do not include how to calculate LBTT as part of this specification. LBTT can be complex to calculate as it varies according to the circumstances of the buyer so for simplicity you may assume: 
* The buyer of the house currently owns a property and lives in it as their main residence 
* The buyer does not conduct any kind of business activity from their house i.e. it is purely for personal use 
* The buyer does not own any other properties 
* At the end of the purchase the buyer will still only own one house i.e. they intent to sell their current home at the same date they buy the new one 
Note: Across the UK changes to how this tax is calculated have been made recently, or in the case of Scotland are being changed this week. We are happy for you to use the old or the new calculation but advise you use as the older one as it is simpler to understand and information more readily available. You will not be penalised in any way for whichever version you implement. 

# Calculating LBTT
_From https://www.gov.scot/policies/taxes/land-and-buildings-transaction-tax/_

Residential LBTT
The residential LBTT rates and bands are set out in the table below. As confirmed in the Scottish Budget, these will remain unchanged in 2022-23.

| Purchase price       | LBTT rate |
|----------------------|-----------|
| Up to £145,000       | 0%        |
| £145,001 to £250,000 | 2%        |
| £250,001 to £325,000 | 5%        |
| £325,001 to £750,000 | 10%       |
| Over £750,000        | 12%       |

First-time buyers
A relief for first-time buyers is available, which increases the residential nil rate band of LBTT to £175,000.

The relief will result in a reduction in tax payable of up to £600 for qualifying first-time buyers.

More information, including first-time buyer FAQs, is available on the Revenue Scotland website.

Additional dwelling supplement
The LBTT Additional Dwelling Supplement (ADS) came into force on 1 April 2016. The ADS is charged at 4%, and is payable on the total purchase price of an additional dwelling if the relevant consideration (usually the purchase price) is £40,000 or more.

The ADS is an important element of the Scottish Government’s drive to protect opportunities for first-time buyers in Scotland, reinforcing the progressive approach in place for LBTT rates and bands.

Further information and guidance regarding the ADS is available on the Revenue Scotland website.

# Expectations
Expectations on the code 
We are looking for you to prepare a start-for-ten codebase which we can do some pair programming to add functionality. At a minimum the code should: 
* Compile without errors 
* Have Unit tests which are runnable (either via an IDE or command line) 
* Have Units tests which pass 

In order to assist in keeping the functionality as simple as possible the Unit tests do not need to cover all possible scenarios, simply that they pass for the scenario they cover in your code e.g. if you only have code which works for a certain price range of house then only this needs to be covered in the tests.

For the pair programming to be achievable in a small-time frame we ask you do not move far beyond this minimum e.g. adding a UI or other ancillary capabilities. The pair programming will focus on adding more logic to the LBBT calculation, so anything extra will be a wasted effort on your part, or worse could get in the way of achieving the task. 
