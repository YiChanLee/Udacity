"""

You should try to optimize your code from PS3-2 to get the correct
answer in as few steps as possible.

We will be hosting a scoreboard along with additional test cases
from both us and other students on our forums. Go check it out!

"""

test_cases = ['<vbox><listbox rows="2"><listitem label="listitem"/><listitem><html:input type="checkbox" style="margin:0px;"/></listitem></listbox></vbox>',
              '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html;charset=utf-8"><title>wushi0016</title><script type="text/javascript">function goodbye() {nodeList = document.getElementsByTagName("input");testNode = nodeList.item(0);testNode.type = "yabba-dabba-do";return testNode.blur();}</script></head><body onload="goodbye()"><input type="file" /></body></html>',
              '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd"><html lang="en"><head></head><body><p><b>BUG ID:</b> <a href="http://bugs.webkit.org/show_bug.cgi?id=3855">Bugzilla Bug 3855</a> Table with Form Field and Hidden DIV crashes Safari</p><p id="test" style="background-color:skyblue; padding:3px;"><b>STEPS TO TEST:</b>Type in the text field below.</p><p id="success" style="background-color:palegreen; padding:3px;"><b>TEST PASS:</b>Safari will not crash, text will show up in text field as expected.</p><p id="failure" style="background-color:#FF3300; padding:3px;"><b>TEST FAIL:</b>Safari will crash.</p>Type in the input field below:<form><div style="display:none;"><table><tr><td>test</td></tr></table></div><input type="text" value="" /></form></body></html>',
              '<form name="changeform" id="changeform" method="post" action="process_bug.cgi"><input type="hidden" name="delta_ts" value="2007-04-26 07:34:56"><input type="hidden" name="longdesclength" value="8"><input type="hidden" name="id" value="356999"><input type="hidden" name="token" value="1346633823-befc508ae6f90d359299be7ea39c463a"><div class="bz_alias_short_desc_container edit_form"><span class="last_comment_link"><a href="#c7" accesskey="l"><b>L</b>ast Comment</a></span><a href="show_bug.cgi?id=356999"><b>Bug&nbsp;356999</b></a> -<span id="summary_alias_container" class="bz_default_hidden"> <span id="short_desc_nonedit_display">&lt;html:input type=&quot;text&quot;&gt; inside scaled &lt;svg:foreignObject&gt; is horribly broken</span></span><div id="summary_alias_input"><table id="summary"><td colspan="2">          </td>        </tr><tr><td><label accesskey="s" for="short_desc"><u>S</u>ummary</label>:</td><td>&lt;html:input type=&quot;text&quot;&gt; inside scaled &lt;svg:foreignObject&gt; is horribly broken          </td>        </tr>      </table>    </div>  </div><input type="range" value="2" min="-5" max="5" step="1"></form>',
              '<div id="content">     <div class="indent-main">        <div class="indent">            <div class="container">                <div class="col-1">                    <div class="indent-col1">                        <h1 class="title">Welcome</h1>                        <p class="p1">Welcome Pet Lovers! &nbsp;Here you\'ll find just what you\'re looking for - with a big extra bonus: FUN! &nbsp;Sure, you could buy that catnip or dog toy anywhere else, but here at the Go-To Guide, we are SERIOUSLY committed to making you SMILE. &nbsp;Maybe even LAUGH!</p>                      <div class="box">                            <div class="border-top">                                <div class="border-bottom">                                    <div class="corner-top-right">                                        <div class="corner-top-left">                                            <div class="corner-bottom-left">                                                <div class="corner-bottom-right">                                                   <div class="indent-box">                                                        <div class="container">                                                          <div class="col-3">                                                                <img alt="" src="images/1page_img1.jpg" class="img-indent" /><br />                                                              <a href="#" class="link2"><strong>News</strong></a> <br />                                                                <ul class="boxlist">                                                                   <li>Link to News Story</li>                                                                   <li>Link to News Story 2</li>                                                                   <li>Link to News Story 3</li>                                                                </ul>                                                               </div>                                                            <div class="col-3">                                                                <img alt="" src="images/1page_img2.jpg" class="img-indent" /><br />                                                              <a href="#" class="link2"><strong>Information</strong> <br />                                                               &nbsp; &nbsp; &nbsp; &nbsp;mau <span>rillus</span> </a>                                                            </div>                                                            <div class="col-3">                                                                <img alt="" src="images/1page_img3.jpg" class="img-indent" /><br />                                                              <a href="#" class="link2"><strong>Products</strong> <br />                                                               &nbsp; &nbsp; &nbsp; &nbsp;cumsoci <span>inatot</span> </a>                                                            </div>                                                            <div class="col-4">                                                                <img alt="" src="images/1page_img4.jpg" class="img-indent" /><br />                                                              <a href="#" class="link2"><strong>Services</strong> <br />                                                              &nbsp; &nbsp; &nbsp; &nbsp;us etgnis <span>sriea</span>  </a>                                                          </div>                                                        </div>                                                    </div>                                                </div>                                            </div>                                        </div>                                    </div>                                </div>                            </div>                        </div>                        <img alt="" src="images/1page_title2.gif" class="title1" /><br />                        <p><strong>04/18/2009 - 14:53</strong></p>']

from ps3_mystery import mystery_test as test
import random

def html_structure_maker(string):
    tag_mode = False
    list_ele = str()
    token_list = list()
    count = 0
    for ch in string:
        count = count + 1
        if ch == '<' and tag_mode is False:
            if list_ele != '':
                token_list.append(list_ele)
            list_ele = ''
            tag_mode = True

        list_ele = list_ele + ch

        if ch == '>' and tag_mode is True:
            tag_mode = False
            token_list.append(list_ele)
            list_ele = ''
    assert "".join(token_list) == string
    return token_list

def tag_text_separator(token_list):
    import re
    tag_list = list()
    text_list = list()
    for token in token_list:
        if re.search("^<.*>$", token) is None:
            text_list.append(token)
        else:
            tag_list.append(token)
    assert set(tag_list + text_list) == set(token_list)
    return tag_list, text_list

def whitespace_remover(text_list):
    import re
    output = list()
    for text in text_list:
        text = ' '.join(text.split())
        output.append(text)
    return filter(None, output)

def ddmin(case_num, s):
    counter = 0
    n = 2     # Initial granularity
    while len(s) >= 2:
        start = 0
        subset_length = len(s) / n
        some_complement_is_failing = False

        while start < len(s):
            counter += 1
            complement = s[:start] + s[start + subset_length:]

            if type(complement) == list:
                if test(case_num, " ".join(complement)) == "FAIL":
                    s = complement
                    n = max(n - 1, 2)
                    some_complement_is_failing = True
                    break
            else:
                if test(case_num, complement) == "FAIL":
                    s = complement
                    n = max(n - 1, 2)
                    some_complement_is_failing = True
                    break

            start += subset_length

        if not some_complement_is_failing:
            if n == len(s):
                break
            n = min(n * 2, len(s))
    return s, counter

answer = list()
counters = list()
for case_num, case in enumerate(test_cases):
    tags, texts = tag_text_separator(html_structure_maker(case))
    filteredTexts = whitespace_remover(texts)
    str1, count1 = ddmin(case_num, tags)
    str2, count2 = ddmin(case_num, " ".join(str1))
    total_count = count1 + count2
    answer.append(str2)
    counters.append(total_count)

    print "\n"
    print "case", case_num
    print "stage1", count1, str1
    print "stage2", count2, str2
    print "total count = ", total_count


#answer = ['' for _ in test_cases]
#counters = ['' for _ in test_cases]
