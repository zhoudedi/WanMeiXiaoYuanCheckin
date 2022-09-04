<html lang="zh-CN" data-default-color-scheme="&quot;auto&quot;" data-user-color-scheme="light" class=" "><head>
  <meta charset="UTF-8">
  <link rel="apple-touch-icon" sizes="76x76" href="https://cdn.jsdelivr.net/gh/ReaJason/blog_imgs/default/website.png">
  <link rel="icon" href="https://cdn.jsdelivr.net/gh/ReaJason/blog_imgs/default/website.png">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, shrink-to-fit=no">
  <meta http-equiv="x-ua-compatible" content="ie=edge">
  
  <meta name="theme-color" content="#fc9d9a">
  <meta name="description" content="
            今天你打卡了吗？
          ">
  <meta name="author" content="ReaJason">
  <meta name="keywords" content="">
  
  <title>完美校园自动打卡 - ReaJason</title>

  <style class="anchorjs"></style><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css">


  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/github-markdown-css@4.0.0/github-markdown.min.css">
  <link rel="stylesheet" href="/lib/hint/hint.min.css">

  
    
    
      
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/highlight.js@10.6.0/styles/github-gist.min.css">
    
  

  
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fancyapps/fancybox@3.5.7/dist/jquery.fancybox.min.css">
  



<!-- 主题依赖的图标库，不要自行修改 -->

<link rel="stylesheet" href="//at.alicdn.com/t/font_1749284_ba1fz6golrf.css">



<link rel="stylesheet" href="//at.alicdn.com/t/font_1736178_kmeydafke9r.css">


<link rel="stylesheet" href="/css/main.css">

<!-- 自定义样式保持在最底部 -->

  
<link rel="stylesheet" href="/css/custom.css">
<link rel="stylesheet" href="//at.alicdn.com/t/font_2805938_q5x4gqy1kjn.css">



  <script id="fluid-configs">
    var Fluid = window.Fluid || {};
    var CONFIG = {"hostname":"example.com","root":"/","version":"1.8.10","typing":{"enable":true,"typeSpeed":150,"cursorChar":"❤️","loop":false},"anchorjs":{"enable":true,"element":"h1,h2,h3,h4,h5,h6","placement":"right","visible":"hover","icon":""},"progressbar":{"enable":true,"height_px":3,"color":"#29d","options":{"showSpinner":false,"trickleSpeed":100}},"copy_btn":true,"image_zoom":{"enable":true},"toc":{"enable":true,"headingSelector":"h1,h2,h3,h4,h5,h6","collapseDepth":1},"lazyload":{"enable":true,"loading_img":"/img/loading.gif","onlypost":false,"offset_factor":2},"web_analytics":{"enable":false,"baidu":null,"google":null,"gtag":null,"tencent":{"sid":null,"cid":null},"woyaola":null,"cnzz":null,"leancloud":{"app_id":"HohGa0vcu0iQIbm7ELytbaKs-gzGzoHsz","app_key":"9TiVNoKrg63RPL3ALyu72tt2","server_url":"https://hohga0vc.lc-cn-n1-shared.com"}}};
  </script>
  <script src="/js/utils.js"></script>
  <script src="/js/color-schema.js"></script>
<meta name="generator" content="Hexo 5.2.0"></head>


<body>
  <header style="height: 70vh;">
    <nav id="navbar" class="navbar fixed-top navbar-expand-lg scrolling-navbar navbar-dark">
  <div class="container">
    <a class="navbar-brand" href="/">&nbsp;<strong>ReaJason's Space</strong>&nbsp;</a>

    <button id="navbar-toggler-btn" class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <div class="animated-icon"><span></span><span></span><span></span></div>
    </button>

    <!-- Collapsible content -->
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav ml-auto text-center">
        
          
          
          
          
            <li class="nav-item">
              <a class="nav-link" href="/">
                <i class="iconfont icon-home-fill"></i>
                首页
              </a>
            </li>
          
        
          
          
          
          
            <li class="nav-item">
              <a class="nav-link" href="/archives/">
                <i class="iconfont icon-archive-fill"></i>
                归档
              </a>
            </li>
          
        
          
          
          
          
            <li class="nav-item">
              <a class="nav-link" href="/categories/">
                <i class="iconfont icon-category-fill"></i>
                分类
              </a>
            </li>
          
        
          
          
          
          
            <li class="nav-item">
              <a class="nav-link" href="/tags/">
                <i class="iconfont icon-tags-fill"></i>
                标签
              </a>
            </li>
          
        
          
          
          
          
            <li class="nav-item">
              <a class="nav-link" href="/about/">
                <i class="iconfont icon-user-fill"></i>
                关于
              </a>
            </li>
          
        
          
          
          
          
            <li class="nav-item">
              <a class="nav-link" href="/links/">
                <i class="iconfont icon-link-fill"></i>
                友链
              </a>
            </li>
          
        
        
          <li class="nav-item" id="search-btn">
            <a class="nav-link" target="_self" data-toggle="modal" data-target="#modalSearch">&nbsp;<i class="iconfont icon-search"></i>&nbsp;</a>
          </li>
        
        
          <li class="nav-item" id="color-toggle-btn">
            <a class="nav-link" target="_self">&nbsp;<i class="iconfont icon-dark" id="color-toggle-icon" data="dark"></i>&nbsp;</a>
          </li>
        
      </ul>
    </div>
  </div>
