(self.webpackChunksketchfab=self.webpackChunksketchfab||[]).push([[6100],{AxWo:(e,t,i)=>{"use strict";i.d(t,{Z:()=>y});var n=i("Hjnd"),o=i.n(n),s=i("di37"),h=i("yfOW"),r=i("PGhl"),l=i("rRD0"),c=i("hDWi"),u=i("pcq+"),a=i("/VXM"),d=i("69kl"),p=i("mV4i"),f=i("Fgrz"),m=i("Oyie"),w=[];const y=h.Z.extend({parent:"body",el:'<div data-element="popup" />',optionTypes:{cleanOnClose:a.Z.bool,shouldExitOnClickOutside:a.Z.bool,shouldExitOnEscape:a.Z.bool,shouldRejectOnCancel:a.Z.bool},defaultOptions:{cleanOnClose:!0,shouldExitOnClickOutside:!0,shouldExitOnEscape:!0,shouldRejectOnCancel:!1},events:{'click [data-action="close"]':"cancel","click button:not([type])":c.PF,"mousedown .popup-container":"onMouseDown","mouseup .popup-container":"onMouseUp"},onMouseDown:function(e){this.lastMouseDownTarget=e.target},onMouseUp:function(e){this.options.shouldExitOnClickOutside&&e.currentTarget===this.lastMouseDownTarget&&(this.cancel(),delete this.lastMouseDownTarget)},constructor:function(){this.onKeyDown=this.onKeyDown.bind(this),this.identifier=Symbol(Math.random()),this.resizeHandler=function(){o().each(w,(function(e,t){t.setHeightForMobileResolution()}))}.bind(this),h.Z.apply(this,arguments)},initialize:function(){h.Z.prototype.initialize.apply(this,arguments),this.renderLayout()},setElement:function(){return h.Z.prototype.setElement.apply(this,arguments),this.$container=this.$(".popup-container"),this},delegateEvents:function(){h.Z.prototype.delegateEvents.apply(this,arguments),o()(window).on("resize",this.resizeHandler),document.addEventListener("keydown",this.onKeyDown,!0)},undelegateEvents:function(){h.Z.prototype.undelegateEvents.apply(this,arguments),o()(window).off("resize",this.resizeHandler),document.removeEventListener("keydown",this.onKeyDown,!0)},getPromise:function(){return this._promise||(this._promise=(0,p.pJ)()),this._promise},open:function(){return-1!==w.indexOf(this)?(this.show(),this.setElement(this.$el),this.getPromise()):(this.render(),w.unshift(this),o()((0,s.Z)(this,"parent")).append(this.$el),this.setElement(this.$el),this.hide(),this.setHeightForMobileResolution(),window.requestAnimationFrame(function(){this.show()}.bind(this)),this.getPromise())},show:function(){this.$container.removeClass("hidden"),document.body.classList.add("--prevent-scroll"),d.K.add(this.identifier)},hide:function(){this.$container.addClass("hidden"),d.K.delete(this.identifier),d.K.isEmpty()&&document.body.classList.remove("--prevent-scroll")},setIsLoading:function(e){this.$container.toggleClass("popup-loading",e)},isHidden:function(){return this.$container.hasClass("hidden")},onKeyDown:function(e){27===e.keyCode&&this.options.shouldExitOnEscape&&d.K.getTopPopup()===this.identifier&&(this.cancel(),e.stopPropagation())},cancel:function(e){return this._close(),this.options.shouldRejectOnCancel?this.getPromise().reject(new l.ud(e)):this.getPromise().resolve()},continue:function(e){return this._close(),this.getPromise().resolve(e)},_close:function(e,t){return this.$container.closest(".inline-popup").length>0?this:this.options.cleanOnClose||t?(this.hide(),(0,p.Vs)(500,(0,f.Z)(this.$el)).catch((function(){})).then(this.remove.bind(this))):(this.hide(),m.resolve())},close:function(e){return this._close(null,e)},replaceWith:function(e,t){return this.close(t),e.open()},setHeightForMobileResolution:function(){if(u.default.any){var e=this.$(".js-popup");(0,r.Nc)({width:window.innerWidth,breakpoint:"breakpointXSmall"})&&e.css({height:window.innerHeight})}},resize:function(e){var t=this.$(".js-popup");e.width&&t.width(e.width),e.height&&t.height(e.height)},autofocus:function(){var e=window.scrollX,t=window.scrollY;this.$(".form-input:visible").length>0?(this.$(".form-input").eq(0).focus(),window.scrollTo(e,t)):(this.$(".btn-primary, .submit").focus(),window.scrollTo(e,t))},_removeElement:function(){this.$el.remove()},remove:function(){return this.undelegateEvents(),h.Z.prototype.remove.apply(this,arguments)},renderLayout:function(){this.$el.html(this.template()),this.$container=this.$(".popup-container")},afterRender:function(){h.Z.prototype.afterRender.apply(this,arguments),this.renderChildren()}})}}]);