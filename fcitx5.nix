
{ pkgs, inputs, ... }:
{
  imports = [ inputs.home-manager.nixosModules.default ];

  i18n.inputMethod = {
    enable = true;
    type = "fcitx5";
    fcitx5 = {
      addons = with pkgs; [ fcitx5-table-other kdePackages.fcitx5-chinese-addons ]; #tables dont work without chinese addons
      waylandFrontend = true; #comment this out if using x11
    };
  };

  home-manager.users.USERNAME = {
    home.file = {
      "tok-punctuation" = {
        source = ./nasin-mun/punctuation/punc.mb.tok;
        target = ".local/share/fcitx5/punctuation/punc.mb.tok";
      };
      "configuration" = {
        source = ./nasin-mun/inputmethod/nasin-mun.conf;
        target = ".local/share/fcitx5/inputmethod/nasin-mun.conf";
      };
      "dictionary" = {
        source = ./nasin-mun/table/nasin-mun.dict;
        target = ".local/share/fcitx5/table/nasin-mun.dict";
      };
      "profile" = {
        source = ./nasin-mun/profile;
	target = ".config/fcitx5/profile";
      };
    };
  };
}