</nav>

    <div class="banner" id="banner" parallax="true" style="background: url(&quot;https://cdn.jsdelivr.net/gh/ReaJason/blog_imgs/default/default.jpg&quot;) center center / cover no-repeat; transform: translate3d(0px, 0px, 0px);">
      <div class="full-bg-img">
        <div class="mask flex-center" style="background-color: rgba(0, 0, 0, 0.3)">
          <div class="page-header text-center fade-in-up">
            <span class="h2" id="subtitle" title="完美校园自动打卡">完美校园自动打卡&nbsp;</span><span class="typed-cursor h2 typed-cursor--blink">❤️</span>

            
              <div class="mt-3">
  
  
    <span class="post-meta">
      <i class="iconfont icon-date-fill" aria-hidden="true"></i>
      <time datetime="2021-03-19 23:00" pubdate="">
        2021年3月19日 晚上
      </time>
    </span>
  
</div>

<div class="mt-1">
  
    
    <span class="post-meta mr-2">
      <i class="iconfont icon-chart"></i>
      682 字
    </span>
  

  
    
    <span class="post-meta mr-2">
      <i class="iconfont icon-clock-fill"></i>
      
      
      7
       分钟
    </span>
  

  
  
    
      <!-- 不蒜子统计文章PV -->
      <span id="busuanzi_container_page_pv" style="display: inline;">
        <i class="iconfont icon-eye" aria-hidden="true"></i>
        <span id="busuanzi_value_page_pv">11991</span> 次
      </span>
    
  
</div>

            
          </div>

          
        </div>
      </div>
    </div>
  </header>

  <main>
    
      

<div class="container-fluid nopadding-x">
  <div class="row nomargin-x">
    <div class="d-none d-lg-block col-lg-2"></div>
    <div class="col-lg-8 nopadding-x-md">
      <div class="container nopadding-x-md" id="board-ctn">
        <div class="py-5" id="board">
          <article class="post-content mx-auto">
            <!-- SEO header -->
            <h1 style="display: none">完美校园自动打卡</h1>
            
            <div class="markdown-body">
              <div class="note note-info">
            <p>今天你打卡了吗？</p>
          </div>
<a id="more"></a>

<div class="note note-success">
            <p>项目地址：<a target="_blank" rel="noopener" href="https://github.com/ReaJason/17wanxiaoCheckin">https://github.com/ReaJason/17wanxiaoCheckin</a></p>
          </div>



