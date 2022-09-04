<div class="container nopadding-x-md" id="board-ctn">
        <div class="py-5" id="board">
          <article class="post-content mx-auto">
            <!-- SEO header -->
            <h1 style="display: none">Xposed Hook 完美校园获取本机 DeviceId</h1>
            
            <div class="markdown-body">
              <div class="note note-info">
            <p>简单记录一下完美校园 app 逆向 + Hook 获取 deviceId 生成的方法</p>
          </div>
<a id="more"></a>

<div class="note note-success">
            <p>完美校园自动打卡项目：<a target="_blank" rel="noopener" href="https://github.com/ReaJason/17wanxiaoCheckin">https://github.com/ReaJason/17wanxiaoCheckin</a><br>本文使用的所有资源包括成品链接：<a target="_blank" rel="noopener" href="https://lingsiki.lanzoui.com/b0eklg2ih">https://lingsiki.lanzoui.com/b0eklg2ih</a> 密码：2333</p>
          </div>

<h2 id="🤝静态分析"><a href="#🤝静态分析" class="headerlink" title="🤝静态分析"></a>🤝静态分析<a class="anchorjs-link " aria-label="Anchor" data-anchorjs-icon="" href="#🤝静态分析" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h2><h3 id="🔍查壳"><a href="#🔍查壳" class="headerlink" title="🔍查壳"></a>🔍查壳<a class="anchorjs-link " aria-label="Anchor" data-anchorjs-icon="" href="#🔍查壳" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3><div class="note note-info">
            <p>查壳工具：<a target="_blank" rel="noopener" href="http://www.legendsec.org/1888.html">ApkScan-PKID</a> 查看 app 是否加固（需要 Java 环境）</p>
          </div>

<p>  如果 app 加固的话需要脱壳才能看到源码，没有加固则最好，在豌豆荚下载了完美校园历史版本发现，5.0.2 版本没有加固，而最新的 5.3.6 版本使用了 360 加固，其他版本有阿里和腾讯加固的都有，不知道他们为什么换这么多壳……，因此本文采取的思路是在 5.0.2 版本中找到 deviceId 的获取方法，然后使用 xp hook 绕壳去 hook 5.3.6 版本的相关代码，也很幸运 5.3.6 版本生成 deviceId 的代码虽然修改了位置，但是还是找到了 hook 出来的办法。</p>
<p><a class="fancybox fancybox.image" href="https://cdn.jsdelivr.net/gh/ReaJason/blog_imgs/17WanXiaoHookGetDeviceId_img/5.0.2.png" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default" title="5.0.2" data-caption="5.0.2"><img src="https://cdn.jsdelivr.net/gh/ReaJason/blog_imgs/17WanXiaoHookGetDeviceId_img/5.0.2.png" alt="5.0.2"><p class="image-caption">5.0.2</p></a></p>
<p><a class="fancybox fancybox.image" href="https://cdn.jsdelivr.net/gh/ReaJason/blog_imgs/17WanXiaoHookGetDeviceId_img/5.3.6.png" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default" title="5.3.6" data-caption="5.3.6"><img src="https://cdn.jsdelivr.net/gh/ReaJason/blog_imgs/17WanXiaoHookGetDeviceId_img/5.3.6.png" alt="5.3.6"><p class="image-caption">5.3.6</p></a></p>
<h3 id="🤔分析源码"><a href="#🤔分析源码" class="headerlink" title="🤔分析源码"></a>🤔分析源码<a class="anchorjs-link " aria-label="Anchor" data-anchorjs-icon="" href="#🤔分析源码" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3><div class="note note-info">
            <p>源码查看工具：<a target="_blank" rel="noopener" href="https://github.com/skylot/jadx">jadx</a><br>把使用方法为打开 bin 目录下的 jadx-gui.bat，然后选择 apk</p>
          </div>

