(function(g){var window=this;'use strict';var B6=function(a){g.W.call(this,{G:"div",L:"ytp-miniplayer-ui"});this.oe=!1;this.player=a;this.T(a,"minimized",this.xg);this.T(a,"onStateChange",this.BG)},C6=function(a){g.RM.call(this,a);
this.i=new B6(this.player);this.i.hide();g.EM(this.player,this.i.element,4);a.Je()&&(this.load(),g.M(a.getRootNode(),"ytp-player-minimized",!0))};
g.v(B6,g.W);g.k=B6.prototype;
g.k.yE=function(){this.tooltip=new g.rQ(this.player,this);g.H(this,this.tooltip);g.EM(this.player,this.tooltip.element,4);this.tooltip.scale=.6;this.uc=new g.KN(this.player);g.H(this,this.uc);this.Cg=new g.W({G:"div",L:"ytp-miniplayer-scrim"});g.H(this,this.Cg);this.Cg.Ea(this.element);this.T(this.Cg.element,"click",this.qA);var a=new g.W({G:"button",Ga:["ytp-miniplayer-close-button","ytp-button"],W:{"aria-label":"Chiudi"},U:[g.LK()]});g.H(this,a);a.Ea(this.Cg.element);this.T(a.element,"click",this.Di);
a=new g.V1(this.player,this);g.H(this,a);a.Ea(this.Cg.element);this.wp=new g.W({G:"div",L:"ytp-miniplayer-controls"});g.H(this,this.wp);this.wp.Ea(this.Cg.element);this.T(this.wp.element,"click",this.qA);var b=new g.W({G:"div",L:"ytp-miniplayer-button-container"});g.H(this,b);b.Ea(this.wp.element);a=new g.W({G:"div",L:"ytp-miniplayer-play-button-container"});g.H(this,a);a.Ea(this.wp.element);var c=new g.W({G:"div",L:"ytp-miniplayer-button-container"});g.H(this,c);c.Ea(this.wp.element);this.kN=new g.iP(this.player,
this,!1);g.H(this,this.kN);this.kN.Ea(b.element);b=new g.gP(this.player,this);g.H(this,b);b.Ea(a.element);this.nextButton=new g.iP(this.player,this,!0);g.H(this,this.nextButton);this.nextButton.Ea(c.element);this.Fg=new g.cQ(this.player,this);g.H(this,this.Fg);this.Fg.Ea(this.Cg.element);this.Fc=new g.pP(this.player,this);g.H(this,this.Fc);g.EM(this.player,this.Fc.element,4);this.eA=new g.W({G:"div",L:"ytp-miniplayer-buttons"});g.H(this,this.eA);g.EM(this.player,this.eA.element,4);a=new g.W({G:"button",
Ga:["ytp-miniplayer-close-button","ytp-button"],W:{"aria-label":"Chiudi"},U:[g.LK()]});g.H(this,a);a.Ea(this.eA.element);this.T(a.element,"click",this.Di);a=new g.W({G:"button",Ga:["ytp-miniplayer-replay-button","ytp-button"],W:{"aria-label":"Chiudi"},U:[g.QK()]});g.H(this,a);a.Ea(this.eA.element);this.T(a.element,"click",this.BV);this.T(this.player,"presentingplayerstatechange",this.Mc);this.T(this.player,"appresize",this.wb);this.T(this.player,"fullscreentoggled",this.wb);this.wb()};
g.k.show=function(){this.Kd=new g.Sq(this.lq,null,this);this.Kd.start();this.oe||(this.yE(),this.oe=!0);0!==this.player.getPlayerState()&&g.W.prototype.show.call(this);this.Fc.show();this.player.unloadModule("annotations_module")};
g.k.hide=function(){this.Kd&&(this.Kd.dispose(),this.Kd=void 0);g.W.prototype.hide.call(this);this.player.Je()||(this.oe&&this.Fc.hide(),this.player.loadModule("annotations_module"))};
g.k.xa=function(){this.Kd&&(this.Kd.dispose(),this.Kd=void 0);g.W.prototype.xa.call(this)};
g.k.Di=function(){this.player.stopVideo();this.player.Ma("onCloseMiniplayer")};
g.k.BV=function(){this.player.playVideo()};
g.k.qA=function(a){if(a.target===this.Cg.element||a.target===this.wp.element)this.player.V().N("kevlar_miniplayer_play_pause_on_scrim")?g.OJ(this.player.zb())?this.player.pauseVideo():this.player.playVideo():this.player.Ma("onExpandMiniplayer")};
g.k.xg=function(){g.M(this.player.getRootNode(),"ytp-player-minimized",this.player.Je())};
g.k.od=function(){this.Fc.Xb();this.Fg.Xb()};
g.k.lq=function(){this.od();this.Kd&&this.Kd.start()};
g.k.Mc=function(a){g.U(a.state,32)&&this.tooltip.hide()};
g.k.wb=function(){g.CP(this.Fc,0,this.player.eb().getPlayerSize().width,!1);g.qP(this.Fc)};
g.k.BG=function(a){this.player.Je()&&(0===a?this.hide():this.show())};
g.k.fc=function(){return this.tooltip};
g.k.Re=function(){return!1};
g.k.rf=function(){return!1};
g.k.xi=function(){return!1};
g.k.dB=function(){};
g.k.dn=function(){};
g.k.Zr=function(){};
g.k.Dn=function(){return null};
g.k.lj=function(){return new g.Wl(0,0,0,0)};
g.k.handleGlobalKeyDown=function(){return!1};
g.k.handleGlobalKeyUp=function(){return!1};
g.k.uq=function(a,b,c,d,e){var f=0,h=d=0,l=g.om(a);if(b){c=g.cr(b,"ytp-prev-button")||g.cr(b,"ytp-next-button");var m=g.cr(b,"ytp-play-button"),n=g.cr(b,"ytp-miniplayer-expand-watch-page-button");c?f=h=12:m?(b=g.mm(b,this.element),h=b.x,f=b.y-12):n&&(h=g.cr(b,"ytp-miniplayer-button-top-left"),f=g.mm(b,this.element),b=g.om(b),h?(h=8,f=f.y+40):(h=f.x-l.width+b.width,f=f.y-20))}else h=c-l.width/2,d=25+(e||0);b=this.player.eb().getPlayerSize().width;e=f+(e||0);l=g.jg(h,0,b-l.width);e?(a.style.top=e+"px",
a.style.bottom=""):(a.style.top="",a.style.bottom=d+"px");a.style.left=l+"px"};
g.k.showControls=function(){};
g.k.Zk=function(){};
g.k.Ak=function(){return!1};g.v(C6,g.RM);C6.prototype.create=function(){};
C6.prototype.Ki=function(){return!1};
C6.prototype.load=function(){this.player.hideControls();this.i.show()};
C6.prototype.unload=function(){this.player.showControls();this.i.hide()};g.QM("miniplayer",C6);})(_yt_player);