<h2 id="🌈使用方法"><a href="#🌈使用方法" class="headerlink" title="🌈使用方法"></a>🌈使用方法<a class="anchorjs-link " aria-label="Anchor" data-anchorjs-icon="" href="#🌈使用方法" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h2><h3 id="1、新建云函数"><a href="#1、新建云函数" class="headerlink" title="1、新建云函数"></a>1、新建云函数<a class="anchorjs-link " aria-label="Anchor" data-anchorjs-icon="" href="#1、新建云函数" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3><p><a class="fancybox fancybox.image" href="https://cdn.jsdelivr.net/gh/ReaJason/17wanxiaoCheckin/Pictures/%E6%90%9C%E7%B4%A2%E4%BA%91%E5%87%BD%E6%95%B0.png" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default"><img src="https://cdn.jsdelivr.net/gh/ReaJason/17wanxiaoCheckin/Pictures/%E6%90%9C%E7%B4%A2%E4%BA%91%E5%87%BD%E6%95%B0.png"></a></p>
<p><a class="fancybox fancybox.image" href="https://cdn.jsdelivr.net/gh/ReaJason/17wanxiaoCheckin/Pictures/%E6%96%B0%E5%BB%BA%E4%BA%91%E5%87%BD%E6%95%B01.png" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default"><img src="https://cdn.jsdelivr.net/gh/ReaJason/17wanxiaoCheckin/Pictures/%E6%96%B0%E5%BB%BA%E4%BA%91%E5%87%BD%E6%95%B01.png"></a></p>
<h3 id="2、上传-SCF-包"><a href="#2、上传-SCF-包" class="headerlink" title="2、上传 SCF 包"></a>2、上传 SCF 包<a class="anchorjs-link " aria-label="Anchor" data-anchorjs-icon="" href="#2、上传-SCF-包" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3><p>本地上传 zip 包（17wanxiaoCheckin-SCF v*.*.zip：<a target="_blank" rel="noopener" href="https://lingsiki.lanzoui.com/b0ekhmcxe">蓝奏云</a>，密码：2333）</p>
<p><a class="fancybox fancybox.image" href="https://cdn.jsdelivr.net/gh/ReaJason/17wanxiaoCheckin/Pictures/%E6%96%B0%E5%BB%BA%E4%BA%91%E5%87%BD%E6%95%B02.png" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default"><img src="https://cdn.jsdelivr.net/gh/ReaJason/17wanxiaoCheckin/Pictures/%E6%96%B0%E5%BB%BA%E4%BA%91%E5%87%BD%E6%95%B02.png"></a></p>
<h3 id="3、触发器配置"><a href="#3、触发器配置" class="headerlink" title="3、触发器配置"></a>3、触发器配置<a class="anchorjs-link " aria-label="Anchor" data-anchorjs-icon="" href="#3、触发器配置" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3><p>自定义创建 — 触发周期：自定义触发 — Cron 表达式：0 0 6,14 * * * * — 完成 — 立即跳转</p>
<p><a class="fancybox fancybox.image" href="https://cdn.jsdelivr.net/gh/ReaJason/17wanxiaoCheckin/Pictures/%E8%AE%BE%E7%BD%AE%E8%A7%A6%E5%8F%91%E5%99%A8.png" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default"><img src="https://cdn.jsdelivr.net/gh/ReaJason/17wanxiaoCheckin/Pictures/%E8%AE%BE%E7%BD%AE%E8%A7%A6%E5%8F%91%E5%99%A8.png"></a></p>
<h3 id="4、超时设置"><a href="#4、超时设置" class="headerlink" title="4、超时设置"></a>4、超时设置<a class="anchorjs-link " aria-label="Anchor" data-anchorjs-icon="" href="#4、超时设置" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3><p>函数管理 — 函数配置 — 编辑 — 执行超时时间：900 — 保存</p>
<p><a class="fancybox fancybox.image" href="https://cdn.jsdelivr.net/gh/ReaJason/17wanxiaoCheckin/Pictures/%E7%BC%96%E8%BE%91%E4%BA%91%E5%87%BD%E6%95%B0.png" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default"><img src="https://cdn.jsdelivr.net/gh/ReaJason/17wanxiaoCheckin/Pictures/%E7%BC%96%E8%BE%91%E4%BA%91%E5%87%BD%E6%95%B0.png"></a></p>
<p><a class="fancybox fancybox.image" href="https://cdn.jsdelivr.net/gh/ReaJason/17wanxiaoCheckin/Pictures/%E7%BC%96%E8%BE%91%E4%BA%91%E5%87%BD%E6%95%B02.png" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default"><img src="https://cdn.jsdelivr.net/gh/ReaJason/17wanxiaoCheckin/Pictures/%E7%BC%96%E8%BE%91%E4%BA%91%E5%87%BD%E6%95%B02.png"></a></p>
<h3 id="5、配置文件"><a href="#5、配置文件" class="headerlink" title="5、配置文件"></a>5、配置文件<a class="anchorjs-link " aria-label="Anchor" data-anchorjs-icon="" href="#5、配置文件" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3><ul>
<li><p>整个 json 文件使用一个 <code>[]</code> 列表用来存储打卡用户数据，每一个用户占据了一个 <code>{}</code>键值对，初次修改务必填写的数据为：<code>phone</code>、<code>password</code>、<code>device_id</code>（获取方法：<a target="_blank" rel="noopener" href="https://lingsiki.lanzoui.com/iQamDmt165i">蓝奏云</a>，下载解压使用）、健康打卡的开关（根据截图判断自己属于哪一类<a target="_blank" rel="noopener" href="https://cdn.jsdelivr.net/gh/ReaJason/17wanxiaoCheckin/Pictures/one.png">【1】</a>、<a target="_blank" rel="noopener" href="https://cdn.jsdelivr.net/gh/ReaJason/17wanxiaoCheckin/Pictures/two.png">【2】</a>），校内打卡开关（有则开），推送设置 <code>push</code>。</p>
</li>
<li><p>关于 <code>post_json</code>，如若打卡推送数据中无错误，则不用管，若有 null，或其他获取不到的情况，则酌情修改即可，和推送是一一对应的。</p>
</li>
<li><p>如果多人打卡，则复制单个用户完整的 <code>{}</code>，紧接在上个用户其后即可。</p>
</li>
<li><p>【第一次使用推荐 QQ 邮箱推送，数据推送全面】</p>
</li>
</ul>
<p><a class="fancybox fancybox.image" href="https://cdn.jsdelivr.net/gh/ReaJason/17wanxiaoCheckin/Pictures/%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6%E7%BC%96%E5%86%99.png" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default"><img src="https://cdn.jsdelivr.net/gh/ReaJason/17wanxiaoCheckin/Pictures/%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6%E7%BC%96%E5%86%99.png"></a></p>
<h3 id="6、测试部署"><a href="#6、测试部署" class="headerlink" title="6、测试部署"></a>6、测试部署<a class="anchorjs-link " aria-label="Anchor" data-anchorjs-icon="" href="#6、测试部署" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3><p>若弹框【检测到您的函数未部署……】选是 — 查看执行日志以及推送信息（执行失败请带上执行日志完整截图反馈）</p>
<p><a class="fancybox fancybox.image" href="https://cdn.jsdelivr.net/gh/ReaJason/17wanxiaoCheckin/Pictures/%E6%B5%8B%E8%AF%95%E4%BB%A3%E7%A0%81.png" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default"><img src="https://cdn.jsdelivr.net/gh/ReaJason/17wanxiaoCheckin/Pictures/%E6%B5%8B%E8%AF%95%E4%BB%A3%E7%A0%81.png"></a></p>
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
<p><a class="fancybox fancybox.image" href="https://cdn.jsdelivr.net/gh/ReaJason/17wanxiaoCheckin/Pictures/%E6%9F%A5%E7%9C%8B%E8%A1%A8%E6%A0%BC.png" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default"><img src="https://cdn.jsdelivr.net/gh/ReaJason/17wanxiaoCheckin/Pictures/%E6%9F%A5%E7%9C%8B%E8%A1%A8%E6%A0%BC.png"></a></p>
<ul>
<li>打开第一行推送数据，找到与之对应的推送数据</li>
</ul>
<p><a class="fancybox fancybox.image" href="https://cdn.jsdelivr.net/gh/ReaJason/17wanxiaoCheckin/Pictures/%E6%9F%A5%E7%9C%8B%E6%8E%A8%E9%80%81.png" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default"><img src="https://cdn.jsdelivr.net/gh/ReaJason/17wanxiaoCheckin/Pictures/%E6%9F%A5%E7%9C%8B%E6%8E%A8%E9%80%81.png"></a></p>
<ul>
<li>在第二行中查找推送数据，propertyname 下的 checkValue 为我们所能填写的值</li>
</ul>
<p><a class="fancybox fancybox.image" href="https://cdn.jsdelivr.net/gh/ReaJason/17wanxiaoCheckin/Pictures/%E8%8E%B7%E5%8F%96%E5%80%BC.png" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default"><img src="https://cdn.jsdelivr.net/gh/ReaJason/17wanxiaoCheckin/Pictures/%E8%8E%B7%E5%8F%96%E5%80%BC.png"></a></p>
<ul>
<li>最后修改配置文件，第一类健康打卡则在 one_check 下的 post_json 下修改，校内即校内下面的</li>
</ul>
<p><a class="fancybox fancybox.image" href="https://cdn.jsdelivr.net/gh/ReaJason/17wanxiaoCheckin/Pictures/%E4%BF%AE%E6%94%B9%E9%85%8D%E7%BD%AE.png" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default"><img src="https://cdn.jsdelivr.net/gh/ReaJason/17wanxiaoCheckin/Pictures/%E4%BF%AE%E6%94%B9%E9%85%8D%E7%BD%AE.png"></a></p>
<h2 id="📜FQA"><a href="#📜FQA" class="headerlink" title="📜FQA"></a>📜FQA<a class="anchorjs-link " aria-label="Anchor" data-anchorjs-icon="" href="#📜FQA" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h2><ul>
<li>如果有问题，这边请 <a target="_blank" rel="noopener" href="https://github.com/ReaJason/17wanxiaoCheckin#fqa">GitHub</a>，或进群反馈 <a target="_blank" rel="noopener" href="https://github.com/ReaJason/17wanxiaoCheckin-Actions/issues/30">交流群</a></li>
</ul>

            </div>
            <hr>
            <div>
              <div class="post-metas mb-3">
                
                  <div class="post-meta mr-3">
                    <i class="iconfont icon-category"></i>
                    
                      <a class="hover-with-bg" href="/categories/Python/">Python</a>
                    
                  </div>
                
                
                  <div class="post-meta">
                    <i class="iconfont icon-tags"></i>
                    
                      <a class="hover-with-bg" href="/tags/Script/">Script</a>
                    
                  </div>
                
              </div>
              
                <p class="note note-warning">
                  
                    本博客所有文章除特别声明外，均采用 <a target="_blank" href="https://creativecommons.org/licenses/by-sa/4.0/deed.zh" rel="nofollow noopener noopener">CC BY-SA 4.0 协议</a> ，转载请注明出处！
                  
                </p>
              
              
                <div class="post-prevnext">
                  <article class="post-prev col-6">
                    
                    
                      <a href="/2021/03/28/CppSTL/">
                        <i class="iconfont icon-arrowleft"></i>
                        <span class="hidden-mobile">C++ の STL</span>
                        <span class="visible-mobile">上一篇</span>
                      </a>
                    
                  </article>
                  <article class="post-next col-6">
                    
                    
                      <a href="/2021/02/04/WBTopicCheckTool/">
                        <span class="hidden-mobile">微博超话签到工具</span>
                        <span class="visible-mobile">下一篇</span>
                        <i class="iconfont icon-arrowright"></i>
                      </a>
                    
                  </article>
                </div>
              
            </div>

            
          </article>
        </div>
      </div>
    </div>
    
      <div class="d-none d-lg-block col-lg-2 toc-container" id="toc-ctn" style="padding-top: 0px;">
        <div id="toc" style="visibility: visible;">
  <p class="toc-header"><i class="iconfont icon-list"></i>&nbsp;目录</p>
  <div class="toc-body" id="toc-body"><ol class="tocbot-list "><li class="toc-list-item is-active-li"><a href="#🌈使用方法" class="tocbot-link node-name--H2  tocbot-active-link">🌈使用方法</a><ol class="tocbot-list  tocbot-is-collapsible"><li class="toc-list-item"><a href="#1、新建云函数" class="tocbot-link node-name--H3 ">1、新建云函数</a></li><li class="toc-list-item"><a href="#2、上传-SCF-包" class="tocbot-link node-name--H3 ">2、上传 SCF 包</a></li><li class="toc-list-item"><a href="#3、触发器配置" class="tocbot-link node-name--H3 ">3、触发器配置</a></li><li class="toc-list-item"><a href="#4、超时设置" class="tocbot-link node-name--H3 ">4、超时设置</a></li><li class="toc-list-item"><a href="#5、配置文件" class="tocbot-link node-name--H3 ">5、配置文件</a></li><li class="toc-list-item"><a href="#6、测试部署" class="tocbot-link node-name--H3 ">6、测试部署</a></li><li class="toc-list-item"><a href="#7、检测成功" class="tocbot-link node-name--H3 ">7、检测成功</a></li><li class="toc-list-item"><a href="#8、表格数据-None" class="tocbot-link node-name--H3 ">8、表格数据 None</a></li></ol></li><li class="toc-list-item"><a href="#📜FQA" class="tocbot-link node-name--H2 ">📜FQA</a></li></ol></div>