<ol>
<li><p>在搜索文本工具中搜索 <code>/loginnew</code>，即可查看有一个匹配值，双击进去，然后右键查看该值 <code>i</code> 的用例，也就是哪里用了这个值，也刚好发现一个 <code>c.i</code>，双击进入即可发现登录报表的所有参数，基本都在这里出现了</p>
<p><a class="fancybox fancybox.image" href="https://cdn.jsdelivr.net/gh/ReaJason/blog_imgs/17WanXiaoHookGetDeviceId_img/loginnew.png" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default" title="search_loginnew" data-caption="search_loginnew"><img src="https://cdn.jsdelivr.net/gh/ReaJason/blog_imgs/17WanXiaoHookGetDeviceId_img/loginnew.png" alt="search_loginnew"><p class="image-caption">search_loginnew</p></a></p>
<p><a class="fancybox fancybox.image" href="https://cdn.jsdelivr.net/gh/ReaJason/blog_imgs/17WanXiaoHookGetDeviceId_img/loginnew_example.png" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default" title="find_i" data-caption="find_i"><img src="https://cdn.jsdelivr.net/gh/ReaJason/blog_imgs/17WanXiaoHookGetDeviceId_img/loginnew_example.png" alt="find_i"><p class="image-caption">find_i</p></a></p>
<p><a class="fancybox fancybox.image" href="https://cdn.jsdelivr.net/gh/ReaJason/blog_imgs/17WanXiaoHookGetDeviceId_img/loginreqdata.png" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default" title="loginreqdata" data-caption="loginreqdata"><img src="https://cdn.jsdelivr.net/gh/ReaJason/blog_imgs/17WanXiaoHookGetDeviceId_img/loginreqdata.png" alt="loginreqdata"><p class="image-caption">loginreqdata</p></a></p>
<p><a class="fancybox fancybox.image" href="https://cdn.jsdelivr.net/gh/ReaJason/blog_imgs/17WanXiaoHookGetDeviceId_img/logindata.png" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default" title="logindata" data-caption="logindata"><img src="https://cdn.jsdelivr.net/gh/ReaJason/blog_imgs/17WanXiaoHookGetDeviceId_img/logindata.png" alt="logindata"><p class="image-caption">logindata</p></a></p>
</li>
<li><p>我们可以看到这个 <code>private String deviceId = AppUtils.f(SystemApplication.e());</code> 这行代码说明了 deviceId 生成的来源，选中 <code>f</code> ，右键跳到声明，即可查看对应源码</p>
<p><a class="fancybox fancybox.image" href="https://cdn.jsdelivr.net/gh/ReaJason/blog_imgs/17WanXiaoHookGetDeviceId_img/deviceid_f.png" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default" title="deviceId_f" data-caption="deviceId_f"><img src="https://cdn.jsdelivr.net/gh/ReaJason/blog_imgs/17WanXiaoHookGetDeviceId_img/deviceid_f.png" alt="deviceId_f"><p class="image-caption">deviceId_f</p></a></p>
<p><a class="fancybox fancybox.image" href="https://cdn.jsdelivr.net/gh/ReaJason/blog_imgs/17WanXiaoHookGetDeviceId_img/deviceid_func.png" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default" title="deviceid_func" data-caption="deviceid_func"><img src="https://cdn.jsdelivr.net/gh/ReaJason/blog_imgs/17WanXiaoHookGetDeviceId_img/deviceid_func.png" alt="deviceid_func"><p class="image-caption">deviceid_func</p></a></p>
</li>
<li><p>可以看到该类有许多的 get 方法，我们可以通过 hook 这些方法，来获取对应值（不过还得看登录方式是否使用了对应值）</p>
<p><a class="fancybox fancybox.image" href="https://cdn.jsdelivr.net/gh/ReaJason/blog_imgs/17WanXiaoHookGetDeviceId_img/hook_point.png" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default" title="hook_point" data-caption="hook_point"><img src="https://cdn.jsdelivr.net/gh/ReaJason/blog_imgs/17WanXiaoHookGetDeviceId_img/hook_point.png" alt="hook_point"><p class="image-caption">hook_point</p></a></p>
</li>
<li><p>使用 jadx 找到 5.3.6 版本 360 加固后的 app 入口</p>
<p><a class="fancybox fancybox.image" href="https://cdn.jsdelivr.net/gh/ReaJason/blog_imgs/17WanXiaoHookGetDeviceId_img/360.png" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default" title="classloader" data-caption="classloader"><img src="https://cdn.jsdelivr.net/gh/ReaJason/blog_imgs/17WanXiaoHookGetDeviceId_img/360.png" alt="classloader"><p class="image-caption">classloader</p></a></p>
</li>
</ol>
<h2 id="🪂Xp-Hook"><a href="#🪂Xp-Hook" class="headerlink" title="🪂Xp Hook"></a>🪂Xp Hook<a class="anchorjs-link " aria-label="Anchor" data-anchorjs-icon="" href="#🪂Xp-Hook" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h2><div class="note note-info">
            <p>环境搭建以及入门：<a target="_blank" rel="noopener" href="https://www.52pojie.cn/forum.php?mod=viewthread&amp;tid=1315865&amp;highlight=frida+hook"> [超级详细]Frida Hook和Xposed Hook 再搞Crackme</a><br>网上 Xp Hook 的教程还是有一点点可以学习的，可自行搜索学习相应知识</p>
          </div>

