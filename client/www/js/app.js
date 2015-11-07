(function(){
  'use strict';
  var module = angular.module('app', ['onsen']);
  var config = new Config();

  var URL_BASE = config.URL_BASE;

  module.controller('AppController', ['$scope', function($scope) {
    $scope.showAdd = function() {
      $scope.navi.pushPage('add.html');
    };

    $scope.doSomething = function() {
      setTimeout(function() {
        ons.notification.alert({ message: 'tapped' });
      }, 100);
    };
  }]);

  module.controller('DetailController', ['$scope', '$http', '$sce', '$data', function($scope, $http, $sce, $data) {
    $scope.item = $data.selectedItem;
    $scope.isEdit = false;
    $scope.editQ = '';
    $scope.editA = '';
    $scope.message = $sce.trustAsHtml('');

    $scope.toggleEdit = function(){
        $scope.isEdit = !$scope.isEdit;
        if ($scope.isEdit) {
            $scope.editQ = $scope.item.q;
            $scope.editA = $scope.item.a;
        }
    }
    $scope.cancel = function(){
        $scope.isEdit = false;
        $scope.message = $sce.trustAsHtml('');
    }
    $scope.update = function(id){
        var data = {
            'id': $scope.item.id,
            'q': $scope.editQ,
            'a': $scope.editA
        };
        $http.put(URL_BASE + '/cards/' + $scope.item.id, data)
        .then(function(res){
            $scope.item.q = $scope.editQ;
            $scope.item.a = $scope.editA;
            $scope.item.marked_q = $sce.trustAsHtml(markdown.toHTML($scope.item.q));
            $scope.item.marked_a = $sce.trustAsHtml(markdown.toHTML($scope.item.a));
            $scope.message = $sce.trustAsHtml('saved!');
            $scope.toggleEdit();
        }, function(res){
            $scope.message = $sce.trustAsHtml(res.data);
        });
    }
    $scope.delete = function(id){
        if(!window.confirm('本当に削除してもよいですか？')){
            return;
        }

        $http.delete(URL_BASE + '/cards/' + id)
        .then(function(res){
            for(var i=0; i<$data.items.length; i++){
                if($data.items[i].id == id){
                    $data.items.splice(i, 1);
                    break;
                }
            }
            $scope.navi.popPage();
        }, function(res){
            alert('error');
        });

    };

  }]);

  module.controller('MasterController', ['$scope', '$http', '$sce', '$data', 
                    function($scope, $http, $sce, $data) {
    $scope.data = $data;

    $scope.data.reload();

    $scope.showDetail = function(index) {
      var selectedItem = $data.items[index];
      $data.selectedItem = selectedItem;
      $scope.navi.pushPage('detail.html', {title : selectedItem.title});
    };
  }]);

  module.factory('$data', ['$http', '$sce', function($http, $sce) {
      var Data = function() {};
      Data.prototype.selectedItem = null;
      Data.prototype.items = [];
      Data.prototype.reload = function() {
          var _this = this;
          $http.get(URL_BASE + '/cards/')
            .then(function(res){
                _this.items = res.data.data;
                _this.items.forEach(function(item){
                    item.marked_q = $sce.trustAsHtml(markdown.toHTML(item.q));
                    item.marked_a = $sce.trustAsHtml(markdown.toHTML(item.a));
                });
            }, function(res){
                alert('ERROR: load cards');
            });
      };
      return new Data();
  }]);

  module.controller('AddController', ['$scope', '$http', '$sce', '$data',
                    function($scope, $http, $sce, $data) {
    $scope.q = '';
    $scope.a = '';
    $scope.message = $sce.trustAsHtml('');

    $scope.add = function(){
        var data = {
            'q': $scope.q,
            'a': $scope.a
        };
        var req = {
            method: "POST",
            url: URL_BASE + "/cards/",
            data: data
        };
        $http(req)
            .then(function(res){
                $scope.message = $sce.trustAsHtml("Added!");
                $scope.q = '';
                $scope.a = '';
            }, function(res){
                $scope.message = $sce.trustAsHtml(res.data);
            });
    };

    $scope.back = function() {
        $data.reload();
        $scope.navi.popPage();
    }

    $scope.showDetail = function(index) {
      var selectedItem = $data.items[index];
      $data.selectedItem = selectedItem;
      $scope.navi.pushPage('detail.html', {title : selectedItem.title});
    };
  }]);

})();