</div>

<script>
  $(document).ready(function () {
      var boardCtn = $('#board-ctn');
      var boardTop = boardCtn.offset().top;
      tocbot.init({
        tocSelector: '#tocbot',
        contentSelector: '#post-body',
        linkClass: 'tocbot-link',
        activeLinkClass: 'tocbot-active-link',
        listClass: 'tocbot-list',
        isCollapsedClass: 'tocbot-is-collapsed',
        collapsibleClass: 'tocbot-is-collapsible',
        scrollSmooth: true,
        headingsOffset: -boardTop
      });
      if ($('.toc-list-item').length > 0) {
        $('#toc').css('visibility', 'visible');
      }
  });
</script>

      </div>
    
  </div>
</div>

<!-- Custom -->


    

    
      <a id="scroll-top-button" href="#" role="button" style="bottom: -60px; right: 143.675px;">
        <i class="iconfont icon-arrowup" aria-hidden="true"></i>
      </a>
    

    
      <div class="modal fade" id="modalSearch" tabindex="-1" role="dialog" aria-labelledby="ModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-dialog-scrollable modal-lg" role="document">
    <div class="modal-content">
      <div class="modal-header text-center">
        <h4 class="modal-title w-100 font-weight-bold">搜索</h4>
        <button type="button" id="local-search-close" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">×</span>
        </button>
      </div>
      <div class="modal-body mx-3">
        <div class="md-form mb-5">
          <input type="text" id="local-search-input" class="form-control validate">
          <label data-error="x" data-success="v" for="local-search-input">关键词</label>
        </div>
        <div class="list-group" id="local-search-result"></div>
      </div>
    </div>
  </div>
