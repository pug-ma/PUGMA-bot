{ bootstrap ? import <nixpkgs> {}
, json ? ./.nixpkgs-version.json
}:

let
  nixpkgs = builtins.fromJSON (builtins.readFile json);
  src = bootstrap.fetchFromGitHub {
    owner = "NixOS";
    repo = "nixpkgs-channels";
    inherit (nixpkgs) rev sha256;
  };
in
  import src {
    overlays = [
      (import ./overlays.nix)
    ];
  }
