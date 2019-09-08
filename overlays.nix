self: super:

let
  py-override = {
    packageOverrides = python-self: python-super: {
      python-decouple = python-super.buildPythonPackage rec {
        pname = "python-decouple";
        version = "3.1";
        name = "${pname}-${version}";
        src = python-super.fetchPypi {
          inherit pname version;
          sha256 = "0bgyqk44wiz6jkc4nv3dsl602kq0pwa2k82ag8ry9ziynhady5qk";
        };
      };
    };
  };
in
{
  python3 = super.python3.override py-override;
  python37 = super.python37.override py-override;
}