</div>
    

    
  </main>

  <footer class="text-center mt-5 py-3">
  <div class="footer-content">
     <i class="iconfont icon-copyright"></i> 2019-2021 <a target="_blank" rel="noopener" href="https://reajason.top">ReaJason</a> <br>Powered by  <a href="https://hexo.io" target="_blank" rel="nofollow noopener"><span>Hexo</span></a> ❤️ <a href="https://github.com/fluid-dev/hexo-theme-fluid" target="_blank" rel="nofollow noopener"><span>Fluid</span></a> <div> ❄我们在一起玩耍了❄ <br> <span id="timeDate">&nbsp;1270&nbsp;天</span> <span id="times">06&nbsp;小时&nbsp;31&nbsp;分&nbsp;53&nbsp;秒</span> <script src="/js/duration.js"></script> </div> 
  </div>
  

  

  
</footer>


  <!-- SCRIPTS -->
  
  <script src="https://cdn.jsdelivr.net/npm/nprogress@0.2.0/nprogress.min.js"></script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/nprogress@0.2.0/nprogress.min.css">

  <script>
    NProgress.configure({"showSpinner":false,"trickleSpeed":100})
    NProgress.start()
    window.addEventListener('load', function() {
      NProgress.done();
    })
  </script>


<script src="https://cdn.jsdelivr.net/npm/jquery@3.6.0/dist/jquery.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.min.js"></script>
<script src="/js/events.js"></script>
<script src="/js/plugins.js"></script>

