{ pkgs ? import ./pinned-nixpkgs.nix {} }:

let
  python = pkgs.python37Packages;

  pythonPkgs = with python; [
    aiohttp
    pillow
    python-decouple
    pytest
    telethon
    requests
  ];

  devPkgs = with python; [
    pip
    python-language-server
    pyls-black
  ];

  # None of these packages are installed
  # globally.
  systemPkgs = with pkgs; [
    openssl
    python37Full
  ];
in
pkgs.mkShell rec {
  name = "py-env";
  buildInputs = systemPkgs ++ pythonPkgs ++ devPkgs;
  shellHook = ''
    export NIX_SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
  '';
}
