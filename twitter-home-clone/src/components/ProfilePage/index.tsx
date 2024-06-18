import React from "react";

import Feed from "../Feed";

import {
  Container,
  Banner,
  Avatar,
  ProfileData,
  LocationIcon,
  CakeIcon,
  Followage,
  EditButton,
} from "./styles";

const ProfilePage: React.FC = () => {
  return (
    <Container>
      <Banner>
        <Avatar />
      </Banner>

      <ProfileData>
        <EditButton outlined>Editar perfil</EditButton>

        <h1>Leonardo Antunens</h1>
        <h2>@leozinhodelas</h2>

        <p>Searching for meaning</p>

        <ul>
          <li>
            <LocationIcon />
            Belo Horizonte, Brasil
          </li>
          <li>
            <CakeIcon />
            Nascido(a) em 17 de Abril de 1997
          </li>
        </ul>

        <Followage>
          <span>
            seguindo <strong>55</strong>
          </span>
          <span>
            <strong>69 </strong> seguidores
          </span>
        </Followage>
      </ProfileData>

      <Feed />
    </Container>
  );
};

export default ProfilePage;