<ol>
<li><p>新建项目，打开左侧资源管理设置为 Project，将 api-82 的两个文件放到 app/libs 下</p>
</li>
<li><p>在 app/bulid.gradle 下面的 dependencies 中加入以下代码，然后点击右上角的 Sync</p>
<figure class="highlight xml"><table><tbody><tr><td class="gutter hljs"><div class="hljs code-wrapper"><pre><span class="line">1</span><br><span class="line">2</span><br></pre></div></td><td class="code"><div class="hljs code-wrapper"><pre><code class="hljs xml">compileOnly 'de.robv.android.xposed:api:82'<br>compileOnly 'de.robv.android.xposed:api:82:sources'<br></code><button class="copy-btn copy-btn-light" data-clipboard-snippet=""><i class="iconfont icon-copy"></i><span>Copy</span></button></pre></div></td></tr></tbody></table></figure>

<p><a class="fancybox fancybox.image" href="https://cdn.jsdelivr.net/gh/ReaJason/blog_imgs/17WanXiaoHookGetDeviceId_img/xphook_set1.png" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default" title="xphook_set1" data-caption="xphook_set1"><img src="https://cdn.jsdelivr.net/gh/ReaJason/blog_imgs/17WanXiaoHookGetDeviceId_img/xphook_set1.png" alt="xphook_set1"><p class="image-caption">xphook_set1</p></a></p>
</li>
<li><p>在 AndroidManifest.xml 中加入一下代码</p>
<figure class="highlight xml"><table><tbody><tr><td class="gutter hljs"><div class="hljs code-wrapper"><pre><span class="line">1</span><br><span class="line">2</span><br><span class="line">3</span><br><span class="line">4</span><br><span class="line">5</span><br><span class="line">6</span><br><span class="line">7</span><br><span class="line">8</span><br><span class="line">9</span><br></pre></div></td><td class="code"><div class="hljs code-wrapper"><pre><code class="hljs xml"><span class="hljs-tag">&lt;<span class="hljs-name">meta-data</span></span><br><span class="hljs-tag">           <span class="hljs-attr">android:name</span>=<span class="hljs-string">"xposedmodule"</span></span><br><span class="hljs-tag">           <span class="hljs-attr">android:value</span>=<span class="hljs-string">"true"</span> /&gt;</span><br><span class="hljs-tag">&lt;<span class="hljs-name">meta-data</span></span><br><span class="hljs-tag">           <span class="hljs-attr">android:name</span>=<span class="hljs-string">"xposeddescription"</span></span><br><span class="hljs-tag">           <span class="hljs-attr">android:value</span>=<span class="hljs-string">"hook 5.3.6 版本完美校园登录参数，包括 deviceId"</span> /&gt;</span><br><span class="hljs-tag">&lt;<span class="hljs-name">meta-data</span></span><br><span class="hljs-tag">           <span class="hljs-attr">android:name</span>=<span class="hljs-string">"xposedminversion"</span></span><br><span class="hljs-tag">           <span class="hljs-attr">android:value</span>=<span class="hljs-string">"54"</span> /&gt;</span><br></code><button class="copy-btn copy-btn-light" data-clipboard-snippet=""><i class="iconfont icon-copy"></i><span>Copy</span></button></pre></div></td></tr></tbody></table></figure>
<p><a class="fancybox fancybox.image" href="https://cdn.jsdelivr.net/gh/ReaJason/blog_imgs/17WanXiaoHookGetDeviceId_img/xphook_set2.png" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default" title="xphook_set2" data-caption="xphook_set2"><img src="https://cdn.jsdelivr.net/gh/ReaJason/blog_imgs/17WanXiaoHookGetDeviceId_img/xphook_set2.png" srcset="/img/loading.gif" lazyload="" alt="xphook_set2"><p class="image-caption">xphook_set2</p></a></p>
</li>
<li><p>在 main 文件下创建 assets 文件夹，在其下创建 xposed_init 文件，文件中写 xposed 的入口即 <code>com.wanxiao.xp_hook.MainHook</code>（包名 + 类名）</p>
<p><a class="fancybox fancybox.image" href="https://cdn.jsdelivr.net/gh/ReaJason/blog_imgs/17WanXiaoHookGetDeviceId_img/xphook_set3.png" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default" title="xphook_set3" data-caption="xphook_set3"><img src="https://cdn.jsdelivr.net/gh/ReaJason/blog_imgs/17WanXiaoHookGetDeviceId_img/xphook_set3.png" srcset="/img/loading.gif" lazyload="" alt="xphook_set3"><p class="image-caption">xphook_set3</p></a></p>
</li>
<li><p>在 MainActivity 同级目录下创建 MainHook 的 Java class 文件</p>
</li>
<li><p>编写 Hook 代码，当前代码为 Hook 5.3.6 版本的代码，因为需要绕过 360 加固 Hook</p>
<figure class="highlight java"><table><tbody><tr><td class="gutter hljs"><div class="hljs code-wrapper"><pre><span class="line">1</span><br><span class="line">2</span><br><span class="line">3</span><br><span class="line">4</span><br><span class="line">5</span><br><span class="line">6</span><br><span class="line">7</span><br><span class="line">8</span><br><span class="line">9</span><br><span class="line">10</span><br><span class="line">11</span><br><span class="line">12</span><br><span class="line">13</span><br><span class="line">14</span><br><span class="line">15</span><br><span class="line">16</span><br><span class="line">17</span><br><span class="line">18</span><br><span class="line">19</span><br><span class="line">20</span><br><span class="line">21</span><br><span class="line">22</span><br><span class="line">23</span><br><span class="line">24</span><br><span class="line">25</span><br><span class="line">26</span><br><span class="line">27</span><br><span class="line">28</span><br><span class="line">29</span><br><span class="line">30</span><br><span class="line">31</span><br><span class="line">32</span><br><span class="line">33</span><br><span class="line">34</span><br><span class="line">35</span><br><span class="line">36</span><br><span class="line">37</span><br><span class="line">38</span><br><span class="line">39</span><br><span class="line">40</span><br><span class="line">41</span><br><span class="line">42</span><br><span class="line">43</span><br><span class="line">44</span><br><span class="line">45</span><br><span class="line">46</span><br><span class="line">47</span><br><span class="line">48</span><br><span class="line">49</span><br><span class="line">50</span><br><span class="line">51</span><br><span class="line">52</span><br><span class="line">53</span><br><span class="line">54</span><br><span class="line">55</span><br><span class="line">56</span><br><span class="line">57</span><br><span class="line">58</span><br></pre></div></td><td class="code"><div class="hljs code-wrapper"><pre><code class="hljs java"><span class="hljs-comment">// Hook 完美校园</span><br><span class="hljs-keyword">if</span> (!loadPackageParam.packageName.equals(<span class="hljs-string">"com.newcapec.mobile.ncp"</span>)) {<br>    <span class="hljs-keyword">return</span>;<br>}<br>XposedBridge.log(<span class="hljs-string">"已 HOOK 到完美校园"</span>);<br><br><span class="hljs-comment">// Hook 360加固</span><br>findAndHookMethod(<span class="hljs-string">"com.stub.StubApp"</span>, <br>                  loadPackageParam.classLoader,<br>                  <span class="hljs-string">"attachBaseContext"</span>, <br>                  Context.class, <br>                  <span class="hljs-keyword">new</span> XC_MethodHook() {<br>                      <span class="hljs-meta">@Override</span><br>                      <span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">void</span> <span class="hljs-title">afterHookedMethod</span><span class="hljs-params">(MethodHookParam param)</span> <span class="hljs-keyword">throws</span> Throwable </span>{<br>                          <span class="hljs-keyword">super</span>.afterHookedMethod(param);<br>                          <span class="hljs-comment">//获取到Context对象，通过这个对象来获取classloader</span><br>                          Context context = (Context) param.args[<span class="hljs-number">0</span>];<br>                          <span class="hljs-comment">//获取classloader，之后hook加固后的就使用这个classloader</span><br>                          ClassLoader classLoader = context.getClassLoader();<br>                          hook_param(classLoader, <span class="hljs-string">"getAppCode"</span>, <span class="hljs-string">"appCode: "</span>);<br>                          hook_param(classLoader, <span class="hljs-string">"getDeviceId"</span>, <span class="hljs-string">"deviceId: "</span>);<br>                          hook_param(classLoader, <span class="hljs-string">"getNetWork"</span>, <span class="hljs-string">"netWork: "</span>);<br>                          hook_param(classLoader, <span class="hljs-string">"getPassword"</span>, <span class="hljs-string">"password: "</span>);<br>                          hook_param(classLoader, <span class="hljs-string">"getQudao"</span>, <span class="hljs-string">"qudao: "</span>);<br>                          hook_param(classLoader, <span class="hljs-string">"getRequestMethod"</span>, <span class="hljs-string">"requestMethod: "</span>);<br>                          hook_param(classLoader, <span class="hljs-string">"getSms"</span>, <span class="hljs-string">"sms: "</span>);<br>                          hook_param(classLoader, <span class="hljs-string">"getShebeixinghao"</span>, <span class="hljs-string">"shebeixinghao: "</span>);<br>                          hook_param(classLoader, <span class="hljs-string">"getSystemType"</span>, <span class="hljs-string">"systemType: "</span>);<br>                          hook_param(classLoader, <span class="hljs-string">"getTelephoneInfo"</span>, <span class="hljs-string">"telephoneInfo: "</span>);<br>                          hook_param(classLoader, <span class="hljs-string">"getTelephoneModel"</span>, <span class="hljs-string">"telephoneModel: "</span>);<br>                          hook_param(classLoader, <span class="hljs-string">"getToken"</span>, <span class="hljs-string">"token: "</span>);<br>                          hook_param(classLoader, <span class="hljs-string">"getType"</span>, <span class="hljs-string">"type: "</span>);<br>                          hook_param(classLoader, <span class="hljs-string">"getUnionid"</span>, <span class="hljs-string">"unionid: "</span>);<br>                          hook_param(classLoader, <span class="hljs-string">"getUserId"</span>, <span class="hljs-string">"userId: "</span>);<br>                          hook_param(classLoader, <span class="hljs-string">"getUserName"</span>, <span class="hljs-string">"userName: "</span>);<br>                          hook_param(classLoader, <span class="hljs-string">"getWanxiaoVersion"</span>, <span class="hljs-string">"wanxiaoVersion: "</span>);<br>                          hook_param(classLoader, <span class="hljs-string">"getYunyingshang"</span>, <span class="hljs-string">"yunyingshang: "</span>);<br>                          hook_param(classLoader, <span class="hljs-string">"toJsonString"</span>, <span class="hljs-string">"当前登录方式请求参数: "</span>);<br>                      }<br>                  });<br><br><br>}<br><br><span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">hook_param</span><span class="hljs-params">(ClassLoader classLoader, String methodName, String resultName)</span></span>{<br>    findAndHookMethod(<br>        <span class="hljs-string">"com.wanxiao.rest.entities.login.LoginReqData"</span>, classLoader, methodName,<br>        <span class="hljs-keyword">new</span> XC_MethodHook() {<br>            <span class="hljs-meta">@Override</span><br>            <span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">void</span> <span class="hljs-title">afterHookedMethod</span><span class="hljs-params">(MethodHookParam param)</span> <span class="hljs-keyword">throws</span> Throwable </span>{<br>                String msg = resultName + param.getResult();<br>                XposedBridge.log(msg);<br>                Log.i(<span class="hljs-string">"[ 17wanxiaoHook ]"</span>, msg);<br>            }<br>        }<br>    );<br><br>};<br></code><button class="copy-btn copy-btn-light" data-clipboard-snippet=""><i class="iconfont icon-copy"></i><span>Copy</span></button></pre></div></td></tr></tbody></table></figure></li>
<li><p>结果展示</p>
<p><a class="fancybox fancybox.image" href="https://cdn.jsdelivr.net/gh/ReaJason/blog_imgs/17WanXiaoHookGetDeviceId_img/result.jpg" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default" title="result" data-caption="result"><img src="https://cdn.jsdelivr.net/gh/ReaJason/blog_imgs/17WanXiaoHookGetDeviceId_img/result.jpg" srcset="/img/loading.gif" lazyload="" alt="result"><p class="image-caption">result</p></a></p>
</li>
</ol>
<h2 id="❄总结"><a href="#❄总结" class="headerlink" title="❄总结"></a>❄总结<a class="anchorjs-link " aria-label="Anchor" data-anchorjs-icon="" href="#❄总结" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h2><p>  安卓逆向这方面我只是个小小新手，Xp Hook 真的很牛皮，更强大的功能目前还用不上，Frida Hook 测试只能 Hook 5.0.2 版本，5.3.6 版本死活显示多进程，Frida Hook 不到，有机会接触这方面的再继续学习，目前也就这样了。</p>
<div class="note note-danger">
            <p>本文仅供交流学习，请勿用于违法用途</p>
          </div>
            </div>
            <hr>
            <div>
              <div class="post-metas mb-3">
                
                  <div class="post-meta mr-3">
                    <i class="iconfont icon-category"></i>
                    
                      <a class="hover-with-bg" href="/categories/Android/">Android</a>
                    
                  </div>
                
                
                  <div class="post-meta">
                    <i class="iconfont icon-tags"></i>
                    
                      <a class="hover-with-bg" href="/tags/Notes/">Notes</a>
                    
                      <a class="hover-with-bg" href="/tags/Xposed/">Xposed</a>
                    
                  </div>
                
              </div>
              
                <p class="note note-warning">
                  
                    本博客所有文章除特别声明外，均采用 <a target="_blank" href="https://creativecommons.org/licenses/by-sa/4.0/deed.zh" rel="nofollow noopener noopener">CC BY-SA 4.0 协议</a> ，转载请注明出处！
                  
                </p>
              
              
                <div class="post-prevnext">
                  <article class="post-prev col-6">
                    
                    
                      <a href="/2021/05/01/WindowsUsage/">
                        <i class="iconfont icon-arrowleft"></i>
                        <span class="hidden-mobile">Windows10 使用心得与总结</span>
                        <span class="visible-mobile">上一篇</span>
                      </a>
                    
                  </article>
                  <article class="post-next col-6">
                    
                    
                      <a href="/2021/04/12/AndroidFlashRom/">
                        <span class="hidden-mobile">我的刷机之旅 — Redmi K20 Pro</span>
                        <span class="visible-mobile">下一篇</span>
                        <i class="iconfont icon-arrowright"></i>
                      </a>
                    
                  </article>
                </div>
              
            </div>

            
          </article>
        </div>
      </div>