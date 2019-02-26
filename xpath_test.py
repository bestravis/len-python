from lxml import etree
import requests

str='''
<div class="el">
    <p class="t1 ">
        <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
        <input class="checkbox" type="checkbox" name="delivery_jobid" value="102953363" jt="0" style="display:none">
        <span>
            <a target="_blank" title="数据挖掘工程师" href="https://jobs.51job.com/shanghai-jaq/102953363.html?s=01&amp;t=0" onmousedown="">
                数据挖掘工程师                                </a>
        </span>
                                                            </p>
    <span class="t2"><a target="_blank" title="上海裕宁信息科技有限公司" href="https://jobs.51job.com/all/co4085855.html">上海裕宁信息科技有限公司</a></span>
    <span class="t3">上海-静安区</span>
    <span class="t4">1-2万/月</span>
    <span class="t5">01-19</span>
</div>
<div class="el">
    <p class="t1 ">
        <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
        <input class="checkbox" type="checkbox" name="delivery_jobid" value="102953363" jt="0" style="display:none">
        <span>
            <a target="_blank" title="数据挖掘工程师" href="https://jobs.51job.com/shanghai-jaq/102953363.html?s=01&amp;t=0" onmousedown="">
                13434                                </a>
        </span>
                                                            </p>
    <span class="t2"><a target="_blank" title="上海裕宁信息科技有限公司" href="https://jobs.51job.com/all/co4085855.html">上海裕宁信息科技有限公司</a></span>
    <span class="t3">上海-111</span>
    <span class="t4">1-222万/月</span>
    <span class="t5">01-19</span>
</div>
'''
str = etree.HTML(str)

foo=str.xpath('//div[@class="el"]/./descendant::*')
print(foo)


    



    