<div class="py-5" id="board">
          <article class="post-content mx-auto">
            <!-- SEO header -->
            <h1 style="display: none">完美校园自动打卡</h1>
            
            
<a id="more"></a>

<div class="note note-success">
            <p>项目地址：<a target="_blank" rel="noopener" href="https://github.com/zhoudedi/WanMeiXiaoYuanCheckin">https://github.com/zhoudedi/WanMeiXiaoYuanCheckin</a></p>
          </div>



<h2 id="🌈使用方法"><a href="#🌈使用方法" class="headerlink" title="🌈使用方法"></a>🌈使用方法<a class="anchorjs-link " aria-label="Anchor" data-anchorjs-icon="" href="#🌈使用方法" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h2><h3 id="1、新建云函数"><a href="#1、新建云函数" class="headerlink" title="1、新建云函数"></a>1、新建云函数<a class="anchorjs-link " aria-label="Anchor" data-anchorjs-icon="" href="#1、新建云函数" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3><p><a class="fancybox fancybox.image" href="https://cdn.jsdelivr.net/gh/zhoudedi/WanMeiXiaoYuanCheckin/Pictures/%E6%90%9C%E7%B4%A2%E4%BA%91%E5%87%BD%E6%95%B0.png" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default"><img src="https://cdn.jsdelivr.net/gh/zhoudedi/WanMeiXiaoYuanCheckin/Pictures/%E6%90%9C%E7%B4%A2%E4%BA%91%E5%87%BD%E6%95%B0.png"></a></p>
<p><a class="fancybox fancybox.image" href="https://cdn.jsdelivr.net/gh/zhoudedi/WanMeiXiaoYuanCheckin/Pictures/%E6%96%B0%E5%BB%BA%E4%BA%91%E5%87%BD%E6%95%B01.png" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default"><img src="https://cdn.jsdelivr.net/gh/zhoudedi/WanMeiXiaoYuanCheckin/Pictures/%E6%96%B0%E5%BB%BA%E4%BA%91%E5%87%BD%E6%95%B01.png"></a></p>
<h3 id="2、上传-SCF-包"><a href="#2、上传-SCF-包" class="headerlink" title="2、上传 SCF 包"></a>2、上传 SCF 包<a class="anchorjs-link " aria-label="Anchor" data-anchorjs-icon="" href="#2、上传-SCF-包" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3><p>本地上传 zip 包（WanMeiXiaoYuanCheckin-SCF.v*.*.*.zip)：[[ghproxy.com加速](https://ghproxy.com/https://github.com/zhoudedi/WanMeiXiaoYuanCheckin/releases/download/1.0.0/WanMeiXiaoYuanCheckin-SCF.v1.0.0.zip)]，或者[[releases最新版本](https://github.com/zhoudedi/WanMeiXiaoYuanCheckin/releases)]下载解压使用）</p>
<p><a class="fancybox fancybox.image" href="https://cdn.jsdelivr.net/gh/zhoudedi/WanMeiXiaoYuanCheckin/Pictures/%E6%96%B0%E5%BB%BA%E4%BA%91%E5%87%BD%E6%95%B02.png" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default"><img src="https://cdn.jsdelivr.net/gh/zhoudedi/WanMeiXiaoYuanCheckin/Pictures/%E6%96%B0%E5%BB%BA%E4%BA%91%E5%87%BD%E6%95%B02.png"></a></p>
<h3 id="3、触发器配置"><a href="#3、触发器配置" class="headerlink" title="3、触发器配置"></a>3、触发器配置<a class="anchorjs-link " aria-label="Anchor" data-anchorjs-icon="" href="#3、触发器配置" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3><p>自定义创建 — 触发周期：自定义触发 — Cron 表达式：0 0 6,14 * * * * — 完成 — 立即跳转</p>
<p><a class="fancybox fancybox.image" href="https://cdn.jsdelivr.net/gh/zhoudedi/WanMeiXiaoYuanCheckin/Pictures/%E8%AE%BE%E7%BD%AE%E8%A7%A6%E5%8F%91%E5%99%A8.png" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default"><img src="https://cdn.jsdelivr.net/gh/zhoudedi/WanMeiXiaoYuanCheckin/Pictures/%E8%AE%BE%E7%BD%AE%E8%A7%A6%E5%8F%91%E5%99%A8.png"></a></p>
<h3 id="4、超时设置"><a href="#4、超时设置" class="headerlink" title="4、超时设置"></a>4、超时设置<a class="anchorjs-link " aria-label="Anchor" data-anchorjs-icon="" href="#4、超时设置" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3><p>函数管理 — 函数配置 — 编辑 — 执行超时时间：900 — 保存</p>
<p><a class="fancybox fancybox.image" href="https://cdn.jsdelivr.net/gh/zhoudedi/WanMeiXiaoYuanCheckin/Pictures/%E7%BC%96%E8%BE%91%E4%BA%91%E5%87%BD%E6%95%B0.png" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default"><img src="https://cdn.jsdelivr.net/gh/zhoudedi/WanMeiXiaoYuanCheckin/Pictures/%E7%BC%96%E8%BE%91%E4%BA%91%E5%87%BD%E6%95%B0.png"></a></p>
<p><a class="fancybox fancybox.image" href="https://cdn.jsdelivr.net/gh/zhoudedi/WanMeiXiaoYuanCheckin/Pictures/%E7%BC%96%E8%BE%91%E4%BA%91%E5%87%BD%E6%95%B02.png" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default"><img src="https://cdn.jsdelivr.net/gh/zhoudedi/WanMeiXiaoYuanCheckin/Pictures/%E7%BC%96%E8%BE%91%E4%BA%91%E5%87%BD%E6%95%B02.png"></a></p>
<h3 id="5、配置文件"><a href="#5、配置文件" class="headerlink" title="5、配置文件"></a>5、配置文件<a class="anchorjs-link " aria-label="Anchor" data-anchorjs-icon="" href="#5、配置文件" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3><ul>
<li><p>整个 json 文件使用一个 <code>[]</code> 列表用来存储打卡用户数据，每一个用户占据了一个 <code>{}</code>键值对，初次修改务必填写的数据为：<code>phone</code>、<code>password</code>、<code>device_id</code>（获取方法：<a target="_blank" rel="noopener" href="https://lingsiki.lanzoui.com/iQamDmt165i">蓝奏云</a>，下载解压使用）、健康打卡的开关（根据截图判断自己属于哪一类<a target="_blank" rel="noopener" href="https://cdn.jsdelivr.net/gh/zhoudedi/WanMeiXiaoYuanCheckin/Pictures/one.png">【1】</a>、<a target="_blank" rel="noopener" href="https://cdn.jsdelivr.net/gh/zhoudedi/WanMeiXiaoYuanCheckin/Pictures/two.png">【2】</a>），校内打卡开关（有则开），推送设置 <code>push</code>。</p>
</li>
<li><p>关于 <code>post_json</code>，如若打卡推送数据中无错误，则不用管，若有 null，或其他获取不到的情况，则酌情修改即可，和推送是一一对应的。</p>
</li>
<li><p>如果多人打卡，则复制单个用户完整的 <code>{}</code>，紧接在上个用户其后即可。</p>
</li>
<li><p>【第一次使用推荐 QQ 邮箱推送，数据推送全面】</p>
</li>
</ul>
<p><a class="fancybox fancybox.image" href="https://cdn.jsdelivr.net/gh/zhoudedi/WanMeiXiaoYuanCheckin/Pictures/%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6%E7%BC%96%E5%86%99.png" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default"><img src="https://cdn.jsdelivr.net/gh/zhoudedi/WanMeiXiaoYuanCheckin/Pictures/%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6%E7%BC%96%E5%86%99.png"></a></p>
<h3 id="6、测试部署"><a href="#6、测试部署" class="headerlink" title="6、测试部署"></a>6、测试部署<a class="anchorjs-link " aria-label="Anchor" data-anchorjs-icon="" href="#6、测试部署" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3><p>若弹框【检测到您的函数未部署……】选是 — 查看执行日志以及推送信息（执行失败请带上执行日志完整截图反馈）</p>
<p><a class="fancybox fancybox.image" href="https://cdn.jsdelivr.net/gh/zhoudedi/WanMeiXiaoYuanCheckin/Pictures/%E6%B5%8B%E8%AF%95%E4%BB%A3%E7%A0%81.png" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default"><img src="https://cdn.jsdelivr.net/gh/zhoudedi/WanMeiXiaoYuanCheckin/Pictures/%E6%B5%8B%E8%AF%95%E4%BB%A3%E7%A0%81.png"></a></p>
<h3 id="7、检测成功"><a href="#7、检测成功" class="headerlink" title="7、检测成功"></a>7、检测成功<a class="anchorjs-link " aria-label="Anchor" data-anchorjs-icon="" href="#7、检测成功" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3><ul>
<li>第一类健康打卡成功结果：<code>{'msg': '成功', 'code': '10000', 'data': 1}</code>，显示打卡频繁也算</li>
<li>第二类健康打卡成功结果：<code>{'code': 0, 'msg': '成功'}</code></li>
<li>校内打卡成功结果：<code>{'msg': '成功', 'code': '10000', 'data': 1}</code></li>
<li>仔细查看打卡的数据，如果有值为 null 的，可能是因为打卡数据无法自动填写，请在配置文件中添加该项的赋值</li>
<li>由于前面使用软件获取了 device_id，所以请使用支付宝小程序查看打卡结果是否记录上去，以免手机登录使用的 device_id 失效</li>
</ul>
<h3 id="8、表格数据-None"><a href="#8、表格数据-None" class="headerlink" title="8、表格数据 None"></a>8、表格数据 None<a class="anchorjs-link " aria-label="Anchor" data-anchorjs-icon="" href="#8、表格数据-None" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3><ul>
<li>找到并记住自己值为 None 的选项，并记住此 propertyname，我们需要修改 value 为我们所填写的信息，有多少就修改多少</li>
</ul>
<p><a class="fancybox fancybox.image" href="https://cdn.jsdelivr.net/gh/zhoudedi/WanMeiXiaoYuanCheckin/Pictures/%E6%9F%A5%E7%9C%8B%E8%A1%A8%E6%A0%BC.png" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default"><img src="https://cdn.jsdelivr.net/gh/zhoudedi/WanMeiXiaoYuanCheckin/Pictures/%E6%9F%A5%E7%9C%8B%E8%A1%A8%E6%A0%BC.png"></a></p>
<ul>
<li>打开第一行推送数据，找到与之对应的推送数据</li>
</ul>
<p><a class="fancybox fancybox.image" href="https://cdn.jsdelivr.net/gh/zhoudedi/WanMeiXiaoYuanCheckin/Pictures/%E6%9F%A5%E7%9C%8B%E6%8E%A8%E9%80%81.png" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default"><img src="https://cdn.jsdelivr.net/gh/zhoudedi/WanMeiXiaoYuanCheckin/Pictures/%E6%9F%A5%E7%9C%8B%E6%8E%A8%E9%80%81.png"></a></p>
<ul>
<li>在第二行中查找推送数据，propertyname 下的 checkValue 为我们所能填写的值</li>
</ul>
<p><a class="fancybox fancybox.image" href="https://cdn.jsdelivr.net/gh/zhoudedi/WanMeiXiaoYuanCheckin/Pictures/%E8%8E%B7%E5%8F%96%E5%80%BC.png" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default"><img src="https://cdn.jsdelivr.net/gh/zhoudedi/WanMeiXiaoYuanCheckin/Pictures/%E8%8E%B7%E5%8F%96%E5%80%BC.png"></a></p>
<ul>
<li>最后修改配置文件，第一类健康打卡则在 one_check 下的 post_json 下修改，校内即校内下面的</li>
</ul>
<p><a class="fancybox fancybox.image" href="https://cdn.jsdelivr.net/gh/zhoudedi/WanMeiXiaoYuanCheckin/Pictures/%E4%BF%AE%E6%94%B9%E9%85%8D%E7%BD%AE.png" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default"><img src="https://cdn.jsdelivr.net/gh/zhoudedi/WanMeiXiaoYuanCheckin/Pictures/%E4%BF%AE%E6%94%B9%E9%85%8D%E7%BD%AE.png"></a></p>
<h2 id="📜FQA"><a href="#📜FQA" class="headerlink" title="📜FQA"></a>📜FQA<a class="anchorjs-link " aria-label="Anchor" data-anchorjs-icon="" href="#📜FQA" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h2><ul>
<li>如果有问题，这边请 <a target="_blank" rel="noopener" href="https://github.com/zhoudedi/WanMeiXiaoYuanCheckin#fqa">GitHub</a>，或进群反馈 <a target="_blank" rel="noopener" href="https://github.com/zhoudedi/WanMeiXiaoYuanCheckin/issues/1">交流群</a></li>
</ul>
