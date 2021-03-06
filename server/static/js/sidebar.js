(function() {
    var NavigateBar = function(elementId) {
        this.eId = elementId||'wrap';
        this.el = document.getElementById(this.eId);
        this.el.addEventListener('click',function(evt) {
            evt.stopPropagation();
        });
        this.state = 'allClosed';//hasOpened
        this.currentOpenedEl = null;

        //var forEach = Array.prototype.forEach;
        var self = this;
        //var navigatorList =  document.querySelectorAll('#' + this.eId + ' > div');
		var toolsOption = document.getElementById("tools");
        toolsOption.addEventListener('mouseover',function(evt) {
			var currentEl = document.getElementById(evt.currentTarget.id + '-content');
			if(self.state === 'allClosed') {
				/*
				currentEl.className = 'nav-content';
                currentEl.style.top = '0px';
                currentEl.style.left = '-65px';
                currentEl.classList.add('nc_move_right');
				*/
                self.state = 'hasOpened';
                self.currentOpenedEl = currentEl;
			}else{
                self.currentOpenedEl.className = 'nav-content';
                self.currentOpenedEl.style.top = '0px';
                self.currentOpenedEl.style.left = '0px';
                self.currentOpenedEl.classList.add('nc_move_left');

                currentEl.className = 'nav-content';
                currentEl.style.top = '250px';
                currentEl.style.left = '35px';
                currentEl.classList.add('move_up');
                self.currentOpenedEl = currentEl;
			}
		});
		
        //var navConCloseBarList = document.querySelectorAll('.nav-content > div.nav-con-close');
        var closeToolsBar = document.querySelector("#tools-content .nav-con-close");
		//forEach.call(navConCloseBarList, function(navConCloseBar){
        closeToolsBar.addEventListener('click',function(evt) {
            //var currentEl = evt.currentTarget.parentNode;
			toolCategoriesBar.close();
			self.close();
        });
        ///});
    };

    NavigateBar.prototype.close = function() {
        if(this.currentOpenedEl !== null){
			this.currentOpenedEl.className = 'nav-content';
			this.currentOpenedEl.style.top = '0px';
			this.currentOpenedEl.style.left = '0px';
			this.currentOpenedEl.classList.add('nc_move_left');
		}
        this.state = 'allClosed';
    };

    var navigateBar = new NavigateBar();

	//=======================================================================
	var ToolCategoriesBar = function(elementId) {
        this.eId = elementId||'toolCategories';
        this.el = document.getElementById(this.eId);
        this.el.addEventListener('click',function(evt) {
            evt.stopPropagation();
        });
        this.state = 'allClosed';//hasOpened
        this.currentOpenedEl = null;

        var forEach = Array.prototype.forEach;
        var self = this;
        var toolCategoriesList =  document.querySelectorAll('#' + this.eId + ' > div');
        forEach.call(toolCategoriesList, function(toolCategory){
            toolCategory.addEventListener('mouseover',function(evt) {
                var currentEl = document.getElementById(evt.currentTarget.id + '-options');
                if(self.state === 'allClosed') {           
					self.state = 'hasOpened';
                    self.currentOpenedEl = currentEl;
                }else {
                    self.currentOpenedEl.className = 'tool-content';
                    self.currentOpenedEl.style.top = '0px';
                    self.currentOpenedEl.style.left = '0px';
                    self.currentOpenedEl.classList.add('nc_move_left');

                    currentEl.className = 'tool-content';
                    currentEl.style.top = '250px';
                    currentEl.style.left = '185px';
                    currentEl.classList.add('move_up');
                    self.currentOpenedEl = currentEl;
                }
            });
        });

        var toolConCloseBarList = document.querySelectorAll('.tool-content > div.nav-con-close');
        forEach.call(toolConCloseBarList, function(toolConCloseBar){
            toolConCloseBar.addEventListener('click',function(evt) {
                //var currentEl = evt.currentTarget.parentNode;
                self.close();
            });
        });
    };

    ToolCategoriesBar.prototype.close = function() {
        if(this.currentOpenedEl !== null){
			this.currentOpenedEl.className = 'tool-content';
			this.currentOpenedEl.style.top = '0px';
			this.currentOpenedEl.style.left = '0px';
			this.currentOpenedEl.classList.add('nc_move_left');
		}
        this.state = 'allClosed';
    };

    var toolCategoriesBar = new ToolCategoriesBar();
	//=======================================================================
	
    var SideBar = function(elementId) {
        this.eId = elementId||'sidebar';
        this.el = document.getElementById(this.eId);
        this.closeBarEl = document.getElementById('closeBar');
        this.state = 'opened';
        var self = this;
        this.el.addEventListener('click',function(evt) {
            if(evt.target !==  self.el) {
                self.triggerSwitch(); 
            }
        });
    };

    SideBar.prototype.triggerSwitch = function() {
        if(this.state === 'opened')
            this.close();
        else if(this.state === 'closed')
            this.open();
    };

    SideBar.prototype.close = function() {
        //==========================================================
		toolCategoriesBar.close();
		//==========================================================
		navigateBar.close();
        this.el.style.left = '0';
        this.el.className ='move_left';
        this.closeBarEl.style.left = '0';
        this.closeBarEl.className = 'closeBar_move_right';
        this.state = 'closed';
    };

    SideBar.prototype.open = function() {
        this.el.style.left = '-150px';
        this.el.className = 'move_right';
        this.closeBarEl.style.left = '190px';
        this.closeBarEl.className = 'closeBar_move_left';
        this.state = 'opened';
    };
    var sideBar = new SideBar();
    //===========================================================
    var closeSetArg = document.getElementById("closeSetArg");
	closeSetArg.onclick = function(){
		window.history.back();
	};
    /*var ToolSelectBar = function(elementId) {
        this.eId = elementId||'toolOptions';
      
        var forEach = Array.prototype.forEach;
        //var self = this;
        var toolsList =  document.querySelectorAll('.' + this.eId + ' > div');
        forEach.call(toolsList, function(tool){
            tool.addEventListener('click',function(evt) {
				var pageWidth = document.body.scrollWidth;
				var pageHeight = document.body.scrollHeight;
			
				var visibleHeight = document.documentElement.clientHeight;
				
				var popupMask = document.createElement("div");
				popupMask.id = "maskSetArg";
				popupMask.style.height = pageHeight + "px";
				popupMask.style.width = pageWidth + "px";
				document.body.appendChild(popupMask);
			
				var setArgContainer = document.getElementById('setArgContainer');
				setArgContainer.style.display = 'block';
				//document.body.appendChild(setArgContainer);
				var containerHeight = setArgContainer.offsetHeight;
				var containerWidth = setArgContainer.offsetWidth;
				setArgContainer.style.left = pageWidth/2 - containerWidth/2 + 'px';
				setArgContainer.style.top = visibleHeight/2 - containerHeight/2 + 'px';
			
				var closeSetArg = document.getElementById("closeSetArg");
				closeSetArg.onclick = popupMask.onclick = function(){
					setArgContainer.style.display = 'none';
					document.body.removeChild(popupMask);
				};
			});
		});
	};
	var toolSelectBar = new ToolSelectBar();
	*/
})();
