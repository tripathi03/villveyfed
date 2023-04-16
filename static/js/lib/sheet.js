class Sheet{
	__init__ = function (){
		this.DIV = "div";
		this.SPAN = "span";
		this.TABLE_CLASS = "sheet-table"
		this.ROW_VISIBLE_CLASS = "sheet-row sheet-row-visible";
		this.ROW_INVISIBLE_CLASS = "sheet-row sheet-row-invisible";
		this.HEADER_CLASS = "sheet-header";
		this.BODY_CLASS = "sheet-body";
		this.COLUMN_VISIBLE_CLASS = "sheet-column sheet-column-visible";
		this.COLUMN_INVISIBLE_CLASS = "sheet-column sheet-column-invisible";
		this.COLUMN_VISIBLE_HEADER_CLASS = "sheet-column sheet-column-header";
		this.COLUMN_HEADER_CELL = "sheet-header-cell";
		this.SORTER_ICON_CLASS = "glyphicon glyphicon-filter";
		this.MOUSE_POS=-1;
		this.ACTIVE_COLUMN="";
	}
	resizeColumn = function(e){
		e.preventDefault();
		this.ACTIVE_COLUMN=$(e.target).parent()[0];
		let dx = e.x-this.MOUSE_POS;
		this.MOUSE_POS=e.x;
		let currWidth = parseInt(getComputedStyle(this.ACTIVE_COLUMN,'').width)+dx;
		if(currWidth>30 && currWidth<500){
			this.ACTIVE_COLUMN.style.width=currWidth+"px";
			$(this.ACTIVE_COLUMN).children()[0].style.width=currWidth+"px";
		}
		
	}
	getElement = function(tagName, className, value){
		return "<"+tagName+" class='"+(className||"")+"'>"+(value||"")+"</"+tagName+">"
	}
	appendHeader = function(){
		this.$table.append("<div class='"+this.HEADER_CLASS+"'></div>");
		this.header = this.$table.find('.'+this.HEADER_CLASS);
		this.headers.forEach( h => 
			this.header.append(
				this.getElement(this.DIV,
					this.COLUMN_VISIBLE_HEADER_CLASS,
					this.getElement(this.DIV, 
						this.COLUMN_HEADER_CELL,
						h
					)
				)
			)
		);
		$.each($('.'+this.COLUMN_HEADER_CELL),(i,v) => {
			$(v).append(this.getElement(this.DIV,this.SORTER_ICON_CLASS));
		});
	}
	
	addResizeListener = function(){
		$.each($(".sheet-header-cell"),(i, v)=>{
			v.addEventListener("mousedown", (e)=>{
				e.preventDefault();
				document.body.style.cursor = "resize";
				this.MOUSE_POS=e.x;
				document.addEventListener("mousemove", this.resizeColumn, false);
			});
			document.addEventListener("mouseup", () => {
				document.removeEventListener("mousemove", this.resizeColumn, false);
				document.body.style.cursor = "auto";
			})
		});
	}
	adjustColumnWidth = function(){
		
	}
	appendRows = function(){
		this.$table.append("<div class='"+this.BODY_CLASS+"'></div>");
		this.body = this.$table.find('.'+this.BODY_CLASS);
		$.each(this.header.children(), (i,v)=>{
			$.each(this.rows, (j,w) => {
				$(v).append(this.getElement(this.SPAN,this.ROW_VISIBLE_CLASS,this.rows[j][i]));
			})
		})
	}
	constructor(mainDiv, options){
		if(!options) {
			throw new Error("Usage : new Sheet(selector, options)");
		}
		if(options.data && options.rows){
			throw new Error("Provide either rows or data, not both");
		}
		if(!options.data && !options.rows){
			throw new Error("Provide either rows or data");
		}
		if(!options.headers && !options.data.length){
			throw new Error("Empty Data");
		}
		this.__init__();
		this.$sheet = $(mainDiv);
		$(mainDiv).html("");
		$(mainDiv).append("<div class='"+this.TABLE_CLASS+"'></div>");
		this.$table = $(mainDiv).find('.'+this.TABLE_CLASS);
		if(options){
			this.rows = options.rows || [];
			this.headers = options.headers || [];
			this.data = options.data || {};
		}
		if(this.data){
			this.headers = Object.keys(this.data[0]);
			this.rows = []
			this.data.forEach(d => {
				this.rows.push(this.headers.map(h => d[h]));
			});
		}
		this.appendHeader();
		this.appendRows();
		this.adjustColumnWidth();
		this.addResizeListener();
	}
}