<!-- Plugins -->


  
    <script src="/js/img-lazyload.js"></script>
  



  



  <script src="https://cdn.jsdelivr.net/npm/tocbot@4.12.2/dist/tocbot.min.js"></script>



  <script src="https://cdn.jsdelivr.net/npm/@fancyapps/fancybox@3.5.7/dist/jquery.fancybox.min.js"></script>



  <script src="https://cdn.jsdelivr.net/npm/anchor-js@4.3.0/anchor.min.js"></script>



  <script defer="" src="https://cdn.jsdelivr.net/npm/clipboard@2.0.8/dist/clipboard.min.js"></script>



  <script defer="" src="https://busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js"></script>




  <script src="https://cdn.jsdelivr.net/npm/typed.js@2.0.11/lib/typed.min.js"></script>
  <script>
    (function (window, document) {
      var typing = Fluid.plugins.typing;
      var title = document.getElementById('subtitle').title;
      
      typing(title)
      
    })(window, document);
  </script><style type="text/css" data-typed-js-css="true">
        .typed-cursor{
          opacity: 1;
        }
        .typed-cursor.typed-cursor--blink{
          animation: typedjsBlink 0.7s infinite;
          -webkit-animation: typedjsBlink 0.7s infinite;
                  animation: typedjsBlink 0.7s infinite;
        }
        @keyframes typedjsBlink{
          50% { opacity: 0.0; }
        }
        @-webkit-keyframes typedjsBlink{
          0% { opacity: 1; }
          50% { opacity: 0.0; }
          100% { opacity: 1; }
        }
      </style>



  <script src="/js/local-search.js"></script>
  <script>
    (function () {
      var path = "/local-search.xml";
      $('#local-search-input').on('click', function() {
        searchFunc(path, 'local-search-input', 'local-search-result');
      });
      $('#modalSearch').on('shown.bs.modal', function() {
        $('#local-search-input').focus();
      });
    })()
  </script>















<!-- 主题的启动项 保持在最底部 -->
<script src="/js/boot.js"></script>




</body></html>
